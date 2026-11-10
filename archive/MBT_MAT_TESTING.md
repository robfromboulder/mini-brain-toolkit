# Minimum Acceptance Testing: Manual Test Plan

Checks run by hand for this work item (UI, API calls, data checks). At closeout these fold into the canonical testing doc.

## Setup

A machine with at least one supported harness and the toolkit cloned, plus a first run's report.

## Test cases

1. **Probe report matches the machine** — compare the report's header with `command -v`, `--version` and the brains you know are on the machine.
   - **Expected:** every installed harness and reachable brain is listed, and every one that's missing appears among the skips with a reason.
2. **A pass is short and a failure is loud** — read an all-pass report, then a report from a run against a reintroduced defect.
   - **Expected:** the all-pass report fits on one screen. The failure leads the report and says what was expected, what happened, and where the scratch copy is.
3. **No private project detail in `MBT_EXAMPLES.md`** — read every entry.
   - **Expected:** each entry carries only a name, a location or holder, an author, a seeding release and a shape.
4. **Nothing left behind** — after a run, run `git status` in the toolkit and in every example brain, and checksum the install.
   - **Expected:** no changes and no report in any repository, and the install is unchanged.
