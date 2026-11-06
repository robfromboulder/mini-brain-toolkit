# Template Drift: Session Log

Running log of implementation sessions. Each session appends after a `---` separator.

The first entry, and every one after it, follows the entry format and content rules in `MBT_SESSION_CLOSEOUT.md` — that spec is the authority, not the prior entry, since a fresh LOG file has none to copy.

---

# Plan reviewed against the current toolkit, and the drift check redesigned as a three-way merge (2026-11-05)

**Session ID**: `ee2c2ade-b187-4574-8c63-6ac120cef31c`

Rob's session, with Claude as co-author. Rob asked for a review of this item's plan and findings against the latest toolkit, since the item is the main fix planned for 0.73. The review found the plan stale against SKILL_INSTALL part 2, and Claude corrected it. Rob then asked for enough research to put every implementation part above 80 confidence. Claude ran the comparison by script against three real brains, and the evidence replaced the plan's two-way comparison with a three-way merge from a per-file base stamp. Rob accepted the design, and the plan, findings and experiment script were committed and pushed to `main` as `925e2a6`.

## Turn by turn

- **Review.** Claude read the PLAN and FINDINGS, then the current `MBT_CHECK_BRAIN.md`, `MBT_CREATE_BRAIN.md`, `SKILL.md`, the procedure templates, the archived SKILL_INSTALL plan, the other open work items, the published 0.71 and 0.72 release notes and this repo's log. Most of the plan predated PR #19:
  - Its 0.72 acceptance test passed on the hook move to `AGENTS.md` and the brain-side `AGENTS.md`, which check 8 (loading reach) already does and explicitly reserves for itself, so the test exercised no drift check.
  - The procedure files were named `<LOBESPACE>_*` rather than `<HUB>_*`.
  - The `CLAUDE.md` row's "conventions sections only" missed the retire-move paragraph from PR #20, which sits in the Read Index section.
  - Work setup's inlined `templates/work/` scaffolds were wrongly excluded.
  - The FINDINGS problem statement said every release carried upgrade steps, which contradicted its own alternatives and the published notes.
- **Codex's three wording issues were checked against the templates.** Two hold in `templates/DREAM_CYCLE.md`: Phase 5 cites an enforced-terms rule a brain without the file doesn't have, and Phase 4 routes problem-reframing discoveries to FINDINGS. The third, "LOG files are never archived", lives in both `CLAUDE.md` templates and this repo's `CLAUDE.md`, not the dream cycle. Claude also found that check 3 in `MBT_CHECK_BRAIN.md` shares the dream cycle's commented-row defect.
- Rob had the mechanical corrections applied. The enforced-terms preamble and the multi-lobe dream cycle went to open issues as his calls.
- **Research, at Rob's direction.**
  - Claude read the PR #19 comments for Codex's wording and the retest's `seed.sh`.
  - Rob supplied mini-subtitle-wizard-brain's Codeberg URL. Claude cloned it into the scratchpad and found it was seeded from the toolkit's templates, with deviations its first log entry records. The plan had cast it as a brain grown without the toolkit.
  - lamarr-brain's history showed its procedure copies were never hand-updated, contrary to the plan.
  - Both brains were seeded on 2026-10-21, and the last template commit before then is the 0.71 tip.
  - Claude scripted a three-way comparison: the template at the seed version, the template now, and the brain's copy, merged with `git merge-file`. The first run raised false conflicts from inconsistent placeholder filling. Folding the lobespace back to `<LOBESPACE>` removed them. Work setup's scaffolds turned up in three inline shapes, and once the script split them out by content, they matched `templates/work/`.
  - virtual-view-brain, the pre-0.70 exemplar, kept every adaptation and raised conflicts in four files.
  - Scoring each tagged release recovered lamarr's base as 0.71.
  - The hook's text is unchanged since 0.71 apart from its merge comment. lamarr's hook is split across sections of its project `CLAUDE.md`.
  - A reworded check 6 exemption, run through `create`'s substitution, still exempts `<WORK>` placeholders and flags real names.
- Claude rewrote the PLAN and FINDINGS around the three-way design. It kept the script as `working/MBT_TEMPLATE_DRIFT_EXPERIMENT.py`, the tests' reference output.
- Rob accepted the design and asked for a commit and push. Claude dropped the confirmation open issue and recorded the acceptance in FINDINGS. It committed to `main` as the item's earlier plan edits were, with no attribution trailer, and pushed.

## Decisions

- **The drift check is a three-way merge from a per-file base stamp**, with a declined change becoming the brain's adaptation once the stamp advances — Claude proposed it from the evidence; Rob accepted it.
- **Check 8 keeps the whole `AGENTS.md` loading path, and in a template-seeded brain its fix takes the current template's wording**, so the drift check finds those paragraphs current — Claude.
- **Placeholder normalization replaces restating `create`'s substitution rules in `check`** — Claude, from the evidence that normalizing needs only the brain's lobespace and names.
- **The enforced-terms preamble, multi-lobe dream cycles, `create`'s `archive/` `.gitkeep` and check 8's move of a split hook stay open** — Claude raised them; Rob left them open.
- **This session's commit went straight to `main`** — Claude, matching the item's earlier plan edits, on Rob's instruction to commit and push.

## What didn't work

- Comparing without normalizing placeholders. Real brains fill `<LOBESPACE>` inconsistently, and the raw comparison reported that as conflicts and local changes.
- Splitting work setup's scaffolds by one heading convention. Each brain inlined them differently, so the split has to work by content.

## Lessons

- **A plan written before a sibling item lands needs re-reading against what landed**, especially its tests. A test written for a future change can pass on code that already exists, and so test nothing.
- **Check a test brain's history before assigning it a role.** Two of the plan's three test brains had been cast wrongly from memory.
- **A merge needs a base, so a comparison that must tell adaptation from drift needs one too.** Recording the base per file is what lets a declined change stay declined.
