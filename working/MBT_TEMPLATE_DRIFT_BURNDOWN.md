# Template Drift: Burndown

Everything between working code and two merged PRs: PR #22 (branch `template-drift`), which brings brains up to date through `check`, and the install-pin PR (branch `install-pin`), which pins the install lines to the newest release and has the template dream cycle prompt a `check` when a newer one is published. The testing approach in `archive/MBT_TEMPLATE_DRIFT_PLAN.md` carries each test's expectations.

## PR #22

* push `5050c4b` (the split) and `34b65ef` (the review fixes), and update the PR description to match
* automated retest on the PR code, each run graded on disk against `MBT_TEMPLATE_DRIFT_COMPARE.py` — tests 1 and 6–8 headless, tests 3–5 and 9 by script, and test 2, which has not run since the two-way switch
* new test from the review: procedure files copied at `8ad8deb`, between releases, report every difference as behind, missing or dropped, with no own edits — passed by script on 2026-11-07
* respond to review feedback
* merge

## Install-pin PR

* open it, stacked on `template-drift`
* after #22 squash-merges, rebase it onto `main` (`git rebase --onto main template-drift install-pin`)
* merge only once a release tag exists at or after #22's merge, since until then the install line checks out `0.72`, which predates #19, #20 and #22

## Closeout

* closeout notes — the work shipped as two PRs, and the PLAN retired early, after the review round on `8090a94`
* follow-on: offer to file a toolkit issue for an own edit the owner keeps because the template broke for them — Rob's follow-up for a later release
* overlaps: WORK_PLACEMENT and REHOMING both change `templates/WORK_SETUP.md`, and MULTI_LOBE_DREAM redesigns `templates/DREAM_CYCLE.md` and replaces check 10's multi-lobe skip; whichever lands after this item changes what its tests expect
