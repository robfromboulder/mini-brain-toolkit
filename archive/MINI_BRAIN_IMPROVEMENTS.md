# Mini-Brain — Improvement Roadmap

Working document. Not in the read index by design — a parking lot for where the mini-brain could go next, refined over time.

## The guiding idea

The mini-brain holds **only the answers a fresh Claude + the codebase can't derive on its own.** Decisions, rationale, threat-model thinking, what was tried and rejected. A shrinking brain isn't failing — it's converging on what's irreducible. This is deliberately not a "second brain" mega-catalog of every concept and relationship; it's a small store of un-derivable knowledge.

---

## Near-term: enrich what we already capture

### Provenance in findings

Tag each finding with where it was born — "PR #X / Session Y." A thread back to the episode that created it, surviving after working docs archive. Cheap, no duplication, big recall value.

### Confidence tags on findings

Mark findings `settled` / `provisional` / `contested`. The dream cycle revisits provisional ones; "contested" becomes a flag-for-human channel. Once others rely on findings (multi-user), confidence becomes load-bearing, not nice-to-have.

### Freshness ledger

Note the commit/date each verifiable claim was last checked against. The dream prioritizes the stalest first — a gentle TTL on memories.

---

## Mid-term: let the codebase enforce the memory

Today the memory-to-code link is one-way and manual: we read code to check claims. The leap is to close the loop.

### Verification recipes instead of stored facts

Don't store "the allowlist has 15 types" — store *how to re-derive it* (a file/symbol anchor, a grep, or a test name) plus *why it matters*. The durable "why" stays; the volatile number self-checks.

### Claim-to-code dependency index

Each claim records which files/symbols it depends on. The dream cycle reads `git log` since last run and only re-verifies claims whose ground truth actually moved. The memory stops duplicating the code and starts *subscribing* to it.

### Test-binding

A finding cites the test that would fail if it became false. Delete or change that test and the finding is automatically suspect — the codebase becomes the enforcer.

---

## Mid-term: fill cognitive gaps

### Open-questions registry

Right now a PLAN's "open issues" are durable knowledge that dies in `archive/` at closeout. Promote consciously-deferred decisions ("per-setting permissions deferred until phase N") to a canonical registry, so a future feature can check whether it *resolves a standing question*.

### Rejected-approaches graveyard

The "alternatives considered" sections are gold but scattered per-feature. A queryable record of what was tried and why it lost stops future work re-litigating settled questions. Negative knowledge is the most expensive to rediscover.

---

## Mid-term: lifecycle stages not yet built

### Pre-merge consistency gate

A lightweight subset of closeout's structural check, run before merge, so drift is caught at the source. Could be a CI hook or a manual "pre-flight" instruction.

### Review-as-capture

Teammate PR review is often where drift is *first noticed*. An instruction that reviews PRs through the lens of SCOPE/FINDINGS and routes anything surprising back into capture turns an existing habit into a memory input.

---

## Longer-term: the dream cycle studying itself

### Instruction drift detection

Periodically check: do the SETUP/CLOSEOUT templates still match what features actually produce? The world changes under the instructions, not just the content.

### Sleep pressure and nap vs. deep sleep

Let merge activity build "pressure" so the brain dreams more after a burst of merges, less when quiet. Offer a quick **nap** (structural checks only) vs. a full **deep sleep** (all phases, web search, explore fan-out). The dream could track its own hit rate to self-tune cadence.

### Surprise as the capture trigger

Mark prediction-error moments in NOTES as they happen, and let closeout preferentially promote them. Surprise is where learning lives.

### Readiness probes (exit criteria for the dream)

Today the dream ends with a report but no objective "done." Keep a curated set of questions — stable between merges — and at exit require the dream to confirm it can answer each with high confidence using the mini-brain and the codebase together. A question it can't confidently answer is the finding: knowledge was lost or never captured.

**Critical discipline:** store questions only, never cached answers — or it's a second copy of FINDINGS waiting to drift. The dream answers fresh each cycle.

**Still open:** the name ("readiness probes" / "confidence checks"); whether the set is one global list or composed from per-feature questions contributed at closeout.

---

## Longer-term: multi-user evolution

The mini-brain now lives in a shared git repo with access controls — the infrastructure prerequisite from the original brainstorm is done. What remains is the usage model.

### Role-lensed queries, not forked brains

One canonical store, conditioned recall: PM reads deferred-decisions + approach; support reads "what this doesn't solve" + field log; eng reads threat model + findings. The low-risk wedge: expose one consolidated lens to one adjacent role (e.g. a read-only "known limitations" view for QA) and see if it kills even one handoff.

