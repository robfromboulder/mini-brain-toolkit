# Template Drift: Decision Record

## Problem

`create` seeds a brain by copying the toolkit's templates and substituting their placeholders. The copies fall into two kinds. Knowledge files (SCOPE, APPROACH, FINDINGS, the logs, the enforced-terms entries) fill with the project's own content, and differing from the template is their purpose. Procedure files are the template's text with the placeholders filled in, and are meant to stay that way: the session closeout, work setup, work closeout and dream cycle procedures, the conventions in the brain's `CLAUDE.md`, the hook merged into each project repo's `CLAUDE.md`, and the prompts in the brain's `README.md`.

When the toolkit fixes a procedure template, every existing brain keeps the old text, and `check` never compares a brain's procedure files with the current templates. Each release so far has carried the gap in its release notes, as upgrade steps to follow by hand. 0.71's worktree fix to the hook and its per-part routing in session closeout reached a brain only if its owner copied them in. 0.72's error-recovery and Phase 4 fixes to the dream cycle do the same. Release notes are the wrong home for that: users don't walk releases version by version, and the steps for one release say nothing about a brain several releases behind.

## Preferred approach: `check` compares procedure files with the current templates

Upgrading a brain is always the same act: run `check` and follow its recommendations. `check` reads each procedure file the brain holds and compares it with the matching template from the toolkit it runs from, after substituting the brain's own placeholder values. Each difference is reported as a recommendation carrying the template's current text, and the walk-through applies it only where the owner approves, as every other recommendation is applied. Knowledge files are never compared with a template.

Three constraints the comparison has to respect:

- **A difference is not always drift.** A brain may adapt a procedure on purpose, and text alone can't tell an adaptation from a missed fix. Every difference goes to the owner, never overwritten, and an adaptation the owner keeps stays out of later reports only if the brain records it somewhere `check` can read.
- **Filled-in parts survive.** Substituted placeholders, a lobe paragraph in the hook, a work-item block uncommented as the brain matured, and the brain's own read index and exemption table are the brain's, not drift. The comparison works section by section, so an update to one section never replaces the brain's content in another.
- **A missing procedure file is a maturity question, not drift.** `check` already recommends adopting machinery when the work justifies it, and a brain that never adopted a procedure has no copy to compare.

## Alternatives considered

- **Upgrade steps in release notes.** The practice so far, dropped from the 0.70–0.72 releases on Rob's call: it makes release notes load-bearing, and it reaches only owners who read every release in order.
- **A plain diff against the template.** Rejected: placeholders, maturity comments and legitimate adaptations make every brain differ, so a diff reports noise and can't say which differences matter.
- **A toolkit-version stamp in each copy.** It would show that a copy is stale but not what changed, and the copy would still need the comparison to say what to update. It may still be worth having as a cheap first signal, which the plan leaves open.
- **Updating procedure files automatically.** Rejected: the toolkit's SCOPE puts migrating a knowledge store automatically out of scope, because the owner directs each change. Procedure files are part of the store's conventions, so the same holds.

## What this doesn't solve

- **Knowledge files written to an older standard.** A SCOPE seeded under a rule a later release changed is already `check`'s substance work, and stays there.
- **A brain that grew on its own.** Its procedure files were never copied from a template, so there is nothing to compare, and `check`'s principle scoring covers it as before.
