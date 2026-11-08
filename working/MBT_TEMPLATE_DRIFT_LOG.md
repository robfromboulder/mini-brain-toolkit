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

---

# Drift check reset to a two-way comparison against the current template (2026-11-07)

**Session ID**: `29f05522-fc6f-4cc4-9b42-a0d41b06d7c1`

A continuation of Rob's session above, with Claude as co-author. Retesting the bounded base rule against mini-subtitle-wizard-brain and lamarr turned up two more false conflicts. Rob asked why check looks for the release a file most resembles at all, rather than comparing it with the current template, and gave his reason for refusing version stamps: an owner may edit a procedure file on purpose, so no version identifies what the file holds. Check 10 became a two-way comparison with a per-paragraph label from the release history, and every test passed headless and by script.

## Turn by turn

- Rob asked for the remaining tests and a rewritten PR description. Claude cloned subwiz and its project repo from Codeberg into its scratchpad. By script, subwiz's brain files behaved as before, but its hook took 0.70 under the bounded rule and raised a false conflict over its fixed clone path: its rewrite of 0.71's worktree paragraph was too short to count as a version.
- Claude prototyped a resemblance tie-break, which fixed subwiz's hook. A simulated walk-through declining one of lamarr's README changes then showed `git merge-file` joining the declined change with lamarr's own description line into a false conflict. Claude stopped and put both defects to Rob, proposing the resemblance tie-break and a paragraph-level merge.
- Rob questioned the premise: compare the brain's file with the current template, offer to add a missing paragraph, and offer to update a changed one or keep it knowingly. Claude measured that on the real brains. The release history labels each changed paragraph on its own as behind (a release's text) or an own edit (in no release), so no base is needed, and every item stays a proposal.
- Rob had Claude rewrite check 10 that way, update this item and rerun the tests. He said he welcomes own edits reappearing on every check, as a prompt to revisit them or suggest them upstream, and deferred offering to file a toolkit issue to a later release.
- Claude added a dropped label for a paragraph the toolkit removed. The first scripted pass showed three kinds of noise, all from text `create` resolves: staged comments, read-index and registry rows, and work setup's pointer to `templates/work/`. Claude left them out of the comparison.
- The 0.72 fixture, with a project repo and inlined scaffolds, came out fully current after an approve-everything walk-through, and a second check reported nothing. Both review cases and the decline walk-through passed headless; lamarr, subwiz, virtual-view and the lamarr README declines passed by script.

## Decisions

- **No version stamps, because an owner's edits mean a version doesn't identify a file's contents** — Rob, stating the reason behind his earlier refusals.
- **Compare each procedure file with the current template, two ways, and drop base inference and `git merge-file`** — Rob, over Claude's resemblance tie-break and paragraph-level merge.
- **Report own edits and declined changes on every check, as a recurring review** — Rob.
- **Label a paragraph behind when the brain's text is any release's, and dropped when the toolkit removed it** — Claude.
- **Leave what `create` resolves out of the comparison** — Claude, from the scripted noise.
- **Defer offering to file a toolkit issue for a kept edit** — Rob.

## What didn't work

- The bounded base rule's tie-break by paragraphs with no version: a short rewrite falls under any similarity line, and subwiz's hook took the wrong base.
- `git merge-file` for a paragraph-level merge: it joins changes on nearby lines into one conflict region.
- Running test loops in zsh, which doesn't word-split an unquoted variable; the loops moved into bash scripts.

## Lessons

- **When a rule keeps needing tie-breaks, question what it is choosing between.** Each fix to base inference handled one brain and broke another; the two-way comparison needs no choice.
- **Ask what the owner's edits mean before designing around them.** Stamps, bases and merges each tried to hide edits that the owner is entitled to make and should see again.

---

# Install pin split out, PR #22 review addressed, plan retired, and every test rerun (2026-11-07)

**Session ID**: `7852c504-efdb-4b1b-b31f-74f45aea2acb`

Rob's session, with Claude as co-author. Rob asked for this item's status and wanted PR #22 mergeable, counting only his last review comment on `8090a94`, since the three-way design it replaced was squashed away. Claude addressed every point of that review except the release tag. Rob moved the release-pinned install lines out to their own PR, #24, rather than tag a release to make #22 safe. He retired the PLAN early in favor of a burndown that tracks both PRs. All nine tests passed against the pushed head, `08d8012`.

## Turn by turn

