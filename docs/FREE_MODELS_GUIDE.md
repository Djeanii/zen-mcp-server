# FREE MODELS GUIDE - Zero API Costs! 🆓

**Updated**: 2025-06-20  
**Status**: 100% FREE operation with powerful AI models

This guide details the curated free models available in this Zen MCP server configuration. All models are completely free through OpenRouter with **ZERO API COSTS**.

## 🚀 Top-Tier Free Models

### 1. DeepSeek R1 (Advanced Reasoning)
- **Model ID**: `deepseek/deepseek-r1:free`
- **Aliases**: `reasoning`, `r1`, `deepseek`, `thinking`, `opus`
- **Context**: 163K tokens
- **Parameters**: 671B (massive!)
- **Features**: ✅ Extended thinking mode, ✅ JSON mode, ✅ Function calling
- **Best For**: Complex reasoning, debugging, deep analysis, strategic thinking
- **Special**: Thinking mode provides detailed reasoning process

### 2. Google Gemini 2.0 Flash (Ultra-Fast + Huge Context)
- **Model ID**: `google/gemini-2.0-flash-exp:free`
- **Aliases**: `flash`, `fast`, `gemini-flash`, `gemini-fast`
- **Context**: 1M tokens (1,000,000!)
- **Features**: ✅ JSON mode, ✅ Function calling, ✅ Images, ✅ Ultra-fast
- **Best For**: Large documents, fast responses, image analysis, quick tasks
- **Special**: Experimental model with massive context window

### 3. Qwen 2.5 Coder (Code Specialist)
- **Model ID**: `qwen/qwen-2.5-coder-32b-instruct:free`
- **Aliases**: `coder`, `code`, `qwen-coder`, `qwen-free`
- **Context**: 128K tokens
- **Parameters**: 32B
- **Features**: ✅ JSON mode, ✅ Function calling, specialized for code
- **Best For**: Code generation, code review, debugging, refactoring
- **Special**: Fine-tuned specifically for programming tasks

### 4. Mistral Devstral (Code Development)
- **Model ID**: `mistralai/devstral-small:free`
- **Aliases**: `devstral`, `mistral`, `mistral-dev`
- **Context**: 128K tokens
- **Features**: ✅ JSON mode, ✅ Function calling
- **Best For**: Code generation, development workflows, technical tasks
- **Special**: Optimized for development and coding tasks

### 5. Llama 3.3 70B (High-Quality Chat)
- **Model ID**: `meta-llama/llama-3.3-70b-instruct:free`
- **Aliases**: `llama`, `chat`, `pro`, `general`, `sonnet`
- **Context**: 128K tokens
- **Parameters**: 70B
- **Features**: ✅ JSON mode, ✅ Function calling, excellent for general chat
- **Best For**: General conversation, writing, analysis, balanced tasks
- **Special**: Latest Llama model with strong performance across domains

## 📋 Quick Reference Table

| Model | Alias | Context | Params | Thinking | Images | Best Use Case |
|-------|-------|---------|--------|----------|--------|---------------|
| DeepSeek R1 | `reasoning` | 163K | 671B | ✅ | ❌ | Complex reasoning |
| Gemini Flash | `flash` | 1M | - | ❌ | ✅ | Fast + huge context |
| Qwen Coder | `coder` | 128K | 32B | ❌ | ❌ | Code generation |
| Devstral | `mistral` | 128K | - | ❌ | ❌ | Development tasks |
| Llama 3.3 | `pro` | 128K | 70B | ❌ | ❌ | General chat |

## 🛠️ Tool-Specific Recommendations

### For thinkdeep (Extended Thinking)
- **Complex problems**: `reasoning` (DeepSeek R1 with thinking mode)
- **Quick analysis**: `flash` (Gemini Flash for speed)
- **Balanced**: `pro` (Llama 3.3 for general reasoning)

### For codereview (Code Review)
- **Code-focused**: `coder` (Qwen Coder specialization)
- **Complex logic**: `reasoning` (DeepSeek R1 for deep analysis)
- **Development**: `mistral` (Devstral for dev workflows)

### For debug (Debugging)
- **Complex bugs**: `reasoning` (DeepSeek R1 thinking mode)
- **Quick fixes**: `flash` (Gemini Flash for speed)
- **Code issues**: `coder` (Qwen Coder for code understanding)

### For chat (General Discussion)
- **General chat**: `pro` (Llama 3.3 balanced performance)
- **Quick responses**: `flash` (Gemini Flash ultra-fast)
- **Technical discussion**: `coder` (Qwen for technical topics)

## 🔧 Configuration Details

### Model Selection in Auto Mode
When using `DEFAULT_MODEL=auto`, the system intelligently selects:
1. **Complex reasoning tasks** → DeepSeek R1 (`reasoning`)
2. **Fast responses needed** → Gemini Flash (`flash`)
3. **Code-related tasks** → Qwen Coder (`coder`)
4. **General tasks** → Llama 3.3 (`pro`)
5. **Development work** → Mistral Devstral (`mistral`)

### Custom Model Usage
You can specify exact models in any tool:
```bash
# Use specific model by alias
mcp_zen_chat --model reasoning "Complex analysis question"
mcp_zen_codereview --model coder path/to/code.py
mcp_zen_debug --model flash "Quick debugging task"
```

## 💡 Pro Tips

### 1. Context Window Optimization
- **Large documents/files**: Use `flash` (1M context)
- **Standard tasks**: Use `reasoning` (163K) or others (128K)
- **Multiple files**: Prefer `flash` for massive context needs

### 2. Speed vs Quality Trade-offs
- **Need speed**: `flash` → ultra-fast responses
- **Need depth**: `reasoning` → thinking mode with detailed analysis
- **Need balance**: `pro` → good quality with reasonable speed

### 3. Task-Specific Selection
- **Code tasks**: `coder` > `mistral` > `reasoning`
- **Analysis tasks**: `reasoning` > `pro` > `flash`
- **Quick tasks**: `flash` > `pro` > others
- **Writing tasks**: `pro` > `reasoning` > `flash`

## 🎯 Cost Comparison

| Our Free Setup | Typical Paid Setup | Savings |
|----------------|-------------------|---------|
| DeepSeek R1 (FREE) | Claude 3 Opus ($15/1M) | $15/1M tokens |
| Gemini Flash (FREE) | GPT-4 Turbo ($10/1M) | $10/1M tokens |
| Qwen Coder (FREE) | Claude 3.5 Sonnet ($3/1M) | $3/1M tokens |
| All models (FREE) | Typical setup ($28+/1M) | **100% savings** |

## 📊 Performance Benchmarks

Based on community testing and real-world usage:

- **DeepSeek R1**: Matches GPT-4o performance on reasoning tasks
- **Gemini Flash**: Faster than GPT-4 Turbo, comparable quality
- **Qwen Coder**: Competitive with CodeLlama and Claude for coding
- **Llama 3.3**: Strong general performance, reliable for most tasks

## 🔄 Updates & Maintenance

### Staying Current
- Free model availability can change - check OpenRouter periodically
- New free models are added regularly to OpenRouter
- This configuration prioritizes stability with proven free models

### Adding New Free Models
1. Check OpenRouter for new `:free` models
2. Update `/conf/custom_models.json`
3. Add appropriate aliases
4. Test with quality checks: `./code_quality_checks.sh`

---

**Result**: World-class AI capabilities with zero ongoing costs! 🎉