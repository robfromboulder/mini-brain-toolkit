# Mini-Brain Toolkit: Comparable Systems Registry

> V2, 2026-07-16.

A registry of the systems the mini-brain is measured against — coding-agent instruction conventions, production agent-memory systems, academic reflection/memory work, and human knowledge patterns. It holds *facts* about each system — state, canonical source, and when we last checked — as rows to be diffed, not prose to be re-read. The conclusions these facts support live in `MBT_RESEARCH.md`.

Keeping facts here and conclusions there is deliberate: conclusions are stable and re-derived rarely; facts about a fast-moving field go stale and must be diffed, not rebuilt. So the registry is refreshed as a *delta* — re-check the stalest entries, add whatever is new — never re-surveyed from scratch.

**Living vs. static.**
- **Living** — repos and products that version, release, and change state (stars, licensing, forgetting behavior). These carry a `change signal` and are the entries a currency pass actually re-checks. Sort by `verified` date; check the stalest.
- **Static** — published papers and foundational conventions whose content is fixed. Once recorded they are not re-fetched; the only work they generate is *supersession* (a follow-up paper) or *new siblings appearing*. They accumulate; they do not need freshness checks.

**Maintenance.** Update state and `verified` dates **in place** — do not paste a fresh giant table each cycle (that is how the old single-table survey drifted). `verified` is the date we last confirmed the state against the canonical source. When a new system appears, add a row; when one is deprecated/archived, keep the row and set status — a dead project we've already accounted for is cheaper than one we rediscover and re-investigate every run.

---

## 1. Coding-agent instruction conventions

Highest adoption, lowest similarity to us: these inject *how to act*, not *why*. The instruction-file paradigm has converged on YAML frontmatter + Markdown body across all major tools; "context engineering" has displaced "prompt engineering" as the field's label.

| System | Type | Canonical source | Verified | Known state | Relevance & change signal |
|---|---|---|---|---|---|
| CLAUDE.md | living | code.claude.com/docs/en/memory | 2026-07-15 | Anthropic's memory-file convention; the mini-brain's own substrate | Baseline convention, not a competitor. Watch: auto-memory / Auto Dream behavior. |
| AGENTS.md | living | agents.md | 2026-07-15 | ~60k+ repos; donated to Linux Foundation's Agentic AI Foundation (Dec 2025) | The explicit **anti-mini-brain** — spec excludes rationale/lineage. Watch: spec adding any "why" capture. |
| Cursor rules | living | cursor.com/docs/rules | 2026-07-15 | `.cursor/rules/*.mdc`, YAML frontmatter; activation modes | Rules only, no rationale. Watch: any consolidation/forgetting feature. |
| Copilot custom instructions | living | docs.github.com/copilot | 2026-07-15 | Seven file types; **Copilot Memory auto-learns, 28-day expiry, code-citation invalidation** | Code-citation invalidation is our most significant competitive gap. Watch: editorial/curation controls. |
| Windsurf Memories | living | docs.windsurf.com/windsurf/cascade/memories | 2026-07-15 | Cascade auto-generated + user memories | Auto-managed. Watch: shrink/forget behavior. |
| GEMINI.md | living | (Google Gemini CLI docs) | 2026-07-15 | Gemini's memory-file convention | Convention sibling. Watch: rationale/lineage capture. |
| Aider `CONVENTIONS.md` | living | aider.chat/docs/usage/conventions.html | 2026-07-15 | Static conventions file, human-authored | Rules only. Low volatility. |
| Cline Memory Bank | static | docs.cline.bot/best-practices/memory-bank | 2026-07-15 | **Deprecated Apr 2026**; fixed 6 markdown files, no reflection, grows | Frozen. The heavyweight fixed-file approach ceding ground — evidence *for* our thesis. |
| Kilo Code Memory Bank | static | kilocode.ai/docs/advanced-usage/memory-bank | 2026-07-15 | **Deprecated Apr 2026** | Frozen. Same signal as Cline. |
| Roo Code | static | (project archived) | 2026-07-15 | **Archived May 2026** | Frozen. Same signal. |
| Claude Code Auto Dream | living | (Claude Code changelog) | 2026-07-15 | Auto-consolidation with ~200-line budget | Closest shipping "dream" analog — but automatic, budget-based, no editorial judgment. Watch: any human-curation step. |

## 2. Production agent-memory systems

Mostly opaque and machine-managed; they validate the episodic→semantic shape but invert our curation-and-shrink stance. Agent memory is now an infrastructure category with its own benchmarks (LongMemEval, LoCoMo, ConvoMem, BEAM).

