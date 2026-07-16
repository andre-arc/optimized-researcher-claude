# Cost-Optimized Parallel Research & Document Ingestion Engine Plugin

A multi-stage research plugin built for **Claude Code** — pure native orchestration, no Python, no external runtime. The `/research` command breaks a topic into 5 angles, fans out parallel `web-searcher` subagents to harvest web results and local workspace PDFs, caches by angle, adversarially verifies claims, and synthesizes a technical report. Cost savings come from routing the high-volume scrape phase to Haiku subagents.

## ⚡ Pipeline & Model Allocation

| Phase | Operation | Model | Optimization Strategy |
| :--- | :--- | :--- | :--- |
| **1. Decompose** | Angle generation | Session model | Splits the topic into 5 precise engineering vectors. |
| **2. Scrape & Extract** | 5× parallel fetch | **Haiku** subagents | High-volume web + PDF ingestion offloaded to Haiku; reads capped at 1,000 words to drop boilerplate. |
| **3. Cache** | Per-angle dedup | File system | Angles with an existing cache file are skipped — recurring runs cost nothing. |
| **4. Verify** | Adversarial check | Session model | Cross-examines contradictions, keeps only falsifiable facts. |
| **5. Synthesize** | Architectural fusion | Session model | Maps validated facts to a low-overhead, CPU-vectorized architecture. |

---

## 📂 Plugin Directory Structure

Ensure your local plugin folder structure matches this exact layout block:

```text
cost-optimized-researcher/
├── .claude-plugin/
│   └── plugin.json           # Plugin package manifest metadata
├── agents/
│   └── web-searcher.md       # Haiku-backed web scraper & PDF extraction subagent
└── commands/
    └── research.md           # The /research pipeline — decompose, search, verify, synthesize
```

---

## 📥 Installation

### 1. Global Installation (Recommended)
You can install this plugin natively inside your Claude Code session by pulling it directly from your team's central repository:

```text
/plugin install https://github.com
```

### 2. Local Developer Mounting
If you are modifying or maintaining the source code locally, load the folder directory directly into your workspace session via the plugin path flag:

```bash
claude --plugin-dir=/absolute/path/to/cost-optimized-researcher
```
*Run `/reload-plugins` inside your interactive shell if you modify configuration parameters on the fly.*

---

## 🚀 Usage

Drop reference materials—such as academic whitepapers, hardware manuals, or vendor specifications—directly into your project workspace as `.pdf` files. Then, trigger the optimization pipeline from your active Claude Code terminal on any target framework:

```bash
/research high performance CPU vector execution loops
```

### 📦 Outputs
The orchestrator isolates operational data footprints outside the plugin directory to keep your repository history pristine:
* **Raw Extracted Contexts**: Written to `.claude/scratchpad/cache/` (using MD5 query hashes).
* **Adversarial Verification Gate**: Clean claims array isolated at `.claude/scratchpad/verified_claims.json`.
* **Final Synthesis Report**: Written to `.claude/outputs/your_topic_manifest.md`, featuring fully cited, ranked recommendations tailored strictly to a vectorized, low-overhead, CPU-only architecture.

---

## 📝 License
MIT — Restricted to internal engineering development pipelines.
