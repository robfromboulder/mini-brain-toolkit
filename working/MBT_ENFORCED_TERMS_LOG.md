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

---

# Align enforced-term hooks with the first adopting brain after PR #7 review (2026-09-22)

**Session ID**: `b8c5688f-8d1f-4731-ba54-62fa02f39b85`

Rob and Claude ran a medium-effort code review of PR #7, compared the branch's enforcement hooks against the first product brain to use enforced terms, and cut the hooks back to what that brain actually runs. Everything landed on the `enforced-terms` branch.

## Review

The review found seven issues. Three came from hooks the adopting brain doesn't have. First, the coined-term callout in the closeout and work FINDINGS templates was recorded but nothing ever acted on it, and the templates disagreed about where it went. Second, the dream cycle's term check sat in the mechanical Phase 1 but needed judgment, said to fix things "in Phase 2", and grepped the append-only logs, whose hits can never be fixed. Third, the check procedure only recommended declaring a term once a collision "recurs across checks", which conflicted with the Harvest rule. The other two issues didn't depend on that brain: the dream cycle still used "findings" in its generic sense in several places, and the Work item entry used "issue" in the tracker sense while the Finding entry reserves it as the generic word.

## Comparison with the adopting brain

Rob recalled that the adopting brain has no instruction for coining terms in a work item and no closeout step that acts on them, and asked for nothing beyond what it does. Reading that brain confirmed it. It enforces terms in three places: a terms rule at session closeout, a terminology conformance check in work closeout's structural checks, and a dedicated dream-cycle phase. That phase checks the terms file against its own rules, reads the canonical knowledge docs for drift, and proposes unlisted terms for the user to confirm. It never scans the log.

## What changed

- Reverted the coined-term callout in `templates/WORK_CLOSEOUT.md` and `templates/work/FINDINGS.md`. Added the adopting brain's terminology check to the closeout's structural checks in its place.
- In both dream cycle files, removed the Phase 1 term check and the Phase 4 candidates paragraph, and added an "Enforced terms" phase before the report, modeled on the adopting brain's. The report moves to Phase 6. In the toolkit's own cycle, the drift pass reads every top-level doc, since its product docs and procedures are its knowledge. The template reads only SCOPE, APPROACH and FINDINGS, as the adopting brain does.
- Changed the check procedure's term bullet to grep listed terms outside the logs and to report every unlisted collision as a candidate for the user.
- Fixed the remaining generic uses of "findings" in `MBT_DREAM_CYCLE.md`, and reworded the Work item entry to "not a tracker ticket or a task".
- Updated the decision record's enforcement points and added the two rejected designs as alternatives.

The adopting brain's session-closeout terms rule was not copied. The entrypoint's write-time rule already covers log entries.

---

# Keep other brains unnamed in mini-brain docs (2026-09-22)

**Session ID**: `b8c5688f-8d1f-4731-ba54-62fa02f39b85`

Rob and Claude finished the review follow-up from the previous entry: they removed another brain's name from this item's docs, then committed and pushed the enforced-term changes to PR #7.

## Decisions

Rob directed that mini-brain docs never name the product brain the hooks were compared against. The previous entry had named it before it was committed, so Claude rewrote it to say "the first product brain to use enforced terms" before the commit. The decision record already used that phrasing. An older `MBT_LOG.md` entry that names the same brain was left alone because the log is append-only. Mentions in `archive/` were left alone as well.

## Landed

The review follow-up was committed as one change and pushed to the `enforced-terms` branch, updating PR #7.