| System | Type | Canonical source | Verified | Known state | Relevance & change signal |
|---|---|---|---|---|---|
| Mem0 | living | github.com/mem0ai/mem0 | 2026-07-15 | ~61k★; adoption leader; **V3 regressed to ADD-only** extraction (accumulates forever) | The adoption leader moving *away* from forgetting — strong evidence for our differentiator. Watch: any return of consolidation-with-deletion. |
| Cognee | living | github.com/topoteretes/cognee | 2026-07-15 | ~28k★; graph+vector; explicit **`forget` API** and `improve` API | Closest "forgets" API — but automatic, not editorial. Watch: human-in-the-loop curation. |
| Zep / Graphiti | living | github.com/getzep/graphiti · arxiv 2501.13956 | 2026-07-15 | ~29k★; temporal knowledge graph; **fact invalidation preserves rather than deletes**; Zep CE discontinued, Graphiti sole open offering | Bi-temporal provenance leader. Invalidation ≠ deletion. Watch: a delete/shrink path. |
| Letta / MemGPT | living | github.com/letta-ai/letta · letta.com/blog/sleep-time-compute | 2026-07-15 | ~24k★; **pivoted to git-backed "Context Repositories" (MemFS)**; sleep-time compute; archival memory has **no forgetting mechanism** | The git-backed pivot is structurally closest on substrate. Watch: editorial deletion/shrink in MemFS. |
| LangMem / LangGraph | living | langchain.com/blog/langmem-sdk-launch | 2026-07-15 | Backend-agnostic store; names episodic/semantic/procedural taxonomy; can delete | Source of the memory-type vocabulary. Watch: shrink-toward-core behavior. |
| MemOS / MemCube | living | arxiv 2507.03724 | 2026-07-15 | ~10k★, Alibaba-backed; multi-type + per-memory governance metadata + lifecycle | Governance-metadata leader. Watch: editorial-curation semantics. |
| MemClaw / Caura | living | (vendor docs) | 2026-07-15 | Four-tier trust, PII detection; in production at eToro | Governance/classification leader. Watch: forgetting-by-judgment. |
| Vektor Memory | static | (research paper) | 2026-07-15 | Hierarchical store; **7-phase REM cycle, ~97% reduction** | Structurally closest to "shrink toward irreducible core" — but **fully automatic, no editorial judgment**. The strongest differentiator threat. Watch: a productized repo or a human-curation step. |

## 3. Academic reflection / memory

The seminal mechanisms our dream cycle echoes. The field has an ICLR 2026 workshop (MemAgents, 110+ submissions). These are mostly **static** (papers) — the recurring work is finding *new* ones, not re-reading these.

| System | Type | Canonical source | Verified | Known state | Relevance & change signal |
|---|---|---|---|---|---|
| Generative Agents (Park et al.) | static | arxiv 2304.03442 | 2026-07-15 | NL memory stream; **seminal periodic reflection**; recency decay | Closest single ancestor for *mechanism* (our dream cycle echoes its reflection). Foundational, cited. |
| A-MEM | static | arxiv 2502.12110 · github.com/agiresearch/a-mem | 2026-07-15 | ~1k★; Zettelkasten-for-agents; human-readable evolving notes | Closest *conceptual* cousin (human-readable, evolving). Watch: a shrink/curation step. |
| MemoryBank | static | arxiv 2305.10250 | 2026-07-15 | Vectors + profile; **Ebbinghaus forgetting curve** | Forgetting-by-decay — but mechanical, not editorial. |
| Vektor Memory | static | (research paper) | 2026-07-15 | See §2 (dual-listed) | Shrinks to core, automatically. Cross-ref §2. |
| Auto-Dreamer | static | arxiv 2605.20616 | 2026-07-15 | Session-log-then-consolidate; decouples fast acquisition from slow cross-session consolidation | **Mirrors LOG + dream cycle architecture.** The closest published architecture to ours — but automatic. |
| Reflexion | static | promptingguide.ai/techniques/reflexion | 2026-07-15 | Persisted self-critique | Reflection lineage. |
| Voyager | static | voyager.minedojo.org | 2026-07-15 | Verified-skill library | Reflection/skill-library lineage. |

## 4. Human knowledge patterns

Closest to our *content and intent*; farthest on *reader* (human, not machine) and *lifecycle* (grow, not shrink). Nearly all **static** conventions.

| System | Type | Canonical source | Verified | Known state | Relevance & change signal |
|---|---|---|---|---|---|
| ADRs (Nygard / MADR) | static | adr.github.io · icepanel.io | 2026-07-15 | High (eng standard); context→decision→consequences + rejected alternatives; immutable, grows | **Closest match to our content/intent** — but immutable and monotonic (opposite lifecycle). Anchor for the "intent" side of our positioning. |
| Karpathy LLM Wiki | static | gist.github.com/karpathy/442a6bf… | 2026-07-15 | ~5k★ (one gist); markdown + `log.md`; **explicit lint pass** | **Closest match to our workflow** — only other convention with append-only log + semantic layer + lint/reflection. Watch: a shrink step (it currently compounds). |
| Zettelkasten / Obsidian | static | zettelkasten.de · cassidoo.co (Dataview) | 2026-07-15 | Very high (PKM); linked atomic markdown; human review; compounds | Same substrate, opposite organization (atomic linking vs. few large indexed files). git-vs-Obsidian resolved. |
| Docs-as-code / Diátaxis | static | diataxis.fr | 2026-07-15 | Universal; markdown in repo; organized for humans; never mandates deleting re-derivable content | Substrate sibling, human reader, no contraction mandate. |
| RFCs / design docs | static | (various) | 2026-07-15 | Design rationale captured pre-decision; grows | Intent-capture sibling; monotonic. |
| Runbooks | static | (various) | 2026-07-15 | Operational procedures; human reader | Procedural sibling. |

---

## 5. Sources

Star counts are tier-accurate (firsthand for a few repos fetched directly; otherwise secondary aggregators / 2025–26 roundups). Primary sources are linked in the `canonical source` column above.