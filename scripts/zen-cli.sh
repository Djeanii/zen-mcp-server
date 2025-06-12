#!/bin/bash

# Zen MCP CLI - Command line interface for zen-mcp-fork
set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
API_URL="${ZEN_API_URL:-http://localhost:8765}"
API_KEY="${ZEN_API_KEY:-}"

# Load API key from .env if not set
if [ -z "$API_KEY" ] && [ -f .env ]; then
    API_KEY=$(grep "^ZEN_API_KEY=" .env | cut -d'=' -f2 | tr -d '"' | tr -d "'" || true)
fi

# Check if API key is needed (production mode)
check_auth_required() {
    # In development mode, auth is not required
    if [ -f .env ] && grep -q "PRODUCTION=false" .env 2>/dev/null; then
        return 1  # Auth not required
    fi
    return 0  # Auth required
}

# Function to display help
show_help() {
    echo "Zen MCP CLI - Interact with the persistent zen-mcp server"
    echo ""
    echo "Usage: $0 <command> [arguments]"
    echo ""
    echo "Server Commands:"
    echo "  start              - Start the persistent server"
    echo "  stop               - Stop the persistent server"
    echo "  logs               - Show server logs"
    echo "  health             - Check server health"
    echo "  genkey             - Generate a secure API key"
    echo ""
    echo "Tool Commands:"
    echo "  tools              - List available tools"
    echo "  models             - List available models"
    echo "  chat <message>     - Chat with AI (uses free models)"
    echo "  think <problem>    - Deep thinking about complex problems"
    echo "  review <file>      - Review code in a file"
    echo "  debug <error>      - Debug an error message"
    echo "  sessions           - List active sessions"
    echo ""
    echo "Authentication:"
    if check_auth_required; then
        echo "  ⚠️  Production mode - API key required!"
        echo "  Set ZEN_API_KEY in .env file or environment"
    else
        echo "  ✅ Development mode - no auth needed"
    fi
    echo "  Generate a key with: $0 genkey"
    echo ""
    echo "Examples:"
    echo "  $0 start"
    echo "  $0 chat \"What is the best way to implement caching?\""
    echo "  $0 think \"How should I architect a microservices system?\""
    echo "  $0 review /path/to/file.py security"
    echo "  $0 debug \"TypeError: cannot read property 'id' of undefined\""
}

# Function to make API calls
api_call() {
    local endpoint=$1
    local method=${2:-GET}
    local data=${3:-}
    
    local auth_header=""
    if check_auth_required && [ -n "$API_KEY" ]; then
        auth_header="-H \"Authorization: Bearer $API_KEY\""
    fi
    
    if [ "$method" = "GET" ]; then
        eval curl -s -X GET $auth_header "$API_URL$endpoint"
    else
        eval curl -s -X POST $auth_header \
            -H "Content-Type: application/json" \
            -d "'$data'" \
            "$API_URL$endpoint"
    fi
}

# Command handlers
cmd_start() {
    echo -e "${BLUE}Starting Zen MCP persistent server...${NC}"
    docker-compose -f docker-compose.persistent.yml up -d
    echo -e "${GREEN}✅ Server started!${NC}"
    echo ""
    echo "Available at: $API_URL"
    if ! check_auth_required; then
        echo -e "${GREEN}Development mode - no auth needed${NC}"
    fi
}

cmd_stop() {
    echo -e "${BLUE}Stopping Zen MCP server...${NC}"
    docker-compose -f docker-compose.persistent.yml down
    echo -e "${GREEN}✅ Server stopped!${NC}"
}

cmd_logs() {
    docker-compose -f docker-compose.persistent.yml logs -f
}

cmd_health() {
    echo -e "${BLUE}Checking server health...${NC}"
    response=$(api_call "/health" GET 2>/dev/null || echo "error")
    
    if [[ "$response" == *"healthy"* ]]; then
        echo -e "${GREEN}✅ Server is healthy!${NC}"
        echo "$response" | jq . 2>/dev/null || echo "$response"
    else
        echo -e "${RED}❌ Server is not responding${NC}"
        echo "Make sure the server is running: $0 start"
    fi
}

cmd_genkey() {
    echo -e "${BLUE}Generating secure API key...${NC}"
    key=$(python3 -c "import secrets; print(secrets.token_urlsafe(32))" 2>/dev/null || openssl rand -base64 32)
    echo ""
    echo -e "${GREEN}Your new API key:${NC}"
    echo "$key"
    echo ""
    echo "Add this to your .env file:"
    echo "ZEN_API_KEY=$key"
}

