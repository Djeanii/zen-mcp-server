# 🆓 Free Models Guide - zen-mcp-fork

All models in this project are **100% FREE** on OpenRouter. No paid models included!

## 🎯 Simple Model Names (NEW!)

Instead of complex model names, just use these simple aliases:
- **`chat`** → Qwen 2.5 Coder (best overall, 128K context)
- **`think`** → DeepSeek R1 (671B reasoning, 163K context)
- **`code`** → Mistral Devstral (code specialist, SWE-Bench 46.8%)
- **`fast`** → Gemini Flash (ultra-fast, 1M context!)
- **`smart`** → Llama 3.3 (high-quality, 128K context)

## Quick Start Examples

### With Claude Code (Easiest!)
```
"chat about Python async/await"
"think about distributed cache design"
"code review this function"
"fast analysis of this error"
"smart suggestions for optimization"
```

### With CLI (Advanced mode)
```bash
./zen-cli.sh chat "Explain Redis pub/sub"
./zen-cli.sh think "Design a distributed system"
./zen-cli.sh review /path/to/file.py
```

### With REST API (Development mode - no auth needed!)
```bash
curl -X POST http://localhost:8765/tools/chat \
  -H "Content-Type: application/json" \
  -d '{
    "arguments": {
      "prompt": "Quick Python question",
      "model": "fast"
    }
  }'
# Great for: Quick queries, large documents
```

## Complete Free Model List

### Top Tier Models (Recommended)
| Model | Context | Best For |
|-------|---------|----------|
| `qwen/qwen-2.5-coder-32b-instruct:free` | 128K | General chat + code |
| `deepseek/deepseek-r1:free` | 163K | Deep reasoning (671B params!) |
| `mistralai/devstral-small:free` | 128K | Code generation/review |
| `google/gemini-2.0-flash-exp:free` | 1M | Fast responses, huge context |
| `meta-llama/llama-3.3-70b-instruct:free` | 128K | High-quality chat |

### Additional Quality Models
| Model | Context | Special Features |
|-------|---------|------------------|
| `qwen/qwq-32b:free` | 32K | Step-by-step reasoning |
| `nvidia/llama-3.1-nemotron-ultra-253b-v1:free` | 128K | NVIDIA's enhanced Llama |
| `deepseek/deepseek-chat:free` | 64K | Good code + conversation |
| `meta-llama/llama-3.2-3b-instruct:free` | 128K | Tiny but capable |
| `mistralai/mistral-7b-instruct:free` | 32K | Fast, reliable |

### Extended List
- `deepseek/deepseek-r1-0528:free` - Updated DeepSeek R1
- `meta-llama/llama-3.3-8b-instruct:free` - Smaller Llama 3.3
- `qwen/qwen-2.5-72b-instruct:free` - Large Qwen model
- `google/gemma-2-9b-it:free` - Google's efficient model
- `qwen/qwen3-235b-a22b:free` - Massive multilingual

## Testing Models

Run the included test script to verify which models are currently available:

```bash
cd /path/to/zen-mcp-fork
python tests/integration/test_free_models.py
```

## Rate Limits

Free models have rate limits:
- **New users**: 50 requests/day total
- **After purchasing 10+ credits**: 1000 requests/day total

If you hit rate limits, try:
1. Different free models
2. Wait a bit and retry
3. Consider purchasing minimal credits to increase limits

## Model Selection in Code

### Auto Mode (Default)
```python
# Let Claude pick the best model
"model": "auto"
```

### Specific Model
```python
# Use a specific free model
"model": "qwen/qwen-2.5-coder-32b-instruct:free"
```

### Legacy Shortcuts
The system maps legacy shortcuts to free models:
- `"flash"` → `google/gemini-2.0-flash-exp:free`
- `"pro"` → `deepseek/deepseek-r1:free`
- `"o3"` → `qwen/qwq-32b:free`
- `"o3-mini"` → `mistralai/mistral-7b-instruct:free`

## Environment Variables

Set defaults in your `.env`:
```bash
# Default to best free chat model
DEFAULT_MODEL=qwen/qwen-2.5-coder-32b-instruct:free

# Or let Claude auto-select
DEFAULT_MODEL=auto
```

## Troubleshooting

### Model Not Found
- Ensure you're using the exact model ID with `:free` suffix
- Check if model is temporarily unavailable
- Run test script to see current availability

### Rate Limited
- Free tier has low limits (50-1000 req/day)
- Try different models
- Space out requests

### Empty Responses
- Some models may be overloaded
- Try alternative models from same category
- Check your API key is valid

## No Hidden Costs!

✅ All models listed here are **100% FREE** on OpenRouter  
✅ No credit card required  
✅ No paid models in codebase  
✅ Full functionality with free tier  

Just set your `OPENROUTER_API_KEY` and start using powerful AI models for free!