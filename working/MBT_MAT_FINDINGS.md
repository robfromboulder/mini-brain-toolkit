# Minimum Acceptance Testing: Decision Record

## Problem

The toolkit has no standard battery of tests to run before a release. Each work item writes its own fixtures, prompts and grading scripts, which go to `archive/` at closeout, and the 0.72 preflight ran its tests by hand from a checklist kept outside the repo. A fixed defect can come back unnoticed. The toolkit is open source, and its contributors won't all have a Mac, every supported harness, the tokens for a full run, or access to every example brain.

## Preferred approach: a recipe that fits the machine, and a short local report

- **A recipe, not a script.** `MBT_TESTING.md` states each scenario's setup and its expected outcome, and leaves the steps to the agent running it. Scenarios grow by one for each fixed defect or known weak point.
- **Coverage fits the machine.** The agent detects the harnesses, shells and example brains present and runs the scenarios they allow. It reports each skip with its reason. No full matrix is required. Rob, 2026-11-08.
- **The runner sets the budget.** Scenarios declare their cost, so a run fits whatever token budget the runner states. A scenario that needs one harness runs once, not once in each harness. Rob, 2026-11-08: there are no unlimited tokens.
- **Grading also reads how the agent got there.** Scenarios check outcomes, but most of the 0.72 preflight's procedure fixes came from what its transcripts showed: agents improvising, asking questions the procedure didn't, or contradicting themselves. Each of these is reported as a note, not a failure. An optional judgment scenario scores a blind check against an owner's own revision of a real brain, which was the strongest test of check's judgment at 0.72. Rob, 2026-11-08.
- **Agent scenarios run under a scratch `HOME`.** The harnesses read skills only from fixed directories under `HOME`, so a scratch `HOME` lets the commit under test install there without overwriting the runner's own install. The PR #19 runs had copied the branch over the real install. The alternatives were restoring the real install afterwards, which fails if a run is interrupted, and the Other-harnesses prompt, which never tests the skill's real install path. Rob, 2026-11-08.
- **Every scenario but the judgment one runs on fixtures.** Fixtures are seeded from the toolkit's own release tags, so a contributor without example brains can still run the battery. Real brains add coverage where they are reachable.
- **The report is local and short.** A failure is reported loudly, with the reason. A pass gets a count and a skip gets one line. The report is saved outside the repo and never committed. Rob, 2026-11-08.
- **The release bar is judgment, with three fixed blockers.** A release is ready when the rounds run on the machines available report no major problem. Three failures are always major: the upgrade from the last release, a write to the install, and a report-only run that changes a repository. Rob, 2026-11-08.
- **The drift grader ships in the toolkit.** The scripted check-10 comparison moves to `tests/`, so every clone can grade drift scenarios the same way, and it changes whenever check 10 does. The other option was to drop it and let the agent judge drift unaided, which would leave the agent grading the agent. Rob, 2026-11-08: the battery has to run on more than one machine. Keeping the script in `archive/` was rejected for two reasons. `MBT_TESTING.md` would have to cite an archived file, which the cross-reference rule forbids. The dream cycle's leakage check would also try to inline the script into that doc. `tests/` needs a line in `CLAUDE.md`, an entry in the dream cycle's product list, and an allowance for `tests/` paths in its cross-reference check. The cycle's other mechanical checks cover only top-level `.md` files.
- **A list of examples, `MBT_EXAMPLES.md`.** It stands alone and records provenance only: where a brain is published or who holds it, its author, the release it was seeded from, and its shape.

## Alternatives considered

- **Keep testing ad hoc, per work item and release.** Rejected by Rob on 2026-11-07. Each item's tests leave with its working docs, and no battery is repeated between releases.
- **A full matrix of harnesses, shells and brains as a definition of done.** Rejected by Rob on 2026-11-08. No machine has every harness and example today, and contributors won't either.
- **Recording each release's results.** Rejected by Rob on 2026-11-08. A record nobody audits only adds work. The report on each machine is enough.
- **A golden machine with every harness and example as a precondition.** Deferred. It is worth working toward, but it doesn't exist, and the battery mustn't wait for it.
- **Fold the list of examples into the testing procedure.** Rejected: the list changes as brains are found, and on its own it can be read without the procedure.

## What this doesn't solve

- **Testing on machines nobody has.** A harness or shell that no maintainer's machine has is reported as skipped, not tested.
- **Comparison between runs.** With no stored results, a regression between two rounds is caught only by a scenario that fails, not by a changed result.
