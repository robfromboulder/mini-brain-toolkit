# Mini-Brain Toolkit: Dream Cycle

> V12, 2026-08-04.

Follow these instructions when the user asks the toolkit to dream and improve itself — the periodic reflection pass that keeps this brain true and small (principle 10).

**Important:** Read `CLAUDE.md` first for file conventions — those govern all edits made during this cycle.

**This brain has two natures.** It is a mini-brain *and* its subject is the mini-brain pattern. So its top-level docs split two ways: its **own brain** (`MBT_SCOPE`, `MBT_APPROACH`, `MBT_FINDINGS`, `MBT_LOG`) and the **product it defines** (`MBT_PATTERN`, `MBT_COMPONENTS`, `MBT_CREATE_BRAIN`, `MBT_CHECK_BRAIN`, `MBT_RESEARCH`, plus `templates/`). The phases below touch both: Phase 2 keeps the product self-consistent and the brain dogfooding honestly; Phase 3 — because this brain's *subject* is the pattern — is where the standard follow-on research over APPROACH's external assumptions widens to the whole memory-systems field and the pattern's scientific grounding.

**Guiding principle:** When in doubt, flag for the user rather than auto-correcting. This cycle detects drift and corrects factual staleness; strategy, thesis, and framing changes require human judgment. Version control provides rollback safety, so be thorough about detecting problems — conservative about changing conclusions. **Exception — Phase 3 stance:** the follow-on-research phase is *adversarial by mandate*. Being aggressive about hunting disconfirming evidence and conservative about auto-applying thesis changes are not in tension — do both.

**Confidence discipline.** As you draw each conclusion — *before* writing the edit — state a confidence from 1–100. It is a proxy for how many unknowns remain, not a grade. A score below ~70 is a signal to search harder or to flag rather than edit, and obligates you to name the specific unknowns capping it (an unverifiable claim, an inconclusive agent, a thin search). Never round up to look finished. In Phase 3 the score is additionally bounded by that phase's disconfirmation gate. Carry the final scores into the Phase 5 self-evaluation.

