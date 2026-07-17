# Platform adapters

The same `/research` pipeline, ported to other agentic tools. Each tree is copy-paste-ready — drop the platform's folder contents into your project root.

| Platform | Copy into project root | Trigger | Scrape model (cheap phase) | Model pinning |
| :-- | :-- | :-- | :-- | :-- |
| Claude Code | (repo root, native plugin) | `/research` | `haiku` (subagent) | per-subagent ✅ |
| opencode | `adapters/opencode/.opencode/` | `/research` | `anthropic/claude-haiku-4-5-…` | per-agent ✅ |
| Cursor | `adapters/cursor/.cursor/` | `/research` | `model: fast` (subagent) | per-subagent ✅ (not per-command) |
| Antigravity | `adapters/antigravity/{.agent,agents.md}` | `/research` | Gemini 3 Flash (pick in UI) | per-agent ⚠️ undocumented |
| Windsurf | `adapters/windsurf/.windsurf/` | `/research` | cheap model (pick in UI) | ❌ none — UI-only |

## Model split (same rule everywhere)

- **Scrape & extract** → cheapest/fastest tier (Haiku / Cursor `fast` / Gemini Flash). This is the 5×-parallel high-volume phase; the savings live here.
- **Verify & synthesize** → session's strong model. Report quality is decided here; don't skimp.

## Caveats

- **Cursor** has no per-command model pinning yet, so the split is enforced at the `web-searcher` subagent (`model: fast`) instead of in the command.
- **Antigravity** doesn't document a per-agent model field yet — set the web-searcher to Gemini 3 Flash manually in the model picker. Everything else (workflow `.md`, `agents.md`) is confirmed.
- **opencode** parallel subagents run via the Task tool (currently near-sequential), but the cache in phase 2 means reruns still cost nothing.
- **Windsurf** (Cascade) is single-agent with no custom subagents and no per-workflow model pinning, so the 5 angles run sequentially on the UI-selected model — the cache still makes reruns free. Cascade's successor **Devin Local** (`.devin/workflows/`) restores up to 5 parallel worker agents.
