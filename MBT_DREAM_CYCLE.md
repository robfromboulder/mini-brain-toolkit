# Mini-Brain Toolkit: Dream Cycle

> V2, 2026-07-15.

Follow these instructions when the user asks the toolkit to dream and improve itself — the periodic reflection pass that keeps this brain true and small (principle 10).

**Important:** Read `CLAUDE.md` first for file conventions — those govern all edits made during this cycle.

**This brain has two natures.** It is a mini-brain *and* its subject is the mini-brain pattern (`MBT_APPROACH.md` §1.1). So its top-level docs split two ways: its **own brain** (`MBT_SCOPE`, `MBT_APPROACH`, `MBT_FINDINGS`, `MBT_LOG`) and the **product it defines** (`MBT_PATTERN`, `MBT_CREATE_BRAIN`, `MBT_CHECK_BRAIN`, `MBT_RESEARCH`, plus `templates/`). The phases below touch both: Phase 2 keeps the product self-consistent and the brain dogfooding honestly; Phase 3 — because this brain's *subject* is the pattern — is where the standard "refresh APPROACH's external assumptions" becomes a currency check on the research field and the pattern's scientific grounding.

**Guiding principle:** When in doubt, flag for the user rather than auto-correcting. This cycle detects drift and corrects factual staleness; strategy, thesis, and framing changes require human judgment. Version control provides rollback safety, so be thorough about detecting problems — conservative about changing conclusions. **Exception — Phase 3 stance:** the currency phase is *adversarial by mandate* (see there). Being aggressive about hunting disconfirming evidence and conservative about auto-applying thesis changes are not in tension — do both.

**Confidence discipline.** As you draw each conclusion — *before* writing the edit — state a confidence from 1–100. It is a proxy for how many unknowns remain, not a grade. A score below ~70 is a signal to search harder or to flag rather than edit, and obligates you to name the specific unknowns capping it (an unverifiable claim, an inconclusive agent, a thin search). Never round up to look finished. In Phase 3 the score is bounded by the disconfirmation gate: a high confidence you have *not* earned with a real disconfirmation search is exactly the motivated reasoning this cycle is built to resist. Carry the final scores into the Phase 5 self-evaluation.

