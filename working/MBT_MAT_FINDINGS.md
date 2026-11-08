# Minimum Acceptance Testing: Decision Record

## Problem

The toolkit's procedures are verified more and more by headless runs and dry runs on disposable copies, and the need grows with each harness the toolkit supports and each environment difference found, such as zsh against bash. These tests are ad hoc. The 0.72 release ran them by hand, and each work item writes its own fixtures, prompts and grading scripts, which go to `archive/` at closeout. Nothing records which tests to run before a release, so a fixed defect can come back unnoticed, and a release is tested only on the machine, harnesses and example brains its author happens to have.

## Preferred approach: one probing acceptance procedure, plus a list of examples

- **A standing procedure, `MBT_TESTING.md`.** It covers everything the toolkit does, and gives recent fixes and known weak points their own tests. It grows by one test for each defect fixed.
- **Probe before running.** The procedure checks which harnesses are installed (Claude Code, Codex, OpenCode 2) and which example brains are reachable, runs the tests those allow, and reports each skip with its reason. One procedure then serves every machine.
- **A list of examples, `MBT_EXAMPLES.md`.** It stands alone and records provenance only: where a brain is published or who holds it, its author, the release it was seeded from, and its shape. Seeded with mini-nebula-brain, mini-guardrails-brain, virtual-view-brain and mini-subtitle-wizard-brain.

## Alternatives considered

- **Keep testing ad hoc, per work item and release.** Rejected by Rob on 2026-11-07: coverage depends on who runs the release and what their machine has, and each item's tests leave with its working docs.
- **Fold the list of examples into the testing procedure.** Rejected: the list changes as brains are found, and on its own it can be read without the procedure.

## What this doesn't solve

- **Testing on machines nobody has.** A harness or shell that no maintainer's machine has is reported as skipped, not tested.