cmd_tools() {
    echo -e "${BLUE}Available tools:${NC}"
    response=$(api_call "/tools" GET)
    echo "$response" | jq -r '.tools[]' 2>/dev/null || echo "$response"
}

cmd_models() {
    echo -e "${BLUE}Available FREE models:${NC}"
    echo ""
    echo "🎯 Simple Aliases:"
    echo "  chat  - Best overall chat model (Qwen 2.5 Coder)"
    echo "  think - Deep reasoning (DeepSeek R1 671B!)"
    echo "  code  - Code specialist (Mistral Devstral)"
    echo "  fast  - Ultra-fast (Gemini Flash 1M context!)"
    echo "  smart - High-quality (Llama 3.3 70B)"
    echo ""
    echo "📋 All Free Models:"
    echo "  qwen/qwen-2.5-coder-32b-instruct:free"
    echo "  deepseek/deepseek-r1:free"
    echo "  mistralai/devstral-small:free"
    echo "  google/gemini-2.0-flash-exp:free"
    echo "  meta-llama/llama-3.3-70b-instruct:free"
    echo "  ...and 10+ more!"
}

cmd_chat() {
    local message="$1"
    echo -e "${BLUE}Chatting with AI...${NC}"
    
    local data=$(jq -n \
        --arg msg "$message" \
        '{
            arguments: {
                prompt: $msg,
                model: "chat"
            }
        }')
    
    response=$(api_call "/tools/chat" POST "$data")
    echo "$response" | jq -r '.content' 2>/dev/null || echo "$response"
}

cmd_think() {
    local problem="$1"
    echo -e "${BLUE}Deep thinking about your problem...${NC}"
    
    local data=$(jq -n \
        --arg prob "$problem" \
        '{
            arguments: {
                current_analysis: $prob,
                model: "think"
            }
        }')
    
    response=$(api_call "/tools/thinkdeep" POST "$data")
    echo "$response" | jq -r '.content' 2>/dev/null || echo "$response"
}

cmd_review() {
    local file="$1"
    local review_type="${2:-full}"
    
    if [ ! -f "$file" ]; then
        echo -e "${RED}Error: File not found: $file${NC}"
        exit 1
    fi
    
    echo -e "${BLUE}Reviewing code...${NC}"
    
    local data=$(jq -n \
        --arg f "$file" \
        --arg rt "$review_type" \
        '{
            arguments: {
                files: [$f],
                review_type: $rt,
                model: "code"
            }
        }')
    
    response=$(api_call "/tools/codereview" POST "$data")
    echo "$response" | jq -r '.content' 2>/dev/null || echo "$response"
}

cmd_debug() {
    local error="$1"
    echo -e "${BLUE}Debugging error...${NC}"
    
    local data=$(jq -n \
        --arg err "$error" \
        '{
            arguments: {
                error_description: $err,
                model: "smart"
            }
        }')
    
    response=$(api_call "/tools/debug" POST "$data")
    echo "$response" | jq -r '.content' 2>/dev/null || echo "$response"
}

cmd_sessions() {
    echo -e "${BLUE}Active sessions:${NC}"
    response=$(api_call "/sessions" GET)
    echo "$response" | jq . 2>/dev/null || echo "$response"
}

# Main command router
case "${1:-help}" in
    start)
        cmd_start
        ;;
    stop)
        cmd_stop
        ;;
    logs)
        cmd_logs
        ;;
    health)
        cmd_health
        ;;
    genkey)
        cmd_genkey
        ;;
    tools)
        cmd_tools
        ;;
    models)
        cmd_models
        ;;
    chat)
        if [ -z "${2:-}" ]; then
            echo -e "${RED}Error: Please provide a message${NC}"
            echo "Usage: $0 chat \"Your message here\""
            exit 1
        fi
        cmd_chat "$2"
        ;;
    think)
        if [ -z "${2:-}" ]; then
            echo -e "${RED}Error: Please provide a problem to think about${NC}"
            echo "Usage: $0 think \"Your complex problem here\""
            exit 1
        fi
        cmd_think "$2"
        ;;
    review)
        if [ -z "${2:-}" ]; then
            echo -e "${RED}Error: Please provide a file to review${NC}"
            echo "Usage: $0 review /path/to/file.py [review_type]"
            exit 1
        fi
        cmd_review "$2" "${3:-full}"
        ;;
    debug)
        if [ -z "${2:-}" ]; then
            echo -e "${RED}Error: Please provide an error to debug${NC}"
            echo "Usage: $0 debug \"Error message here\""
            exit 1
        fi
        cmd_debug "$2"
        ;;
    sessions)
        cmd_sessions
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        echo -e "${RED}Unknown command: $1${NC}"
        echo ""
        show_help
        exit 1
        ;;
esac