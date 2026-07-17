---
description: 5-angle parallel research pipeline — decompose, fan-out search, adversarial verify, synthesize.
argument-hint: [research topic]
---

Research topic: **$ARGUMENTS**

Run the pipeline below in order. Report progress after each phase.

## 0. Resolve topic (only if `$ARGUMENTS` is empty)
If a topic was given above, use it and skip this phase.
Otherwise derive one from session memory: read `AGENTS.md` / `.cursor/rules/*.mdc` and the running conversation context, pick the most salient current research interest, state it as `Derived topic: <topic>`, and use that for the rest of the pipeline.
If nothing usable exists, stop and ask the user for a topic — do not invent one.

## 1. Decompose
Split the topic into exactly 5 distinct research angles, one short slug each, covering:
architectural bottlenecks · uncertainty & calibration · algorithmic optimization · domain literature · performance trade-offs.

## 2. Search (parallel)
Glob the workspace for `**/*.pdf` and note matches.
Spawn the `web-searcher` subagent once **per angle, in parallel**. Tell each:
- its angle query,
- the list of local PDFs to check for relevance,
- to write compact JSON claims to `.cursor/scratchpad/cache/<slug>.json`.

Skip any angle whose cache file already exists (that's the cache — recurring runs cost nothing).

## 3. Verify
Read every `.cursor/scratchpad/cache/*.json`. Cross-examine claims, drop contradictions and unfalsifiable marketing fluff, keep only strict falsifiable facts. Write survivors to `.cursor/scratchpad/verified_claims.json`.

## 4. Synthesize
From the verified claims, write a technical engineering report to `.cursor/outputs/<topic-slug>_manifest.md`: map findings to a low-overhead, CPU-vectorized architecture (NumPy vectorization, structural memory packing), with code blocks and citations.

Report the final report path.
