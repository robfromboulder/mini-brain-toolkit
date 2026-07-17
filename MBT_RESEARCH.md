# Mini-Brain Toolkit: Research Agenda

> V8, 2026-07-16.

This document is the forward-looking research agenda for the mini-brain pattern: where it could go next, and the *conclusions* of how it sits among related work. Nothing here is a committed decision — it holds the open gaps and the threads worth pulling.

The two comparison surfaces have their own data registries, so this file stays conclusions-only and doesn't re-derive facts each cycle:
- **System comparisons** (the "second brain" / agent-memory / instruction-file neighborhood) — per-system state, sources, and freshness live in a dedicated registry, refreshed on its own cadence.
- **Cognitive-science grounding** (biological models the pattern draws on) — per-field research, mappings, and freshness live in a dedicated registry, refreshed on its own cadence.

The lead thread is the comparative analysis (§1), which is the one most worth investing in next.

---

## 1. Comparative analysis: mini-brain vs. related work

### 1.1 Where we stand today

The neighborhood has been surveyed across four families — coding-agent instruction conventions (CLAUDE.md, AGENTS.md, Cursor/Copilot rules), production agent-memory systems (Mem0, Letta/MemGPT, Zep/Graphiti, LangMem, MemOS), academic reflection/memory (Generative Agents, Reflexion, A-MEM, MemoryBank), and human knowledge patterns (ADRs, Zettelkasten, docs-as-code, Karpathy's LLM wiki). Three conclusions carry the most weight and are the baseline any deeper comparison starts from:

- **Popularity and similarity to us are anti-correlated.** The most-adopted tools (Copilot instructions, Cursor rules, Mem0) are the *least* like the mini-brain; the things most like it (ADRs, Karpathy's wiki, A-MEM, Generative-Agents reflection) are niche or academic.
- **Almost everyone accumulates automatically and is machine-managed** — the exact inverse of the mini-brain axiom: human-curated, deliberately shrinking, store-only-the-non-re-derivable.
- **The property nobody else shares is "forgets/shrinks by design."** Only MemoryBank (Ebbinghaus decay) and Zep (fact invalidation) come close, and both do it *mechanically*, not by editorial judgment.

The best one-line positioning: *durable reflection memory for an AI coding agent, expressed as docs-as-code, governed by ADR-like rationale capture and an irreducible-core / minimize-tokens constraint.* Two anchors for a newcomer: **ADRs for the intent, Generative-Agents reflection for the mechanism — the mini-brain sits where they meet.**

### 1.2 The landscape — conclusions

The conclusions the landscape data supports, grouped by the four families:

- **The column nobody else shares is "forgets/shrinks by design" via human editorial judgment.** Cognee has an explicit `forget` API, Vektor Memory achieves ~97% automatic reduction, and Zep invalidates facts — but all three do it *mechanically*. The three major platforms (Mem0, Letta, Zep) all moved *away* from forgetting in their latest releases.
- **Per family, in one line each:** coding-agent conventions — highest adoption, lowest similarity; they inject *how to act*, not *why*, and AGENTS.md is the explicit anti-mini-brain (spec excludes rationale/lineage). Production memory systems — mostly opaque and machine-managed; they validate the episodic→semantic shape but invert our curation-and-shrink stance. Academic reflection/memory — the seminal mechanisms our dream cycle echoes (Generative Agents, A-MEM, Auto-Dreamer), all automatic. Human knowledge patterns — closest to our content/intent (ADRs) and workflow (Karpathy's wiki), but human-reader and monotonic.

**Ranked on two axes (because they diverge):**
- **By adoption** (most→least): Copilot instructions → Cursor rules → CLAUDE.md → AGENTS.md → Mem0 → Cognee ≈ Zep → Letta → ADRs (eng-ubiquitous) → Obsidian/Zettelkasten → MemOS → LangMem → Vektor → A-MEM → MemoryBank/Generative Agents. (Cline/Kilo Memory Bank deprecated; Roo Code archived — 2026.)
- **By similarity to us** (closest→farthest): Karpathy LLM Wiki (workflow) → ADRs (content) → A-MEM → Generative Agents/Auto-Dreamer (mechanism) → Vektor Memory (shrinks, but automatic) → MemOS (governance) → MemoryBank (forgetting) → … → Mem0/Cursor/Copilot. **Structurally closest new entrant is Vektor Memory (shrinks to irreducible core) — but fully automatic, no editorial judgment. The combination of human-curated + shrinks-by-design remains unoccupied.**

**Are we our own pattern, or a subset? — Our own pattern, a genuine hybrid at an intersection, not a subset of any single parent.** Not just ADRs (same intent, opposite lifecycle: ADRs are immutable and monotonic; our canonical layer is living and shrinks; ADRs have no episodic log or consolidation pass). Not just Zettelkasten/Obsidian (we reject dense atomic linking for few large indexed files; our reader is a machine, not a browsing human). Not just docs-as-code/Diátaxis (those organize for human readers and never mandate deleting re-derivable content). The closest single ancestor for *mechanism* is Generative-Agents/A-MEM reflection.

Two ingredients make it more than a relabel: (1) the **shrink-toward-irreducible mandate** — the inverse of every monotonic pattern above; and (2) **LLM-as-primary-reader**, which justifies few-large-files-with-a-read-index over many-small-linked-notes. **Our distinguishing bet:** the negative-space rule — define the brain by what the code can't say, and let it shrink toward that. It is the one property no popular framework in the neighborhood shares.

### 1.3 The deeper comparison — method and standing results

The first deep pass ran in the July 2026 dream cycle, executing all four threads below; the systems registry has been refreshed with primary-source data and the conclusions follow each thread. Future runs should attack the thesis from a different angle and re-verify only the *stale* entries rather than re-running the whole landscape.

1. **Refresh the landscape against primary sources.** Done July 2026. Major shifts: Mem0 V3 regressed to ADD-only (accumulates forever), Letta pivoted to git-backed "Context Repositories," Zep CE discontinued, Cognee emerged as a major player (~28k★), AGENTS.md donated to Linux Foundation, Copilot Memory shipped with code-citation-based invalidation. "Context engineering" displaced "prompt engineering" as the field's label.
2. **Stress-test the "shrink-by-design" claim.** Done July 2026. **The differentiator holds.** Closest threats: Vektor Memory (97% automatic reduction), Claude Code Auto Dream (200-line budget), "Memory as Metabolism" paper (eigenvector-centrality-based pruning). Each shares one element — none combine human editorial curation + deliberate shrinking + irreducible-core convergence. One published counterargument found: Folkman's "Your CLAUDE.md should grow, not shrink" — conflates lossy automated summarization with editorial distillation, but the underlying concern (context collapse from aggressive compression) deserves engagement.
3. **Move from system-level to feature-level.** Done July 2026. Best-in-class per capability: provenance (Zep/Graphiti bi-temporal), governance metadata (MemClaw/Caura four-tier trust), memory-to-code invalidation (Copilot Memory code citations — **the most significant competitive gap**; the STALE benchmark shows even the best automated approaches achieve only 55.2% accuracy), episodic-to-semantic consolidation (structural strength for us; validated by SimpleMem's deferred-consolidation outperformance of Mem0).
4. **Look for empirical evidence, not just taxonomy.** Done July 2026. Key findings in §1.5. "Less is more" is well-supported empirically. Stale information is actively harmful. Deferred consolidation outperforms eager. LLM-driven continuous consolidation degrades quality. **Critical gap: no direct human-curated-vs-automated A/B test exists at the mini-brain's level of operation.**

### 1.4 Borrowable forms (without borrowing the growth bias)

Several established idioms map directly onto roadmap items in §2; adopting the idiom lends prior art and tooling. But every one of these source patterns *grows*, so the discipline is: borrow the form, keep the contraction.

| Roadmap idea | Borrow from | Concretely |
|---|---|---|
| Rejected-approaches graveyard / open-questions registry | **ADRs (MADR)** | Discrete records with explicit "alternatives considered / rejected." |
| Confidence + provenance + freshness tags | **MemOS metadata** + **Zep bi-temporal** | Per-finding frontmatter: `status`, `born: PR#/session`, `last_verified`. |
| Claim-to-code dependency index / test-binding | **Graphiti fact invalidation** + **Copilot Memory code citations** | A code change is the event that flips a claim's validity — subscribe, don't duplicate. Copilot's approach (verify citations at read time) is the only shipping implementation. |
| Vocabulary for NOTES vs findings vs instructions | **LangMem taxonomy** | Adopt episodic / semantic / procedural as explicit terms. |
| Multi-user classification | **MemOS MemGovernance** | Per-memory permission/classification built into capture. |
| Dream cycle health pass / exit criteria | **Karpathy lint** + **Generative Agents threshold** | Formalize the lint checklist; trigger reflection on accumulated importance/surprise. |

The one comparison already resolved and not worth re-opening: **git vs. Obsidian.** The substrate is identical — a mini-brain vault opens in Obsidian today with zero conversion — so this is purely about tooling around the files. Obsidian would help the **human maintainer** (Dataview/Bases for an auto-generated read-index and "stalest files" dashboard, open-task rollups from frontmatter, backlinks to flag dangling cross-references) but adds **nothing for the LLM consumer**, which reads raw `.md` and ignores the graph/plugins. It is also worse on what matters here: git already gives versioning, blame, PR review, and CI, and the confidentiality posture favors an auditable git/PR trail over third-party sync. Adopting Obsidian's *atomic-note* style would actively fight the load-whole-files design. **Net:** git stays the source of truth (versioning, blame, PR review, CI, auditable confidentiality trail); Obsidian is at most an optional read-only lens for dashboards and link hygiene — additive, never a migration. Recorded here so a future "should we use Obsidian?" doesn't re-litigate it.

### 1.5 Empirical evidence

Evidence relevant to the mini-brain's core hypotheses, assembled from the July 2026 dream cycle. No prior evidence review existed.

**Supporting "less is more" / "shrink toward irreducible":**
- Microsoft "Less Context, Better Agents" (Jun 2026, arXiv:2606.10209): context pruned to last 5 tool calls outperformed full context with 63.9% fewer tokens.
- FSFM (Apr 2026, arXiv:2604.20300): agents using add-all accumulated 2,400+ records with accuracy dropping to 13%; selective management (248 records) achieved 39% — 3x improvement from storing less.
- "Maximum Effective Context Window" (Sep 2025, arXiv:2509.21361): most models show severe accuracy degradation by 1,000 tokens. "Lost in the Middle" replicates 30%+ degradation for middle-positioned information.

**Supporting periodic deferred consolidation (the dream cycle):**
- SimpleMem: deferred consolidation achieves 33.45 F1 vs Mem0's 25.80 with 14x faster construction.
- RecMem (ACL 2026): recurrence-triggered consolidation beats eager approaches with token savings.
- Auto-Dreamer (May 2026, arXiv:2605.20616): decouples fast per-session acquisition from slow cross-session consolidation, mirroring the LOG + dream cycle architecture.

**Supporting human editorial judgment over automated curation:**
- "Useful Memories Become Faulty When Continuously Updated by LLMs" (arXiv:2605.12978): even from ground-truth solutions, GPT-5.4 fails on 54% of problems it previously solved without memory.
- Harvard/Lakkaraju et al. (May 2025, arXiv:2505.16067): bad memories propagate errors; selective addition and deletion boost long-term performance by 10%.
- Agent Drift study (Jan 2026, arXiv:2601.04170): 42% drop in task success from drift over extended interactions.

**Qualifying or challenging:**
- ETH Zurich (Feb 2026, arXiv:2602.11988): LLM-generated context files drop performance 0.5–2%; human-written show marginal improvement. But measures single-task SWE-bench, not multi-session development.
- McMillan factorial study (May 2026, arXiv:2605.10039): file-structure variables have no detectable effect on adherence; within-session compliance decay (~5.6% per function) is the real enemy. Supports conciseness over structure.
- MemDelta (Jun 2026, arXiv:2606.29914): warns that gains reported by memory systems often confound memory-method with model/embedding changes.

**Critical evidence gaps** (absence is itself a finding):
1. No direct human-curated-vs-automated A/B test at the mini-brain's level of operation.
2. No longitudinal study of curated context files over weeks/months.
3. No "dream cycle" effectiveness measurement.
4. No coding-specific memory benchmark beyond single-task SWE-bench.

---

## 2. Capability roadmap

Ideas for extending the pattern, grouped by horizon. Each is a one-line pointer; the reasoning for the whole set is the negative-space bet in §1.

**Near-term — enrich what's already captured.**
- *Provenance in findings* — tag each finding with the PR/session that birthed it.
- *Confidence tags* — mark findings `settled` / `provisional` / `contested`; the dream cycle revisits the shaky ones.
- *Freshness ledger* — record the commit/date each verifiable claim was last checked; the dream prioritizes the stalest. **Partly operationalized:** the research registries now carry `verified` and `reviewed` dates so the dream cycle's research-currency pass diffs rather than re-derives; not yet applied to internal findings.

**Mid-term — let the codebase enforce the memory.**
- *Verification recipes over stored facts* — store *how to re-derive* a volatile number (a grep, a test name) plus *why it matters*, not the number.
- *Claim-to-code dependency index* — each claim records the files/symbols it depends on; the dream only re-verifies claims whose ground truth moved.
- *Test-binding* — a finding cites the test that would fail if it became false, so the codebase becomes the enforcer.
- *Open-questions registry* + *rejected-approaches graveyard* — promote consciously-deferred decisions and dead ends out of per-work-item docs into a queryable canonical record, so future work doesn't re-litigate settled questions.
- *Pre-merge consistency gate* + *review-as-capture* — catch drift at the source (a lightweight closeout subset in CI) and route PR-review surprises back into capture.

**Longer-term — the dream cycle studying itself, and multi-user.**
- *Instruction-drift detection* — check that the setup/closeout/dream templates still match what work items actually produce.
- *Sleep pressure; nap vs. deep sleep* — let merge activity modulate how often and how deeply the brain dreams. (The dream cycle's delta workflow is the precondition: a cheap "is anything stale?" check over the registries is what a cadence gate would trigger on.)
- *Surprise as the capture trigger* — mark prediction-error moments in the log and preferentially promote them.
- *Readiness probes* — keep a curated set of questions (never cached answers) the dream must answer with high confidence from brain + code; a question it can't answer is the finding.
- *Negative-space self-audit* — the generative twin of the dream's reactive check: generate the "questions the repo can't answer" set against the current branch, then sort brain content three ways — questions the brain answers (confirmed load-bearing), questions it misses (capture gap), and content now answerable from code alone (shed it). This adds a second drift axis beyond "is this still true?": "is this still *ours to hold*?"
- *Multi-user evolution* — role-lensed recall over one canonical store (PM reads deferred-decisions + approach; support reads "what this doesn't solve" + field log; eng reads threat model + findings), new episodic streams (support tickets, QA repros, customer conversations) that consolidate into the same findings, and classification built into capture rather than bolted on. The framing: the brain is a **boundary object** — episodic stays personal (NOTES remain attributed to who saw it), semantic goes collective (findings are shared), so one artifact serves each role's lens without forking the brain. Transactive memory: the team need not all know everything, only collectively know it and where it lives.

---

## 3. Open questions

- **Which roadmap items survive the shrink test?** Several ideas (provenance, freshness, confidence tags) *add* per-finding structure. Each must earn its keep against principle 1 — does it capture something non-re-derivable, or is it metadata the git history already implies? The comparison in §1 is partly in service of answering this: adopt a form only where it beats what version control already gives for free.
- **Does the pattern's differentiator hold as the field matures?** Tracked as §1.3 thread 2; escalate to a positioning change in the approach only if a deeper compare shows "shrink-by-design" is no longer distinctive.
- **How do we operationalize "is this still ours to hold?"** The negative-space self-audit (§2) implies a second drift axis: content that has quietly become derivable from code should be shed, not just re-verified. Where does that check live in the dream cycle's checklist, and how does it avoid false positives on knowledge that only *looks* re-derivable?
- **How is the readiness-probe set composed?** One global list, or composed from per-work-item questions contributed at closeout — and store questions only, never cached answers, or it becomes a second copy of FINDINGS waiting to drift. The name is also unsettled ("readiness probes" / "confidence checks"). Interacts with the toolkit-vs-brain question below.
- **How much of this belongs in the toolkit vs. in an individual brain?** Some items (test-binding, freshness ledger) are per-brain conventions the templates would carry; others (instruction-drift detection) are toolkit-level. The line is unsettled and interacts with the universal-vs-exemplar-specific machinery question. The two comparison registries are firmly toolkit-specific — they exist because *this* brain's subject is the pattern; a product brain's research pass is a plain currency check that needs neither.
- **When does shrinking go too far?** *Shrink-by-design* is the differentiator, but aggressive compression can cause context collapse — shedding load-bearing signal, the concern behind Folkman's "your CLAUDE.md should grow, not shrink" (§1.3 thread 2). The pattern separates editorial distillation from lossy summarization but doesn't say where distillation crosses into loss. Should it name an explicit floor on the shrink mandate, or does principle 1 (store only what can't be re-derived) already bound it?
- **Is "few large files" still the right bet for an LLM reader?** LLM-as-primary-reader is what justifies few-large-files-with-a-read-index over many-small-linked-notes (§1.2), but the empirical support is thin: the McMillan factorial study found file structure has no detectable effect on adherence (§1.5), and the field is drifting toward more, smaller, mode-activated files (Cursor, Copilot). Does the stance still hold — and if the evidence is genuinely neutral, is it a bet we keep on other grounds (human maintainability, token cost)?
- **Should memory-to-code invalidation move to near-term?** It is the pattern's most significant competitive gap and the one capability with a shipping external implementation (Copilot's read-time code-citation check, §1.3 thread 3). The enabling pieces — claim-to-code dependency index, test-binding — currently sit under mid-term (§2). Given it is where the field is ahead of us, does it earn promotion?
- **Should the pattern openly acknowledge that its biological grounding is only partially load-bearing?** The honest verdict is 2-of-7 mappings load-bearing, the rest decorative or mixed (§4). The pattern uses biological metaphors — episodic/semantic, consolidation, pruning, dreaming — without marking which are structural and which merely evocative. Should its self-presentation say the grounding is a useful design heuristic rather than a deep parallel, or is implicit use fine as long as §4 stays honest?

---

## 4. Biological grounding

The pattern leans on biological metaphors for memory and cognition; the open question is whether that grounding is load-bearing or merely flattering.

**Headline (2026-07-15):** partially load-bearing. 2 of 7 mappings are genuinely load-bearing (canonical docs as semantic memory; the dream cycle as sleep-dependent consolidation + synaptic pruning), 3 are decorative (`working/`, work rituals, the re-derivability criterion), 2 are mixed (LOG as episodic memory, shrinking as pruning). The grounding is a useful design heuristic and a generative source of mechanism candidates — not a deep structural parallel; alternative frameworks (ADR practice, document management, knowledge graphs) produce similar designs for most mechanisms.