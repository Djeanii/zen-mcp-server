#!/bin/bash

# Quick start script for zen-mcp-fork - gets you running in seconds!
set -euo pipefail

echo "🚀 Zen MCP Quick Start - 100% FREE AI Models!"
echo "=============================================="
echo ""

# Check for OpenRouter API key
if [ -z "${OPENROUTER_API_KEY:-}" ]; then
    echo "❌ No OpenRouter API key found!"
    echo ""
    echo "To get started:"
    echo "1. Get your FREE key at: https://openrouter.ai/keys"
    echo "   (No credit card required!)"
    echo ""
    echo "2. Set your key:"
    echo "   export OPENROUTER_API_KEY=sk-or-v1-your-key-here"
    echo ""
    echo "3. Run this script again"
    echo ""
    exit 1
fi

echo "✅ OpenRouter API key found!"
echo ""

# Check if Docker is running
if ! docker info &> /dev/null; then
    echo "❌ Docker is not running. Please start Docker Desktop first."
    exit 1
fi

# Auto-create .env if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating configuration..."
    cat > .env << EOF
# Auto-generated configuration
OPENROUTER_API_KEY=${OPENROUTER_API_KEY}

# Development mode - no auth needed for localhost
PRODUCTION=false

# Auto-generated secure keys (only used in production)
ZEN_API_KEY=$(python3 -c "import secrets; print(secrets.token_urlsafe(32))" 2>/dev/null || echo "auto-generated-key")
REDIS_PASSWORD=$(python3 -c "import secrets; print(secrets.token_urlsafe(16))" 2>/dev/null || echo "auto-generated-pass")

# Smart defaults
DEFAULT_MODEL=auto
LOG_LEVEL=INFO
WORKSPACE_ROOT=${HOME}
EOF
    echo "✅ Configuration created!"
else
    echo "✅ Using existing configuration"
fi

# Parse command line arguments
ADVANCED_MODE=false
PRODUCTION_MODE=false

for arg in "$@"; do
    case $arg in
        --advanced)
            ADVANCED_MODE=true
            shift
            ;;
        --production)
            PRODUCTION_MODE=true
            shift
            ;;
        --help)
            echo "Usage: ./quickstart.sh [options]"
            echo ""
            echo "Options:"
            echo "  --advanced    Enable REST API and CLI tools"
            echo "  --production  Enable production security"
            echo "  --help        Show this help"
            echo ""
            exit 0
            ;;
    esac
done

# Update production flag if needed
if [ "$PRODUCTION_MODE" = true ]; then
    sed -i.bak 's/PRODUCTION=false/PRODUCTION=true/' .env && rm -f .env.bak
    echo "🔒 Production mode enabled (auth required)"
fi

# Simple MCP-only mode by default
if [ "$ADVANCED_MODE" = false ]; then
    echo "🚀 Starting in Simple Mode (MCP only)..."
    
    # Build if needed
    if [ ! "$(docker images -q zen-mcp-server:latest 2> /dev/null)" ]; then
        echo "📦 Building Docker image (one-time setup)..."
        docker build -t zen-mcp-server:latest . > /dev/null 2>&1
    fi
    
    # Start minimal setup
    docker run -d \
        --name zen-mcp-server \
        --env-file .env \
        -v "${HOME}:/workspace:ro" \
        --restart unless-stopped \
        zen-mcp-server:latest > /dev/null 2>&1 || true
    
    echo "✅ Simple mode started!"
    echo ""
    echo "📋 Next Steps:"
    echo "1. Add to Claude Code:"
    echo "   claude mcp add zen -s user -- docker exec -i zen-mcp-server python server.py"
    echo ""
    echo "2. Start using FREE models:"
    echo '   "chat about Python"  → Uses best free chat model'
    echo '   "think about my architecture"  → Uses DeepSeek R1 (671B!)'
    echo '   "review my code"  → Uses Mistral Devstral'
    echo ""
    echo "💡 For REST API and CLI tools, run: ./quickstart.sh --advanced"
    
else
    echo "🚀 Starting in Advanced Mode (with REST API)..."
    
    # Use docker-compose for full setup
    docker-compose -f docker-compose.persistent.yml up -d --build
    
    echo "✅ Advanced mode started!"
    echo ""
    echo "📋 Available tools:"
    echo "• Claude Code MCP: claude mcp add zen -s user -- docker exec -i zen-mcp-server python server.py"
    echo "• REST API: http://localhost:8765"
    echo "• CLI: ./zen-cli.sh chat 'Hello!'"
    echo ""
    
    if [ "$PRODUCTION_MODE" = false ]; then
        echo "🔓 Development mode - no auth needed for REST API"
    else
        echo "🔒 Production mode - use this header for REST API:"
        echo "   Authorization: Bearer $(grep ZEN_API_KEY .env | cut -d'=' -f2)"
    fi
fi

echo ""
echo "✨ Enjoy your FREE AI models!"
echo "📚 Full docs: https://github.com/[your-username]/zen-mcp-fork"