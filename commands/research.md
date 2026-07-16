---
name: research
description: 5-angle parallel research pipeline — decompose, fan-out search, adversarial verify, synthesize. No Python.
---

Research topic: **$ARGUMENTS**

Run the pipeline below in order. Report progress after each phase.

## 1. Decompose
Split the topic into exactly 5 distinct research angles, one short slug each, covering:
architectural bottlenecks · uncertainty & calibration · algorithmic optimization · domain literature · performance trade-offs.

## 2. Search (parallel)
Glob the workspace for `**/*.pdf` and note matches.
Launch one `web-searcher` subagent **per angle, all in a single message** so they run in parallel. Tell each agent:
- its angle query,
- the list of local PDFs to check for relevance,
- to write compact JSON claims to `.claude/scratchpad/cache/<slug>.json`.

Skip any angle whose cache file already exists (that's the cache — recurring runs cost nothing).

## 3. Verify
Read every `.claude/scratchpad/cache/*.json`. Cross-examine claims, drop contradictions and unfalsifiable marketing fluff, keep only strict falsifiable facts. Write survivors to `.claude/scratchpad/verified_claims.json`.

## 4. Synthesize
From the verified claims, write a technical engineering report to `.claude/outputs/<topic-slug>_manifest.md`: map findings to a low-overhead, CPU-vectorized architecture (NumPy vectorization, structural memory packing), with code blocks and citations.

Report the final report path.