- **Status.** Claude found the local `main` behind `origin/main`, where the two-way switch was recorded, and read the work item from there. Implementation steps 1–7 were done. Test 2 hadn't run since the switch to two-way.
- **Review triage.** Claude checked the review's claims against the repo and found all twelve held. The blocking one besides the tag was that check 10 compared only tagged releases. Installs had tracked `main`, so a brain seeded between tags would see toolkit text as own edits. One example, a work setup copied after #19, didn't actually show the defect, because work setup didn't change between `0.70` and #20. A dream cycle copied at the same point did.
- **The tag.** Claude first held that merging #22 without a new tag would roll every install back to `0.72`. Rob countered that the README didn't advertise Codex or OpenCode 2. Claude showed that `main`'s README does, from #19, and that `main`-tracking Claude Code installs would lose #19, #20 and #22 as well. Rob objected that tagging `0.73` to merge #22 was exactly the pressure he wanted to avoid, and asked about a release-candidate tag. Claude tested git's version sort: by default it ranks `0.73-rc1` above `0.73`, so the line would need `versionsort.suffix`. Rob then asked whether the install-line change could move to its own PR. Claude listed what moves with it, including the dream cycle's toolkit-release check, which never fires on a `main`-tracking install. With installs still tracking `main`, the off-release fix and the full-history fix become required in #22.
- **Split and fixes.** On Rob's go-ahead, Claude reverted the pin on `template-drift` and applied the review fixes:
  - earlier template versions read from every commit that changed a template, each distinct blob once;
  - `--exact-match` for the installed release, with any other install reported as off-release;
  - the brain's own text left out of the comparison: exemptions-table rows, the hook's lobe paragraph, and a multi-lobe README's namespace sentence;
  - check 8 no longer replacing paragraphs itself, with check 10's approved change still applying to a paragraph check 8 edited;
  - the toolkit recognized by `SKILL.md` and `MBT_CHECK_BRAIN.md`;
  - a multi-lobe dream cycle's skip listing the template's changes, and the README's "whole upgrade" qualified to match;
  - check 9's separate outcomes for an empty directory, untracked files and a non-git brain;
  - `create` leaving `<LOBESPACE>` intact where it names the owning lobe at runtime;
  - the pattern naming its four procedures.

  `install-pin` took the reverted pin back, with `--exact-match` in the dream cycle's check and the "update is a `git pull`" finding corrected.
- **Script.** Claude gave `MBT_TEMPLATE_DRIFT_COMPARE.py` the full-history rule. Its first parse paired the lines of `git log --name-only` two by two, which misaligns on a commit that lists no file, so it now keys on commit hashes. Claude then ran the case the review suggested, procedure files copied at `8ad8deb`: every difference came out behind, missing or dropped. Against lamarr, subwiz and virtual-view, virtual-view's four pre-0.70 own edits became behind.
- **Plan retired.** Claude walked Rob through the PLAN's unaddressed items: the retests, the review's new case, the deferred offer to file a toolkit issue, and the overlaps with other items. It left the accepted risks out. Rob had the PLAN moved to `archive/` and a burndown tracking both PRs written in its place. The MAT plan's pointer to the test expectations moved to the archived path.
- **Push.** Rob asked for a separate commit on the PR branch, so Claude squashed the split and the fixes into `08d8012` on top of `8090a94` and moved `install-pin` onto it. At Rob's request Claude rewrote #22's description.
- **Retests.** Claude rebuilt the previous session's fixtures from its scratchpad scripts against a scratch install of `08d8012`. It ran three headless batches in Claude Code 2.1.319 and graded each on disk. Tests 1, 2 and 6–8 passed. Each report-only run left every repository unchanged, and every run reported the install as off-release at `0.72-18-g08d8012`. Test 7 now shows six behind and no missing paragraph, since the missing one had been the dream cycle's release check. Tests 3–5 and 9 passed by script. Two mismatches between agent and script were the script's own. It counted a multi-lobe README's unchanged namespace sentence as dropped, which Claude fixed. It also treats Phase 1's numbered list as one paragraph, so its four behind paragraphs are the agent's six items.
- **PR #24.** Claude reran the pinned install line on a scratch path: a fresh install and a rerun land on `0.72`, a bad URL exits 128, and check 7's commands behave on and off a tag. It then pushed `install-pin` and opened #24, based on `template-drift`, with its merge order stated.

## Decisions

- **Ship the install pin in its own PR rather than tag a release to merge #22** — Rob, over Claude's proposal to tag `0.73` at merge and the release-candidate option, so no release is cut under pressure.
- **Merge #24 only after #22, and only once a release tag exists at or after #22's merge** — Claude, from the rollback to `0.72` that an earlier merge would cause; Rob accepted it with the split.
- **Move the dream cycle's toolkit-release check with the pin** — Claude, since it never fires on a `main`-tracking install.
- **Read every commit's version of a template, not only releases** — the review's fix, which Claude adopted, with distinct blobs read once.
- **Track both PRs under TEMPLATE_DRIFT, with no new work item, and retire the PLAN early for a focused burndown** — Rob.
- **Push the review round as one new commit, not an amendment** — Rob.

## What didn't work

- An RC tag with the line's default version sort: `0.73-rc1` outranks `0.73`, so installs would stay on the last candidate.
- Parsing `git log --name-only` in fixed pairs, which a commit listing no file throws out of step.
- `echo` lines starting with `=` in zsh, which expands them as a command lookup and fails.

## Lessons

- **Check a reviewer's premise against what the repo publishes before conceding or rebutting.** Both the reviewer's work-setup example and Rob's claim about the README were partly wrong, and each was settled by one grep.
- **When an inert feature depends on a later change, ship them together.** The dream cycle's release check only means something once installs are pinned.
- **Grade a headless run's counts against what the script calls a paragraph.** A numbered list is one paragraph to the script and several items to the agent.

---

# The comparison script moves to `tests/` for MAT (2026-11-08)

**Session ID**: `9dd62b33-2b95-4dd2-b2de-07c645e0d576`

Rob's session, with Claude as co-author, recorded in full in `MBT_LOG.md`. The consequence for this item: `MBT_TEMPLATE_DRIFT_COMPARE.py` doesn't retire to `archive/` at closeout. It moves to `tests/MBT_DRIFT_COMPARE.py` as MAT's drift grader, and whichever item closes first makes the move.
