"""REST API server for zen-mcp-fork - provides HTTP endpoints for all tools."""

import asyncio
import json
import logging
import os
import secrets
import time
from typing import Any, Dict, Optional

from aiohttp import web
from aiohttp.web import middleware
from pydantic import BaseModel, Field, ValidationError

from server import configure_providers, TOOLS, handle_get_version
from tools.base import TextContent
from utils.conversation_memory import (
    create_thread,
    add_conversation_turn,
    get_thread_context,
)

# Configure logging
logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Server configuration
HOST = "0.0.0.0"
PORT = int(os.getenv("ZEN_API_PORT", "8765"))

# Security configuration
API_KEY = os.getenv("ZEN_API_KEY")
PRODUCTION_MODE = os.getenv("PRODUCTION", "false").lower() == "true"

# Rate limiting configuration
RATE_LIMIT_REQUESTS = 100  # requests per window
RATE_LIMIT_WINDOW = 300    # 5 minutes in seconds

# Session management
sessions: Dict[str, Dict[str, Any]] = {}
rate_limit_store: Dict[str, Dict[str, Any]] = {}


class ToolRequest(BaseModel):
    """Request model for tool execution."""
    arguments: Dict[str, Any] = Field(..., description="Tool arguments")
    session_id: Optional[str] = Field(None, description="Session ID for conversation continuity")


class ToolResponse(BaseModel):
    """Response model for tool execution."""
    content: str
    status: str = "success"
    session_id: Optional[str] = None
    continuation_id: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


@middleware
async def auth_middleware(request: web.Request, handler):
    """Authentication middleware for API key validation."""
    # Skip auth for health check
    if request.path == "/health":
        return await handler(request)
    
    # Check if we're in production mode
    if not PRODUCTION_MODE:
        logger.debug("Development mode: Skipping authentication")
        return await handler(request)
    
    # In production, require API key
    if not API_KEY:
        logger.error("No API key configured in production mode")
        return web.json_response(
            {"error": "Server misconfiguration: No API key set"},
            status=500
        )
    
    # Check Authorization header
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return web.json_response(
            {"error": "Missing or invalid authorization header"},
            status=401
        )
    
    provided_key = auth_header.split(" ", 1)[1]
    if not secrets.compare_digest(provided_key, API_KEY):
        return web.json_response(
            {"error": "Invalid API key"},
            status=401
        )
    
    return await handler(request)


@middleware
async def rate_limit_middleware(request: web.Request, handler):
    """Rate limiting middleware."""
    # Skip rate limiting for health check
    if request.path == "/health":
        return await handler(request)
    
    # Get client identifier (IP or API key)
    client_id = request.headers.get("X-Forwarded-For", request.remote)
    if PRODUCTION_MODE and request.headers.get("Authorization"):
        # Use API key as identifier in production
        client_id = request.headers.get("Authorization")
    
    now = time.time()
    
    # Clean up old entries
    for cid in list(rate_limit_store.keys()):
        if now - rate_limit_store[cid]["window_start"] > RATE_LIMIT_WINDOW:
            del rate_limit_store[cid]
    
    # Check rate limit
    if client_id not in rate_limit_store:
        rate_limit_store[client_id] = {
            "window_start": now,
            "requests": 0
        }
    
    client_data = rate_limit_store[client_id]
    
    # Reset window if expired
    if now - client_data["window_start"] > RATE_LIMIT_WINDOW:
        client_data["window_start"] = now
        client_data["requests"] = 0
    
    # Increment request count
    client_data["requests"] += 1
    
    # Check if rate limit exceeded
    if client_data["requests"] > RATE_LIMIT_REQUESTS:
        return web.json_response(
            {
                "error": "Rate limit exceeded",
                "retry_after": int(RATE_LIMIT_WINDOW - (now - client_data["window_start"]))
            },
            status=429
        )
    
    return await handler(request)


@middleware
async def error_middleware(request: web.Request, handler):
    """Error handling middleware."""
    try:
        return await handler(request)
    except ValidationError as e:
        logger.warning(f"Validation error: {e}")
        return web.json_response(
            {"error": "Invalid request", "details": e.errors()},
            status=400
        )
    except Exception as e:
        logger.error(f"Unhandled error: {e}", exc_info=True)
        # Don't expose internal errors in production
        if PRODUCTION_MODE:
            return web.json_response(
                {"error": "Internal server error"},
                status=500
            )
        else:
            return web.json_response(
                {"error": str(e)},
                status=500
            )


async def health_check(request: web.Request) -> web.Response:
    """Health check endpoint."""
    return web.json_response({
        "status": "healthy",
        "version": "1.1.1",
        "mode": "production" if PRODUCTION_MODE else "development",
        "timestamp": time.time()
    })


async def list_tools(request: web.Request) -> web.Response:
    """List available tools."""
    tools_info = []
    for name, tool in TOOLS.items():
        tools_info.append({
            "name": name,
            "description": tool.description,
            "schema": tool.get_input_schema()
        })
    
    # Add utility tools
    tools_info.append({
        "name": "get_version",
        "description": "Get server version and configuration",
        "schema": {"type": "object", "properties": {}}
    })
    
    return web.json_response({
        "tools": tools_info,
        "total": len(tools_info)
    })