### New episodic streams

Support tickets, QA repros, PM/customer conversations become episodic inputs that consolidate into the same findings. A field issue that reveals a limitation flows into "what this doesn't solve" instead of dying in a ticket.

### Transactive memory over boundary objects

The team's shared memory isn't "everyone knows everything" — it's "we collectively know it, and we know where it lives." The brain is a boundary object: one artifact that different groups each read through their own lens while staying coordinated. Episodic stays personal (NOTES remain attributed); semantic goes collective (findings are shared).

### Classification is part of capture

Some wisdom is need-to-know. The handoff-eliminating brain is also a confidential store, and those only conflict if classification is an afterthought. Build classification into the capture workflow, not as a retroactive review.

---

## Negative-space self-audit

The generative form of what the dream cycle does reactively. Periodically generate the "questions the repo can't answer" set against the current branch, then check three things:

- Questions the brain answers: confirmed load-bearing.
- Questions the brain misses: capture gaps.
- Brain content now answerable from code: delete (drift shed).

This adds a second drift question: not just "is this still true?" but "is this still *ours to hold*?"

---

## Comparable frameworks (reference)

These aren't action items — they're the neighborhood, kept for context on how this mini-brain differs from existing approaches. The one finding worth leading with: **popularity and similarity to us are anti-correlated.** The most-adopted tools (Copilot instructions, Cursor rules, Mem0) are the *least* like us; the things most like us (ADRs, Karpathy's wiki, A-MEM, Generative-Agents reflection) are niche or academic. And nearly every popular system **accumulates automatically and is machine-managed** — the exact inverse of our axiom: human-curated, deliberately shrinking, store-only-the-non-re-derivable.

### Tradeoffs at a glance

| Pattern | Popularity | Substrate | Reflection/consolidation | Forgets / shrinks? | Human-readable | Captures rationale & rejected paths | Primary reader |
|---|---|---|---|---|---|---|---|
| **Mini-brain (us)** | n/a | Markdown in git | **Yes — dream cycle** | **Yes — by design** | Yes | **Yes** | LLM agent |
| ADRs (Nygard/MADR) | High (eng standard) | Markdown in git | No | No (immutable, grows) | Yes | **Yes** | Human |
| Cline Memory Bank | ~58k★, 5M installs | Fixed 6 markdown files | Update workflow, no reflection | No (grows) | Yes | Partial (current-state) | LLM agent |
| Karpathy LLM Wiki | ~5k★ (one gist) | Markdown + `log.md` | **Yes — lint pass** | No (compounds) | Yes | Partial (synthesis) | LLM agent |
| AGENTS.md | ~60k repos | Markdown in repo | No | No | Yes | **No (by spec)** | LLM agent |
| Cursor rules / Copilot instr. | Highest adoption | Markdown (`.mdc`) | No | No | Yes | No (rules only) | LLM agent |
| Mem0 | ~58k★ | Vector + graph + KV | Auto-extract | Accumulate-only | No (opaque) | Indirect | LLM agent |
| Letta / MemGPT | ~23k★ | DB (core/recall/archival) | **Yes — sleep-time compute** | Consolidation-driven | Semi | Indirect | LLM agent |
| Zep / Graphiti | ~20k★ | Temporal knowledge graph | **Yes — episodic→semantic** | **Yes — fact invalidation** | No (graph DB) | Via provenance | LLM agent |
| LangMem / LangGraph | High reach (LangChain) | Backend-agnostic store | **Yes — memory manager** | Yes (can delete) | Depends | Partial (procedural) | LLM agent |
| A-MEM | ~1k★ (research) | Notes in ChromaDB | **Yes — memory evolution** | No | **Yes** | Partial | LLM agent |
| MemOS / MemCube | New (research) | Multi-type + metadata | **Yes — MemScheduler** | Lifecycle-managed | Semi | Via governance | LLM agent |
| MemoryBank | Research | Vectors + profile | Profile synthesis | **Yes — Ebbinghaus decay** | Semi | No | LLM agent |
| Generative Agents (Park) | Foundational (cited) | NL memory stream | **Yes — seminal reflection** | Recency decay | Yes | Indirect | LLM agent |
| Zettelkasten / Obsidian | Very high (PKM) | Linked markdown notes | Human review | No (compounds) | Yes | Possible | Human |
| Docs-as-code / Diátaxis | Universal | Markdown in repo | No | No | Yes | In design docs | Human |

The column nobody else shares is **"forgets/shrinks by design."** Only MemoryBank (auto-decay) and Zep (fact invalidation) come close — and both do it mechanically, not by editorial judgment.

### The neighborhood, in four families

- **Coding-agent instruction conventions** — CLAUDE.md, AGENTS.md (~60k repos, multi-vendor standard), Cursor rules, Copilot custom instructions, Windsurf Memories, Aider `CONVENTIONS.md`. Highest adoption, lowest similarity: these inject *how to act*, not *why*. AGENTS.md is explicitly the anti-mini-brain (its spec excludes rationale/lineage). Signal worth noting: Kilo Code **deprecated its Memory Bank in favor of AGENTS.md** — the heavyweight fixed-file approach is ceding ground.
- **Production agent-memory systems** — Mem0 (~58k★, the adoption leader; accumulate-only), Letta/MemGPT (~23k★; OS-paging + sleep-time consolidation), Zep/Graphiti (~20k★; bi-temporal graph with automatic fact invalidation), LangMem/LangGraph (names the episodic/semantic/procedural taxonomy), Cognee, MemOS/MemCube (per-memory metadata carrying lifecycle + permission/governance). Mostly opaque (vectors/graphs/DBs) and machine-managed; they validate the episodic→semantic shape but invert our curation-and-shrink stance.
- **Academic reflection / memory** — Generative Agents (Park et al.; the seminal periodic reflection our dream cycle echoes), Reflexion (persisted self-critique), Voyager (verified-skill library), A-MEM (Zettelkasten-for-agents; human-readable evolving notes — our closest *conceptual* cousin in this family), MemoryBank (Ebbinghaus forgetting curve — the one whose thesis is "forgetting is a feature").
- **Human knowledge patterns** — **ADRs** (the biggest prior omission: context→decision→consequences + rejected alternatives, plain markdown in git — closest match to our *content/intent*), Zettelkasten/Obsidian, docs-as-code, Diátaxis, RFCs/design docs, runbooks, and Karpathy's LLM Wiki (the only convention besides us with append-only log + semantic layer + an explicit lint/reflection pass).

### Ranked on two axes (because they diverge)

- **By adoption** (most→least): Copilot instructions → Cursor rules → CLAUDE.md → AGENTS.md → Cline Memory Bank ≈ Mem0 → Letta → Zep → ADRs (eng-ubiquitous) → Obsidian/Zettelkasten → LangMem → MemOS → A-MEM → MemoryBank/Generative Agents.
- **By similarity to us** (closest→farthest): Karpathy LLM Wiki (workflow) → ADRs (content) → A-MEM → Generative Agents/Reflexion (mechanism) → Cline Memory Bank (form only) → MemOS (governance) → MemoryBank (forgetting) → … → Mem0/Cursor/Copilot. **Structurally closest is Cline Memory Bank; spiritually closest is Karpathy + ADRs + Generative Agents — but none share the shrink-to-irreducible mandate.**

### Are we our own pattern, or a subset?

**Our own pattern — a genuine hybrid at an intersection, not a subset of any single parent.** Not just ADRs (same intent, opposite lifecycle: ADRs are immutable and monotonic; our canonical layer is living and shrinks; ADRs have no episodic log or consolidation pass). Not just Zettelkasten/Obsidian (we reject dense atomic linking for few large indexed files; our reader is a machine, not a browsing human). Not just docs-as-code/Diátaxis (those organize for human readers and never mandate deleting re-derivable content). The closest single ancestor for *mechanism* is Generative-Agents/A-MEM reflection.

Best one-line positioning: **"durable reflection memory for an AI coding agent, expressed as docs-as-code, governed by ADR-like rationale capture and an irreducible-core/minimize-tokens constraint."** Two ingredients make it more than a relabel: (1) the **shrink-toward-irreducible mandate** — the inverse of every monotonic pattern above; and (2) **LLM-as-primary-reader**, which justifies few-large-files-with-a-read-index over many-small-linked-notes. Give a newcomer two anchors: **ADRs for the intent, Generative-Agents reflection for the mechanism — we sit where they meet.**

### Borrowable forms (without borrowing the growth bias)

Several established idioms map directly onto ideas already on this roadmap; adopting the idiom gives them prior art and tooling. But every one of these source patterns *grows* — borrow their forms, keep our contraction.

| Roadmap idea | Borrow from | Concretely |
|---|---|---|
| Rejected-approaches graveyard / open-questions registry | **ADRs (MADR)** | Discrete records with explicit "alternatives considered / rejected." |
| Confidence + provenance + freshness tags | **MemOS metadata** + **Zep bi-temporal** | Per-finding frontmatter: `status`, `born: PR#/session`, `last_verified`. |
| Claim-to-code dependency index / test-binding | **Graphiti fact invalidation** | A code change is the event that flips a claim's validity — subscribe, don't duplicate. |
| Vocabulary for NOTES vs findings vs instructions | **LangMem taxonomy** | Adopt episodic / semantic / procedural as explicit terms. |
| Multi-user classification | **MemOS MemGovernance** | Per-memory permission/classification built into capture. |
| Dream cycle health pass / exit criteria | **Karpathy lint** + **Generative Agents threshold** | Formalize the lint checklist; trigger reflection on accumulated importance/surprise. |

### Git vs Obsidian (same files, different ergonomics)

The substrate is identical — a mini-brain vault opens in Obsidian today with zero conversion — so this is purely about tooling around the files. Obsidian would help the **human maintainer**: Dataview/Bases could auto-generate the read-index table, a "stalest files" dashboard for the dream cycle, and open-task rollups from frontmatter (the biggest practical win, replacing manual upkeep and the `grep`-for-last-`---` ritual); backlinks would keep cross-references honest and flag dangling links to archived files; Templater + Periodic Notes could scaffold and schedule NOTES entries and the dream cycle. But it adds **nothing for the LLM consumer** (the agent reads raw `.md` and ignores the graph/plugins), the graph view is cosmetic at ~15 files, and it's worse on the things that matter here — git already gives versioning, blame, PR review, and CI, while Obsidian Sync's advantages are single-user-centric; the confidentiality posture also favors an auditable git/PR trail over third-party sync. Adopting Obsidian's *atomic-note* style would actively fight the load-whole-files design. **Net:** git stays the source of truth and history; Obsidian is at best an optional read-only lens for dashboards and link hygiene — additive, never a migration. The pattern itself is unchanged.

**Our distinguishing bet:** the negative-space rule — define the brain by what the code can't say, and let it shrink toward that. It is the one property no popular framework in the neighborhood shares.

---

### Sources

Star counts are tier-accurate (firsthand for a few repos fetched directly; otherwise secondary aggregators / 2025–26 roundups). Agent memory: Letta ([github.com/letta-ai/letta](https://github.com/letta-ai/letta), [sleep-time-compute](https://www.letta.com/blog/sleep-time-compute)), Mem0 ([github.com/mem0ai/mem0](https://github.com/mem0ai/mem0)), Zep/Graphiti ([arxiv 2501.13956](https://arxiv.org/abs/2501.13956), [neo4j.com](https://neo4j.com/blog/developer/graphiti-knowledge-graph-memory/)), LangMem ([langchain.com/blog/langmem-sdk-launch](https://www.langchain.com/blog/langmem-sdk-launch)), A-MEM ([arxiv 2502.12110](https://arxiv.org/abs/2502.12110), [github.com/agiresearch/a-mem](https://github.com/agiresearch/a-mem)), Cognee ([github.com/topoteretes/cognee](https://github.com/topoteretes/cognee)), MemOS ([arxiv 2507.03724](https://arxiv.org/abs/2507.03724)), MemoryBank ([arxiv 2305.10250](https://arxiv.org/pdf/2305.10250)), Generative Agents ([arxiv 2304.03442](https://arxiv.org/pdf/2304.03442)). Coding-agent conventions: CLAUDE.md ([code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory)), AGENTS.md ([agents.md](https://agents.md/)), Cline Memory Bank ([docs.cline.bot/best-practices/memory-bank](https://docs.cline.bot/best-practices/memory-bank)), Cursor rules ([cursor.com/docs/rules](https://cursor.com/docs/rules)), Windsurf Memories ([docs.windsurf.com](https://docs.windsurf.com/windsurf/cascade/memories)), Aider ([aider.chat/docs/usage/conventions.html](https://aider.chat/docs/usage/conventions.html)), Copilot ([docs.github.com/copilot](https://docs.github.com/en/copilot)), Kilo Code deprecation ([kilocode.ai/docs/advanced-usage/memory-bank](https://kilocode.ai/docs/advanced-usage/memory-bank)), Karpathy LLM Wiki ([gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)). Human patterns: ADRs ([adr.github.io](https://adr.github.io/), [icepanel.io](https://icepanel.io/blog/2023-03-29-architecture-decision-records-adrs)), Zettelkasten ([zettelkasten.de](https://zettelkasten.de/atomicity/guide/)), Diátaxis ([diataxis.fr](https://diataxis.fr/)), Reflexion ([promptingguide.ai](https://www.promptingguide.ai/techniques/reflexion)), Voyager ([voyager.minedojo.org](https://voyager.minedojo.org/)), Obsidian Dataview ([cassidoo.co](https://cassidoo.co/post/obsidian-dataview/)).