# Template Drift: Burndown

Everything between working code and this item's last merged PR, #24 (branch `install-pin`), which pins the install lines to the newest release and has the template dream cycle prompt a `check` when a newer one is published. The testing approach in `archive/MBT_TEMPLATE_DRIFT_PLAN.md` carries each test's expectations.

## PR #24

* rebase it onto `main` (`git rebase --onto main template-drift install-pin`), set its base to `main`, and delete the `template-drift` branch; #22 was squash-merged, so that branch's commits aren't on `main`
* retest the rebased branch with `MBT_TESTING.md`: scenario 1 for the pinned install lines, and scenario 12 for the dream cycle's release check
* merge it as the last commit before the 0.73 release, and tag 0.73 on it straight away, since until a tag exists at or after #22's merge the install line checks out `0.72`, which predates #19, #20 and #22

## Closeout

* closeout notes — the work shipped as two PRs, and the PLAN retired early, after the review round on `8090a94`
* follow-on: offer to file a toolkit issue for an own edit the owner keeps because the template broke for them — Rob's follow-up for a later release
* overlaps: WORK_PLACEMENT and REHOMING both change `templates/WORK_SETUP.md`, and MULTI_LOBE_DREAM redesigns `templates/DREAM_CYCLE.md` and replaces check 10's multi-lobe skip; whichever lands after this item changes what its tests expect
