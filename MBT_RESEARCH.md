# Mini-Brain Toolkit: Research Agenda

> V3, 2026-07-09.

This document is the forward-looking research agenda for the mini-brain pattern: where it could go next, and how it sits among the other systems doing related work. Nothing here is a committed decision — it holds the open gaps and the threads worth pulling. It is self-contained: the full comparative survey, tables, and sources live here, not in any other file.

The lead thread is the comparative analysis (§1), which is the one most worth investing in next.

---

## 1. Comparative analysis: mini-brain vs. related work

### 1.1 Where we stand today

The neighborhood has been surveyed once already, across four families — coding-agent instruction conventions (CLAUDE.md, AGENTS.md, Cursor/Copilot rules), production agent-memory systems (Mem0, Letta/MemGPT, Zep/Graphiti, LangMem, MemOS), academic reflection/memory (Generative Agents, Reflexion, A-MEM, MemoryBank), and human knowledge patterns (ADRs, Zettelkasten, docs-as-code, Karpathy's LLM wiki). The full survey is reproduced in §1.2. Three conclusions carry the most weight and are the baseline any deeper comparison starts from:

- **Popularity and similarity to us are anti-correlated.** The most-adopted tools (Copilot instructions, Cursor rules, Mem0) are the *least* like the mini-brain; the things most like it (ADRs, Karpathy's wiki, A-MEM, Generative-Agents reflection) are niche or academic.
- **Almost everyone accumulates automatically and is machine-managed** — the exact inverse of the mini-brain axiom: human-curated, deliberately shrinking, store-only-the-non-re-derivable.
- **The property nobody else shares is "forgets/shrinks by design."** Only MemoryBank (Ebbinghaus decay) and Zep (fact invalidation) come close, and both do it *mechanically*, not by editorial judgment.

The best one-line positioning: *durable reflection memory for an AI coding agent, expressed as docs-as-code, governed by ADR-like rationale capture and an irreducible-core / minimize-tokens constraint.* Two anchors for a newcomer: **ADRs for the intent, Generative-Agents reflection for the mechanism — the mini-brain sits where they meet.**

### 1.2 The landscape

The survey below is a point-in-time snapshot assembled largely from secondary sources; §1.3 describes the deeper pass worth doing to refresh it.

#### Tradeoffs at a glance

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

#### The neighborhood, in four families

- **Coding-agent instruction conventions** — CLAUDE.md, AGENTS.md (~60k repos, multi-vendor standard), Cursor rules, Copilot custom instructions, Windsurf Memories, Aider `CONVENTIONS.md`. Highest adoption, lowest similarity: these inject *how to act*, not *why*. AGENTS.md is explicitly the anti-mini-brain (its spec excludes rationale/lineage). Signal worth noting: Kilo Code **deprecated its Memory Bank in favor of AGENTS.md** — the heavyweight fixed-file approach is ceding ground.
- **Production agent-memory systems** — Mem0 (~58k★, the adoption leader; accumulate-only), Letta/MemGPT (~23k★; OS-paging + sleep-time consolidation), Zep/Graphiti (~20k★; bi-temporal graph with automatic fact invalidation), LangMem/LangGraph (names the episodic/semantic/procedural taxonomy), Cognee, MemOS/MemCube (per-memory metadata carrying lifecycle + permission/governance). Mostly opaque (vectors/graphs/DBs) and machine-managed; they validate the episodic→semantic shape but invert our curation-and-shrink stance.
- **Academic reflection / memory** — Generative Agents (Park et al.; the seminal periodic reflection our dream cycle echoes), Reflexion (persisted self-critique), Voyager (verified-skill library), A-MEM (Zettelkasten-for-agents; human-readable evolving notes — our closest *conceptual* cousin in this family), MemoryBank (Ebbinghaus forgetting curve — the one whose thesis is "forgetting is a feature").
- **Human knowledge patterns** — **ADRs** (the biggest prior omission: context→decision→consequences + rejected alternatives, plain markdown in git — closest match to our *content/intent*), Zettelkasten/Obsidian, docs-as-code, Diátaxis, RFCs/design docs, runbooks, and Karpathy's LLM Wiki (the only convention besides us with append-only log + semantic layer + an explicit lint/reflection pass).

#### Ranked on two axes (because they diverge)

- **By adoption** (most→least): Copilot instructions → Cursor rules → CLAUDE.md → AGENTS.md → Cline Memory Bank ≈ Mem0 → Letta → Zep → ADRs (eng-ubiquitous) → Obsidian/Zettelkasten → LangMem → MemOS → A-MEM → MemoryBank/Generative Agents.
- **By similarity to us** (closest→farthest): Karpathy LLM Wiki (workflow) → ADRs (content) → A-MEM → Generative Agents/Reflexion (mechanism) → Cline Memory Bank (form only) → MemOS (governance) → MemoryBank (forgetting) → … → Mem0/Cursor/Copilot. **Structurally closest is Cline Memory Bank; spiritually closest is Karpathy + ADRs + Generative Agents — but none share the shrink-to-irreducible mandate.**

#### Are we our own pattern, or a subset?

**Our own pattern — a genuine hybrid at an intersection, not a subset of any single parent.** Not just ADRs (same intent, opposite lifecycle: ADRs are immutable and monotonic; our canonical layer is living and shrinks; ADRs have no episodic log or consolidation pass). Not just Zettelkasten/Obsidian (we reject dense atomic linking for few large indexed files; our reader is a machine, not a browsing human). Not just docs-as-code/Diátaxis (those organize for human readers and never mandate deleting re-derivable content). The closest single ancestor for *mechanism* is Generative-Agents/A-MEM reflection.

Two ingredients make it more than a relabel: (1) the **shrink-toward-irreducible mandate** — the inverse of every monotonic pattern above; and (2) **LLM-as-primary-reader**, which justifies few-large-files-with-a-read-index over many-small-linked-notes. **Our distinguishing bet:** the negative-space rule — define the brain by what the code can't say, and let it shrink toward that. It is the one property no popular framework in the neighborhood shares.

### 1.3 The deeper comparison worth doing

The survey in §1.2 is a point-in-time snapshot assembled largely from secondary sources, and this is a fast-moving field. A deeper comparison should do four things the snapshot did not:

1. **Refresh the landscape against primary sources.** Re-verify star counts, adoption, licensing, and especially acquisitions/pivots among the surveyed systems. This is the same work `templates/DREAM_CYCLE.md` Phase 3 does for a brain's APPROACH — a web-search pass — pointed at the comparison instead.
2. **Stress-test the "shrink-by-design" claim.** It is the load-bearing differentiator, so it deserves adversarial checking: has any popular system since the survey added editorial forgetting, consolidation-with-deletion, or a human-curated shrink step? If the claim is weakening, the positioning needs to move; if it is holding, that is a stronger result stated with fresh evidence.
3. **Move from system-level to feature-level.** The snapshot compares whole systems. The more useful cut for *borrowing* is per-capability: who does provenance well (Zep bi-temporal), who does per-memory governance metadata (MemOS), who closes the memory-to-code loop (Graphiti fact invalidation). Each maps to a roadmap item in §2 and to prior art worth studying before building it.
4. **Look for empirical evidence, not just taxonomy.** Is there any published comparison of human-curated vs. machine-managed agent memory on recall quality, drift, or token cost? The mini-brain's bet is largely argued, not measured; finding (or noting the absence of) evidence either way is itself a finding.

Method when this runs: treat it like a scoped literature/landscape review — Explore/web-search agents per family, primary sources where possible, and write the *conclusions* here (refreshing the table in §1.2 in place) rather than pasting a new giant table that will drift.

### 1.4 Borrowable forms (without borrowing the growth bias)

Several established idioms map directly onto roadmap items in §2; adopting the idiom lends prior art and tooling. But every one of these source patterns *grows*, so the discipline is: borrow the form, keep the contraction.

| Roadmap idea | Borrow from | Concretely |
|---|---|---|
| Rejected-approaches graveyard / open-questions registry | **ADRs (MADR)** | Discrete records with explicit "alternatives considered / rejected." |
| Confidence + provenance + freshness tags | **MemOS metadata** + **Zep bi-temporal** | Per-finding frontmatter: `status`, `born: PR#/session`, `last_verified`. |
| Claim-to-code dependency index / test-binding | **Graphiti fact invalidation** | A code change is the event that flips a claim's validity — subscribe, don't duplicate. |
| Vocabulary for NOTES vs findings vs instructions | **LangMem taxonomy** | Adopt episodic / semantic / procedural as explicit terms. |
| Multi-user classification | **MemOS MemGovernance** | Per-memory permission/classification built into capture. |
| Dream cycle health pass / exit criteria | **Karpathy lint** + **Generative Agents threshold** | Formalize the lint checklist; trigger reflection on accumulated importance/surprise. |

The one comparison already resolved and not worth re-opening: **git vs. Obsidian.** The substrate is identical — a mini-brain vault opens in Obsidian today with zero conversion — so this is purely about tooling around the files. Obsidian would help the **human maintainer** (Dataview/Bases for an auto-generated read-index and "stalest files" dashboard, open-task rollups from frontmatter, backlinks to flag dangling cross-references) but adds **nothing for the LLM consumer**, which reads raw `.md` and ignores the graph/plugins. It is also worse on what matters here: git already gives versioning, blame, PR review, and CI, and the confidentiality posture favors an auditable git/PR trail over third-party sync. Adopting Obsidian's *atomic-note* style would actively fight the load-whole-files design. **Net:** git stays the source of truth (versioning, blame, PR review, CI, auditable confidentiality trail); Obsidian is at most an optional read-only lens for dashboards and link hygiene — additive, never a migration. Recorded here so a future "should we use Obsidian?" doesn't re-litigate it.

### 1.5 Sources

Star counts are tier-accurate (firsthand for a few repos fetched directly; otherwise secondary aggregators / 2025–26 roundups). Agent memory: Letta ([github.com/letta-ai/letta](https://github.com/letta-ai/letta), [sleep-time-compute](https://www.letta.com/blog/sleep-time-compute)), Mem0 ([github.com/mem0ai/mem0](https://github.com/mem0ai/mem0)), Zep/Graphiti ([arxiv 2501.13956](https://arxiv.org/abs/2501.13956), [neo4j.com](https://neo4j.com/blog/developer/graphiti-knowledge-graph-memory/)), LangMem ([langchain.com/blog/langmem-sdk-launch](https://www.langchain.com/blog/langmem-sdk-launch)), A-MEM ([arxiv 2502.12110](https://arxiv.org/abs/2502.12110), [github.com/agiresearch/a-mem](https://github.com/agiresearch/a-mem)), Cognee ([github.com/topoteretes/cognee](https://github.com/topoteretes/cognee)), MemOS ([arxiv 2507.03724](https://arxiv.org/abs/2507.03724)), MemoryBank ([arxiv 2305.10250](https://arxiv.org/pdf/2305.10250)), Generative Agents ([arxiv 2304.03442](https://arxiv.org/pdf/2304.03442)). Coding-agent conventions: CLAUDE.md ([code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory)), AGENTS.md ([agents.md](https://agents.md/)), Cline Memory Bank ([docs.cline.bot/best-practices/memory-bank](https://docs.cline.bot/best-practices/memory-bank)), Cursor rules ([cursor.com/docs/rules](https://cursor.com/docs/rules)), Windsurf Memories ([docs.windsurf.com](https://docs.windsurf.com/windsurf/cascade/memories)), Aider ([aider.chat/docs/usage/conventions.html](https://aider.chat/docs/usage/conventions.html)), Copilot ([docs.github.com/copilot](https://docs.github.com/en/copilot)), Kilo Code deprecation ([kilocode.ai/docs/advanced-usage/memory-bank](https://kilocode.ai/docs/advanced-usage/memory-bank)), Karpathy LLM Wiki ([gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)). Human patterns: ADRs ([adr.github.io](https://adr.github.io/), [icepanel.io](https://icepanel.io/blog/2023-03-29-architecture-decision-records-adrs)), Zettelkasten ([zettelkasten.de](https://zettelkasten.de/atomicity/guide/)), Diátaxis ([diataxis.fr](https://diataxis.fr/)), Reflexion ([promptingguide.ai](https://www.promptingguide.ai/techniques/reflexion)), Voyager ([voyager.minedojo.org](https://voyager.minedojo.org/)), Obsidian Dataview ([cassidoo.co](https://cassidoo.co/post/obsidian-dataview/)).

---

## 2. Capability roadmap

Ideas for extending the pattern, grouped by horizon. Each is a one-line pointer; the reasoning for the whole set is the negative-space bet in §1.

**Near-term — enrich what's already captured.**
- *Provenance in findings* — tag each finding with the PR/session that birthed it.
- *Confidence tags* — mark findings `settled` / `provisional` / `contested`; the dream cycle revisits the shaky ones.
- *Freshness ledger* — record the commit/date each verifiable claim was last checked; the dream prioritizes the stalest.

**Mid-term — let the codebase enforce the memory.**
- *Verification recipes over stored facts* — store *how to re-derive* a volatile number (a grep, a test name) plus *why it matters*, not the number.
- *Claim-to-code dependency index* — each claim records the files/symbols it depends on; the dream only re-verifies claims whose ground truth moved.
- *Test-binding* — a finding cites the test that would fail if it became false, so the codebase becomes the enforcer.
- *Open-questions registry* + *rejected-approaches graveyard* — promote consciously-deferred decisions and dead ends out of per-feature docs into a queryable canonical record, so future work doesn't re-litigate settled questions.
- *Pre-merge consistency gate* + *review-as-capture* — catch drift at the source (a lightweight closeout subset in CI) and route PR-review surprises back into capture.

**Longer-term — the dream cycle studying itself, and multi-user.**
- *Instruction-drift detection* — check that the setup/closeout/dream templates still match what features actually produce.
- *Sleep pressure; nap vs. deep sleep* — let merge activity modulate how often and how deeply the brain dreams.
- *Surprise as the capture trigger* — mark prediction-error moments in the log and preferentially promote them.
- *Readiness probes* — keep a curated set of questions (never cached answers) the dream must answer with high confidence from brain + code; a question it can't answer is the finding.
- *Negative-space self-audit* — the generative twin of the dream's reactive check: generate the "questions the repo can't answer" set against the current branch, then sort brain content three ways — questions the brain answers (confirmed load-bearing), questions it misses (capture gap), and content now answerable from code alone (shed it). This adds a second drift axis beyond "is this still true?": "is this still *ours to hold*?"
- *Multi-user evolution* — role-lensed recall over one canonical store (PM reads deferred-decisions + approach; support reads "what this doesn't solve" + field log; eng reads threat model + findings), new episodic streams (support tickets, QA repros, customer conversations) that consolidate into the same findings, and classification built into capture rather than bolted on. The framing: the brain is a **boundary object** — episodic stays personal (NOTES remain attributed to who saw it), semantic goes collective (findings are shared), so one artifact serves each role's lens without forking the brain. Transactive memory: the team need not all know everything, only collectively know it and where it lives.

---

## 3. Open questions

- **Which roadmap items survive the shrink test?** Several ideas (provenance, freshness, confidence tags) *add* per-finding structure. Each must earn its keep against principle 1 — does it capture something non-re-derivable, or is it metadata the git history already implies? The comparison in §1 is partly in service of answering this: adopt a form only where it beats what version control already gives for free.
- **Does the pattern's differentiator hold as the field matures?** Tracked as §1.3 thread 2; escalate to an `MBT_APPROACH.md` positioning change only if a deeper compare shows "shrink-by-design" is no longer distinctive.
- **How do we operationalize "is this still ours to hold?"** The negative-space self-audit (§2) implies a second drift axis: content that has quietly become derivable from code should be shed, not just re-verified. Where does that check live in the dream cycle's checklist, and how does it avoid false positives on knowledge that only *looks* re-derivable?
- **How is the readiness-probe set composed?** One global list, or composed from per-feature questions contributed at closeout — and store questions only, never cached answers, or it becomes a second copy of FINDINGS waiting to drift. The name is also unsettled ("readiness probes" / "confidence checks"). Interacts with the toolkit-vs-brain question below.
- **How much of this belongs in the toolkit vs. in an individual brain?** Some items (test-binding, freshness ledger) are per-brain conventions the templates would carry; others (instruction-drift detection) are toolkit-level. The line is unsettled and interacts with `MBT_SCOPE.md` 4.1 (universal vs. exemplar-specific machinery).