**Context management:** Phases 1 and 2 have bounded footprints (file listings, cross-doc reads) and are handled directly. Phase 3 is research-heavy — delegate landscape/literature surveys to research agents (general-purpose with web search; Explore is file-only and won't reach the web). Phase 4's LOG/FINDINGS read goes to an Explore agent. The active context briefs agents, synthesizes, makes editorial judgments, and makes all edits.

**Error recovery:** None. If an agent returns inconclusive results, a file is unexpectedly missing, a claim can't be verified, or any step produces an outcome these instructions don't cover — stop the cycle and report to the user. Do not retry, work around, or silently skip. A stopped cycle means the instructions need updating, not that the executor should improvise.

**Before you begin — orient against the last cycle.** Read the last entry in `MBT_DREAM_LOG.md` (grep the final `---`). Carry forward: (a) what the last cycle flagged as *needs human decision* — resolved, still open, or now actionable; (b) what it said it would change about these instructions; (c) which phases found nothing last time — if nothing relevant has changed since, calibrate effort there instead of re-deriving from scratch; (d) the disconfirmation searches the last Phase 3 already ran, so this run attacks the thesis from a *different* angle rather than repeating a spent search. This makes the dream log an input, not only an output, and is what lets a cycle notice it is re-treading. First run (empty log): note it and proceed.

---

## Phase 1: Structural integrity

Mechanical checks over top-level `MBT_*` docs. Run all first; fix failures before the content phases. `templates/` and `archive/` are excluded — template files are bare-named and un-namespaced by design (`MBT_APPROACH.md` §2.5).

1. **Read index → disk.** Every file in the `CLAUDE.md` read index exists on disk.
2. **Disk → read index.** Every top-level `.md` file (excluding `CLAUDE.md`, `README.md`, and this file) appears in the read index. The index is grouped in two blocks (product, then own-brain) — check both. Flag orphans.
3. **Version headers.** Every top-level file except the version-exempt ones (`*_LOG.md`, `*_TASKS.md`) carries a well-formed `> V<N>, YYYY-MM-DD.` line — version and date only. Flag any that smuggled a change note into the header.
4. **Cross-references.** Grep all top-level `.md` files for references to other mini-brain filenames. Every reference must resolve to an existing top-level file — not an `archive/` copy, not a deleted file.
5. **Namespace prefix.** `ls *.md | grep -vE '^(CLAUDE|README)\.md$' | grep -v MBT` should return nothing. Flag any hit.

Fix any failures. Report what was found and fixed.

---

## Phase 2: Dogfooding & self-consistency

A product brain verifies `SCOPE` against its code. This brain has no product code — its "code" is its own teaching artifacts, and its `SCOPE` §2.5 / `APPROACH` §1.1 commit it to *being* the pattern it defines. So Phase 2 has two checks. Both are internal (no web); delegate the cross-doc read to one Explore agent that reads `MBT_PATTERN`, `MBT_CREATE_BRAIN`, `MBT_CHECK_BRAIN`, and lists `templates/` (and `templates/work/`), then reports divergences for the active context to fix or flag.

**(a) Teaching-artifact consistency.** `MBT_PATTERN.md` is the spec; `MBT_CREATE_BRAIN.md` builds it, `MBT_CHECK_BRAIN.md` scores it, `templates/` supplies it. These four must agree. This operationalizes `MBT_SCOPE.md` §4.2 (templates ↔ reference in sync) and the roadmap's *instruction-drift detection*. Check:

- **Principles.** `MBT_PATTERN.md` §2 is authoritative. `MBT_CHECK_BRAIN.md` §2's scorecard must have exactly those principles, same count and meaning, same numbering (`MBT_CHECK_BRAIN.md` §2 already says §2-of-PATTERN wins on divergence — enforce it).
- **File set.** `MBT_PATTERN.md` §3 stage tables ↔ `MBT_CREATE_BRAIN.md` §3 create-table and §5 stage-3 list ↔ actual files in `templates/`. Every file named in one appears in the others; no template is orphaned; no referenced template is missing. (This cycle's own files, `MBT_DREAM_CYCLE`/`MBT_DREAM_LOG`, correspond to `templates/DREAM_CYCLE.md` + a dream-log — verify that mapping too.)
- **Lifecycle.** `MBT_PATTERN.md` §4 and the procedure/template docs describe the same rituals (session → work item → maintenance).

**(b) Dogfooding self-check.** The toolkit must still obey its own pattern at content-stage-or-better health. Apply `MBT_CHECK_BRAIN.md`'s logic to *this repo* (it is a brain) — do not re-implement it, run it. Expect principles 1–8 present and 9–10 present once this file lands. Confirm `SCOPE`/`APPROACH` are still orthogonal (problem vs. chosen design — no solution bias bleeding into `SCOPE`) and the two read-index blocks stay cleanly separated.

**Update.** Mechanical divergences (a scorecard row out of sync with a reworded principle, a template missing from a table, a stale file-set count) — fix directly, bump each touched file. A divergence that changes the *meaning* of a principle or the pattern's structure is thesis work — **flag, don't auto-resolve**. **Do not** add, remove, or renumber principles, or restructure the file set, inside this phase; that is `MBT_PATTERN.md`-level change and belongs to the user.

---

## Phase 3: Research currency — adversarial

This brain's subject is the pattern, so the APPROACH-currency check becomes a currency check on (3a) the competitive/research landscape and (3b) the pattern's grounding in how minds actually work. Both land in `MBT_RESEARCH.md`, whose content is explicitly uncommitted — refreshing it is in-bounds editing. Thesis-level consequences (`MBT_PATTERN` principles, `MBT_APPROACH` positioning, the `MBT_SCOPE` differentiator) are **flagged**, never auto-applied.

**Stance — attack the thesis, don't defend it.** The load-bearing claims — *shrink/forgets-by-design*, the *negative-space rule* (define the brain by what the code can't say), *LLM-as-primary-reader*, *human-curated not machine-managed* — are hypotheses to be attacked with fresh evidence every run. **A cycle that surfaces only confirming evidence has probably fallen into motivated reasoning — treat that as a defect, not a win.** Do not anchor on a fixed reference model or a frozen competitor list; re-survey creatively each time, weight recent and high-adoption work, and go looking for the system or study that makes a mini-brain claim *false*. (This adversarial mandate is specific to this research brain; a product brain's Phase 3 is a plain currency check and should not inherit it.)

**Disconfirmation gate (both sub-phases).** Before concluding, state — for each load-bearing claim examined — what evidence *would* have falsified it and confirm you actually ran that search. If you cannot name a real disconfirmation search you performed, the phase is incomplete. Record these searches in the Phase 5 cycle log so the stance is auditable.

### 3a — Competitive novelty (the peer-review analog)

Execute the four-part method already specified in `MBT_RESEARCH.md` §1.3, via research agents (one per family where useful), primary sources where possible:

1. **Refresh the landscape** (§1.2) against primary sources — re-verify adoption/stars, licensing, and especially acquisitions/pivots among surveyed systems; add systems that appeared since the last cycle. Weight recency and adoption.
2. **Stress-test the differentiator.** Has any system since the last pass added editorial/human-curated forgetting, consolidation-with-deletion, or a shrink-toward-irreducible step? Try to prove *"forgets/shrinks by design"* is no longer unique. Weakening → flag (`MBT_SCOPE` differentiator / `MBT_APPROACH` positioning is the user's call, per `MBT_RESEARCH.md` §3). Holding → a stronger result; state it with fresh evidence.
3. **Feature-level cut.** Move from whole-system to per-capability (who does provenance, governance metadata, memory-to-code invalidation best) and map each to a roadmap item in §2.
4. **Empirical evidence.** Hunt for any published measurement of human-curated vs. machine-managed agent memory (recall, drift, token cost). Absence is itself a finding.

Update the §1.2 table **in place** (do not paste a new giant table — it drifts) and refresh §1.5 sources.

### 3b — Biological / theory-of-mind grounding

The pattern leans on biological metaphors — this pass grounds *and interrogates* them; it does not rubber-stamp them. No pinned model: each cycle, reach for whichever memory/cognition/neuroscience work is most relevant and best-supported, and think from scratch.

1. **Map** the pattern's mechanisms to analogs — `MBT_LOG` ≈ episodic memory, canonical docs ≈ semantic/declarative memory, `working/` ≈ working memory, the dream cycle ≈ sleep-dependent consolidation + synaptic pruning, work rituals ≈ procedural memory. Use the models that fit; don't force one.
2. **Challenge each analogy.** Is it load-bearing or a flattering just-so story? Where the biology and the pattern diverge, name the divergence — a broken metaphor is a finding, not an embarrassment, and is exactly what the adversarial stance is for.
3. **Mine for missing mechanisms** — present in memory/cognition science, absent from the pattern, and plausibly worth adopting *natively* (e.g., an explicit episodic/semantic split, forgetting-curve-driven consolidation, salience/surprise-gated capture, replay, interference effects, metacognitive confidence). Weight well-supported findings over novelty for its own sake.
4. **Flag candidates for the user.** Each candidate is a proposal, not an edit: the user decides whether it graduates to the roadmap (`MBT_RESEARCH.md` §2) or escalates to the pattern (`MBT_PATTERN.md`). **Do not** fold a mechanism into the pattern here.

Maintain the mapping and the live candidate set as a section *within* `MBT_RESEARCH.md` (not a new top-level file — keep the read index from growing). Bump `MBT_RESEARCH.md`.

---

## Phase 4: Findings extraction and reflow

`MBT_LOG.md` accumulates decisions; some belong in `MBT_FINDINGS.md`. **Unlike a product brain, the toolkit runs no work-item closeout on itself** — nothing has pre-promoted findings — so treat extraction as **primary, not a backstop**: scan the LOG forward from the last cycle for promotable material. Then reflow. Delegate the end-to-end read of both files to one Explore agent; it reports extraction candidates, contradictions/supersessions, internal contradictions, and reflow issues.

**Extraction.** Candidates: decisions where one option won for non-obvious reasons, discoveries that reframed the work, constraints that would surprise a future maintainer, approaches tried and abandoned. Grep `MBT_FINDINGS.md` for each candidate's key terms. A **duplicate** is skipped. A **contradiction/supersession** — the candidate makes an existing finding false or reverses a committed direction — is a rewrite in place (bump the version), not a second finding beside the old one. Write in the existing format: **bold statement**, then a reasoning paragraph that stands without the LOG entry it came from.

**Reflow.** Read `MBT_FINDINGS.md` end to end. Its own rule is "assume the current files are ground truth — don't restate what they show," so a finding now made self-evident by the shipped files is a **stale-now-obvious** removal candidate. Also check redundancy/overlap (merge, preserving every distinct reason) and section drift (wrong grouping, split-worthy section, duplicated/empty header from an append). Structural fixes (merges, section repair) — do directly, bump the version. Removing a finding's *substance* or rewriting a conclusion — flag for the user.

---

## Phase 5: Report

Present a summary after all phases complete:

- **Structural fixes** (Phase 1): issues and resolutions, or "none".
- **Dogfooding & consistency** (Phase 2): what agreed; what drifted and was synced; anything meaning-level flagged.
- **Files updated** (Phases 2–4): each as `file V<old> → V<new> — one-line summary`.
- **Research — novelty** (3a): differentiator status (holding / weakening, with the evidence), landscape deltas, and flags.
- **Research — biology** (3b): mapping/analogy updates (including any metaphor found broken) and candidate mechanisms flagged.
- **New findings extracted** (Phase 4): each bold statement.
- **Findings reflow**: structural changes applied; substance items flagged.
- **Needs human decision**: thesis-level flags from Phases 2–3, each with what changed and the implication.

If a phase found nothing, say so in one line — don't pad.

**Cycle log.** Append an entry to `MBT_DREAM_LOG.md` using the LOG-entry format from `MBT_SESSION_CLOSEOUT.md`. Cover the standard signal — which phases ran/were skipped and why, what broke or surprised, how many agents were spawned and whether their results were useful, what you'd change about these instructions. Two additions specific to this brain: (1) record the **disconfirmation searches** run in Phase 3, so the adversarial stance is auditable; (2) note anything about *this cycle's structure* that worked or didn't **relative to a product brain's cycle** — this is one of three cycles being run and compared, and that contrast is the raw signal for evolving the dream-cycle pattern across all of them.

**Self-evaluation.** Close the entry by scoring the *cycle's own performance*, not only its findings — this is the signal for whether dreaming is converging or spinning, and what makes runs comparable across cycles and over time:
- **Confidence per headline conclusion (1–100)** — Phase 2 "the teaching artifacts are self-consistent and the toolkit still obeys its own pattern"; Phase 3a "the *forgets/shrinks-by-design* differentiator still holds"; Phase 3b "the biological grounding is load-bearing, not flattering". Each Phase 3 score must be justified by the disconfirmation search actually run, not by absence of contrary evidence you didn't look for. For any score below ~70, name the unknowns that cap it.
- **New ground vs. re-tread** — classify this run against the last: *net-new* (surfaced findings/changes the last run didn't), *incremental*, or *re-tread* (same ground, no movement), with one line of evidence. For a research brain, a re-tread run that merely re-confirms the thesis is a specific warning sign — say so.
- **Depth achieved** — did each phase run to its intent, or run shallow (agent inconclusive, source unavailable, halted)? Name any that did.
- **Diminishing returns** — if this is the Nth consecutive *re-tread* run with no findings and no edits, say so and recommend either dreaming less often or that the brain has reached a fixed point on current inputs (a real result, not a failure).
