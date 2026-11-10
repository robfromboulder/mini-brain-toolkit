# Minimum Acceptance Testing: Burndown

Everything between the merged battery and this item's closeout.

## Before closeout

* run the battery against 0.73 once #24 merges and the release is tagged, at a budget that covers what neither run reached: scenarios 3–5, 11–13 and 15, 6 on the final code and from 0.70, and 7d–e
* fold that run's findings into the recipe, including the nine smaller gaps the dry run listed

## Closeout

* closeout notes — the battery shipped before its first release run, and #25 also carried four procedure fixes, by Rob's call, rather than leaving them to their own changes
* fold `MBT_MAT_TESTING.md` into `MBT_TESTING.md`, as scenarios worth repeating each release
* retire `MBT_MAT_CLAUDE.md` to `archive/` unfolded, since this brain has no canonical runbook
* overlaps: MIGRATIONS, REHOMING, WORK_PLACEMENT and MULTI_LOBE_DREAM each add scenarios when they land, and MULTI_LOBE_DREAM replaces check 10's multi-lobe dream-cycle skip, which scenario 10 tests
