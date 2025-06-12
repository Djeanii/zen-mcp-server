"""OpenRouter provider for free tier models."""
import os
import logging
import aiohttp
import json
from typing import Optional, Dict, Any

from .base import ModelProvider, ModelResponse, ProviderType

logger = logging.getLogger(__name__)


class OpenRouterModelProvider(ModelProvider):
    """Provider for OpenRouter free tier models."""
    
    def __init__(self):
        """Initialize the OpenRouter provider."""
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY environment variable is required")
        super().__init__(api_key=self.api_key)
        
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "HTTP-Referer": "https://github.com/BeehiveInnovations/zen-mcp-server",
            "X-Title": "Zen MCP Server"
        }
    
    @property
    def provider_type(self) -> ProviderType:
        """Return the provider type."""
        return ProviderType.OPENROUTER
    
    def supports_model(self, model_name: str) -> bool:
        """Check if this provider supports the given model."""
        # Support models ending with -free suffix
        return model_name.endswith("-free")
    
    async def generate_response(
        self,
        model_name: str,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.7,
        thinking_mode: Optional[str] = None,
        **kwargs
    ) -> ModelResponse:
        """Generate a response using OpenRouter's free tier models."""
        
        # Map our simplified names to OpenRouter model IDs
        model_mapping = {
            "qwen-coder-free": "qwen/qwen-2.5-coder-32b-instruct:free",
            "deepseek-r1-free": "deepseek/deepseek-r1:free",
            "mistral-devstral-free": "mistralai/devstral-small:free",
            "gemini-flash-free": "google/gemini-2.0-flash-exp:free",
            "llama-70b-free": "meta-llama/llama-3.3-70b-instruct:free",
            "qwq-32b-free": "qwen/qwq-32b:free",
            "nemotron-free": "nvidia/llama-3.1-nemotron-ultra-253b-v1:free"
        }
        
        # Get the actual model ID
        actual_model = model_mapping.get(model_name, model_name)
        
        # Ensure it has :free suffix if not already present
        if not actual_model.endswith(":free"):
            actual_model += ":free"
        
        logger.debug(f"Using OpenRouter model: {actual_model}")
        
        # Build the request
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        
        request_data = {
            "model": actual_model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": 4096  # Reasonable default for free tier
        }
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    self.base_url,
                    headers=self.headers,
                    json=request_data,
                    timeout=aiohttp.ClientTimeout(total=120)
                ) as response:
                    
                    if response.status == 429:
                        # Rate limit hit
                        return ModelResponse(
                            content="Rate limit exceeded. Free tier models have daily limits (50-1000 requests). Try again later or use a different free model.",
                            model_info={"error": "rate_limit", "model": actual_model}
                        )
                    
                    if response.status != 200:
                        error_text = await response.text()
                        logger.error(f"OpenRouter API error: {response.status} - {error_text}")
                        return ModelResponse(
                            content=f"OpenRouter API error: {response.status}",
                            model_info={"error": error_text}
                        )
                    
                    data = await response.json()
                    
                    # Extract the response
                    if "choices" in data and len(data["choices"]) > 0:
                        content = data["choices"][0]["message"]["content"]
                        
                        # Handle thinking tokens if present (for models like DeepSeek R1)
                        thinking_content = None
                        if "thinking_content" in data["choices"][0]["message"]:
                            thinking_content = data["choices"][0]["message"]["thinking_content"]
                        
                        model_info = {
                            "model": actual_model,
                            "usage": data.get("usage", {}),
                            "thinking_content": thinking_content
                        }
                        
                        return ModelResponse(
                            content=content,
                            model_info=model_info
                        )
                    else:
                        return ModelResponse(
                            content="No response from model",
                            model_info={"error": "empty_response"}
                        )
                        
        except aiohttp.ClientTimeout:
            return ModelResponse(
                content="Request timed out. Free tier models may be under heavy load. Try again later.",
                model_info={"error": "timeout"}
            )
        except Exception as e:
            logger.error(f"OpenRouter request failed: {str(e)}")
            return ModelResponse(
                content=f"Error calling OpenRouter: {str(e)}",
                model_info={"error": str(e)}
            )
    
    async def count_tokens(self, text: str, model: Optional[str] = None) -> int:
        """Estimate token count for the given text."""
        # Simple estimation: ~4 characters per token
        # OpenRouter doesn't provide a token counting endpoint for free tier
        return len(text) // 4