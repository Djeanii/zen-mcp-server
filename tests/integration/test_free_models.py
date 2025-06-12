#!/usr/bin/env python3
"""Test script to verify FREE models work with OpenRouter."""

import asyncio
import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent.parent))

from providers.openrouter import OpenRouterModelProvider
from config import VALID_MODELS, MODEL_ALIASES


async def test_model(provider, model_name):
    """Test a single model."""
    print(f"\n🧪 Testing {model_name}...")
    
    try:
        response = await provider.generate_response(
            model_name=model_name,
            system_prompt="You are a helpful AI assistant.",
            user_prompt="Say 'Hello! I'm working!' in one line.",
            temperature=0.5
        )
        
        if response.content:
            print(f"✅ {model_name}: {response.content[:100]}...")
            return True
        else:
            print(f"❌ {model_name}: Empty response")
            return False
            
    except Exception as e:
        print(f"❌ {model_name}: {str(e)}")
        return False


async def main():
    """Test all free models."""
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("❌ Please set OPENROUTER_API_KEY environment variable")
        return
    
    print("🚀 Testing FREE models on OpenRouter...")
    print(f"API Key: {api_key[:10]}...{api_key[-4:]}")
    
    try:
        provider = OpenRouterModelProvider()
        print("✅ OpenRouter provider initialized")
    except Exception as e:
        print(f"❌ Failed to initialize provider: {e}")
        return
    
    # Test model aliases first
    print("\n📋 Testing Simple Model Aliases:")
    aliases_to_test = ["chat", "think", "code", "fast", "smart"]
    success_count = 0
    
    for alias in aliases_to_test:
        if alias in MODEL_ALIASES:
            full_model = MODEL_ALIASES[alias]
            print(f"\n  {alias} → {full_model}")
            if await test_model(provider, alias):
                success_count += 1
    
    print(f"\n✅ Aliases working: {success_count}/{len(aliases_to_test)}")
    
    # Test a few key free models
    print("\n📋 Testing Key Free Models:")
    key_models = [
        "qwen/qwen-2.5-coder-32b-instruct:free",
        "deepseek/deepseek-r1:free",
        "mistralai/devstral-small:free",
        "google/gemini-2.0-flash-exp:free",
        "meta-llama/llama-3.3-70b-instruct:free"
    ]
    
    model_success = 0
    for model in key_models:
        if await test_model(provider, model):
            model_success += 1
    
    print(f"\n✅ Models working: {model_success}/{len(key_models)}")
    print("\n🎉 Test complete!")
    
    if success_count + model_success == 0:
        print("\n⚠️  No models responded. Possible issues:")
        print("- Check your API key is valid")
        print("- You may have hit rate limits (50-1000/day for free tier)")
        print("- Try again in a few minutes")


if __name__ == "__main__":
    asyncio.run(main())