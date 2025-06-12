# 🆓 Zen MCP Fork: 100% FREE AI Models!

https://github.com/user-attachments/assets/8097e18e-b926-4d8b-ba14-a979e4c58bda

<div align="center">  
  <b>🤖 One Context. Many Minds. Zero Cost. 🆓</b>
  <br/>
  <i>✨ Access 15+ powerful AI models - No credit card required! ✨</i>
  <br/><br/>
  <b>📖 New to this? Start with the <a href="README_SIMPLE.md">Simple Guide</a> for 2-minute setup!</b>
</div>

<br/>

A secure, production-ready Model Context Protocol (MCP) server that provides access to **100% FREE** AI models through OpenRouter. 
Get the power of **DeepSeek R1 (671B)**, **Qwen 2.5 Coder**, **Llama 3.3**, **Mistral Devstral**, and more - all completely FREE!

**Features true AI orchestration with conversations that continue across tasks** - Give Claude a complex
task and let it orchestrate between models automatically. Claude stays in control, performs the actual work, 
but gets perspectives from the best AI for each subtask. Claude can switch between different tools _and_ models mid-conversation, 
with context carrying forward seamlessly.

**Example Workflow - Claude Code:**
1. Performs its own reasoning
2. Uses Qwen 2.5 Coder to deeply [`analyze`](#6-analyze---smart-file-analysis) the code in question for a second opinion
3. Switches to DeepSeek R1 to continue [`chatting`](#1-chat---general-development-chat--collaborative-thinking) about its findings 
4. Uses Gemini Flash FREE to evaluate formatting suggestions from DeepSeek
5. Performs the actual work after taking in feedback from all three
6. Returns to Mistral Devstral for a [`precommit`](#4-precommit---pre-commit-validation) review

All within a single conversation thread! Mistral Devstral in step 6 _knows_ what was recommended by DeepSeek R1 in step 3! Taking that context
and review into consideration to aid with its pre-commit review.

**Think of it as Claude Code _for_ Claude Code.** This MCP isn't magic. It's just **super-glue**.

## Quick Navigation

- **Getting Started**
  - [Quickstart](#quickstart-5-minutes) - Get running in 5 minutes with Docker
  - [Available Tools](#available-tools) - Overview of all tools
  - [AI-to-AI Conversations](#ai-to-ai-conversation-threading) - Multi-turn conversations

- **Tools Reference**
  - [`chat`](#1-chat---general-development-chat--collaborative-thinking) - Collaborative thinking
  - [`thinkdeep`](#2-thinkdeep---extended-reasoning-partner) - Extended reasoning
  - [`codereview`](#3-codereview---professional-code-review) - Code review
  - [`precommit`](#4-precommit---pre-commit-validation) - Pre-commit validation
  - [`debug`](#5-debug---expert-debugging-assistant) - Debugging help
  - [`analyze`](#6-analyze---smart-file-analysis) - File analysis

- **Advanced Topics**
  - [Model Configuration](#model-configuration) - Auto mode & multi-provider selection
  - [Thinking Modes](#thinking-modes---managing-token-costs--quality) - Control depth vs cost
  - [Working with Large Prompts](#working-with-large-prompts) - Bypass MCP's 25K token limit
  - [Web Search Integration](#web-search-integration) - Smart search recommendations
  - [Collaborative Workflows](#collaborative-workflows) - Multi-tool patterns
  - [Tool Parameters](#tool-parameters) - Detailed parameter reference
  - [Docker Architecture](#docker-architecture) - How Docker integration works

- **Resources**
  - [Windows Setup](#windows-setup-guide) - WSL setup instructions for Windows
  - [Troubleshooting](#troubleshooting) - Common issues and solutions
  - [Testing](#testing) - Running tests

## Why This Server?

Claude is brilliant, but sometimes you need:
- **Multiple AI perspectives** - Let Claude orchestrate between different models to get the best analysis
- **Cost-effective AI access** - Use FREE tier models via OpenRouter for most tasks (default: google/gemini-2.0-flash-exp:free)
- **Access to 20+ models** - OpenRouter integration provides Claude, GPT-4, Llama, Mistral, DeepSeek, and more through a single API
- **Automatic model selection** - Claude picks the right model for each task (or you can specify)
- **A senior developer partner** to validate and extend ideas ([`chat`](#1-chat---general-development-chat--collaborative-thinking))
- **A second opinion** on complex architectural decisions - augment Claude's thinking with perspectives from DeepSeek R1, Qwen, or others ([`thinkdeep`](#2-thinkdeep---extended-reasoning-partner))
- **Professional code reviews** with actionable feedback across entire repositories ([`codereview`](#3-codereview---professional-code-review))
- **Pre-commit validation** with deep analysis using the best model for the job ([`precommit`](#4-precommit---pre-commit-validation))
- **Expert debugging** - Qwen for logical issues, DeepSeek for architectural problems ([`debug`](#5-debug---expert-debugging-assistant))
- **Extended context windows beyond Claude's limits** - Delegate analysis to Gemini Flash (1M tokens) or DeepSeek R1 (163K tokens) for entire codebases, large datasets, or comprehensive documentation
- **Model-specific strengths** - Extended thinking with DeepSeek R1, fast iteration with Gemini Flash, strong reasoning with Qwen
- **Dynamic collaboration** - Models can request additional context and follow-up replies from Claude mid-analysis
- **Smart file handling** - Automatically expands directories, manages token limits based on model capacity
- **[Bypass MCP's token limits](#working-with-large-prompts)** - Work around MCP's 25K limit automatically
- **Built-in rate limiting & retry logic** - Handles API limits gracefully with exponential backoff

This server orchestrates multiple AI models as your development team, with Claude automatically selecting the best model for each task or allowing you to choose specific models for different strengths.

<div align="center">
  <img src="https://github.com/user-attachments/assets/0f3c8e2d-a236-4068-a80e-46f37b0c9d35" width="600">
</div>

**Prompt Used:**
```
Study the code properly, think deeply about what this does and then see if there's any room for improvement in
terms of performance optimizations, brainstorm with gemini on this to get feedback and then confirm any change by
first adding a unit test with `measure` and measuring current code and then implementing the optimization and
measuring again to ensure it improved, then share results. Check with gemini in between as you make tweaks.
```

The final implementation resulted in a 26% improvement in JSON parsing performance for the selected library, reducing processing time through targeted, collaborative optimizations guided by the AI models' analysis and Claude's refinement.

## 🆓 100% FREE Models - No Hidden Costs!

This fork provides access to **15+ POWERFUL FREE MODELS** via OpenRouter:

### ⭐ Top Free Models:
| Model | Params/Features | Best For |
|-------|----------------|----------|
| **DeepSeek R1** | 671B params, 163K context | Complex reasoning & architecture |
| **Qwen 2.5 Coder** | 32B, 128K context | General chat + code |
| **Mistral Devstral** | SWE-Bench 46.8% | Code review & generation |
| **Gemini Flash** | 1M context window! | Large codebases, fast analysis |
| **Llama 3.3 70B** | 70B, 128K context | High-quality conversations |

✅ **No credit card required**  
✅ **No paid tiers needed**  
✅ **Full functionality with free models**  

See [FREE_MODELS_GUIDE.md](docs/FREE_MODELS_GUIDE.md) for the complete list.

## 🚀 What's New in This Fork

### ✨ 100% Free Model Focus (June 2025)
- **ALL paid models removed** - Clean, simple, free-only codebase
- **15+ carefully tested FREE models** - Best of OpenRouter's free tier
- **Enhanced security** - Authentication, rate limiting, Redis protection
- **Production ready** - Persistent server mode with REST API
- **CLI tool included** - Direct command-line access to all tools
- **Smart defaults** - Auto-selects best free model for each task

### 🔒 Security Enhancements
- ✅ Bearer token authentication
- ✅ Rate limiting per session  
- ✅ Redis password protection
- ✅ Input validation with Pydantic
- ✅ Secure session management
- ✅ Environment variable protection

## Quickstart (5 minutes)

### Prerequisites

- Docker Desktop installed ([Download here](https://www.docker.com/products/docker-desktop/))
- Git
- **Windows users**: WSL2 is required for Claude Code CLI

### 1. Get Your FREE OpenRouter API Key
```bash
# Visit OpenRouter (no credit card needed!)
# https://openrouter.ai/keys
```

✅ **100% FREE** - No payment info required  
✅ **Instant access** to 15+ powerful models  
✅ **Simple setup** - Just one API key needed

### 2. Quick Setup

```bash
# Clone the fork
git clone https://github.com/[your-username]/zen-mcp-fork.git
cd zen-mcp-fork

# Add your FREE key and start
export OPENROUTER_API_KEY=sk-or-v1-your-key-here
./quickstart.sh

# That's it! 🎉
```

For advanced setup with REST API:
```bash
./quickstart.sh --advanced
```

> **💡 Configuration Note**: 
> - Use `.env.simple` for quick setup (just the API key)
> - Use `.env.example` for full configuration reference

### 3. Use Simple Model Names!

With Claude Code:
```
"chat about Python"          → Uses Qwen 2.5 Coder
"think about architecture"   → Uses DeepSeek R1 (671B!)
"code review my function"    → Uses Mistral Devstral
"fast check this error"      → Uses Gemini Flash (1M context!)
```

Or with CLI (if using --advanced):
```bash
./zen-cli.sh chat "Hello!"     # Uses best free chat model
./zen-cli.sh think "Design ideas"  # Uses DeepSeek R1
```

### 4. Configure Claude

#### If Setting up for Claude Code
Run the following commands on the terminal to add the MCP directly to Claude Code
```bash
# Add the MCP server directly via Claude Code CLI
claude mcp add zen -s user -- docker exec -i zen-mcp-server python server.py

# List your MCP servers to verify
claude mcp list

# Remove when needed
claude mcp remove zen -s user

# You may need to remove an older version of this MCP after it was renamed:
claude mcp remove gemini -s user
```
Now run `claude` on the terminal for it to connect to the newly added mcp server. If you were already running a `claude` code session,
please exit and start a new session.

#### If Setting up for Claude Desktop

- Open Claude Desktop
- Go to **Settings** → **Developer** → **Edit Config**

This will open a folder revealing `claude_desktop_config.json`.

2. ** Update Docker Configuration**

The setup script shows you the exact configuration. It looks like this. When you ran `setup-docker.sh` it should
have produced a configuration for you to copy:

```json
{
  "mcpServers": {
    "zen": {
      "command": "docker",
      "args": [
        "exec",
        "-i",
        "zen-mcp-server",
        "python",
        "server.py"
      ]
    }
  }
}
```

Paste the above into `claude_desktop_config.json`. If you have several other MCP servers listed, simply add this below the rest after a `,` comma:
```json
  ... other mcp servers ... ,

  "zen": {
      "command": "docker",
      "args": [
        "exec",
        "-i",
        "zen-mcp-server",
        "python",
        "server.py"
      ]
  }
```

3. **Restart Claude Desktop**
Completely quit and restart Claude Desktop for the changes to take effect.

### 5. Start Using It!

Just ask Claude naturally:
- "Think deeper about this architecture design with zen" → Claude picks best model + `thinkdeep`
- "Using zen perform a code review of this code for security issues" → Claude might pick Qwen 2.5 Coder + `codereview`
- "Use zen and debug why this test is failing, the bug might be in my_class.swift" → Claude might pick DeepSeek R1 + `debug`
- "With zen, analyze these files to understand the data flow" → Claude picks appropriate model + `analyze`
- "Use fast to suggest how to format this code based on the specs mentioned in policy.md" → Uses Gemini Flash FREE specifically
- "Think deeply about this and get think to debug this logic error I found in the checkOrders() function" → Uses DeepSeek R1 specifically
- "Brainstorm scaling strategies with smart. Study the code, pick your preferred strategy and debate with smart to settle on two best approaches" → Uses Llama 3.3 specifically

> **Remember:** Claude remains in control — but **you** are the true orchestrator.  
> You're the prompter, the guide, the puppeteer.  
> Your prompt decides when Claude brings in other models — or handles it solo.

## Available Tools

**Quick Tool Selection Guide:**
- **Need a thinking partner?** → `chat` (brainstorm ideas, get second opinions, validate approaches)
- **Need deeper thinking?** → `thinkdeep` (extends analysis, finds edge cases)
- **Code needs review?** → `codereview` (bugs, security, performance issues)
- **Pre-commit validation?** → `precommit` (validate git changes before committing)
- **Something's broken?** → `debug` (root cause analysis, error tracing)
- **Want to understand code?** → `analyze` (architecture, patterns, dependencies)
- **Server info?** → `get_version` (version and configuration details)

**Auto Mode:** When `DEFAULT_MODEL=auto`, Claude automatically picks the best model for each task. You can override with: "Use fast for quick analysis" or "Use think to debug this".

**Model Selection Examples:**
- Complex architecture review → Claude picks DeepSeek R1
- Quick formatting check → Claude picks Gemini Flash FREE
- Logical debugging → Claude picks Qwen QwQ
- General explanations → Claude picks Qwen 2.5 Coder for balance

**Pro Tip:** Thinking modes (for models that support it) control depth vs token cost. Use "minimal" or "low" for quick tasks, "high" or "max" for complex problems. [Learn more](#thinking-modes---managing-token-costs--quality)

**Tools Overview:**
1. [`chat`](#1-chat---general-development-chat--collaborative-thinking) - Collaborative thinking and development conversations
2. [`thinkdeep`](#2-thinkdeep---extended-reasoning-partner) - Extended reasoning and problem-solving
3. [`codereview`](#3-codereview---professional-code-review) - Professional code review with severity levels
4. [`precommit`](#4-precommit---pre-commit-validation) - Validate git changes before committing
5. [`debug`](#5-debug---expert-debugging-assistant) - Root cause analysis and debugging
6. [`analyze`](#6-analyze---smart-file-analysis) - General-purpose file and code analysis
7. [`get_version`](#7-get_version---server-information) - Get server version and configuration

## 🚀 NEW: Persistent Server Mode

Run zen-mcp as a standalone REST API server for direct access without Claude! Perfect for:
- Integration with other tools and IDEs
- CI/CD pipelines
- Batch processing
- Custom applications

### Quick Start with Persistent Server

```bash
# Start the persistent server
./zen-cli.sh start

# Use the CLI tool
./zen-cli.sh chat "What's the best way to implement caching?"
./zen-cli.sh review /path/to/file.py
./zen-cli.sh debug "TypeError: cannot read property 'id' of undefined"

# Or use the REST API directly
curl -X POST http://localhost:8765/tools/chat \
  -H "Content-Type: application/json" \
  -d '{
    "arguments": {
      "prompt": "Explain async/await in Python",
      "model": "qwen/qwen-2.5-coder-32b-instruct"
    }
  }'
```

## 📁 Project Organization

```
zen-mcp-fork/
├── README.md              # You are here!
├── README_SIMPLE.md       # 2-minute quick start
├── docs/                  # All documentation
├── scripts/               # Setup and utility scripts
├── examples/              # Configuration examples
├── tests/                 # All tests (unit + integration)
├── tools/                 # MCP tool implementations
└── bin/                   # Utility programs
```

### 📚 Documentation

**New Users:**
- **[README_SIMPLE.md](README_SIMPLE.md)** - 2-minute setup guide
- **[docs/FREE_MODELS_GUIDE.md](docs/FREE_MODELS_GUIDE.md)** - Simple model names & usage

**Advanced Setup:**
- **[docs/SETUP_GUIDE.md](docs/SETUP_GUIDE.md)** - Detailed installation and configuration  
- **[docs/API_KEYS.md](docs/API_KEYS.md)** - API key configuration options
- **[docs/PERSISTENT_SERVER.md](docs/PERSISTENT_SERVER.md)** - REST API and CLI documentation

**Help:**
- **[docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)** - Common issues and quick fixes

Key features of persistent mode:
- REST API endpoints for all tools
- Session management for conversations
- CLI tool for easy command-line access
- Docker compose for production deployment
- Support for all OpenRouter models including FREE tier

### 1. `chat` - General Development Chat & Collaborative Thinking
**Your thinking partner - bounce ideas, get second opinions, brainstorm collaboratively**

**Thinking Mode:** Default is `medium` (8,192 tokens). Use `low` for quick questions to save tokens, or `high` for complex discussions when thoroughness matters.

#### Example Prompt:

```
Chat with zen and pick the best model for this job. I need to pick between Redis and Memcached for session storage 
and I need an expert opinion for the project I'm working on. Get a good idea of what the project does, pick one of the two options
and then debate with the other models to give me a final verdict
```

**Key Features:**
- Collaborative thinking partner for your analysis and planning
- Get second opinions on your designs and approaches
- Brainstorm solutions and explore alternatives together
- Validate your checklists and implementation plans
- General development questions and explanations
- Technology comparisons and best practices
- Architecture and design discussions
- Can reference files for context: `"Use chat to explain this algorithm with context from algorithm.py"`
- **Dynamic collaboration**: Models can request additional files or context during the conversation if needed for a more thorough response
- **Web search capability**: Analyzes when web searches would be helpful and recommends specific searches for Claude to perform, ensuring access to current documentation and best practices

### 2. `thinkdeep` - Extended Reasoning Partner

**Get a second opinion to augment Claude's own extended thinking**

**Thinking Mode:** Default is `high` (16,384 tokens) for deep analysis. Claude will automatically choose the best mode based on complexity - use `low` for quick validations, `medium` for standard problems, `high` for complex issues (default), or `max` for extremely complex challenges requiring deepest analysis.

#### Example Prompt:

```
Think deeper about my authentication design with think using max thinking mode and brainstorm to come up 
with the best architecture for my project
```

**Key Features:**
- **Uses models with advanced reasoning capabilities** for enhanced analysis
- Provides a second opinion on Claude's analysis
- Challenges assumptions and identifies edge cases Claude might miss
- Offers alternative perspectives and approaches
- Validates architectural decisions and design patterns
- Can reference specific files for context: `"Use think to think deeper about my API design with reference to api/routes.py"`
- **Enhanced Critical Evaluation**: After the model's analysis, Claude is prompted to critically evaluate the suggestions, consider context and constraints, identify risks, and synthesize a final recommendation - ensuring a balanced, well-considered solution
- **Web search capability**: When enabled (default: true), identifies areas where current documentation or community solutions would strengthen the analysis and suggests specific searches for Claude

### 3. `codereview` - Professional Code Review  
**Comprehensive code analysis with prioritized feedback**

**Thinking Mode:** Default is `medium` (8,192 tokens). Use `high` for security-critical code (worth the extra tokens) or `low` for quick style checks (saves ~6k tokens).

#### Example Prompts:

```
Perform a codereview with code and review auth.py for security issues and potential vulnerabilities.
I need an actionable plan but break it down into smaller quick-wins that we can implement and test rapidly 
```

**Key Features:**
- Issues prioritized by severity (🔴 CRITICAL → 🟢 LOW)
- Supports specialized reviews: security, performance, quick
- Can enforce coding standards: `"Use code to review src/ against PEP8 standards"`
- Filters by severity: `"Get code to review auth/ - only report critical vulnerabilities"`

### 4. `precommit` - Pre-Commit Validation
**Comprehensive review of staged/unstaged git changes across multiple repositories**

**Thinking Mode:** Default is `medium` (8,192 tokens). Use `high` or `max` for critical releases when thorough validation justifies the token cost.

<div align="center">
  <img src="https://github.com/user-attachments/assets/584adfa6-d252-49b4-b5b0-0cd6e97fb2c6" width="950">
</div>

**Prompt Used:**
```
Now use code and perform a review and precommit and ensure original requirements are met, no duplication of code or
logic, everything should work as expected
```

How beautiful is that? Claude used `precommit` twice and `codereview` once and actually found and fixed two critical errors before commit!

#### Example Prompts:

```
Use zen and perform a thorough precommit ensuring there aren't any new regressions or bugs introduced
```

**Key Features:**
- **Recursive repository discovery** - finds all git repos including nested ones
- **Validates changes against requirements** - ensures implementation matches intent
- **Detects incomplete changes** - finds added functions never called, missing tests, etc.
- **Multi-repo support** - reviews changes across multiple repositories in one go
- **Configurable scope** - review staged, unstaged, or compare against branches
- **Security focused** - catches exposed secrets, vulnerabilities in new code
- **Smart truncation** - handles large diffs without exceeding context limits

**Parameters:**
- `path`: Starting directory to search for repos (default: current directory)
- `original_request`: The requirements for context
- `compare_to`: Compare against a branch/tag instead of local changes
- `review_type`: full|security|performance|quick
- `severity_filter`: Filter by issue severity
- `max_depth`: How deep to search for nested repos

### 5. `debug` - Expert Debugging Assistant
**Root cause analysis for complex problems**

**Thinking Mode:** Default is `medium` (8,192 tokens). Use `high` for tricky bugs (investment in finding root cause) or `low` for simple errors (save tokens).

#### Example Prompts:

**Basic Usage:**
```
"Use smart to debug this TypeError: 'NoneType' object has no attribute 'split'"
"Get think to debug why my API returns 500 errors with the full stack trace: [paste traceback]"
```

**Key Features:**
- Generates multiple ranked hypotheses for systematic debugging
- Accepts error context, stack traces, and logs
- Can reference relevant files for investigation
- Supports runtime info and previous attempts
- Provides structured root cause analysis with validation steps
- Can request additional context when needed for thorough analysis
- **Web search capability**: When enabled (default: true), identifies when searching for error messages, known issues, or documentation would help solve the problem and recommends specific searches for Claude

### 6. `analyze` - Smart File Analysis
**General-purpose code understanding and exploration**

**Thinking Mode:** Default is `medium` (8,192 tokens). Use `high` for architecture analysis (comprehensive insights worth the cost) or `low` for quick file overviews (save ~6k tokens).

#### Example Prompts:

**Basic Usage:**
```
"Use chat to analyze main.py to understand how it works"
"Get think to do an architecture analysis of the src/ directory"
```

**Key Features:**
- Analyzes single files or entire directories
- Supports specialized analysis types: architecture, performance, security, quality
- Uses file paths (not content) for clean terminal output
- Can identify patterns, anti-patterns, and refactoring opportunities
- **Web search capability**: When enabled with `use_websearch`, can look up framework documentation, design patterns, and best practices relevant to the code being analyzed

### 7. `get_version` - Server Information
```
"Use zen for its version"
"Get zen to show server configuration"
```

## Tool Parameters

All tools that work with files support **both individual files and entire directories**. The server automatically expands directories, filters for relevant code files, and manages token limits.

### File-Processing Tools

**`analyze`** - Analyze files or directories
- `files`: List of file paths or directories (required)
- `question`: What to analyze (required)  
- `model`: auto|chat|think|code|fast|smart (default: server default)
- `analysis_type`: architecture|performance|security|quality|general
- `output_format`: summary|detailed|actionable
- `thinking_mode`: minimal|low|medium|high|max (default: medium, models that support it)
- `use_websearch`: Enable web search for documentation and best practices (default: false)

```
"Analyze the src/ directory for architectural patterns" (auto mode picks best model)
"Use fast to quickly analyze main.py and tests/ to understand test coverage" 
"Use think for logical analysis of the algorithm in backend/core.py"
"Use smart for deep analysis of the entire backend/ directory structure"
```

**`codereview`** - Review code files or directories
- `files`: List of file paths or directories (required)
- `model`: auto|chat|think|code|fast|smart (default: server default)
- `review_type`: full|security|performance|quick
- `focus_on`: Specific aspects to focus on
- `standards`: Coding standards to enforce
- `severity_filter`: critical|high|medium|all
- `thinking_mode`: minimal|low|medium|high|max (default: medium, models that support it)

```
"Review the entire api/ directory for security issues" (auto mode picks best model)
"Use think to review auth/ for deep security analysis"
"Use code to review logic in algorithms/ for correctness"
"Use fast to quickly review src/ with focus on performance, only show critical issues"
```

**`debug`** - Debug with file context
- `error_description`: Description of the issue (required)
- `model`: auto|chat|think|code|fast|smart (default: server default)
- `error_context`: Stack trace or logs
- `files`: Files or directories related to the issue
- `runtime_info`: Environment details
- `previous_attempts`: What you've tried
- `thinking_mode`: minimal|low|medium|high|max (default: medium, models that support it)
- `use_websearch`: Enable web search for error messages and solutions (default: false)

```
"Debug this logic error with context from backend/" (auto mode picks best model)
"Use think to debug this algorithm correctness issue"
"Use smart to debug this complex architecture problem"
```

**`thinkdeep`** - Extended analysis with file context
- `current_analysis`: Your current thinking (required)
- `model`: auto|chat|think|code|fast|smart (default: server default)
- `problem_context`: Additional context
- `focus_areas`: Specific aspects to focus on
- `files`: Files or directories for context
- `thinking_mode`: minimal|low|medium|high|max (default: max, models that support it)
- `use_websearch`: Enable web search for documentation and insights (default: false)

```
"Think deeper about my design with reference to src/models/" (auto mode picks best model)
"Use think to think deeper about this architecture with extended thinking"
"Use smart to think deeper about the logical flow in this algorithm"
```

## Collaborative Workflows

### Design → Review → Implement
```
Design a real-time collaborative editor. Use zen to think deeper about edge cases and scalability.
Implement an improved version incorporating zen's suggestions.
```

### Code → Review → Fix
```
Implement JWT authentication. Get zen to do a security review. Fix any issues zen identifies and
show me the secure implementation.
```

### Debug → Analyze → Solution
```
Debug why our API crashes under load. Use zen to analyze deeper with context from api/handlers/. Implement a
fix based on zen's root cause analysis.
```

### Tool Selection Guidance
To help choose the right tool for your needs:

**Decision Flow:**
1. **Have a specific error/exception?** → Use `debug`
2. **Want to find bugs/issues in code?** → Use `codereview`
3. **Want to understand how code works?** → Use `analyze`
4. **Have analysis that needs extension/validation?** → Use `thinkdeep`
5. **Want to brainstorm or discuss?** → Use `chat`

**Key Distinctions:**
- `analyze` vs `codereview`: analyze explains, codereview prescribes fixes
- `chat` vs `thinkdeep`: chat is open-ended, thinkdeep extends specific analysis
- `debug` vs `codereview`: debug diagnoses runtime errors, review finds static issues

## Thinking Modes - Managing Token Costs & Quality

**Claude automatically manages thinking modes based on task complexity**, but you can also manually control the reasoning depth to balance between response quality and token consumption. Each thinking mode uses a different amount of tokens, directly affecting API costs and response time.

### Thinking Modes & Token Budgets

These only apply to models that support customizing token usage for extended thinking, such as DeepSeek R1.

| Mode | Token Budget | Use Case | Cost Impact |
|------|-------------|----------|-------------|
| `minimal` | 128 tokens | Simple, straightforward tasks | Lowest cost |
| `low` | 2,048 tokens | Basic reasoning tasks | 16x more than minimal |
| `medium` | 8,192 tokens | **Default** - Most development tasks | 64x more than minimal |
| `high` | 16,384 tokens | Complex problems requiring thorough analysis (default for `thinkdeep`) | 128x more than minimal |
| `max` | 32,768 tokens | Exhaustive reasoning | 256x more than minimal |

### How to Use Thinking Modes

**Claude automatically selects appropriate thinking modes**, but you can override this by explicitly requesting a specific mode in your prompts. Remember: higher thinking modes = more tokens = higher cost but better quality:

#### Optimizing Token Usage & Costs

**In most cases, let Claude automatically manage thinking modes** for optimal balance of cost and quality. Override manually when you have specific requirements:

**Use lower modes (`minimal`, `low`) to save tokens when:**
- Doing simple formatting or style checks
- Getting quick explanations of basic concepts
- Working with straightforward code
- You need faster responses
- Working within tight token budgets

**Use higher modes (`high`, `max`) when quality justifies the cost:**
- Debugging complex issues (worth the extra tokens to find root causes)
- Reviewing security-critical code (cost of tokens < cost of vulnerabilities)
- Analyzing system architecture (comprehensive analysis saves development time)
- Finding subtle bugs or edge cases
- Working on performance optimizations

**Token Cost Examples:**
- `minimal` (128 tokens) vs `max` (32,768 tokens) = 256x difference in thinking tokens
- For a simple formatting check, using `minimal` instead of the default `medium` saves ~8,000 thinking tokens
- For critical security reviews, the extra tokens in `high` or `max` mode are a worthwhile investment

**Examples by scenario:**
```
# Quick style check with fast
"Use fast to review formatting in utils.py"

# Security audit with think
"Get think to do a security review of auth/ with thinking mode high"

# Complex debugging
"Use zen to debug this race condition with max thinking mode"

# Architecture analysis with smart
"Analyze the entire src/ directory architecture with high thinking using smart"
```

## Advanced Features

### AI-to-AI Conversation Threading

This server enables **true AI collaboration** between Claude and multiple AI models, where they can coordinate and question each other's approaches:

**How it works:**
- **Models can ask Claude follow-up questions** to clarify requirements or gather more context
- **Claude can respond** with additional information, files, or refined instructions
- **Claude can work independently** between exchanges - implementing solutions, gathering data, or performing analysis
- **Claude can return to models** with progress updates and new context for further collaboration
- **Cross-tool continuation** - Start with one tool (e.g., `analyze`) and continue with another (e.g., `codereview`) using the same conversation thread
- **Both AIs coordinate their approaches** - questioning assumptions, validating solutions, and building on each other's insights
- Each conversation maintains full context while only sending incremental updates
- Conversations are automatically managed with Redis for persistence

**Example of Multi-Model AI Coordination:**
1. You: "Debate SwiftUI vs UIKit - which is better for iOS development?"
2. Claude (auto mode): "I'll orchestrate a debate between different models for diverse perspectives."
3. Qwen 2.5 Coder: "From an architectural standpoint, SwiftUI's declarative paradigm and state management make it superior for maintainable, modern apps."
4. DeepSeek R1: "Logically analyzing the trade-offs: UIKit offers 15+ years of stability, complete control, and proven scalability. SwiftUI has <5 years maturity with ongoing breaking changes."
5. Claude: "Let me get Gemini Flash's quick take on developer experience..."
6. Gemini Flash FREE: "SwiftUI = faster development, less code, better previews. UIKit = more control, better debugging, stable APIs."
7. **Claude's synthesis**: "Based on the multi-model analysis: Use SwiftUI for new projects prioritizing development speed, UIKit for apps requiring fine control or supporting older iOS versions."

**Asynchronous workflow example:**
- Claude can work independently between exchanges (analyzing code, implementing fixes, gathering data)
- Return to models with progress updates and additional context  
- Each exchange shares only incremental information while maintaining full conversation history
- Automatically bypasses MCP's 25K token limits through incremental updates

**Enhanced collaboration features:**
- **Cross-questioning**: AIs can challenge each other's assumptions and approaches
- **Coordinated problem-solving**: Each AI contributes their strengths to complex problems
- **Context building**: Claude gathers information while models provide deep analysis
- **Approach validation**: AIs can verify and improve each other's solutions
- **Cross-tool continuation**: Seamlessly continue conversations across different tools while preserving all context
- **Asynchronous workflow**: Conversations don't need to be sequential - Claude can work on tasks between exchanges, then return to models with additional context and progress updates
- **Incremental updates**: Share only new information in each exchange while maintaining full conversation history
- **Automatic 25K limit bypass**: Each exchange sends only incremental context, allowing unlimited total conversation size
- Up to 5 exchanges per conversation with 1-hour expiry
- Thread-safe with Redis persistence across all tools

**Cross-tool & Cross-Model Continuation Example:**
```
1. Claude: "Analyze /src/auth.py for security issues"
   → Auto mode: Claude picks Qwen 2.5 Coder for deep security analysis
   → Qwen analyzes and finds vulnerabilities, provides continuation_id

2. Claude: "Review the authentication logic thoroughly"
   → Uses same continuation_id, but Claude picks DeepSeek R1 for logical analysis
   → DeepSeek sees previous Qwen analysis and provides logic-focused review

3. Claude: "Debug the auth test failures"
   → Same continuation_id, Claude keeps DeepSeek for debugging
   → DeepSeek provides targeted debugging with full context from both previous analyses

4. Claude: "Quick style check before committing"
   → Same thread, but Claude switches to Gemini Flash for speed
   → Flash quickly validates formatting with awareness of all previous fixes
```

### Working with Large Prompts

The MCP protocol has a combined request+response limit of approximately 25K tokens. This server intelligently works around this limitation by automatically handling large prompts as files:

**How it works:**
1. When you send a prompt larger than the configured limit (default: 50K characters ~10-12K tokens), the server detects this
2. It responds with a special status asking Claude to save the prompt to a file named `prompt.txt`
3. Claude saves the prompt and resends the request with the file path instead
4. The server reads the file content directly into the model's context
5. The full MCP token capacity is preserved for the response

**Example scenario:**
```
# You have a massive code review request with detailed context
User: "Use zen to review this code: [50,000+ character detailed analysis]"

# Server detects the large prompt and responds:
Zen MCP: "The prompt is too large for MCP's token limits (>50,000 characters). 
Please save the prompt text to a temporary file named 'prompt.txt' and resend 
the request with an empty prompt string and the absolute file path included 
in the files parameter, along with any other files you wish to share as context."

# Claude automatically handles this:
- Saves your prompt to /tmp/prompt.txt
- Resends: "Use zen to review this code" with files=["/tmp/prompt.txt", "/path/to/code.py"]

# Server processes the large prompt through model's full context
# Returns comprehensive analysis within MCP's response limits
```

This feature ensures you can send arbitrarily large prompts to models without hitting MCP's protocol limitations, while maximizing the available space for detailed responses.

### Dynamic Context Requests
Tools can request additional context from Claude during execution. When models need more information to provide a thorough analysis, they will ask Claude for specific files or clarification, enabling true collaborative problem-solving.

**Example:** If a model is debugging an error but needs to see a configuration file that wasn't initially provided, it can request: 
```json
{
  "status": "requires_clarification",
  "question": "I need to see the database configuration to understand this connection error",
  "files_needed": ["config/database.yml", "src/db_connection.py"]
}
```

Claude will then provide the requested files and the model can continue with a more complete analysis.

### Web Search Integration

**Smart web search recommendations for enhanced analysis**

Web search is now enabled by default for all tools. Instead of performing searches directly, models intelligently analyze when additional information from the web would enhance their response and provide specific search recommendations for Claude to execute.

**How it works:**
1. Models analyze the request and identify areas where current documentation, API references, or community solutions would be valuable
2. They provide their analysis based on their training data
3. If web searches would strengthen the analysis, models include a "Recommended Web Searches for Claude" section
4. Claude can then perform these searches and incorporate the findings

**Example:**
```
User: "Use zen to debug this FastAPI async error"

Model's Response:
[... debugging analysis ...]

**Recommended Web Searches for Claude:**
- "FastAPI async def vs def performance 2024" - to verify current best practices for async endpoints
- "FastAPI BackgroundTasks memory leak" - to check for known issues with the version you're using
- "FastAPI lifespan context manager pattern" - to explore proper resource management patterns

Claude can then search for these specific topics and provide you with the most current information.
```

**Benefits:**
- Always access to latest documentation and best practices
- Models focus on reasoning about what information would help
- Claude maintains control over actual web searches
- More collaborative approach between the two AI assistants
- Reduces hallucination by encouraging verification of assumptions

**Disabling web search:**
If you prefer models to work only with their training data, you can disable web search:
```
"Use zen to review this code with use_websearch false"
```

### Standardized Response Format
All tools now return structured JSON responses for consistent handling:
```json
{
  "status": "success|error|requires_clarification",
  "content": "The actual response content",
  "content_type": "text|markdown|json",
  "metadata": {"tool_name": "analyze", ...}
}
```

This enables better integration, error handling, and support for the dynamic context request feature.

## Configuration

The server includes several configurable properties that control its behavior:

### Model Configuration

**🎯 Auto Mode (Recommended):**
Set `DEFAULT_MODEL=auto` in your .env file and Claude will intelligently select the best model for each task:

```env
# .env file
DEFAULT_MODEL=auto  # Claude picks the best model automatically

# API Keys (at least one required)
OPENROUTER_API_KEY=your-openrouter-key  # Enables 15+ FREE models!
GEMINI_API_KEY=your-gemini-key    # Enables Gemini Pro & Flash (optional)
OPENAI_API_KEY=your-openai-key    # Enables O3, O3-mini (optional)
```

**How Auto Mode Works:**
- Claude analyzes each request and selects the optimal model
- Model selection is based on task complexity, requirements, and model strengths
- You can always override: "Use fast for quick check" or "Use think to debug"

**Supported Models & When Claude Uses Them:**

| Model | Provider | Context | Strengths | Auto Mode Usage |
|-------|----------|---------|-----------|------------------|
| **FREE MODELS** | | | | |
| **`google/gemini-2.0-flash-exp:free`** ⭐ | OpenRouter | 1M tokens | Ultra-fast, huge context - **DEFAULT MODEL** | Default for all tasks - fast & free! |
| **`deepseek/deepseek-r1:free`** | OpenRouter | 163K tokens | Advanced reasoning (671B) - FREE | Complex logical problems |
| **`mistralai/devstral-small:free`** | OpenRouter | 128K tokens | Code specialist - FREE | Code review and generation |
| **`qwen/qwen-2.5-coder-32b-instruct:free`** | OpenRouter | 128K tokens | Best overall balance - FREE | General chat + code |
| **`meta-llama/llama-3.3-70b-instruct:free`** | OpenRouter | 128K tokens | High-quality - FREE | Thoughtful conversations |
| **`qwen/qwq-32b:free`** | OpenRouter | 32K tokens | Step-by-step reasoning - FREE | Logic problems |
| **`nvidia/llama-3.1-nemotron-ultra-253b-v1:free`** | OpenRouter | 128K tokens | NVIDIA's enhanced - FREE | Large-scale analysis |
| **SIMPLE ALIASES** (Map to Free Models) | | | | |
| **`chat`** → qwen/qwen-2.5-coder-32b-instruct:free | OpenRouter | 128K tokens | Best overall | General conversations |
| **`think`** → deepseek/deepseek-r1:free | OpenRouter | 163K tokens | Deep reasoning (671B) | Complex problems |
| **`code`** → mistralai/devstral-small:free | OpenRouter | 128K tokens | Code specialist | Code tasks |
| **`fast`** → google/gemini-2.0-flash-exp:free | OpenRouter | 1M tokens | Ultra-fast | Quick checks |
| **`smart`** → meta-llama/llama-3.3-70b-instruct:free | OpenRouter | 128K tokens | High quality | Thoughtful analysis |

**Manual Model Selection:**
You can specify a default model instead of auto mode:

```env
# Use a specific free model by default
DEFAULT_MODEL=qwen/qwen-2.5-coder-32b-instruct:free  # Best overall
DEFAULT_MODEL=deepseek/deepseek-r1:free              # Best reasoning
DEFAULT_MODEL=mistralai/devstral-small:free          # Best for code
```

**Per-Request Model Override:**
Regardless of your default setting, you can specify models per request:

*Free Models (Recommended for most tasks):*
- "Use **google/gemini-2.0-flash-exp:free** for quick analysis" (1M context!)
- "Use **deepseek/deepseek-r1:free** for complex reasoning" (671B params!)
- "Use **qwen/qwen-2.5-coder-32b-instruct:free** for code optimization"
- "Use **mistralai/devstral-small:free** for code review" (SWE-Bench 46.8%)
- "Use **meta-llama/llama-3.3-70b-instruct:free** for high-quality chat"
- "Use **nvidia/llama-3.1-nemotron-ultra-253b-v1:free** for comprehensive review"

**Free Model Capabilities:**
- **DeepSeek R1**: 671B params, 163K context, open reasoning tokens
- **Qwen Models**: Excellent coding, 32K-128K context, multilingual support
- **Gemini Flash Free**: 1M context window, ultra-fast responses
- **Mistral Devstral**: SWE-Bench 46.8%, specialized for code, 128K context
- **Llama 3.3**: High-quality general chat, 128K context

### Temperature Defaults
Different tools use optimized temperature settings:
- **`TEMPERATURE_ANALYTICAL`**: `0.2` - Used for code review and debugging (focused, deterministic)
- **`TEMPERATURE_BALANCED`**: `0.5` - Used for general chat (balanced creativity/accuracy)
- **`TEMPERATURE_CREATIVE`**: `0.7` - Used for deep thinking and architecture (more creative)

### Logging Configuration
Control logging verbosity via the `LOG_LEVEL` environment variable:
- **`DEBUG`**: Shows detailed operational messages, tool execution flow, conversation threading
- **`INFO`**: Shows general operational messages (default)
- **`WARNING`**: Shows only warnings and errors
- **`ERROR`**: Shows only errors

**Set in your .env file:**
```bash
LOG_LEVEL=DEBUG  # For troubleshooting
LOG_LEVEL=INFO   # For normal operation (default)
```

**For Docker:**
```bash
# In .env file
LOG_LEVEL=DEBUG

# Or set directly when starting
LOG_LEVEL=DEBUG docker compose up
```


## File Path Requirements

**All file paths must be absolute paths.**

When using any tool, always provide absolute paths:
```
✅ "Use zen to analyze /Users/you/project/src/main.py"
❌ "Use zen to analyze ./src/main.py"  (will be rejected)
```

### Security & File Access

By default, the server allows access to files within your home directory. This is necessary for the server to work with any file you might want to analyze from Claude.

**For Docker environments**, the `WORKSPACE_ROOT` environment variable is used to map your local directory to the internal `/workspace` directory, enabling the MCP to translate absolute file references correctly:

```json
"env": {
  "OPENROUTER_API_KEY": "your-key",
  "WORKSPACE_ROOT": "/Users/you/project"  // Maps to /workspace inside Docker
}
```

This allows Claude to use absolute paths that will be correctly translated between your local filesystem and the Docker container.


## How System Prompts Work

The server uses carefully crafted system prompts to give each tool specialized expertise:

### Prompt Architecture
- **Centralized Prompts**: All system prompts are defined in `prompts/tool_prompts.py`
- **Tool Integration**: Each tool inherits from `BaseTool` and implements `get_system_prompt()`
- **Prompt Flow**: `User Request → Tool Selection → System Prompt + Context → Model Response`

### Specialized Expertise
Each tool has a unique system prompt that defines its role and approach:
- **`thinkdeep`**: Acts as a senior development partner, challenging assumptions and finding edge cases
- **`codereview`**: Expert code reviewer with security/performance focus, uses severity levels
- **`debug`**: Systematic debugger providing root cause analysis and prevention strategies
- **`analyze`**: Code analyst focusing on architecture, patterns, and actionable insights

### Customization
To modify tool behavior, you can:
1. Edit prompts in `prompts/tool_prompts.py` for global changes
2. Override `get_system_prompt()` in a tool class for tool-specific changes
3. Use the `temperature` parameter to adjust response style (0.2 for focused, 0.7 for creative)

## Testing

### Unit Tests (No API Key Required)
The project includes comprehensive unit tests that use mocks and don't require API keys:

```bash
# Run all unit tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ --cov=. --cov-report=html
```

### Simulation Tests (API Key Required)
To test the MCP server with comprehensive end-to-end simulation:

```bash
# Set your API key
export OPENROUTER_API_KEY=your-openrouter-api-key-here

# Run all simulation tests (default: uses existing Docker containers)
python tests/integration/communication_simulator_test.py

# Run specific tests only
python tests/integration/communication_simulator_test.py --tests basic_conversation content_validation

# Run with Docker rebuild (if needed)
python tests/integration/communication_simulator_test.py --rebuild-docker

# List available tests
python tests/integration/communication_simulator_test.py --list-tests
```

The simulation tests validate:
- Basic conversation flow with continuation
- File handling and deduplication
- Cross-tool conversation threading
- Redis memory persistence
- Docker container integration

### GitHub Actions CI/CD
The project includes GitHub Actions workflows that:

- **✅ Run unit tests automatically** - No API key needed, uses mocks
- **✅ Test on Python 3.10, 3.11, 3.12** - Ensures compatibility
- **✅ Run linting and formatting checks** - Maintains code quality

The CI pipeline works without any secrets and will pass all tests using mocked responses. Simulation tests require API key secrets (`OPENROUTER_API_KEY`) to run the communication simulator.

## Troubleshooting

### Docker Issues

**"Connection failed" in Claude Desktop**
- Ensure Docker services are running: `docker compose ps`
- Check if the container name is correct: `docker ps` to see actual container names
- Verify your .env file has a valid OpenRouter API key

**"API key environment variable is required"**
- Edit your .env file and add your OpenRouter API key
- Restart services: `docker compose restart`

**Container fails to start**
- Check logs: `docker compose logs zen-mcp`
- Ensure Docker has enough resources (memory/disk space)
- Try rebuilding: `docker compose build --no-cache`

**"spawn ENOENT" or execution issues**
- Verify the container is running: `docker compose ps`
- Check that Docker Desktop is running
- On Windows: Ensure WSL2 is properly configured for Docker

**Testing your Docker setup:**
```bash
# Check if services are running
docker compose ps

# Test manual connection
docker exec -i zen-mcp-server echo "Connection test"

# View logs
docker compose logs -f
```

### Rate Limiting Issues

**"Rate limit exceeded" errors**
- Free tier has limits (50-1000 requests/day depending on usage)
- Try different free models
- Space out your requests
- Consider minimal OpenRouter credits to increase limits

### Model Not Found

**"No provider found for model"**
- Ensure you're using the exact model ID with `:free` suffix
- Check your OpenRouter API key is valid
- Try using simple aliases: `chat`, `think`, `code`, `fast`, `smart`

## Windows Setup Guide

For Windows users, you'll need WSL2 (Windows Subsystem for Linux) to run Claude Code CLI:

1. **Install WSL2**:
   ```powershell
   wsl --install
   ```

2. **Install Docker Desktop for Windows** and enable WSL2 integration

3. **Clone and setup in WSL2**:
   ```bash
   # In WSL2 terminal
   cd ~
   git clone https://github.com/[your-username]/zen-mcp-fork.git
   cd zen-mcp-fork
   ./quickstart.sh
   ```

4. **Configure Claude Desktop** with the Windows path format

## License

MIT License - see LICENSE file for details.

## Acknowledgments

### 🙏 Special Thanks

A huge thank you to **[BeehiveInnovations](https://github.com/BeehiveInnovations)** for creating the original [zen-mcp-server](https://github.com/BeehiveInnovations/zen-mcp-server)! This fork builds upon their excellent foundation to provide a 100% free model experience.

### Built With

- [MCP (Model Context Protocol)](https://modelcontextprotocol.com) by Anthropic
- [OpenRouter](https://openrouter.ai/) - Unified API for FREE AI models
- [DeepSeek](https://deepseek.com/) - 671B reasoning model (FREE!)
- [Qwen](https://qwenlm.github.io/) - Excellent coding models (FREE!)
- [Meta Llama](https://llama.meta.com/) - Open models (FREE!)
- And the amazing open-source AI community 🤝