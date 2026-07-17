# Research pipeline (5-angle parallel)

Trigger this workflow with `/research <topic>`.

Run the pipeline below in order. Report progress after each phase.

## 0. Resolve topic
If a topic was given after `/research`, use it and skip this phase.
Otherwise derive one from session memory: read `AGENTS.md` / `GEMINI.md` / `.agent/rules/*.md` and the running conversation context, pick the most salient current research interest, state it as `Derived topic: <topic>`, and use that for the rest of the pipeline.
If nothing usable exists, stop and ask for a topic — do not invent one.

## 1. Decompose
Split the topic into exactly 5 distinct research angles, one short slug each, covering:
architectural bottlenecks · uncertainty & calibration · algorithmic optimization · domain literature · performance trade-offs.

## 2. Search (parallel)
Glob the workspace for `**/*.pdf` and note matches.
Dispatch the **web-searcher** agent (see `agents.md`) once per angle — Antigravity runs up to 5 agents in parallel, one per angle. Tell each:
- its angle query,
- the list of local PDFs to check for relevance,
- to write compact JSON claims to `.agent/scratchpad/cache/<slug>.json`.

Skip any angle whose cache file already exists (that's the cache — recurring runs cost nothing).

## 3. Verify
Read every `.agent/scratchpad/cache/*.json`. Cross-examine claims, drop contradictions and unfalsifiable marketing fluff, keep only strict falsifiable facts. Write survivors to `.agent/scratchpad/verified_claims.json`.

## 4. Synthesize
From the verified claims, write a technical engineering report to `.agent/outputs/<topic-slug>_manifest.md`: map findings to a low-overhead, CPU-vectorized architecture (NumPy vectorization, structural memory packing), with code blocks and citations.

Report the final report path.

<!-- ponytail: model per-agent in Antigravity isn't documented yet. Set the web-searcher agent to Gemini 3 Flash in the model picker for the cheap scrape phase; upgrade the path when a per-agent model field ships. -->
