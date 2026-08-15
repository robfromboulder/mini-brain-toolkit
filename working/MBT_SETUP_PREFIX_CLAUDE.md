# Enforce the Work-Item Token Prefix: Claude Runbook

Instructions for branch: `setup-prefix-enforce`

## Running Tests

This work item changes procedure prose in `templates/WORK_SETUP.md`; there is no automated suite. Verification is behavioral — see the manual plan in `MBT_SETUP_PREFIX_TESTING.md`.

### Step N — dry-run the setup transform ← NEW in this branch

Run the revised `WORK_SETUP` against the sample names in the manual test plan and confirm every resulting filename is `<TOKEN>_<WORK>_*` with no double prefix.

**Expected:** every sample case in that plan yields correctly single-prefixed filenames.
