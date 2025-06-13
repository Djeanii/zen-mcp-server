"""OpenRouter provider for accessing free AI models."""

import asyncio
import logging
import os
from typing import Optional

import aiohttp

from config import MODEL_ALIASES
from providers.base import ModelCapabilities, ModelProvider, ModelResponse, ProviderType

logger = logging.getLogger(__name__)


class OpenRouterModelProvider(ModelProvider):
    """Provider for OpenRouter free tier models."""

    def __init__(self, api_key: str = None, **kwargs):
        """Initialize OpenRouter provider with API key."""
        # Allow API key to be passed in or read from environment
        if api_key:
            self.api_key = api_key
        else:
            self.api_key = os.getenv("OPENROUTER_API_KEY")
        
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY must be provided or set as environment variable")
        
        # Call parent constructor
        super().__init__(self.api_key, **kwargs)
        
        self.base_url = "https://openrouter.ai/api/v1"
        self.provider_type = ProviderType.OPENROUTER
        
        # Define supported models with their capabilities
        self.models = {
            # Chat models
            "qwen/qwen-2.5-coder-32b-instruct:free": ModelCapabilities(
                context_window=128000,
                supports_thinking_mode=False,
                supports_files=True,
                supports_functions=False,
                provider=self.provider_type,
            ),
            "meta-llama/llama-3.3-70b-instruct:free": ModelCapabilities(
                context_window=128000,
                supports_thinking_mode=False,
                supports_files=True,
                supports_functions=False,
                provider=self.provider_type,
            ),
            "mistralai/mistral-7b-instruct:free": ModelCapabilities(
                context_window=32000,
                supports_thinking_mode=False,
                supports_files=True,
                supports_functions=False,
                provider=self.provider_type,
            ),
            
            # Reasoning models
            "deepseek/deepseek-r1:free": ModelCapabilities(
                context_window=163000,
                supports_thinking_mode=True,  # Has open reasoning tokens
                supports_files=True,
                supports_functions=False,
                provider=self.provider_type,
            ),
            "qwen/qwq-32b:free": ModelCapabilities(
                context_window=32000,
                supports_thinking_mode=True,
                supports_files=True,
                supports_functions=False,
                provider=self.provider_type,
            ),
            "nvidia/llama-3.1-nemotron-ultra-253b-v1:free": ModelCapabilities(
                context_window=128000,
                supports_thinking_mode=False,
                supports_files=True,
                supports_functions=False,
                provider=self.provider_type,
            ),
            
            # Code models
            "mistralai/devstral-small:free": ModelCapabilities(
                context_window=128000,
                supports_thinking_mode=False,
                supports_files=True,
                supports_functions=False,
                provider=self.provider_type,
            ),
            
            # Fast models
            "google/gemini-2.0-flash-exp:free": ModelCapabilities(
                context_window=1000000,  # 1M context!
                supports_thinking_mode=False,
                supports_files=True,
                supports_functions=False,
                provider=self.provider_type,
            ),
            "google/gemma-2-9b-it:free": ModelCapabilities(
                context_window=8192,
                supports_thinking_mode=False,
                supports_files=True,
                supports_functions=False,
                provider=self.provider_type,
            ),
            
            # Extended models
            "deepseek/deepseek-chat:free": ModelCapabilities(
                context_window=64000,
                supports_thinking_mode=False,
                supports_files=True,
                supports_functions=False,
                provider=self.provider_type,
            ),
            "deepseek/deepseek-r1-0528:free": ModelCapabilities(
                context_window=32000,
                supports_thinking_mode=True,
                supports_files=True,
                supports_functions=False,
                provider=self.provider_type,
            ),
            "meta-llama/llama-3.2-3b-instruct:free": ModelCapabilities(
                context_window=128000,
                supports_thinking_mode=False,
                supports_files=True,
                supports_functions=False,
                provider=self.provider_type,
            ),
            "meta-llama/llama-3.3-8b-instruct:free": ModelCapabilities(
                context_window=128000,
                supports_thinking_mode=False,
                supports_files=True,
                supports_functions=False,
                provider=self.provider_type,
            ),
            "qwen/qwen-2.5-72b-instruct:free": ModelCapabilities(
                context_window=128000,
                supports_thinking_mode=False,
                supports_files=True,
                supports_functions=False,
                provider=self.provider_type,
            ),
            "qwen/qwen3-235b-a22b:free": ModelCapabilities(
                context_window=32000,
                supports_thinking_mode=False,
                supports_files=True,
                supports_functions=False,
                provider=self.provider_type,
            ),
        }

    def validate_model_name(self, model_name: str) -> bool:
        """Validate if the model name is supported by this provider."""
        # Resolve aliases
        if model_name in MODEL_ALIASES:
            model_name = MODEL_ALIASES[model_name]
        return model_name in self.models

    def supports_model(self, model_name: str) -> bool:
        """Check if this provider supports the given model (backward compatibility)."""
        return self.validate_model_name(model_name)

    def get_capabilities(self, model_name: str) -> ModelCapabilities:
        """Get capabilities for a specific model."""
        # Resolve aliases
        if model_name in MODEL_ALIASES:
            model_name = MODEL_ALIASES[model_name]
        
        if model_name not in self.models:
            raise ValueError(f"Model {model_name} not supported by OpenRouter provider")
        
        return self.models[model_name]

    def get_model_capabilities(self, model_name: str) -> Optional[ModelCapabilities]:
        """Get capabilities for a specific model (backward compatibility)."""
        try:
            return self.get_capabilities(model_name)
        except ValueError:
            return None

    async def _generate_content_async(
        self,
        prompt: str,
        model_name: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_output_tokens: Optional[int] = None,
        **kwargs
    ) -> ModelResponse:
        """Generate a response using OpenRouter API."""
        # Extract thinking_mode from kwargs if present
        thinking_mode = kwargs.get('thinking_mode', None)
        
        # Resolve aliases
        original_name = model_name
        if model_name in MODEL_ALIASES:
            model_name = MODEL_ALIASES[model_name]
            logger.info(f"Resolved model alias '{original_name}' to '{model_name}'")
        
        if not self.supports_model(original_name):
            raise ValueError(f"Model {model_name} not supported by OpenRouter provider")
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/zen-mcp-fork",
            "X-Title": "Zen MCP Fork"
        }
        
        # Build messages list
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        
        data = {
            "model": model_name,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_output_tokens or 8192,  # Use provided value or reasonable default
        }
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{self.base_url}/chat/completions",
                    headers=headers,
                    json=data,
                    timeout=aiohttp.ClientTimeout(total=300)  # 5 min timeout
                ) as response:
                    if response.status != 200:
                        error_text = await response.text()
                        logger.error(f"OpenRouter API error: {response.status} - {error_text}")
                        
                        # Handle rate limiting
                        if response.status == 429:
                            return ModelResponse(
                                content=f"Rate limit exceeded. Free tier allows 50-1000 requests/day. Try again later or use a different model.",
                                model_info={
                                    "model": model_name,
                                    "provider": "openrouter",
                                    "error": "rate_limit"
                                }
                            )
                        
                        return ModelResponse(
                            content=f"OpenRouter API error: {response.status} - {error_text}",
                            model_info={
                                "model": model_name,
                                "provider": "openrouter",
                                "error": error_text
                            }
                        )
                    
                    result = await response.json()
                    
                    # Extract response
                    if "choices" in result and len(result["choices"]) > 0:
                        content = result["choices"][0]["message"]["content"]
                        
                        # Check for thinking mode models (DeepSeek R1)
                        thinking_content = None
                        if "deepseek-r1" in model_name and thinking_mode:
                            # DeepSeek R1 includes reasoning in <think> tags
                            import re
                            think_match = re.search(r'<think>(.*?)</think>', content, re.DOTALL)
                            if think_match:
                                thinking_content = think_match.group(1).strip()
                                # Remove thinking from main content
                                content = re.sub(r'<think>.*?</think>', '', content, flags=re.DOTALL).strip()
                        
                        return ModelResponse(
                            content=content,
                            thinking_content=thinking_content,
                            model_info={
                                "model": model_name,
                                "provider": "openrouter",
                                "usage": result.get("usage", {}),
                                "thinking_mode": thinking_mode if thinking_content else None
                            }
                        )
                    else:
                        return ModelResponse(
                            content="No response generated",
                            model_info={
                                "model": model_name,
                                "provider": "openrouter",
                                "error": "empty_response"
                            }
                        )
                        
        except aiohttp.ClientError as e:
            logger.error(f"Network error calling OpenRouter: {e}")
            return ModelResponse(
                content=f"Network error: {str(e)}",
                model_info={
                    "model": model_name,
                    "provider": "openrouter",
                    "error": str(e)
                }
            )
        except Exception as e:
            logger.error(f"Unexpected error calling OpenRouter: {e}")
            return ModelResponse(
                content=f"Unexpected error: {str(e)}",
                model_info={
                    "model": model_name,
                    "provider": "openrouter",
                    "error": str(e)
                }
            )

    def generate_content(
        self,
        prompt: str,
        model_name: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_output_tokens: Optional[int] = None,
        **kwargs
    ) -> ModelResponse:
        """Generate content using the model (synchronous wrapper)."""
        # Get or create event loop
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            # No running loop, create a new one
            return asyncio.run(self._generate_content_async(
                prompt=prompt,
                model_name=model_name,
                system_prompt=system_prompt,
                temperature=temperature,
                max_output_tokens=max_output_tokens,
                **kwargs
            ))
        else:
            # We're already in an async context, create a task
            import concurrent.futures
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(
                    asyncio.run,
                    self._generate_content_async(
                        prompt=prompt,
                        model_name=model_name,
                        system_prompt=system_prompt,
                        temperature=temperature,
                        max_output_tokens=max_output_tokens,
                        **kwargs
                    )
                )
                return future.result()

    async def generate_response(
        self,
        model_name: str,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.7,
        thinking_mode: Optional[str] = None,
        **kwargs
    ) -> ModelResponse:
        """Generate a response using OpenRouter API (backward compatibility wrapper)."""
        return await self._generate_content_async(
            prompt=user_prompt,
            model_name=model_name,
            system_prompt=system_prompt,
            temperature=temperature,
            thinking_mode=thinking_mode,
            **kwargs
        )

    def validate_temperature(self, temperature: float) -> bool:
        """Validate temperature is within acceptable range."""
        return 0.0 <= temperature <= 2.0

    def get_temperature_range(self) -> tuple[float, float]:
        """Get valid temperature range for this provider."""
        return (0.0, 2.0)

    def count_tokens(self, text: str, model_name: str) -> int:
        """Count tokens for the given text using the specified model's tokenizer."""
        # For now, use a simple estimation similar to other providers
        # Rough estimation: ~4 characters per token for English text
        # Note: model_name parameter is required by base class but not used in estimation
        return len(text) // 4

    def get_provider_type(self) -> ProviderType:
        """Get the provider type."""
        return ProviderType.OPENROUTER

    def supports_thinking_mode(self, model_name: str) -> bool:
        """Check if the model supports extended thinking mode."""
        # Resolve aliases
        if model_name in MODEL_ALIASES:
            model_name = MODEL_ALIASES[model_name]
        
        # Check if model exists and supports thinking
        if model_name in self.models:
            return self.models[model_name].supports_thinking_mode
        return False