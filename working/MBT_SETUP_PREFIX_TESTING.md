# Enforce the Work-Item Token Prefix: Manual Test Plan

Checks run by hand for this work item. At closeout these fold into the canonical testing coverage.

## Setup

The revised `templates/WORK_SETUP.md`, and a scratch brain (or this repo) with token `MBT` to reason against.

## Test cases

1. **Bare name** — hand setup a work-item name `BLAH_BLAH`.
   - **Expected:** produced filenames are `MBT_BLAH_BLAH_*.md` — token prepended.
2. **Already-prefixed name** — hand setup `MBT_BLAH_BLAH`.
   - **Expected:** the leading `MBT_` is stripped before use; filenames are `MBT_BLAH_BLAH_*.md`, not `MBT_MBT_BLAH_BLAH_*.md`.
3. **Component-brain case** — a work item owned by a child unit with token `PRESS`.
   - **Expected:** filenames carry the owning unit's token (`PRESS_<WORK>_*`), consistent with longest-match ownership.
4. **Foreign-token name** — a work item owned by child unit `PRESS` in an `MBT`-hub brain, handed `MBT_FOO`.
   - **Expected:** the leading `MBT_` is stripped even though `PRESS` owns the item; filenames are `PRESS_FOO_*.md`, never `PRESS_MBT_FOO_*.md`.
5. **Slug fails the compound checks** — a work item owned by parent unit `ORCHARD` beside child unit `ORCHARD_PRESS`, handed `ORCHARD_PRESS_ERRORS`.
   - **Expected:** the longest-match strip removes `ORCHARD_PRESS`, giving `ORCHARD_ERRORS_*.md`; any slug whose compound still fails a check (e.g. a handed bare `PRESS_ERRORS`) is reworded until it passes, never kept verbatim.
