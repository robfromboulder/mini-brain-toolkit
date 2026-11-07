# Minimum Acceptance Testing: Implementation Plan

## Objective

Give the toolkit a repeatable minimum acceptance-test procedure that exercises everything it does, `create`, `check`, the dream cycle, work setup and closeout, and session closeout, headless or as dry runs on disposable copies, in every harness installed on the machine and against every example brain within reach. Deliver `MBT_TESTING.md`, the procedure, organized so each fixed defect and known weak point adds a test, and `MBT_EXAMPLES.md`, the list of known example brains with provenance only. No private detail about any example's project enters either document.

## Context

See `MBT_MAT_FINDINGS.md` in this directory for the decision record and alternatives considered.

Key references in the mini-brain:
- `MBT_SCOPE.md` — problem space this fits into
- `MBT_FINDINGS.md` — relevant prior decisions, including the install line and the harnesses it covers
- `MBT_APPROACH.md` — design constraints

## What changes

Stub until research begins. Expected surface:

- `MBT_TESTING.md` — new canonical procedure: probe the machine, select the tests that can run, run them, grade each on disk, and report what ran, what passed, and what was skipped and why.
- `MBT_EXAMPLES.md` — new canonical list of example brains, seeded with mini-nebula-brain, mini-guardrails-brain, virtual-view-brain and mini-subtitle-wizard-brain: each entry's name, where it is published or who holds it, its author, the release it was seeded from, and its shape. Nothing about the project the brain describes.
- `CLAUDE.md` — read-index rows for both documents, and the maintenance-doc boundaries that say what each may reference.

Seed tests for `MBT_TESTING.md`, from the TEMPLATE_DRIFT work item (its PLAN's testing approach carries the full expectations):

1. **0.72 upgrade.** A brain seeded from the 0.72 templates, with every procedure file, work setup's scaffolds inlined, a dream cycle, and a sibling project repo whose `CLAUDE.md` holds the hook beside its own instructions. `check` reports only behind and missing paragraphs. A walk-through approving everything leaves every procedure file current, the hook in the project's `AGENTS.md` and the scaffolds intact. A second `check` reports no drift.
2. **0.70 upgrade.** The same, seeded at 0.70.
3. **Added paragraph.** A multi-lobe `CLAUDE.md` seeded from 0.71 shows 0.72's added paragraph as missing.
4. **Partly applied update.** A dream cycle with half of a release's changes applied by hand shows exactly the untaken half.
5. **Declines and tracked directories.** A walk-through that approves check 9's fix and declines an added paragraph and a rewrite. A second `check` passes check 9 and reports both declined changes again.
6. **Real brains.** lamarr-brain, mini-subtitle-wizard-brain (with its project repo) and virtual-view-brain: every difference is a proposal, and each brain's known own edits, such as subwiz's fixed clone path and lamarr's clone name, are never applied unasked.
7. **Declines in a real brain.** Taking all but one of lamarr's README changes brings back only the declined one.
8. **Report-only runs change nothing.** Every repository's `git status` is identical before and after.
9. **Install line.** It exits non-zero and does not check out with an unreachable remote or a bad clone URL. It moves an install to the newest release when the remote answers, in zsh and in bash, and reruns cleanly.

## Interaction with existing docs

| Existing doc | Interaction | Risk |
|---|---|---|
| `MBT_CHECK_BRAIN.md`, `MBT_CREATE_BRAIN.md`, `MBT_DREAM_CYCLE.md`, `templates/` | The procedures under test | A test written against a procedure's wording breaks on every editorial change to it |
| `MBT_FINDINGS.md` | Records past defects that tests should hold fixed | Each defect gets a test in one place and an explanation in another, and the two drift |
| Work items' PLANs | Each carries its own ad-hoc testing approach | Tests written for one item are lost at closeout instead of joining the standing suite |
| `templates/work/TESTING.md` | Its manual cases fold into "the canonical testing doc" at closeout, which this item creates for the toolkit | A brain's testing doc and the toolkit's acceptance procedure are confused for one another |

## Testing approach

The procedure is itself the test, so it is validated by running it:

- On at least two machines with different harnesses installed and different default shells (zsh on macOS, bash on Linux). Each run reports which harnesses and examples it found, and skips the rest with a reason.
- Against known past defects reintroduced on a scratch install, each of which the suite must catch. Candidates: the install line checking out after a failed fetch, check 10 reporting `create`'s staged comments as missing, check 10 applying an own edit's template text without approval, and the dream cycle exempting a seeded brain's real `working/` filenames from its leakage check.
- With no examples reachable, where it falls back to fixtures seeded from the templates at each release tag.

Manual checks live in `MBT_MAT_TESTING.md`.

## Implementation sequence

1. Research: gather the ad-hoc tests of past releases and open work items, the harnesses and shells they ran under, and the defects each caught.
2. Settle the procedure's shape: probes, test registry, fixtures, grading, and the report.
3. Write `MBT_EXAMPLES.md` from the seed list.
4. Write `MBT_TESTING.md`, starting from the tests TEMPLATE_DRIFT ran.
5. Run it on two machines, and against the reintroduced defects.

## Scope boundary — what this does NOT include

- Any private detail of an example brain's project. `MBT_EXAMPLES.md` carries provenance only.
- Changing the procedures under test. A defect the suite finds becomes its own fix, with a test added here.
- Continuous integration. The procedure runs on a developer's machine, where the harnesses and examples are.

## Open issues

1. Where a test lives: inline in `MBT_TESTING.md`, or one file per suite once the list grows.
2. How a test is graded: an agent reading the report, a script reading the brain on disk, or both. TEMPLATE_DRIFT graded every headless run on disk with `MBT_TEMPLATE_DRIFT_COMPARE.py`, which runs check 10's comparison by script; its similarity line only approximates the agent's judgment of what counts as a version of a paragraph.
3. How to probe for harnesses and examples without assuming install paths, and how a test names the harnesses it needs.
4. How to name an example that isn't published, such as a private brain, without leaking its project.
5. How to bound the cost of a full run. Headless runs hit usage limits during TEMPLATE_DRIFT, which ran them in batches of two or three.
6. How the runner's own shell is pinned. Test loops written in zsh silently misread unquoted variables, which zsh doesn't word-split, so TEMPLATE_DRIFT moved them into bash scripts.
7. How a headless run's sign-in is kept valid. Claude Code warns days ahead when a sign-in will expire, and an unattended run would fail on it.
8. Whether a run may modify an example in place. TEMPLATE_DRIFT only ever used scratch copies.
9. Overlaps with open work items. TEMPLATE_DRIFT's tests and fixtures are the first suite, listed under What changes. MIGRATIONS (an extract-and-absorb round trip), REHOMING (a simulated supersession), WORK_PLACEMENT (intake cases against the six-lobe prototype) and MULTI_LOBE_DREAM (a cycle against the prototype and a single-lobe exemplar) each plan tests that belong in the standing suite once they land. Whichever lands first sets the shape the others follow.
