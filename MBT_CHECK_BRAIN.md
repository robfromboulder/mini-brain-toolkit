# Mini-Brain Toolkit: Check an Existing Mini-Brain

> V4, 2026-07-09.

This document is the procedure for evaluating an existing mini-brain against the pattern and surfacing where it could improve — whether the brain was built from this toolkit or grew on its own.

**Stance.** This is a diagnostic that produces *opportunities*, not a grade. Most repos match some principles and not others; partial adherence is normal and fine. A repo can be a healthy mini-brain without doing everything here, and doing everything mechanically without the underlying value misses the point. Lead with what's working, then what would help most. Never edit the target brain during a check unless the user explicitly asks — checking observes; creation and the dream cycle change.

**Inputs.** The path to the target repo. If the user hasn't named it, ask. If a known healthy mini-brain is available to consult, use it to calibrate what "good" looks like for a convention before judging the target against it — but the pattern reference (`MBT_PATTERN.md`) is the authority, not any single exemplar.

---

## 1. Orient

Read the target's entrypoint first (`CLAUDE.md` or equivalent), then list the repo top-level and its `archive/`/`working/` dirs. Identify: the namespace token in use, which canonical docs exist, whether there's a session log, and what stage the brain is at (`MBT_PATTERN.md` §3: seed / content / mature). Read the canonical docs' first lines (not their full bodies yet) to see version headers and purpose. This is a bounded, low-context pass — save heavy full-file reads for §3.

If the repo has no entrypoint and no namespaced docs, it may not be a mini-brain at all — say so, and offer `MBT_CREATE_BRAIN.md` instead of forcing a principle-by-principle scoring.

---

## 2. Score against the principles

Walk the ten principles from `MBT_PATTERN.md` §2 one at a time, in order. For each, give a verdict — **present / partial / absent / not applicable** — with a one-line note on what you actually saw, and (when not present) the concrete opportunity. The table below is a checking aid; if it and `MBT_PATTERN.md` §2 ever diverge, §2 is authoritative.

| # | Principle | What to look for |
|---|---|---|
| 1 | Keep only what can't be re-derived | Docs hold *why*, not a restated copy of the code/README. Is there a stated bias toward small? Contrast: a store that mirrors the architecture and only grows. |
| 2 | Its own repository, outside the code | The brain is a standalone repo beside the product, not a folder committed inside the product repo. Contrast: docs forked and versioned with the code they describe. |
| 3 | Orthogonal documents | Each doc covers one non-overlapping dimension (problem, approach, findings, log); a question maps to one file. Contrast: overlapping docs, or one doc covering everything. |
| 4 | Log separate from distilled docs | An append-only, dated, attributed session log *and* a distinct set of living current-state docs. Contrast: one mutable blob, or an ever-growing log never distilled. |
| 5 | Entrypoint with read index | One file a reader opens first, carrying a table of what to read for a given question and what's current vs. retired. Contrast: finding files by guesswork. |
| 6 | SCREAMING_SNAKE_CASE namespace | A shared uppercase token on every knowledge file; wouldn't clash if two brains loaded together. Contrast: generic names lost among repo files. |
| 7 | Versioned and dated | A lightweight `> V<N>, date` stamp on canonical docs; history left to version control. Contrast: undated docs, or in-tree "old version" copies. |
| 8 | WIP apart from settled | A `working/` (or equivalent) holding area for drafts/experiments, distinct from the trusted core. Contrast: provisional and canonical content mixed. |
| 9 | Standard open/close of a work unit | A setup ritual and a matching closeout that harvests durable lessons into canonical docs and retires (moves, not deletes) scratch files. Contrast: every effort reinventing structure and stranding its insights. |
| 10 | Scheduled reflection pass | A defined, recurring review of the *memory itself* that both prunes re-derivable content and looks for gaps. Contrast: a store only ever added to. |

Principles 9 and 10 are stage-3 machinery — mark them **not applicable** (not **absent**) for a seed or content-stage brain that legitimately doesn't need them yet. The signal is need, not a checkbox: a brain tracking many feature branches with no closeout ritual is a real gap; a small single-purpose brain without one is fine.

---

## 3. Verify substance, not just structure

Structure can be present while the content rots. Spot-check the two things that decay silently — delegate the read-heavy parts to Explore agents so the active context stays free for judgment:

- **SCOPE factual drift.** Pull a handful of falsifiable claims from the scope doc (class/tool/config names, counts, and especially *absence* claims like "no control does X") and check them against the actual codebase. Absence claims break silently when features are added — prioritize them. Report claims that no longer hold.
- **Re-derivable content.** Skim the canonical docs for passages that merely restate what the current code plainly shows. These are pruning candidates (principle 1) — the brain would be *more* trustworthy smaller.

Also run the structural checks below; they're mechanical and catch the cheap, common failures.

### Structural checks

1. **Read index ↔ disk** — every file in the read index exists; no top-level knowledge file is missing from the index (orphans).
2. **Version headers** — every canonical doc (except the exempt `*_LOG.md` / `*_TASKS.md`) opens with a well-formed `> V<N>, YYYY-MM-DD.` and no smuggled change-note.
3. **Cross-references** — every mini-brain filename mentioned resolves to a current top-level file, not an `archive/` copy or a deleted file.
4. **Namespace prefix** — every top-level knowledge file carries the namespace token (`ls *.md | grep -vE '^(CLAUDE|README)\.md$' | grep -v <PREFIX>` should return nothing).
5. **Log discipline** — the session log is append-only and readable from its last separator (not required to be read whole); entries carry a date and session identifier.

---

## 4. Report

Produce a written assessment (do not modify the target). Structure it:

- **Summary** — the brain's stage, its namespace, and a one-line overall read (what kind of shape it's in).
- **What's working** — the principles it embodies well. Lead here.
- **Principle scorecard** — the table from §2 with each verdict and note.
- **Structural findings** — anything the §3 checks flagged, most-actionable first.
- **Substance findings** — drifted SCOPE claims and pruning candidates, if any.
- **Recommended next steps** — ranked, concrete opportunities. Frame each as "this brain does X well but Y would help because …", tied to a principle. If a step is "adopt lifecycle machinery," point at `MBT_CREATE_BRAIN.md` §5 and the relevant `templates/` file.

Keep it proportionate: a healthy brain gets a short report that says so. Reserve length for real, actionable gaps.
