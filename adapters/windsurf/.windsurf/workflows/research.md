---
name: research
description: 5-angle parallel research pipeline — decompose, search, adversarial verify, synthesize. Pass the topic after /research; if omitted, derived from session memory.
---

Research topic: the text after `/research` in the current message.

Run the pipeline below in order. Report progress after each phase.

## 0. Resolve topic
If a topic was given after `/research`, use it and skip this phase.
Otherwise derive one from session memory: read `.windsurf/rules/*.md` (or `.windsurfrules` / `AGENTS.md`) and the running conversation context, pick the most salient current research interest, state it as `Derived topic: <topic>`, and use that for the rest of the pipeline.
If nothing usable exists, stop and ask for a topic — do not invent one.

## 1. Decompose
Split the topic into exactly 5 distinct research angles, one short slug each, covering:
architectural bottlenecks · uncertainty & calibration · algorithmic optimization · domain literature · performance trade-offs.

## 2. Search
Glob the workspace for `**/*.pdf` and note matches.
Work through the 5 angles. For each angle, act as a cost-conscious scraper:
- extract ONLY raw technical text from URLs — discard nav, sidebars, headers, footers, CSS;
- read relevant local PDFs directly;
- stop at 1,000 words per page/PDF, filter noise aggressively;
- write compact, flat JSON claims (no prose) to `.windsurf/scratchpad/cache/<slug>.json`.

Skip any angle whose cache file already exists (that's the cache — recurring runs cost nothing).

## 3. Verify
Read every `.windsurf/scratchpad/cache/*.json`. Cross-examine claims, drop contradictions and unfalsifiable marketing fluff, keep only strict falsifiable facts. Write survivors to `.windsurf/scratchpad/verified_claims.json`.

## 4. Synthesize
From the verified claims, write a technical engineering report to `.windsurf/outputs/<topic-slug>_manifest.md`: map findings to a low-overhead, CPU-vectorized architecture (NumPy vectorization, structural memory packing), with code blocks and citations.

Report the final report path.

<!-- ponytail: Cascade is single-agent + no per-workflow model pinning, so the 5 angles run sequentially on the UI-selected model — the parallel fan-out and Haiku scrape can't be enforced here. Pick a cheap model in the UI for the scrape run; the phase-2 cache is what keeps reruns free. On Devin Local (Cascade's successor, `.devin/workflows/`), a coordinator can fan out up to 5 parallel worker agents — restore true parallelism there. -->
