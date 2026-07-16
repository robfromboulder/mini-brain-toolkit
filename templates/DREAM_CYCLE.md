# <Project>: Mini-Brain Dream Cycle

> V1, <date>.

Follow these instructions when the user asks the mini-brain to dream and improve itself — the periodic reflection pass that keeps the brain true and small (principle 10).

**Important:** Read `CLAUDE.md` first for file conventions — those govern all edits made during this cycle.

**Guiding principle:** When in doubt, flag for the user rather than auto-correcting. This cycle detects drift and corrects factual staleness. Strategy and framing changes require human judgment. Version control provides rollback safety, so be thorough about detecting problems — but conservative about changing analytical conclusions.

**Confidence discipline.** As you draw each conclusion — *before* writing the edit — state a confidence from 1–100. It is a proxy for how many unknowns remain, not a grade. A score below ~70 is a signal to search harder or to flag rather than edit, and obligates you to name the specific unknowns capping it (an unverifiable claim, an inconclusive agent, a thin search). Never round up to look finished. Carry the final scores into the Phase 5 self-evaluation.

**Context management:** Structural checks (Phase 1) and external-currency checks (Phase 3) have bounded context footprints and are handled directly. Heavy reads — full codebase searches, full LOG and FINDINGS files (Phases 2 and 4) — should be delegated to Explore agents. The active context handles agent briefing, result synthesis, editorial judgments, and all file edits.

**Error recovery:** None. If an Explore agent returns inconclusive results, a file is unexpectedly missing, a claim can't be verified, or any step produces an outcome the instructions don't cover — stop the cycle and report the error to the user. Do not retry, work around, or silently skip. A stopped cycle is a signal that the instructions need updating, not that the executor needs to improvise.

**Before you begin — orient against the last cycle.** Read the last entry in `<PREFIX>_DREAM_LOG.md` (grep the final `---`). Carry forward: (a) what the last cycle flagged as *needs human decision* — resolved, still open, or now actionable; (b) what it said it would change about these instructions; (c) which phases found nothing last time — if nothing relevant has changed since, calibrate effort there instead of re-deriving from scratch. This makes the dream log an input, not only an output, and is what lets a cycle notice it is re-treading. First run (empty log): note it and proceed.

---

## Phase 1: Structural integrity

Mechanical checks. Run all first; fix any failures before the content phases.

1. **Read index → disk.** Every file in the `CLAUDE.md` read index exists on disk.
2. **Disk → read index.** Every top-level `.md` file (excluding `CLAUDE.md`, `README.md`, and this file) appears in the read index. Flag orphans.
3. **Version headers.** Every top-level file except the version-exempt ones (`*_LOG.md`, `*_TASKS.md`) carries a well-formed `> V<N>, YYYY-MM-DD.` line — version and date only. Flag any that smuggled a change note into the header.
4. **Cross-references.** Grep all top-level `.md` files for references to other mini-brain filenames. Every reference must resolve to an existing top-level file — not an archive copy, not a deleted file.
5. **Namespace prefix.** Every top-level `.md` except the exempt repo artifacts carries the `<PREFIX>` token: `ls *.md | grep -vE '^(CLAUDE|README)\.md$' | grep -v <PREFIX>` should return nothing. Flag any hit.
6. **Working/archive filename leakage.** Grep all top-level `.md` files for `.md` filename mentions. Any filename that is neither a canonical top-level file (listed in the `CLAUDE.md` read index, or one of the exempted names `CLAUDE.md`, `README.md`) nor this file itself is a stale reference to a working or archived doc and must not appear. For each hit: if the referenced file still exists in `working/` or `archive/`, read it, extract the relevant substance, and replace the reference inline with that content. If the file no longer exists anywhere, flag for the user — don't guess at the content. No top-level file may cite an `archive/` or `working/` filename directly.

Fix any failures. Report what was found and fixed.

---

## Phase 2: Scope accuracy

`<PREFIX>_SCOPE.md` makes factual claims about the codebase. These go stale when the code changes without a document update.

**Extract claims** from SCOPE — implementation details (class/method names, config, constants, counts), architectural facts (trust boundaries, message flow), **absence claims** ("no control does X" — the most fragile, they break silently when a capability is added, so prioritize them), and control/behavior descriptions.

**Verify** by spawning Explore agents with specific claim lists grouped by section. Brief each with the exact claim text and the identifiers it contains; agents search by name, not location, since code moves and gets renamed. Ask each for (a) still true? and (b) easily derivable from code? Check against the main/current release branch, not feature branches.

**Update.** Stale claims: correct to current state, preserving the document's analytical framing. Invalidated absence claims: don't just flip "no X" to "X exists" — describe what was added and the gap that remains. Codebase-derivable detail with no analytical value: consider removing rather than maintaining. Confirmed-accurate claims: note them as verified in the Phase 5 report.