**Context management:** Phase 1 has a bounded footprint (file listings, greps) and is handled directly. File reads are delegated by size: hand a read to an Explore agent only when it exceeds roughly 500 lines — below that, read directly. This covers Phase 2's cross-doc read and Phase 4's LOG/FINDINGS read, which stay in the active context until the brain outgrows the threshold. Phase 3 is research-heavy, but the `MBT_COMPARABLES.md` and `MBT_BIOLOGY.md` registries bound it: spawn web-search agents (general-purpose with web search; Explore is file-only and won't reach the web) only where §3a/§3b call for one — **not one agent per thread.** A routine cycle spends at most ~10 sub-agents in total; needing more is itself a finding to flag in the Phase 5 report, not a license to keep spawning. Do the synthesis (feature-level cut, positioning, verdicts) in the active context over registry data, not in sub-agents — sub-agent fan-out is the dominant cost of this cycle, and most of it was re-confirming facts the registry already holds. Retrieval/change-check agents don't need high reasoning effort — brief them narrowly and prefer a cheaper/faster model where the harness allows. The active context briefs agents, synthesizes, makes editorial judgments, and makes all edits.

**Error recovery:** None. If an agent returns inconclusive results, a file is unexpectedly missing, a claim can't be verified, or any step produces an outcome these instructions don't cover — stop the cycle and report to the user. Do not retry, work around, or silently skip. A stopped cycle means the instructions need updating, not that the executor should improvise.

**Before you begin — orient against the last cycle.** Read the last entry in `MBT_DREAM_LOG.md` (grep the final `---`). Carry forward: (a) what the last cycle flagged as *needs human decision* — resolved, still open, or now actionable; (b) what it said it would change about these instructions; (c) which phases found nothing last time — if nothing relevant has changed since, calibrate effort there instead of re-deriving from scratch; (d) the disconfirmation searches the last Phase 3 already ran, so this run attacks the thesis from a *different* angle rather than repeating a spent search. This makes the dream log an input, not only an output, and is what lets a cycle notice it is re-treading. First run (empty log): note it and proceed.

---

## Phase 1: Structural integrity

Mechanical checks over top-level `MBT_*` docs and `working/`. Run all first; fix failures before the content phases. `templates/` and `archive/` are excluded — template files are bare-named and un-namespaced by design.

1. **Read index → disk.** Every file in the `CLAUDE.md` read index exists on disk.
2. **Disk → read index.** Every top-level `.md` file (excluding `CLAUDE.md`, `README.md`, and this file) appears in the read index. The index is grouped in two blocks (product, then own-brain) — check both. Flag orphans.
3. **Version headers.** Every top-level file except the version-exempt ones (`*_LOG.md`, `*_TASKS.md`) carries a well-formed `> V<N>, YYYY-MM-DD.` line — version and date only. Flag any that smuggled a change note into the header.
4. **Cross-references.** Grep all top-level `.md` files for references to other mini-brain filenames. Every reference must resolve to an existing top-level file — not an `archive/` copy, not a deleted file. Within the docs covered by `CLAUDE.md`'s declared-exemptions table, also hold each reference to that table and to the cross-reference form: a permitted direction only, cited by name, not section number. A stray section number in an otherwise-permitted reference is a mechanical fix; a forbidden-direction reference usually means content bled across a boundary — flag it for the user rather than just deleting the pointer.
5. **Namespace prefix.** `ls *.md working/*.md | grep -vE '^(CLAUDE|README)\.md$' | grep -v MBT` should return nothing. Flag any hit.
6. **Working/archive filename leakage.** Grep all top-level `.md` files for `.md` filename mentions, then flag any that **name an explicit `working/…` or `archive/…` path, or resolve to a file that exists in `working/` or `archive/`** — no top-level doc may cite a transient working/archived doc directly. The *resolves-to* trigger is what keeps this precise on this brain: legitimate mentions that would otherwise look suspicious — canonical top-level files, `templates/` files (the toolkit documents its own templates), this file, and the external- or other-brain names the comparative docs cite as references (`AGENTS.md`, `CONVENTIONS.md`, `GEMINI.md`, `log.md` in `MBT_COMPARABLES.md`/`MBT_RESEARCH.md`; `<PREFIX>_*` placeholder notation) — name things that are not local `working/`/`archive/` files, so they don't match. For each real hit: if the file still exists in `working/` or `archive/`, read it, extract the relevant substance, and replace the reference inline with that content; if it no longer exists there, flag for the user — don't guess at the content.

Fix any failures. Report what was found and fixed.

---

## Phase 2: Dogfooding & self-consistency

A product brain verifies `SCOPE` against its code. This brain has no product code — its "code" is its own teaching artifacts, and its `SCOPE` and `APPROACH` commit it to *being* the pattern it defines. So Phase 2 has three checks. All are internal (no web); the cross-doc read covers `MBT_PATTERN`, `MBT_COMPONENTS`, `MBT_CREATE_BRAIN`, `MBT_CHECK_BRAIN`, and a listing of `templates/` (and `templates/work/`) — one Explore agent or a direct read per the context-management size rule — and reports divergences for the active context to fix or flag.

**(a) Teaching-artifact consistency.** `MBT_PATTERN.md` and `MBT_COMPONENTS.md` are the spec — the base pattern and its component layer; `MBT_CREATE_BRAIN.md` builds it, `MBT_CHECK_BRAIN.md` scores it, `templates/` supplies it. These five must agree. This operationalizes `MBT_SCOPE.md`'s templates-↔-reference-in-sync requirement and the roadmap's *instruction-drift detection*. Check:

- **Principles.** `MBT_PATTERN.md`'s principles list is authoritative. `MBT_CHECK_BRAIN.md`'s scorecard must have exactly those principles, same count and meaning, same numbering (`MBT_CHECK_BRAIN.md` already subordinates its scorecard to `MBT_PATTERN.md` — enforce it).
- **File set.** `MBT_PATTERN.md`'s stage tables ↔ `MBT_CREATE_BRAIN.md`'s create-table and stage-3 file list ↔ actual files in `templates/`. Every file named in one appears in the others; no template is orphaned; no referenced template is missing. (This cycle's own files, `MBT_DREAM_CYCLE`/`MBT_DREAM_LOG`, correspond to `templates/DREAM_CYCLE.md` + a dream-log — verify that mapping too.)
- **Component layer.** `MBT_COMPONENTS.md` ↔ `templates/COMPONENTS_CLAUDE.md`: the naming grammar, token-ownership and naming rules, placement and log-routing rules, and the per-doctype exemption table must state the same convention in both — the template is the layer's shipped copy and drifts independently. The component passages in `MBT_CREATE_BRAIN.md`, `MBT_CHECK_BRAIN.md`, and the maintenance templates must enact that same convention.
- **Lifecycle.** `MBT_PATTERN.md`'s lifecycle section and the procedure/template docs describe the same rituals (session → work item → maintenance).

**(b) Dogfooding self-check.** The toolkit must still obey its own pattern at content-stage-or-better health. Apply `MBT_CHECK_BRAIN.md`'s logic to *this repo* (it is a brain) — do not re-implement it, run it. Expect principles 1–8 present and 9–10 present once this file lands. Confirm `SCOPE`/`APPROACH` are still orthogonal (problem vs. chosen design — no solution bias bleeding into `SCOPE`) and the two read-index blocks stay cleanly separated.

**(c) Open-question scrub.** The Open Questions section of `MBT_SCOPE.md` poses questions the toolkit's own evolution answers out from under the doc — check (a) already bears on its templates-and-reference-sync question, the standing example. Check each question against the artifacts this phase just read; anything that now answers or narrows one is flagged with the evidence — writing a resolution into `MBT_SCOPE.md` is scoping judgment, not a dream-cycle edit.

**Update.** Mechanical divergences (a scorecard row out of sync with a reworded principle, a template missing from a table, a stale file-set count) — fix directly, bump each touched file. A divergence that changes the *meaning* of a principle or the pattern's structure is thesis work — **flag, don't auto-resolve**. **Do not** add, remove, or renumber principles, or restructure the file set, inside this phase; that is `MBT_PATTERN.md`-level change and belongs to the user.

---

## Phase 3: Follow-on research — adversarial

This brain's subject is the pattern, so the standard follow-on research over APPROACH's external assumptions widens to (3a) the competitive/research landscape and (3b) the pattern's grounding in how minds actually work. The **data** lands in the registries — `MBT_COMPARABLES.md` (3a) and `MBT_BIOLOGY.md` (3b), whose content is explicitly uncommitted, so refreshing state and dates there is in-bounds editing; the **conclusions** land in `MBT_RESEARCH.md`. Thesis-level consequences (`MBT_PATTERN` principles, `MBT_APPROACH` positioning, the `MBT_SCOPE` differentiator) are **flagged**, never auto-applied.

**Nap gate.** If every registry `verified`/`reviewed` date is fresher than ~30 days and the last cycle left no Phase 3 flag open, skip Phase 3 and say so in the report — the registry dates *are* the "is anything stale?" check. A user-requested full re-baseline overrides the gate.

**Stance — attack the thesis, don't defend it.** The load-bearing claims — *shrink/forgets-by-design*, the *negative-space rule* (define the brain by what the code can't say), *LLM-as-primary-reader*, *human-curated not machine-managed* — are hypotheses to be attacked with fresh evidence every run. **A cycle that surfaces only confirming evidence has probably fallen into motivated reasoning — treat that as a defect, not a win.** Do not anchor on a fixed reference model or a frozen competitor list; re-survey creatively each time, weight recent and high-adoption work, and go looking for the system or study that makes a mini-brain claim *false*. **"Don't anchor on a frozen list" governs *breadth*** — actively hunt entrants and findings not yet in the registries — **not re-verification** of known entries (§3a/§3b). (The adversarial mandate is specific to this research brain and should not be inherited; a product brain's Phase 3 is still follow-on research — curious about what it doesn't know, aimed at its own field — without the attack-the-thesis stance.)

**Disconfirmation gate (both sub-phases).** Before concluding, state — for each load-bearing claim examined — what evidence *would* have falsified it and confirm you actually ran that search. If you cannot name a real disconfirmation search you performed, the phase is incomplete. Disconfirmation is not additional fan-out: word the new-entrant and new-research hunts adversarially so each search doubles as one. Record these searches in the Phase 5 cycle log so the stance is auditable.

### 3a — Competitive novelty (the peer-review analog)

`MBT_COMPARABLES.md` is the baseline. Work from it as a delta pass, not a re-survey — the method in `MBT_RESEARCH.md` still frames the *questions*, but the registry answers most of them without new web work:

1. **Triage.** Read the registry. **Living** entries carry a `verified` date and a `change signal` — sort by staleness and select the ~5 stalest (plus any flagged fast-moving) for a change-check; the rest wait, and the `verified` dates rotate them in automatically over later cycles. On a user-requested full re-baseline, select every living entry. **Static** entries (papers, frozen conventions) are not re-fetched; they generate work only via supersession or a new sibling appearing.
2. **Change-check the stale living entries.** Fetch each selected entry's canonical source, read current state (stars, version/release, licensing, forgetting behavior), compare to the stored `known state`. Unchanged → just bump `verified`. Changed → it joins the delta set. This is retrieval, not synthesis — default to a direct fetch of the canonical source, and spawn a narrow, low-effort agent only when a fetch can't answer.
3. **Hunt for new entrants** — where the adversarial energy goes (the mandate is about *breadth*: systems not yet in the registry, not re-verifying known ones). One focused search per family where useful, weighting recency and adoption; add rows for what you find.
4. **Deep-dive the delta set only** — changed living entries plus new entrants. For each: run the differentiator stress-test (has it added editorial/human-curated forgetting, consolidation-with-deletion, or a shrink-toward-irreducible step?) and place it on the feature-level map (provenance / governance / memory-to-code invalidation / episodic-to-semantic consolidation, → the roadmap in `MBT_RESEARCH.md`).
5. **Synthesize in the active context** over the now-current registry: re-derive the two-axis rankings and the differentiator verdict only if a delta moves them. Hunt for any published measurement of human-curated vs. machine-managed memory (recall, drift, token cost); absence is itself a finding (record in `MBT_RESEARCH.md`).

Write updated state and `verified` dates to `MBT_COMPARABLES.md` **in place** (do not paste a fresh giant table — it drifts); write conclusions/deltas to `MBT_RESEARCH.md`. A differentiator weakening → flag (`MBT_SCOPE` differentiator / `MBT_APPROACH` positioning is the user's call, per `MBT_RESEARCH.md`). Holding → a stronger result; state it with the fresh evidence.

### 3b — Biological / theory-of-mind grounding

`MBT_BIOLOGY.md` is the baseline — a mechanism-mapping table holding the verdicts, and per-field entries carrying key research, a `reviewed` date, and any candidate mechanisms. A field's foundational science is effectively static (CLS 1995, SHY 2003/2014, Richards & Frankland 2017 don't move month to month), so this is a *new-research* pass, not a re-derivation:

1. **Re-confirm, don't rebuild.** The mechanism mapping and verdicts in `MBT_BIOLOGY.md` are the standing result. Do not re-derive them from scratch. Read them forward and ask, per field, whether anything you already know contradicts the stored verdict.
2. **Hunt new research per field.** For each field in `MBT_BIOLOGY.md`, search for work published since its `reviewed` date that would strengthen, weaken, or add a mechanism — the adversarial move is going after the finding that breaks a "load-bearing" verdict or the mechanism the pattern is missing. Focused, low-effort searches; one per field at most, and skip fields where nothing plausibly moved.
3. **Update in place.** Where new research bears on a field, update that field's research + `reviewed` date and, if a verdict changes, the mapping table — all in `MBT_BIOLOGY.md`. A new candidate mechanism goes in `MBT_BIOLOGY.md`'s candidate list with a status.
4. **Flag candidates for the user.** Each candidate is a proposal, not an edit: the user decides whether it graduates to the roadmap (`MBT_RESEARCH.md`) or escalates to the pattern (`MBT_PATTERN.md`). **Do not** fold a mechanism into the pattern here.

Bump `MBT_BIOLOGY.md`. Refresh the headline verdict in `MBT_RESEARCH.md` only if the load-bearing/decorative tally changed.

---

## Phase 4: Findings extraction and reflow

`MBT_LOG.md` accumulates decisions; some belong in `MBT_FINDINGS.md`. **Unlike a product brain, the toolkit runs no work-item closeout on itself** — nothing has pre-promoted findings — so treat extraction as **primary, not a backstop**: scan the LOG forward from the last cycle for promotable material. Then reflow. Read both files end to end — one Explore agent or a direct read per the context-management size rule — collecting extraction candidates, contradictions/supersessions, internal contradictions, and reflow issues.

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
- **Needs human decision**: flags from any phase — thesis-level (Phases 2–3), extraction/reflow substance (Phase 4) — each with what changed and the implication.

If a phase found nothing, say so in one line — don't pad.

**Needs-human-decision list.** The dream log entry must include a standalone `## Needs human decision` section — a numbered list where each item states the context, what changed, and the specific decision to make. It is the primary output readers act on, and exactly what the next cycle's orientation step reads — each item must be self-contained, understandable without the rest of the entry. An empty list is fine — write "None" and move on.

**Cycle log.** Append an entry to `MBT_DREAM_LOG.md` using the LOG-entry format from `MBT_SESSION_CLOSEOUT.md`. Keep the entry even for a dry or aborted run — the orientation step and self-evaluation only work against a kept log. Cover the standard signal — which phases ran/were skipped and why, what broke or surprised, how many agents were spawned and whether their results were useful, what you'd change about these instructions. Two additions specific to this brain: (1) record the **disconfirmation searches** run in Phase 3, so the adversarial stance is auditable; (2) note anything about *this cycle's structure* that worked or didn't **relative to a product brain's cycle** — this is one of three cycles being run and compared, and that contrast is the raw signal for evolving the dream-cycle pattern across all of them.

**Model and effort.** Record the model and effort level used for the cycle in the dream log entry header (after the session-ID line). The model name is stated in the system environment context ("You are powered by the model named…"); the effort level may appear in session command output. If either cannot be determined, ask the user before writing the entry. This is what makes runs comparable on depth and cost — a low-effort small-model run and a high-effort large-model run are not the same cycle.

**Self-evaluation.** Close the entry by scoring the *cycle's own performance*, not only its findings — this is the signal for whether dreaming is converging or spinning, and what makes runs comparable across cycles and over time:
- **Confidence per headline conclusion (1–100)** — Phase 2 "the teaching artifacts are self-consistent, the toolkit still obeys its own pattern, and no open question has been overtaken unnoticed"; Phase 3a "the *forgets/shrinks-by-design* differentiator still holds"; Phase 3b "the biological grounding is load-bearing, not flattering"; and each **finding extracted this run** (Phase 4), or an overall confidence in the run's findings if none. Each Phase 3 score must cite the disconfirmation search that earned it. For any score below ~70, name the unknowns that cap it.
- **New ground vs. re-tread** — classify this run against the last: *net-new* (surfaced findings/changes the last run didn't), *incremental*, or *re-tread* (same ground, no movement), with one line of evidence. For a research brain, a re-tread run that merely re-confirms the thesis is a specific warning sign — say so.
- **Depth achieved** — did each phase run to its intent, or run shallow (agent inconclusive, source unavailable, halted)? Name any that did.
- **Diminishing returns** — if this is the Nth consecutive *re-tread* run with no findings and no edits, say so and recommend either dreaming less often or that the brain has reached a fixed point on current inputs (a real result, not a failure).
