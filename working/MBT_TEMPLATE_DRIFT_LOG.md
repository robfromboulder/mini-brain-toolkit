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

---

# Drift check implemented and tested, stamps dropped for inference, PR #22 opened (2026-11-06)

**Session ID**: `ee2c2ade-b187-4574-8c63-6ac120cef31c`

Rob's session, with Claude as co-author, continuing the review session above. Rob had all four implementation steps run on branch `template-drift`. Along the way he set the rule for every open choice: upgrades take no manual step. He also overturned three of Claude's design choices: per-file version stamps, a pin decided without him, and HTML-comment skips. Headless tests on two fixtures and three real brains passed after two defects they exposed were fixed. The branch went up as one squashed commit in PR #22. The PLAN and FINDINGS stayed off the branch, at Rob's request, so the PR carries only the change under review.

## Turn by turn

- **Step 1.** Claude fixed the template dream cycle's leakage exemption, its Phase 4 routing (this brain's own dream cycle too) and its Phase 5 rule for proposing a term. It also narrowed the log convention to canonical logs, and added skips for HTML-commented rows to check 3, the dream cycle and work closeout. Rob set the no-manual-step rule. Under it Claude resolved three open issues: follow renamed templates, compare the enforced-terms rules, and keep `archive/` tracked.
- Rob asked that PLAN and FINDINGS changes stay out of feature-branch commits, so a PR reviews only the change, and land on `main` at session end.
- **Step 2.** Claude added a per-file stamp line naming the toolkit version and template to every procedure template, and the `.gitkeep` and check 9.
- **Step 3.** Claude asked how an owner learns a `check` is due. Rob pointed out that the install lines tracked `main`, so any toolkit-version comparison would fire on every merged PR. He chose to pin installs to the newest release, and to have the dream cycle prompt for a `check`. Claude wrote check 10, check 8's split-hook move, the release pin, the dream cycle's release check and the pattern's two file kinds.
- **Step 4, first round.** Claude built two fixtures and scratch copies of the three brains, and ran Claude Code headless on each. The 0.72 fixture, the 0.70 fixture and lamarr passed on disk.
- **Stamps dropped.** Rob objected to the stamps: a version line in every file, every file rewritten on each check, an implied linearity, and `check` turned from a reader into a bookkeeper. Claude offered three options: inference, one brain-wide stamp, or keeping per-file stamps. Rob chose inference. He wanted logic based on the state of the file, not on version numbers, and the dream cycle limited to checking whether the installed toolkit has a newer published release.
- **HTML-comment skips dropped.** Rob asked for a review of the comment-handling lines. Claude found them too broad and blind to comments spanning several lines. Rob said the branch should never have added rules for docs a brain may add later, and kept the staged comment blocks, accepting that a seeded brain's dream cycle flags them. Claude reverted all five skips.
- **Step 4, retest.** A usage limit killed the first batch of retests; they ran again after the reset. The 0.72 fixture passed, along with a report-only second check. Subwiz's and lamarr's hooks inferred 0.70 and raised false conflicts. Settled in the template's favor, as the test prompt directed, they overwrote subwiz's fixed clone path and lamarr's clone name. Claude found the cause: counting differing lines rewards an older, shorter template once a paragraph is rewritten. It switched inference to counting paragraphs matched word for word, which picked the right base on every file it tested, and made the walk-through keep a brain's own values. Reruns of lamarr and subwiz passed, and so did lamarr's second check. Virtual-view-brain passed on the old rule; its hooks were re-scored by script.
- Rob had the branch squashed into one commit and PR #22 opened, then this entry written and the working docs committed to `main`.

## Decisions

- **No upgrade takes a manual step, and that rule decides every open choice in this item** — Rob.
- **Working docs stay off the feature branch and land on `main` at session end** — Rob.
- **Installs pin to the newest release tag** — Rob, after spotting that tracking `main` would make every merged PR look like a release.
- **No version stamps; each file's base is inferred from its text on every run** — Rob, over one brain-wide stamp and per-file stamps.
- **The dream cycle prompts a `check` only when the toolkit's remote has a newer release than the installed one** — Rob.
- **No HTML-comment skips; staged comment blocks stay, and a seeded brain's dream cycle may flag them** — Rob.
- **Infer the base by paragraphs matched word for word, not lines differing** — Claude, from the retest evidence.
- **Keep a brain's own values, such as its clone's name, in applied template text** — Claude.
- **One squashed commit for the PR** — Rob.

## What didn't work

- Per-file stamps: built, then removed as the wrong contract for `check`.
- HTML-comment skips: built, then removed as rules for docs a brain may add later.
- Counting differing lines to infer a base: it misread two adapted hooks, and the false conflicts destroyed adaptations when settled in the template's favor.
- A report-only run feeding the merge through pipes: `git merge-file` misreads them on macOS and reports false conflicts.
- Launching four headless runs at once ran into the usage limit, and the batch had to be rerun.

## Lessons

