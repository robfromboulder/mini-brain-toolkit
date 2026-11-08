# Minimum Acceptance Testing: Implementation Plan

## Objective

Give the toolkit a standard battery of acceptance scenarios to run before a release, written as a recipe an agent follows on whatever machine it runs on. The agent detects the harnesses, shells and example brains it has, runs the scenarios that fit them and the runner's token budget, and grades each one on disk. It then prints a short local report. Failures come first and say why, notes on procedure gaps get one line each, and passes are counted. The battery needs no full matrix, and no run's results are recorded. A release is ready when the rounds run on the machines available report no major problem. Deliver `MBT_TESTING.md`, the recipe and its scenarios, and `MBT_EXAMPLES.md`, the list of known example brains with provenance only. No private detail about any example's project enters either document.

## Context

See `MBT_MAT_FINDINGS.md` in this directory for the decision record and alternatives considered.

Key references in the mini-brain:
- `MBT_SCOPE.md` — problem space this fits into
- `MBT_FINDINGS.md` — relevant prior decisions, including the install line and the harness facts it rests on
- `MBT_APPROACH.md` — design constraints

## What changes

- `MBT_TESTING.md` — new canonical recipe, in five parts:
  - **Probe.** Find the toolkit commit and the newest release tag, every supported harness on `PATH` with its version (OpenCode 1 doesn't count) and a one-prompt headless sign-in check, the shells present, and each example in `MBT_EXAMPLES.md` the runner can reach. Ask the runner for a token budget and for paths to any brains the probe can't find.
  - **Select.** Each scenario declares its needs, which are a harness (any one, each available, or a named one), a brain (a fixture, a multi-lobe fixture, or a real brain), and a cost (script, dry run, or headless). A scenario that needs any one harness runs once, rotating across the harnesses found, not once in each. Within the budget, picks go in order: every script scenario, the upgrade from the last release, the scenarios touching files changed since the last tag (`git diff <tag>..HEAD`), then the rest, and the judgment scenario last.
  - **Run.** Run every agent scenario with `HOME` set to a scratch directory. Install the commit under test there, at each harness's skills path, and give it the git identity fixtures commit with. The runner's own install and settings stay untouched. A harness whose model login lives under `HOME` needs its login file copied in, or an API key in its environment variable. The probe's sign-in check runs under the scratch `HOME`, and a harness that can't reach its model there is skipped with that reason. Work on scratch copies only, never on an example in place. Keep every answers file, script and fixture source out of the tested agent's working directory. Write helper loops in bash. Run headless jobs in batches of two or three.
  - **Grade.** Grade the result on disk, not the agent's summary. A report-only run leaves every repository's `git status` unchanged. After every agent scenario, the install's file checksums match those taken before it. Drift scenarios are also graded by `tests/MBT_DRIFT_COMPARE.py`, and the agent's labels must match the script's file by file. A mismatch is a failure, because either one may be wrong. For every agent scenario, also read the transcript for places where the tested agent improvised, asked something the procedure doesn't ask, or contradicted itself. Each is a note, not a failure, because the gaps they point to are in the procedure. Most of the 0.72 preflight's fixes came from notes like these.
  - **Report.** Print the report and save it outside the repo. Its header gives the commit, harnesses, shells and brains. Then comes one block per failure, saying what was expected, what happened, and where the scratch copy is. Then one line per note, grouped where several agents hit the same gap. Then a count of passes, then one line of skips with their reasons, then the manual scenarios left to the runner. Nothing is committed.
  - **Major problems.** A major problem blocks the release. Three failures are major: the upgrade from the last release, any write to the install, and a report-only run that changes a repository. The report marks them as major, and any other failure is the releaser's call.
- `tests/MBT_DRIFT_COMPARE.py` — TEMPLATE_DRIFT's `MBT_TEMPLATE_DRIFT_COMPARE.py`, moved out of `working/` so it ships with every clone. It labels paragraphs the way check 10 does, and needs only Python 3 and git. A change to check 10's labels or exclusions updates the script in the same change. `tests/` is a new top-level directory that holds what the battery runs. No procedure writes to it or cites it, so a tested agent has no reason to open it, although it sits inside the install.
- `MBT_DREAM_CYCLE.md` — `tests/` joins the product list. The cross-reference check accepts `tests/` paths, since it otherwise requires every mini-brain filename a doc names to be a top-level file, and `MBT_TESTING.md` names the script.
- **Seed scenarios**, every one but the judgment scenario runnable on fixtures seeded from the toolkit's own release tags, so a contributor with no example brains can still run them. Real brains add coverage where they are reachable.
  - **Install.**
    1. *Install line*, by script under the scratch `HOME`, for each of the README's install lines and each shell. A fresh install and a rerun exit 0 on the newest tag. A bad URL exits non-zero and leaves no install. An unreachable remote exits non-zero and leaves the install as it was.
    2. *Invocation*, in each harness. With no argument the skill asks whether to run create or check, and text after the invocation reaches it. Selecting the skill from OpenCode 2's `@` menu is manual, since a typed `@` attaches nothing.
  - **Create.**
    3. *Blind create*, in any harness, on an invented project with an answers file written beforehand. It asks about each premise on its own, keeps design choices out of SCOPE, and writes the hook to the project's `AGENTS.md`. The project's existing `CLAUDE.md` gains `@AGENTS.md` and keeps its own content. `archive/` and `working/` each get a staged `.gitkeep`. The log names the running harness's session ID.
    4. *Create and check agree*. A fresh check of the brain from scenario 3 gives no verdict opposite to create's.
    5. *Loading*, in each harness. The created brain loads on its trigger phrase from the project repo and from inside the brain repo.
  - **Check.**
    6. *Upgrade from the last release*, headless, and the scenario that matters most each release. A fixture seeded at the last tag, with every procedure file, inlined scaffolds, a dream cycle and a sibling project repo, reports only behind, missing and dropped paragraphs. An approve-all walk-through leaves every procedure file current, the hook in the project's `AGENTS.md`, the project's own instructions in place, and the scaffolds intact. A second check reports no drift and changes nothing. An older tag, such as 0.70, runs too when the budget allows.
    7. *Drift edge cases*, by script, or headless when the budget allows. A multi-lobe `CLAUDE.md` from 0.71 shows the paragraph added in 0.72 as missing. A half-applied dream-cycle update shows exactly the untaken half. Declined changes come back on the next check. Files copied between releases, at `8ad8deb`, show no own edits.
    8. *Real brains, report-only*, one per reachable example, by script, or headless when the budget allows. Every difference is a proposal, and known own edits, such as subwiz's clone path and lamarr's clone name, are reported as own edits. A headless run changes nothing.
    9. *Loading reach*. A brain whose hook sits only in a project's `CLAUDE.md` is flagged, and fixed when the runner approves.
    10. *Skips*. The toolkit as its own target skips check 10, a multi-lobe dream cycle is skipped with the template's full history listed, and a brain that isn't a git repository is reported as unchecked for check 9. That last case has never been run.
    11. *Install guard*. A toolkit copy with a planted defect, beside a writable install, with every fix approved: only the copy changes.
  - **Dream cycle.**
    12. *Template dream cycle*, headless on a scratch brain beside its code. It runs every phase unattended and asks nothing. It flags unverifiable claims and carries on, and edits no premise. Its release check raises an item when the remote has a newer tag and skips an off-release install.
    13. *Toolkit dream cycle*, as a dry run. No instruction conflicts in a way that would stop a run or send it the wrong way.
  - **Work items and sessions.**
    14. *Work setup* on single-lobe and multi-lobe fixtures. It creates the scaffolds, audits `working/` only and records overlaps with other open items, and its `find` commands give the same output in each shell.
    15. *Work closeout* of a scratch item. Its docs fold into the canonical docs, its log merges in date order, and a move onto an existing archive name stops and asks for a new slug.
    16. *Session closeout*, in each harness. It appends an entry in the entry format, with the running harness's session ID.
  - **Judgment.**
    17. *Blind check against an owner's revision*, headless, and optional. It needs a reachable real brain that has a known owner revision, such as a merged PR that reworked SCOPE or APPROACH. Check the brain as it stood just before the revision, with an answers file drawn from the revision's description. Score how much of the revision the check reproduces, and list where it placed content differently or removed something the owner kept. No fixed score passes. The report gives the score and the differences, for the releaser to judge. The 0.72 preflight's check of virtual-view-brain against its owner's PR is the model case.
- `MBT_EXAMPLES.md` — new canonical list of example brains, seeded with mini-nebula-brain, mini-guardrails-brain, virtual-view-brain, mini-subtitle-wizard-brain, lamarr-brain and mini-alien-brain (`starburstdata/mini-alien-brain`). Each entry gives the brain's name, where it is published or who holds it, its author, the release it was seeded from and its shape, and nothing about the project the brain describes. A private brain gives its holder in place of a link.
- `CLAUDE.md` — read-index and declared-exemptions rows for both documents, the `tests/` directory beside `templates/` and `archive/`, and maintenance-doc boundaries saying what each may reference. The work-item binding's no-testing-doc bullet and its `_TESTING` text replacement go. An item's `_TESTING` doc then folds into `MBT_TESTING.md` at closeout, adding as scenarios the cases worth repeating at each release.

## Interaction with existing docs

| Existing doc | Interaction | Risk |
|---|---|---|
| `MBT_CHECK_BRAIN.md`, `MBT_CREATE_BRAIN.md`, `MBT_DREAM_CYCLE.md`, `templates/` | The procedures under test | A scenario that quotes a procedure's wording breaks on every editorial change, so a scenario states observable outcomes only |
| `MBT_FINDINGS.md` | Records past defects that scenarios hold fixed | Each defect gets a scenario in one place and its explanation in another, and the two drift |
| Work items' PLANs | Each carries its own testing approach | Tests written for one item are lost at closeout instead of joining the battery |
| `CLAUDE.md`'s work-item binding | Says the toolkit has no canonical testing doc | Left unchanged, closeouts keep retiring tests that belong in the battery |
| `MBT_DREAM_CYCLE.md` | Its product list and cross-reference check | Without the change, the next cycle flags `MBT_TESTING.md`'s reference to the script |
| `MBT_CHECK_BRAIN.md` check 10 | `tests/MBT_DRIFT_COMPARE.py` reimplements its comparison | A check-10 change made without the script makes every drift scenario fail on the mismatch |

## Testing approach

The recipe is validated by running it:

- On this machine, with Claude Code only and every example brain, under a modest budget. The report names Codex and OpenCode 2 as skipped, and the run still finishes inside the budget.
- On a second machine with other harnesses and bash as the default shell, and few or no example brains. There the scenarios run on fixtures, and the judgment scenario is skipped.
- Against past defects reintroduced on a scratch install. The recipe must report each one as a failure that names the cause. Candidates are the install line checking out after a failed fetch, check 10 reporting create's staged comments as missing, check 10 applying an own edit's template text without approval, and the template dream cycle exempting a seeded brain's real `working/` filenames from its leakage check.
- By reading the reports. An all-pass report fits on one screen, and a failure can't be missed.

Manual checks live in `MBT_MAT_TESTING.md`.

## Implementation sequence

1. Write `MBT_EXAMPLES.md` from the seed list, with its read-index and declared-exemptions rows. Done on 2026-11-08.
2. Move the comparison script to `tests/MBT_DRIFT_COMPARE.py` with `git mv`, and check it against check 10's current exclusions.
3. Write `MBT_TESTING.md`: the five parts, then the seed scenarios.
4. Build the fixture recipe: seeding a brain from the templates at a given tag, with a sibling project repo.
5. Run it on this machine, then against the reintroduced defects.
6. Run it on a second machine.
7. Update `CLAUDE.md` (read-index rows, `tests/`, boundaries, and the binding) and `MBT_DREAM_CYCLE.md`.

## Scope boundary — what this does NOT include

- Any private detail of an example brain's project. `MBT_EXAMPLES.md` carries provenance only.
- Changing the procedures under test. A defect the battery finds is fixed as its own change, which adds a scenario here.
- A full matrix or a definition of done. Coverage is whatever the machines available allow, and the report says what was skipped.
- Recording or auditing results across runs or releases.
- Continuous integration, and a golden machine with every harness and example. Either may come later.

## Open issues

1. How the install-line scenario runs before the release tag exists. The pinned line checks out the newest tag, which is the previous release until tagging, so the scenario points the line at a local clone with a scratch tag. For 0.73 there's a further wrinkle. The pinned lines and the template dream cycle's release check exist only on PR #24's branch, which merges after the tag. Until then, scenario 1 and scenario 12's release check test that branch.
2. Where each harness keeps its model login, and whether a scratch `HOME` reaches it. Credentials stored in the macOS keychain may work unchanged, while files under `HOME` need copying. Verify this per harness when the recipe is first run, and record the results with the harness facts in `MBT_FINDINGS.md`.
3. Overlaps with open work items. MIGRATIONS (an extract-and-absorb round trip), REHOMING (a simulated supersession), WORK_PLACEMENT (intake cases against the six-lobe prototype) and MULTI_LOBE_DREAM (a cycle against the prototype and a single-lobe exemplar) each plan tests that join the battery as scenarios when they land. MULTI_LOBE_DREAM also replaces check 10's multi-lobe dream-cycle skip, which scenario 10 tests.
