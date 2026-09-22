# Enforced Terms: Working Log

---

# Implement enforced terms mechanism (2026-09-22)

**Session ID**: `9ca58e07-510b-4f01-b2ad-c3011d671966`

Rob and Claude implemented the enforced terms mechanism from the settled plan and decision record, landing as PR #7 on the `enforced-terms` branch. The session was straight execution — the plan was fully settled, so no design decisions were made; every change followed the plan's implementation sequence.

## What landed

Created the template (`templates/ENFORCED_TERMS.md`) and this brain's own enforced terms file (`MBT_ENFORCED_TERMS.md`) with two entries: "finding" and "work item." Wired four enforcement hooks: two-mode one-term-one-meaning check in `MBT_CHECK_BRAIN.md`, per-entry re-grep (Phase 1 check 7) and candidate harvesting (Phase 4) in both dream cycle files, and the coined-or-repurposed-term callout in the closeout template and work FINDINGS template. Added read-index rows and the write-time rule to all three entrypoint files (`CLAUDE.md`, `templates/CLAUDE.md`, `templates/LOBES_CLAUDE.md`), a declared-exemption row in `CLAUDE.md`, a stage-3 file-set row in `MBT_PATTERN.md`, and the enforced terms file to `MBT_CREATE_BRAIN.md`'s stage-3 growth step. Fixed seven generic uses of "finding" across four files and renamed the check procedure's report headings from "Structural/Substance findings" to "Structural/Substance issues."

## Decisions

Rob confirmed (post-commit) that "lobe" and "lobespace" from PR #5 should not be enforced terms — both fail the empty-disambiguation rule since they were specifically chosen to avoid the collisions the old terms had.

The plan's implementation sequence step 5 said "three entries" but the plan body specified two ("finding" and "work item"). Treated the step-5 count as a stale draft artifact and went with two.

## What didn't work

Nothing — clean execution against a settled plan.