- **Choose how to measure fit by how adaptation happens.** Brains rewrite whole paragraphs, so count the paragraphs that match, not the lines that differ.
- **A test prompt that settles every conflict for the template turns a false conflict into lost work.** That made the defect visible, and it is also the cost a real owner would pay for the same mistake.
- **Bookkeeping a procedure writes into the files it checks changes what the procedure promises.** Infer from state where the evidence allows.
- **Run expensive headless tests in small batches**, grading each before launching the next.

---

# PR #22 review addressed: bounded base inference, declines, and headless tests (2026-11-07)

**Session ID**: `29f05522-fc6f-4cc4-9b42-a0d41b06d7c1`

Rob's session, with Claude as co-author. Rob had Claude read his review comment on PR #22 and address all eight items on branch `template-drift`. He kept inference over a recorded base for the blocking item. Claude rewrote check 10's base rule so a release's added paragraphs and the missed half of a hand update are both recommended. Headless tests of the review's two cases passed, as did a declined-change walk-through. The walk-through exposed an agent second-guessing the merge, which a wording fix closed. The fixes went up as `bb2f6b9`.

## Turn by turn

- Rob asked for the work item's status, then for the latest PR #22 review comment and a switch to the branch. Claude summarized the comment: one blocking item (newest-on-tie inference misses an added paragraph and a partly applied update), two items to settle before `check` carries upgrades (the report names no release; a multi-lobe dream cycle compared with the single-lobe template), and five minor ones. It flagged the blocking item as Rob's call between changing the scoring and recording a base.
- Rob ruled out stamping each file and keying off it, and asked for the scoring to cover both cases. Claude bounded the base by the oldest release whose dropped text the file still holds, broke ties toward the fewest paragraphs the file lacks, and pointed out the cost: without a record, a declined rewrite reads like a missed one and comes back.
- Claude scripted the rule against the review's two cases and the real brains. Counting every lacked paragraph made 0.70 win for lamarr's adapted hook, the false conflict from the previous session. Counting a rewritten paragraph as present fixed it. The same run showed virtual-view-brain's hooks are 0.70 text, so the new rule recommends a worktree fix the old rule had missed.
- The minor items went in alongside: the release and remote's newest in the report, the multi-lobe dream-cycle skip, check 9 and `create` staging the `.gitkeep`, `fi &&` in the install lines (tested against an unreachable remote), the findings sentence narrowed to uncommitted edits rather than a `merge-base` guard that would refuse every fresh clone, and check 10 reordered to define normalization before use.
- Rob asked for headless tests of the two review cases. Claude seeded both fixtures in its scratchpad against a scratch clone of the branch. Both report-only runs inferred the expected base, recommended the expected paragraphs, raised no conflicts and changed nothing.
- Rob asked for check 9's fix and a walk-through that declines a change. The scripted walk-through applied every decision exactly and staged the `.gitkeep`. The second check passed check 9 and asked again about the declined rewrite. The merge left out the declined added paragraph, but the agent read the brain's git history and recommended it anyway as "a gap in check 10". The run also showed that a declined addition goes quiet after a later release's change, not only the same release's.
- Rob approved both wording fixes. Check 10 now treats a paragraph the brain lacks as its own whatever its history, and the decline sentence names "that release or a later one". A rerun of the second check did not mention the paragraph.
- Rob had the branch committed and pushed to PR #22 as `bb2f6b9`, then this entry and the working-doc updates written on `main`.

## Decisions

- **Cover added and partly applied changes by scoring, not by recording a base** — Rob.
- **Bound the base by dropped text, then break ties by paragraphs the file has no version of, then newest** — Claude, from the scripted evidence.
- **Accept that a declined rewrite comes back on every check** — Claude proposed it as the cost of no record; Rob proceeded without a record.
- **Narrow the install-line finding to uncommitted edits rather than guard with `merge-base`** — Claude.
- **Skip a multi-lobe brain's dream cycle and say so** — Claude, from the review's question.
- **Tell check 10 not to second-guess an absent paragraph from history** — Rob approved Claude's proposed wording.
- **Push the review fixes as a second commit, not squashed** — Claude; offered to squash.

## What didn't work

- Counting every template paragraph the file lacks as the tie-break: it rewarded an older, shorter hook template over lamarr's adapted one.
- A `merge-base --is-ancestor` guard on the install line: it would refuse a fresh clone and any install that had tracked `main`.
- Leaving an absent paragraph to the merge alone: the agent searched history and recommended it.
- A shell loop under zsh, which doesn't word-split an unquoted variable, so the first regression run read directories instead of files.

## Lessons

- **Test a tie-break against an adapted copy, not only a pristine one.** The fixture cases passed with the rule that broke lamarr's hook.
- **Say what a procedure must not do when an agent can see evidence the procedure ignores.** The headless agent overruled check 10 from git history until the procedure ruled that out.
- **A rule that infers state can't tell a decline from a miss.** Name which one comes back, so owners aren't surprised.
