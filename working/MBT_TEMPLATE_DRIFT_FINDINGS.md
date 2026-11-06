# Template Drift: Decision Record

## Problem

`create` seeds a brain by copying the toolkit's templates and substituting their placeholders. The copies fall into two kinds. Knowledge files (SCOPE, APPROACH, FINDINGS, the logs, the enforced-terms entries) fill with the project's own content, and differing from the template is their purpose. Procedure files are the template's text with the placeholders filled in, and are meant to stay that way: the session closeout, work setup, work closeout and dream cycle procedures, the template's text in the brain's `CLAUDE.md`, the hook merged into each project repo's `AGENTS.md`, and the prompts in the brain's `README.md`.

When the toolkit fixes a procedure template, every existing brain keeps the old text, and `check` never compares a brain's procedure files with the current templates. Release notes describe each fix without saying how to apply it, so a fix reaches a brain only if its owner copies it in by hand. 0.71's worktree fix to the hook and its per-part routing in session closeout reached brains that way, and 0.72's error-recovery and Phase 4 fixes to the dream cycle do the same. Upgrade steps in the notes would not close the gap: users don't walk releases version by version, and the steps for one release say nothing about a brain several releases behind.

## Preferred approach: `check` merges each template's change into the brain's copy, three ways

Rob accepted this design on 2026-11-05, in place of the two-way comparison the item opened with.

Upgrading a brain is always the same act: run `check` and follow its recommendations. For each procedure file the brain holds, `check` takes three texts: the template at the toolkit version the copy was last brought up to (its base), the template now, and the brain's copy. The base-to-now difference is what the toolkit changed; the base-to-copy difference is what the brain changed. A paragraph only the toolkit changed is a recommendation carrying the template's text. A paragraph both changed is a conflict, put to the owner with both texts. A paragraph only the brain changed is its adaptation, and is not reported. The walk-through applies a recommendation only where the owner approves, as every other recommendation is applied. Knowledge files are never compared with a template.

The base comes from a stamp each procedure file carries, naming the toolkit version its text was last brought up to. Once the owner has decided every recommendation in a file, approved or declined, the stamp advances to the current version. A declined change then sits on the brain's side of the next comparison, as an adaptation, and is not asked again unless the template changes that paragraph again. A file with no stamp takes the tagged release whose template differs least from it, confirmed with the owner. The base templates come from the install's git history, which both install paths keep, since each is a full clone.

Before comparing, all three texts are normalized: the brain's lobespace folds back to `<LOBESPACE>`, `<HUB>` reads as `<LOBESPACE>`, the display and lowercase names fill in, and version lines drop. This needs only the brain's lobespace and names, which `check` identifies while orienting. It does not need `create`'s substitution rules, so those rules gain no second copy.

Three constraints the comparison has to respect:

- **A difference is not always drift.** A brain may adapt a procedure on purpose. The three-way comparison separates an adaptation from a missed fix wherever the two touch different paragraphs, and puts every paragraph where they meet to the owner.
- **Filled-in parts survive.** Substituted placeholders, a lobe paragraph in the hook, a work-item block uncommented as the brain matured, and the brain's own read index and exemption table are the brain's changes, so the merge keeps them.
- **A missing procedure file is a maturity question, not drift.** `check` already recommends adopting machinery when the work justifies it, and a brain that never adopted a procedure has no copy to compare.

## Evidence

On 2026-11-05 the comparison was run by script (`MBT_TEMPLATE_DRIFT_EXPERIMENT.py` in this directory) against three brains, using `git merge-file` for the merge:

- **lamarr-brain and mini-subtitle-wizard-brain**, both seeded on 2026-10-21 from the 0.71 templates. The 0.71-to-`main` changes merged into every file except one with no conflicts, and every local change survived: lamarr's clone name `lamarr-brain`, its rewritten maturity comments and read-index purposes, and subwiz's fixed `~/mini-brains/` path and its Codeberg pull-request rule. The one conflict is subwiz's work-setup step 3, which both the brain and PR #20 rewrote.
- **Normalization is required.** Real brains fill placeholders inconsistently: lamarr's session and work closeouts keep `<LOBESPACE>` where it names the owning lobe at runtime, and subwiz's fill it in. Without normalization, lamarr's work closeout raised two false conflicts and twelve false local differences; with it, none.
- **Work setup inlines its scaffolds in more than one shape**: `` ### `<LOBESPACE>_<WORK>_PLAN.md` `` with a `~~~~` or ```` ```` ```` fence, or `### PLAN template`. Once split out by content, both 0.71 brains' scaffolds matched `templates/work/` exactly, apart from subwiz's burndown rule.
- **virtual-view-brain**, which predates 0.70 and is the exemplar the multi-lobe templates were distilled from. Its session closeout matches the 0.70 template exactly, and its other procedure files are heavily adapted: work setup adds a work-item header and a blocked-by field. The merge kept every adaptation and raised four conflicts in work setup, one in work closeout, three in `CLAUDE.md` and one in the README. A reorganized copy therefore needs no separate recognition: it shows up as conflicts for the owner.
- **Inferring the base works.** Scored against each tagged release, lamarr fit 0.71 best (16 differing lines, against 34 for 0.70 and 20 for 0.72), which matches its seed date. For files seeded before the first tag, several commits fit equally well; any of them gives the same merge.
- **The hook needs no drift update after 0.71.** Its text is unchanged from 0.71 to `main` apart from the merge comment, so the 0.73 hook change is only check 8's move. lamarr's hook is split across two sections of its project `CLAUDE.md` and one rule sits in another list, so the hook's paragraphs have to be matched by content wherever they sit, not as one section.

## Alternatives considered

- **Upgrade steps in release notes.** Left out of the 0.70–0.72 releases on Rob's call: it makes release notes load-bearing, and it reaches only owners who read every release in order.
- **A plain diff against the template.** Rejected: placeholders, maturity comments and legitimate adaptations make every brain differ, so a diff reports noise and can't say which differences matter.
- **A two-way comparison against the current template.** Rejected on the evidence: even normalized, it reports every adaptation as drift on every run, such as lamarr's clone name, and it has no way to stop reporting one the owner kept.
- **Updating procedure files automatically.** Rejected: the toolkit's SCOPE puts migrating a knowledge store automatically out of scope, because the owner directs each change. Procedure files are part of the store's conventions, so the same holds.

## What this doesn't solve

- **Knowledge files written to an older standard.** A SCOPE seeded under a rule a later release changed is already `check`'s substance work, and stays there.
- **A brain that grew on its own.** Its procedure files were never copied from a template, so there is nothing to compare, and `check`'s principle scoring covers it as before.
- **An install without git history.** The comparison falls back to two ways, and every difference goes to the owner.