async def execute_tool(request: web.Request) -> web.Response:
    """Execute a specific tool."""
    tool_name = request.match_info["tool_name"]
    
    # Parse request
    try:
        data = await request.json()
        tool_request = ToolRequest(**data)
    except json.JSONDecodeError:
        return web.json_response(
            {"error": "Invalid JSON"},
            status=400
        )
    except ValidationError as e:
        return web.json_response(
            {"error": "Invalid request", "details": e.errors()},
            status=400
        )
    
    # Handle session management
    session_id = tool_request.session_id
    if not session_id:
        session_id = secrets.token_urlsafe(16)
        sessions[session_id] = {
            "created": time.time(),
            "last_used": time.time(),
            "request_count": 0
        }
    
    if session_id in sessions:
        sessions[session_id]["last_used"] = time.time()
        sessions[session_id]["request_count"] += 1
    
    # Execute tool
    try:
        if tool_name == "get_version":
            result = await handle_get_version()
        elif tool_name in TOOLS:
            tool = TOOLS[tool_name]
            result = await tool.execute(tool_request.arguments)
        else:
            return web.json_response(
                {"error": f"Unknown tool: {tool_name}"},
                status=404
            )
        
        # Extract content from result
        if isinstance(result, list) and len(result) > 0:
            content = result[0].text if hasattr(result[0], 'text') else str(result[0])
        else:
            content = str(result)
        
        # Parse result if it's JSON
        try:
            parsed_content = json.loads(content)
            if isinstance(parsed_content, dict):
                # Extract continuation_id if present
                continuation_id = parsed_content.get("metadata", {}).get("continuation_id")
                
                response = ToolResponse(
                    content=parsed_content.get("content", content),
                    status=parsed_content.get("status", "success"),
                    session_id=session_id,
                    continuation_id=continuation_id,
                    metadata=parsed_content.get("metadata")
                )
            else:
                response = ToolResponse(
                    content=content,
                    session_id=session_id
                )
        except json.JSONDecodeError:
            # Content is not JSON, return as-is
            response = ToolResponse(
                content=content,
                session_id=session_id
            )
        
        return web.json_response(response.model_dump())
        
    except Exception as e:
        logger.error(f"Error executing tool {tool_name}: {e}", exc_info=True)
        return web.json_response(
            {"error": f"Tool execution failed: {str(e)}"},
            status=500
        )


async def list_sessions(request: web.Request) -> web.Response:
    """List active sessions."""
    # Clean up old sessions (older than 1 hour)
    now = time.time()
    expired = [sid for sid, data in sessions.items() 
               if now - data["last_used"] > 3600]
    for sid in expired:
        del sessions[sid]
    
    # Return active sessions
    session_info = []
    for sid, data in sessions.items():
        session_info.append({
            "session_id": sid,
            "created": data["created"],
            "last_used": data["last_used"],
            "request_count": data["request_count"],
            "age_seconds": int(now - data["created"])
        })
    
    return web.json_response({
        "sessions": session_info,
        "total": len(session_info)
    })


async def init_app() -> web.Application:
    """Initialize the web application."""
    # Configure providers (validates API keys)
    try:
        configure_providers()
    except ValueError as e:
        logger.error(f"Failed to configure providers: {e}")
        raise
    
    # Create app with middleware
    app = web.Application(
        middlewares=[
            error_middleware,
            auth_middleware,
            rate_limit_middleware
        ]
    )
    
    # Add routes
    app.router.add_get("/health", health_check)
    app.router.add_get("/tools", list_tools)
    app.router.add_post("/tools/{tool_name}", execute_tool)
    app.router.add_get("/sessions", list_sessions)
    
    # Add CORS headers in development
    if not PRODUCTION_MODE:
        async def cors_middleware(app, handler):
            async def cors_handler(request):
                response = await handler(request)
                response.headers["Access-Control-Allow-Origin"] = "*"
                response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
                response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
                return response
            return cors_handler
        
        app.middlewares.append(cors_middleware)
    
    return app


def main():
    """Main entry point."""
    logger.info(f"Starting Zen MCP REST API server on {HOST}:{PORT}")
    logger.info(f"Mode: {'Production' if PRODUCTION_MODE else 'Development'}")
    
    if not PRODUCTION_MODE:
        logger.info("🔓 Development mode - Authentication disabled")
        logger.info("⚠️  For production, set PRODUCTION=true and configure ZEN_API_KEY")
    else:
        if not API_KEY:
            logger.error("❌ Production mode requires ZEN_API_KEY to be set!")
            raise ValueError("ZEN_API_KEY must be set in production mode")
        logger.info("🔒 Production mode - Authentication enabled")
    
    # Create and run app
    app = init_app()
    web.run_app(
        app,
        host=HOST,
        port=PORT,
        access_log=logger if not PRODUCTION_MODE else None
    )


if __name__ == "__main__":
    main()