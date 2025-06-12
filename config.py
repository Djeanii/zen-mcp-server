"""
Configuration and constants for Zen MCP Server

This module centralizes all configuration settings for the Zen MCP Server.
It defines model configurations, token limits, temperature defaults, and other
constants used throughout the application.

Configuration values can be overridden by environment variables where appropriate.
"""

import os

# Version and metadata
# These values are used in server responses and for tracking releases
# IMPORTANT: This is the single source of truth for version and author info
__version__ = "4.0.0"  # Semantic versioning: MAJOR.MINOR.PATCH
__updated__ = "2025-06-12"  # Last update date in ISO format
__author__ = "Fahad Gilani"  # Primary maintainer

# Model configuration
# DEFAULT_MODEL: The default model used for all AI operations
# This should be a stable, high-performance model suitable for code analysis
# Can be overridden by setting DEFAULT_MODEL environment variable
# Special value "auto" means Claude should pick the best model for each task
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "auto")

# Validate DEFAULT_MODEL and set to "auto" if invalid
# Only include actually supported models from providers
VALID_MODELS = [
    "auto",  # Let Claude pick the best model
    
    # General Purpose / Chat (Best Balance)
    "qwen/qwen-2.5-coder-32b-instruct:free",  # Best overall balance
    "mistralai/mistral-7b-instruct:free",     # Fast, lightweight
    "meta-llama/llama-3.3-70b-instruct:free", # Most capable free chat
    
    # Advanced Reasoning / Thinking
    "deepseek/deepseek-r1:free",                      # Top reasoning (671B)
    "qwen/qwq-32b:free",                              # Strong reasoning, good speed
    "nvidia/llama-3.1-nemotron-ultra-253b-v1:free",  # NVIDIA enhanced reasoning
    
    # Code Specialized
    "mistralai/devstral-small:free",          # Code specialist (SWE-Bench 46.8%)
    "meta-llama/llama-3.2-3b-instruct:free",  # Tiny but capable for simple tasks
    
    # Fast Processing
    "google/gemini-2.0-flash-exp:free",       # 1M context, ultra-fast
    "google/gemma-2-9b-it:free",               # Google's efficient model
    
    # Extended Context
    "deepseek/deepseek-chat:free",            # Good code + conversation (64K)
    "deepseek/deepseek-r1-0528:free",         # Updated R1 variant
    
    # Additional Options
    "meta-llama/llama-3.3-8b-instruct:free",  # Smaller Llama 3.3
    "qwen/qwen-2.5-72b-instruct:free",        # Large Qwen model
    "qwen/qwen3-235b-a22b:free",              # Massive multilingual
    
    # Legacy shortcuts (map to free models)
    "flash",  # maps to google/gemini-2.0-flash-exp:free
    "pro",    # maps to deepseek/deepseek-r1:free
    "o3",     # maps to qwen/qwq-32b:free
    "o3-mini",# maps to mistralai/mistral-7b-instruct:free
]

# Model aliases for simple names
MODEL_ALIASES = {
    # Simple names that map to best free models
    "chat": "qwen/qwen-2.5-coder-32b-instruct:free",
    "think": "deepseek/deepseek-r1:free",
    "code": "mistralai/devstral-small:free",
    "fast": "google/gemini-2.0-flash-exp:free",
    "smart": "meta-llama/llama-3.3-70b-instruct:free",
    
    # Legacy shortcuts
    "flash": "google/gemini-2.0-flash-exp:free",
    "pro": "deepseek/deepseek-r1:free",
    "o3": "qwen/qwq-32b:free",
    "o3-mini": "mistralai/mistral-7b-instruct:free",
}
if DEFAULT_MODEL not in VALID_MODELS:
    import logging

    logger = logging.getLogger(__name__)
    logger.warning(
        f"Invalid DEFAULT_MODEL '{DEFAULT_MODEL}'. Setting to 'auto'. Valid options: {', '.join(VALID_MODELS)}"
    )
    DEFAULT_MODEL = "auto"

# Auto mode detection - when DEFAULT_MODEL is "auto", Claude picks the model
IS_AUTO_MODE = DEFAULT_MODEL.lower() == "auto"

