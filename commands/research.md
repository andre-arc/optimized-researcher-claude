---
name: research
description: 5-angle parallel research pipeline — decompose, fan-out search, adversarial verify, synthesize. No Python.
---

Research topic: **$ARGUMENTS**

Run the pipeline below in order. Report progress after each phase.

## 0. Resolve topic (only if `$ARGUMENTS` is empty)
If a topic was given above, use it and skip this phase.
Otherwise derive one from session memory: read `MEMORY.md` in the session memory dir and the `project`/`user` memory files it indexes. Pick the most salient current research interest and state it in one line as `Derived topic: <topic>`, then use that as the topic for the rest of the pipeline.
If memory is empty or absent, stop and ask the user for a topic — do not invent one.

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
