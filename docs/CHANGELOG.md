# Changelog

## [1.1.1] - 2025-06-12 - Project Organization

### 📁 Project Structure Cleanup
Reorganized project to reduce root directory clutter and improve maintainability.

**Moved to organized directories:**
- 📚 All documentation → `docs/` (11 files)
- 🔧 All scripts → `scripts/` (3 files) 
- 🧪 Test files → `tests/integration/` and `tests/examples/`
- 🔧 Utilities → `bin/`
- 📋 Configuration examples → `examples/`

**Maintained compatibility:**
- Created symlinks for main entry points (`quickstart.sh`, `zen-cli.sh`)
- Updated all documentation links
- All functionality preserved

**Result:** Clean root with only 15 files instead of 25+

## [1.1.0] - 2025-06-12 - Simplification Update

### 🎯 Major Simplification
Achieved original-level simplicity while keeping all free model benefits.

### Added
- ✅ **Simple model aliases**: Use "chat", "think", "code", "fast", "smart" instead of long names
- ✅ **One-command quickstart**: `./quickstart.sh` handles everything
- ✅ **Progressive disclosure**: Basic mode by default, --advanced for power users
- ✅ **Smart security**: No auth needed for localhost, auto-enabled in production
- ✅ **Simplified documentation**: New README_SIMPLE.md for 2-minute setup

### Changed
- 🔄 **No auth in development**: REST API works without Bearer tokens locally
- 🔄 **No Redis password locally**: Simplified development setup
- 🔄 **Auto-generated security keys**: No manual key generation needed
- 🔄 **Better error messages**: Clear, actionable guidance
- 🔄 **CLI uses simple aliases**: `./zen-cli.sh chat "Hi!"` just works

### Developer Experience
- **Before**: Configure 3 API keys, understand auth, manage Redis passwords
- **After**: Set one OpenRouter key and run `./quickstart.sh`

## [1.0.0] - 2025-06-12

### 🆓 100% Free Models Fork
This is a major fork focused on providing 100% FREE AI models through OpenRouter.

### Added
- ✅ 15+ carefully tested FREE models from OpenRouter
- ✅ Persistent REST API server mode
- ✅ CLI tool for direct command-line access
- ✅ Comprehensive security features:
  - Bearer token authentication
  - Rate limiting per session
  - Redis password protection
  - Input validation with Pydantic
  - Secure session management
- ✅ Smart model auto-selection
- ✅ Docker Compose setup for production deployment
- ✅ Comprehensive documentation for free models

### Changed
- 🔄 Complete removal of ALL paid models
- 🔄 Default models now use free tier with `:free` suffix
- 🔄 Simplified configuration - only OpenRouter key required
- 🔄 Updated all documentation to focus on free models
- 🔄 Enhanced error handling for rate limits

### Removed
- ❌ All paid OpenRouter models (Claude, GPT-4, etc.)
- ❌ Microsoft Phi models
- ❌ Requirement for Gemini/OpenAI API keys
- ❌ References to paid tiers in documentation

### Security
- 🔒 API keys protected with .gitignore
- 🔒 Redis authentication enabled by default
- 🔒 Localhost-only binding for services
- 🔒 Environment variable validation
- 🔒 Log sanitization for sensitive data

### Models Included
Top free models available:
- DeepSeek R1 (671B params, 163K context)
- Qwen 2.5 Coder (32B, 128K context)
- Mistral Devstral (SWE-Bench 46.8%)
- Gemini Flash (1M context)
- Llama 3.3 (70B, 128K context)
- Plus 10+ additional free models

### Documentation
- NEW: FREE_MODELS_GUIDE.md - Complete free model reference
- NEW: ZEN_SHARE_READY.md - Quick overview for sharing
- UPDATED: README.md - Focused on free models
- UPDATED: API_KEYS.md - Simplified for OpenRouter only
- UPDATED: All examples use free models

---

Based on the original zen-mcp-server by BeehiveInnovations