# Model capabilities descriptions for auto mode
# These help Claude choose the best model for each task
MODEL_CAPABILITIES_DESC = {
    # Simple aliases
    "chat": "Qwen 2.5 Coder (32B, 128K) - Best overall balance for chat + code",
    "think": "DeepSeek R1 (671B, 163K) - Top reasoning with open thinking tokens",
    "code": "Mistral Devstral (SWE-Bench 46.8%) - Specialized for code tasks",
    "fast": "Gemini Flash (1M context) - Ultra-fast for large documents",
    "smart": "Llama 3.3 (70B, 128K) - High-quality general conversation",
    
    # Legacy shortcuts
    "flash": "Gemini Flash FREE (1M context) - Ultra-fast, huge context",
    "pro": "DeepSeek R1 FREE (671B, 163K) - Deep reasoning + thinking",
    "o3": "Qwen QwQ FREE (32B) - Step-by-step reasoning",
    "o3-mini": "Mistral 7B FREE - Fast lightweight model",
    
    # Full model names
    "qwen/qwen-2.5-coder-32b-instruct:free": "Best overall - Chat + code (128K context)",
    "deepseek/deepseek-r1:free": "Top reasoning (671B params, 163K context)",
    "mistralai/devstral-small:free": "Code specialist (SWE-Bench 46.8%)",
    "google/gemini-2.0-flash-exp:free": "Ultra-fast (1M context window!)",
    "meta-llama/llama-3.3-70b-instruct:free": "High-quality chat (128K context)",
    "qwen/qwq-32b:free": "Strong reasoning with good speed",
    "nvidia/llama-3.1-nemotron-ultra-253b-v1:free": "NVIDIA enhanced reasoning",
    "mistralai/mistral-7b-instruct:free": "Fast, lightweight",
    "meta-llama/llama-3.2-3b-instruct:free": "Tiny but capable",
    "google/gemma-2-9b-it:free": "Google's efficient model",
    "deepseek/deepseek-chat:free": "Good code + conversation",
    "deepseek/deepseek-r1-0528:free": "Updated DeepSeek R1",
    "meta-llama/llama-3.3-8b-instruct:free": "Smaller Llama 3.3",
    "qwen/qwen-2.5-72b-instruct:free": "Large Qwen model",
    "qwen/qwen3-235b-a22b:free": "Massive multilingual",
}

# Token allocation for Gemini Pro (1M total capacity)
# MAX_CONTEXT_TOKENS: Total model capacity
# MAX_CONTENT_TOKENS: Available for prompts, conversation history, and files
# RESPONSE_RESERVE_TOKENS: Reserved for model response generation
MAX_CONTEXT_TOKENS = 1_000_000  # 1M tokens total capacity for Gemini Pro
MAX_CONTENT_TOKENS = 800_000  # 800K tokens for content (prompts + files + history)
RESPONSE_RESERVE_TOKENS = 200_000  # 200K tokens reserved for response generation

# Temperature defaults for different tool types
# Temperature controls the randomness/creativity of model responses
# Lower values (0.0-0.3) produce more deterministic, focused responses
# Higher values (0.7-1.0) produce more creative, varied responses

# TEMPERATURE_ANALYTICAL: Used for tasks requiring precision and consistency
# Ideal for code review, debugging, and error analysis where accuracy is critical
TEMPERATURE_ANALYTICAL = 0.2  # For code review, debugging

# TEMPERATURE_BALANCED: Middle ground for general conversations
# Provides a good balance between consistency and helpful variety
TEMPERATURE_BALANCED = 0.5  # For general chat

# TEMPERATURE_CREATIVE: Higher temperature for exploratory tasks
# Used when brainstorming, exploring alternatives, or architectural discussions
TEMPERATURE_CREATIVE = 0.7  # For architecture, deep thinking

# Thinking Mode Defaults
# DEFAULT_THINKING_MODE_THINKDEEP: Default thinking depth for extended reasoning tool
# Higher modes use more computational budget but provide deeper analysis
DEFAULT_THINKING_MODE_THINKDEEP = os.getenv("DEFAULT_THINKING_MODE_THINKDEEP", "high")

# MCP Protocol Limits
# MCP_PROMPT_SIZE_LIMIT: Maximum character size for prompts sent directly through MCP
# The MCP protocol has a combined request+response limit of ~25K tokens.
# To ensure we have enough space for responses, we limit direct prompt input
# to 50K characters (roughly ~10-12K tokens). Larger prompts must be sent
# as files to bypass MCP's token constraints.
MCP_PROMPT_SIZE_LIMIT = 50_000  # 50K characters

# Threading configuration
# Simple Redis-based conversation threading for stateless MCP environment
# Set REDIS_URL environment variable to connect to your Redis instance
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