**Do not** add new goals, scope categories, or boundaries (that's scoping work), delete analytical content because a premise changed (update the premise, then check the analysis still follows), or rewrite conclusions — flag for the user if a factual change undermines one.

---

## Phase 3: Approach currency

`<PREFIX>_APPROACH.md` may depend on specifics that change independently of the codebase. Two flavors — check whichever the approach actually commits to:

- **Technical currency** — versions of frameworks/libraries the design pins, protocol/spec versions, runtime/platform/model availability, breaking API changes.
- **Vendor/market** — vendor status (acquisitions, shutdowns, pivots), pricing, licensing changes, new entrants.

Use web search to verify. Factual corrections (versions, dates, pricing): update in place. Status/version changes affecting a *recommended* choice: flag for the user. New entrants or alternatives: note without promoting to primary without explicit direction. Do not change strategic framing — flag if a change suggests reconsidering it.

(If the brain's APPROACH has no external dependencies, this phase is a no-op — say so and move on.)

---

## Phase 4: Findings extraction and reflow

Session logs (`<PREFIX>_LOG.md`) accumulate decisions and discoveries; some should be promoted to `<PREFIX>_FINDINGS.md`. Two activities: **extraction** (find LOG candidates not yet promoted, reconcile contradictions) and **reflow** (maintain FINDINGS as a coherent body — merge overlap, fix section drift, prune stale-now-obvious). Run extraction first, then reflow.

Most per-work-item knowledge should already have been promoted at work closeout, so treat extraction as a verification/backstop pass. Delegate the read-heavy work to an Explore agent that reads the full FINDINGS and LOG files and reports: extraction candidates, contradictions/supersessions, internal contradictions, and reflow issues.

**Extraction.** Look for decisions where one option won for non-obvious reasons, discoveries that reframed the problem, constraints that would surprise a future developer, and approaches tried and failed (negative findings are valuable). Grep FINDINGS for each candidate's key terms: a **duplicate** is skipped; a **contradiction/supersession** is a rewrite in place (bump the version), not a second finding beside the old one.

**Reflow.** Read FINDINGS end to end and check for redundancy/overlap (merge, preserving every distinct reason), section drift (re-section, fix duplicated/empty headers), and stale-now-obvious findings (now self-evident from shipped code — removal candidates). Structural fixes (merges, section repair) may be done directly, bumping the version. Removing a finding's *substance* or rewriting a conclusion is analytical — flag it for the user rather than auto-applying.

---

## Phase 5: Report

Present a summary after all phases complete: **structural fixes** (Phase 1, or "none"); **files updated** (Phases 2–4, each as `file V<old> → V<new> — one-line summary`); **confirmed accurate** (grouped by section, not enumerated); **needs human decision** (factual changes that affect strategy/scope/framing); **new findings extracted**; **findings reflow** (structural changes applied, substance items flagged). If a phase found nothing, say so in one line — don't pad.

**Cycle log.** After the report, append an entry to `<PREFIX>_DREAM_LOG.md` using the standard LOG entry format from `<PREFIX>_SESSION_CLOSEOUT.md`. Cover: which phases ran/were skipped and why; what broke or surprised (the raw signal for instruction improvements); how many Explore agents were spawned and whether their results were useful; and what you'd change about these instructions based on this run. **Include a *Questions for humans* section** — the open questions and needs-human-decision items this cycle surfaced but could not resolve — mirroring the Phase 5 report so the next cycle's orientation step picks them up.

**Model and effort.** Record the model and effort level used for the cycle in the dream log entry header (after the session-ID line, if the entry format includes one). The model name is stated in the system environment context ("You are powered by the model named…"); the effort level may appear in session command output. If either cannot be determined, ask the user before writing the entry. This is what makes runs comparable on depth and cost — a low-effort small-model run and a high-effort large-model run are not the same cycle.

**Self-evaluation.** Close the entry by scoring the *cycle's own performance*, not only its findings — this is the signal for whether dreaming is converging or spinning, and what makes runs comparable across cycles and over time:
- **Confidence per headline conclusion (1–100)** — one per phase that draws a conclusion (e.g. Phase 2 "SCOPE matches current code"; Phase 3 "APPROACH's external assumptions are current"), plus a confidence score on the findings this run produced. For any score below ~70, name the unknowns that cap it.
- **New ground vs. re-tread** — classify this run against the last: *net-new* (surfaced findings/changes the last run didn't), *incremental*, or *re-tread* (same ground, no movement), with one line of evidence.
- **Depth achieved** — did each phase run to its intent, or run shallow (agent inconclusive, source unavailable, halted)? Name any that did.
- **Diminishing returns** — if this is the Nth consecutive *re-tread* run with no findings and no edits, say so and recommend either dreaming less often or that the brain has reached a fixed point on current inputs (a real result, not a failure).
