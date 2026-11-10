# Minimum Acceptance Testing: Session Log

Running log of implementation sessions. Each session appends after a `---` separator.

The first entry, and every one after it, follows the entry format and content rules in `MBT_SESSION_CLOSEOUT.md` — that spec is the authority, not the prior entry, since a fresh LOG file has none to copy.

---

# MAT replanned as a recipe that fits each machine (2026-11-08)

**Session ID**: `9dd62b33-2b95-4dd2-b2de-07c645e0d576`

Rob's session, with Claude as co-author. With 0.73 close, Rob gave feedback on the scaffolded plan. Contributors won't all have a Mac, every harness, every example brain or unlimited tokens. The battery should run what each machine allows, keep no record of results, print a short report that is loud on failure, and be a recipe rather than a script. Claude rewrote the PLAN, FINDINGS and TESTING docs to match, and Rob refined them over several turns. The docs were committed to `main`.

## Turn by turn

- **Research.** Claude read the scaffolded docs, the 0.72 preflight entries in `MBT_LOG.md`, and the testing sections of PRs #19, #20, #22, #23 and #24. It also read the testing approaches of the four other open items in `working/`. The machine has Claude Code but not Codex or OpenCode, and holds lamarr-brain and virtual-view-brain.
- **Rewrite.** The plan became a five-part recipe: probe, select, run, grade and report. Selection follows a budget the runner states, and a scenario needing any one harness rotates across the harnesses found. The nine TEMPLATE_DRIFT tests became seed scenarios covering install, create, check, the dream cycle, work items and session closeout. Every scenario runs on fixtures seeded from release tags, so a contributor with no examples can still run the battery. FINDINGS gained the rejected full matrix, the rejected per-release record, and a deferred golden machine. Most of the old open issues were settled in the plan.
- **Rob's answers.** Rob treated the clash with `CLAUDE.md`'s no-testing-doc binding, which PR #23 had flagged, as housekeeping: the binding goes, and `_TESTING` docs fold into `MBT_TESTING.md`. He asked where the drift-grading script would live if it didn't ship, since the battery has to run on several machines, and it moved to `tests/`. He accepted the three fixed release blockers. He added lamarr-brain and `starburstdata/mini-alien-brain` to the examples.
- **`tests/` or `archive/`.** Rob asked whether a new top-level directory would need excluding from other instructions, and whether `archive/` would be simpler. Claude found that `archive/` conflicts with the cross-reference rule and with the dream cycle's leakage check, which would try to inline the script into `MBT_TESTING.md`. Rob kept `tests/`.
- **Comparison with 0.72.** Asked how the plan compares with 0.72's testing, Claude found the plan covers far more of the toolkit. It also found that most of 0.72's fixes came from transcripts showing agents improvising, which a fixed expectation would pass. It had no equivalent for the blind check of virtual-view-brain judged against Rob's own PR. Rob had both added: transcript notes in grading, reported as notes rather than failures, and an optional judgment scenario.
- **Read-back.** Rob asked for a read-back of the PLAN for accuracy. Claude corrected its earlier claim that `tests/` needs no exclusion: the dream cycle's cross-reference check would flag `MBT_TESTING.md` naming the script, so `MBT_DREAM_CYCLE.md` joined the changes. It also corrected "the 0.72 fixes" to "most of", and fixed several scenario details against the procedures. Two gaps went into open issues. PR #24's pinned lines and release check merge only after the 0.73 tag, and installing the commit under test would overwrite the runner's own install.
- **Scratch `HOME`.** Rob chose a scratch `HOME` for the install. Claude added the model login as a caveat, which Rob questioned, since the testing is local. Claude explained that agent scenarios call hosted models through each harness's own login, which a scratch `HOME` can hide. The wording became "model login", and where each harness keeps it is left to verify on the first run.

## Decisions

- **Coverage fits each machine, with no full matrix, no recorded results and a short local report** — Rob.
- **`_TESTING` docs fold into `MBT_TESTING.md` once it exists** — Rob, as housekeeping.
- **The drift-grading script ships in `tests/`, not `archive/`** — Rob, on Claude's analysis.
- **Three fixed release blockers: a failed upgrade from the last release, a write to the install, and a report-only run that changes a repository** — Rob, accepting Claude's proposal.
- **Grade transcripts for improvisation as notes, and add an optional judgment scenario** — Rob, on Claude's recommendation.
- **Agent scenarios run under a scratch `HOME`** — Rob.

## What didn't work

- Claude's first answer on `tests/` said none of the dream cycle's mechanical checks would touch it. Only the read-back against the cycle's text caught that the cross-reference check would.

## Lessons

- Fixed expectations test mechanics, while the 0.72 preflight's fixes came from reading how agents got there. A battery needs both.
- A claim about what an instruction ignores should come from reading every rule in it, not from the rules that look relevant.

---

# MAT's examples, recipe, fixture seeder and grader land on the work branch (2026-11-08)

**Session ID**: `9dd62b33-2b95-4dd2-b2de-07c645e0d576`

Rob's session, with Claude as co-author, continuing after the replan above. Rob had plan steps 1–4 and 7 carried out: `MBT_EXAMPLES.md`, the move of the drift grader to `tests/`, its check against check 10, `MBT_TESTING.md`, and a fixture seeding script. Rob directed the split: plan and log changes go to `main`, and the toolkit changes go to branch `minimum-acceptance-testing`.

## Turn by turn

- **`tests/` again.** Rob asked whether a hidden `.tests` would mean fewer exclusions. Claude found it would remove none: the cross-reference check is triggered by the path written in `MBT_TESTING.md`, not by the directory's visibility. A hidden directory would also hide the grader from `ls` and from search tools. Rob kept `tests/`.
- **`MBT_EXAMPLES.md`.** Claude gathered provenance from the local clones, the Codeberg repo and the toolkit's logs. A seeding release is the newest tag at a brain's first commit. Claude found `mini-okx-brain` as well, and Rob left it out. Claude widened the plan's "name and holder only" rule for private brains, since author, release and shape say nothing about a project and scenario selection needs the shape. Claude first left the read-index row for plan step 7, and Rob pointed out that this breaks the pattern. The row and a declared-exemptions row went in with the file.
- **Moving the grader.** A failed `git checkout` inside a chained command left the plan edit unrun and a stray commit on the branch. Claude redid both before anything was pushed.
- **Checking the grader against check 10.** Claude found three divergences and confirmed each with a test: tables outside `CLAUDE.md` went unpaired, a literal hub name in a multi-lobe runtime slot matched, and pre-0.70 `<PREFIX>` copies showed false own edits. Rob asked for fixes and reruns. Claude then compared the old and new grader on every example brain. That showed the multi-lobe fix had turned a correctly behind paragraph in virtual-view into an own edit, because `create` at `d66dddf` filled `<LOBESPACE>` with the hub's name. Claude made earlier template versions accept that fill too.
- **`MBT_TESTING.md`.** Claude wrote the recipe, with fixtures as a part of their own. It also wired the doc into `CLAUDE.md` and the dream cycle in the same commit, applying Rob's read-index point to step 7.
- **Fixtures.** Claude generalized the single-tag seeding scripts TEMPLATE_DRIFT left in an earlier scratchpad into `tests/MBT_SEED_FIXTURE.py`, following each ref's own create rules. Seeding 0.70, 0.71, 0.72, `8ad8deb` and HEAD in both shapes, and grading every procedure file, found one more grader gap. Create at 0.70–0.72 filled every `<LOBESPACE>` in a multi-lobe hub's procedure files, work-item slots included. With that fixed, HEAD fixtures came out fully current, and no fixture showed an own edit.
- **Whole-brain grading.** Rob had the caller's preparation folded into the grader as `--brain`. Real brains showed that virtual-view, which predates 0.70, labels each scaffold with a bare doc name, and the scaffold cutter was widened to match.
- **Nebula.** Claude's summary blamed nebula's many own edits on a compound prefix. Rob questioned it. Nebula's work files are plain `NEBULA_<WORK>_*`, and word-level diffs showed the own edits are owner adaptations over older template text. Claude corrected the claim in the plan.

## Decisions

- **Keep `tests/` visible** — Rob.
- **Leave `mini-okx-brain` out of the examples** — Rob.
- **A top-level doc gets its read-index row in the commit that adds it** — Rob.
- **Plan and log on `main`, and `CLAUDE.md`, `MBT_EXAMPLES.md` and the rest of the toolkit change on the work branch** — Rob.
- **Fold the caller's preparation into the grader** — Rob, on Claude's offer.

## What didn't work

- A shell command chained across a heredoc kept running after a failed `git checkout`, and committed the plan edit to the wrong branch.
- Claude's first multi-lobe grader fix was checked only against the targeted test, and regressed a real brain.
- Claude passed on the old log's compound-prefix line about nebula without checking it against the brain.

## Lessons

- Run a grader change against every example brain before and after, and diff the two runs. The targeted tests passed on the change that regressed virtual-view.
- Seeding fixtures at every ref and grading them tests the grader and the seeder together. A HEAD fixture must come out fully current, and no fixture may show an own edit.
- A claim about a brain's shape should come from the brain, not from a log entry about it.

---

# MAT's first run, its reintroduced defects, and draft PR #25 (2026-11-09)

**Session ID**: `9dd62b33-2b95-4dd2-b2de-07c645e0d576`

Rob's session, with Claude as co-author, continuing from the entry above. Rob had Claude check the scratch `HOME`, which failed and was replaced by a test-named install. Claude then ran the recipe for the first time on this machine and fixed what the run found. It ran four reintroduced defects against controls, reworked the scenarios that couldn't catch them, and opened draft PR #25.

## Turn by turn

- **Scratch `HOME`.** A one-line headless prompt under an empty scratch `HOME` reported "Not logged in". Claude's next command would have listed keychain item names. The auto-mode classifier blocked it, and Claude stopped and gave Rob three options instead. Rob chose to install the commit under test as `mini-brain-toolkit-mat` beside his own install. His reasons: it leaves every harness's sign-in alone, and nobody knows what Codex or OpenCode do with a moved `HOME`. The renamed skill loaded and asked whether to run create or check. Its sign-in warning showed that Rob's Claude Code sign-in ends between 2026-11-13 and 2026-11-16, so the probe now reports such warnings.
- **First run**, against `7048ac3` on a small budget, with Claude as the running agent. Claude Code was the only harness found. The install line passed in all eight runs across zsh and bash. In the upgrade from 0.72, an approve-all check fixed every file, and a report-only second check found no drift and changed nothing. The two runs cost $4.91 and took 13 minutes. Drift edge cases a–c and all six example brains passed by script. The transcripts gave five notes:
  - the tested agent found the grader inside the test install and tried to run it for check 10;
  - check 10's temp directory and `python3` were outside the run's permissions;
  - the agent and the grader counted a list differently;
  - the seeder named the brain `fix-brain`, where the hook expects `mini-fix-brain`;
  - the grader showed only the template's side of an own edit.
- **Fixes.** Rob had all five made. Testing them showed that Claude had called scenario 8 a pass by pairing paragraphs by hand from the wrong file. The grader had missed subwiz's fixed-path hook paragraph, a 28-word rewrite of a 67-word template paragraph. At Rob's direction the grader now pairs a rewrite in place: the one unpaired paragraph between its neighbours' versions that opens with the same four words.
- **Reintroduced defects.** Claude first worked out which scenario would catch each defect. Two had no scenario.
  - The install line checking out a tag after a failed fetch: caught by scenario 1, at no cost.
  - Check 10 reporting create's staged comments as missing, reintroduced by deleting the sentence that guards against it: the agent behaved correctly anyway. The run also showed agents splitting lists differently from one run to the next.
  - Rob had three changes made. The grader now compares list items one by one. Scenario 6 plants an own edit. Scenario 12 plants a `working/` citation.
  - In a second round, against controls: the own-edit defect was caught. The staged-comment defect reproduced on a stage-1 fixture with the comments deleted, so that fixture joined scenario 7. The template dream cycle's exemption defect didn't reproduce, because both runs flagged the citation. The runs cost about $8.
- **PR.** Rob had Claude open draft PR #25 from `minimum-acceptance-testing`, then close out the session.

## Decisions

- **Install the commit under test under a test name, not under a scratch `HOME`** — Rob.
- **Fix all five of the first run's notes** — Rob, on Claude's proposals.
- **Pair heavy rewrites in place in the grader** — Rob, choosing between Claude's two options.
- **Compare list items one by one, plant an own edit in scenario 6 and a `working/` citation in scenario 12, and pay for the additional runs** — Rob.

## What didn't work

- A scratch `HOME`: Claude Code's sign-in doesn't follow it.
- Claude's first check of scenario 8's known own edits searched the grader's template-side output. Its next check paired paragraphs from the wrong file and reported a pass that wasn't one.
- Two reintroduced defects didn't reproduce from a one-sentence deletion. Agents fell back on the template's own comments, or on whether a file actually exists.
- A setup script edit that assumed the hook's paragraph order matched nothing, and the setup had to be rebuilt.

## Lessons

- A grader in reach of the tested agent gets used. Isolation has to be enforced by what's installed, not by what the procedures cite.
- Reintroduce a defect only after naming the scenario that should catch it. Two of four had none.
- A defect that doesn't reproduce from its sentence alone needs the fixture that triggered it originally, not a weaker test.
- A known own edit has to be checked on the brain's side of the pair, on the file that holds it.

---

# PR #25 squashed, and its working file taken out (2026-11-09)

**Session ID**: `9dd62b33-2b95-4dd2-b2de-07c645e0d576`

Rob's session, with Claude as co-author, continuing after the entry above. Rob had PR #25's branch squashed to one commit. Claude checked that the tree was unchanged and force-pushed with lease. Rob then asked what becomes of TEMPLATE_DRIFT's comparison script. Claude first answered that it would be promoted rather than archived, and suggested a burndown note to keep TEMPLATE_DRIFT's closeout from archiving it. Rob said a review would treat the deleted working file as load-bearing, and that working files don't go in PRs. The decision is recorded in full in `MBT_LOG.md`.

## Turn by turn

- **The consequence for this item.** Claude restored `working/MBT_TEMPLATE_DRIFT_COMPARE.py` on the branch, amended the squashed commit as `abce7be`, and force-pushed with lease. PR #25 now changes six files, none in `working/` or `archive/`. The commit message, the PR description, the plan and FINDINGS now say the grader is a copy, not a move.

## Lessons

- A move out of `working/` puts the working file in the PR's diff. Copying keeps it out, and leaves the original to retire with its item.

---

# PR #25 rebased onto #26 at V33 (2026-11-09)

**Session ID**: `9dd62b33-2b95-4dd2-b2de-07c645e0d576`

Rob's session, with Claude as co-author. The merge order and the rebase-only rule are recorded in `MBT_LOG.md`. The consequence for this item: once #26 merged, Claude rebased #25's single commit onto `main` as `b293660`. The only conflict was `CLAUDE.md`'s version line, which Rob had resolved to V33, one bump for one commit. #25 still changes the same six files, with nothing in `working/` or `archive/`.

---

# MAT's second-machine run, the recipe's improvised steps written in, and a Linux platform (2026-11-09)

**Session ID**: `1f667913-3aba-4e55-9e66-626a2c41a789`

Rob's session, with Claude as co-author, on a machine with Claude Code, Codex and OpenCode 2 and three of the six example brains. Rob asked for the second-machine test, which turned out to be this item's step 6 rather than TEMPLATE_DRIFT's. Claude ran the battery from PR #25's branch on a medium budget, then Rob redirected: the point was to verify the battery, so what mattered was where the runner had to improvise. Those gaps went into `MBT_TESTING.md`, `MBT_EXAMPLES.md` and two new scripts, Linux runs in Docker were added, a fresh-agent dry run found four more gaps, and #25 was squashed to one commit and marked ready for review. The run also found procedure defects, recorded in `MBT_LOG.md` and fixed in #25.

## Turn by turn

- **Which test.** Rob asked to read TEMPLATE_DRIFT and run "the second test" on a second machine. Claude found the matching step in this item's plan, "run it on a second machine", and ran that, saying so.
- **The run.** Rob chose a medium budget and only the brains already on the machine. Claude probed three harnesses, three shells and three brains, then ran scenarios 1, 2, 6, 7a–c, 8, 10 and 16 and the script half of 14. Scenario 6 in Codex reverted a planted own edit, scenario 10b failed in Claude Code, and Codex and OpenCode 2 doubled the log's separator in 16.
- **Rob's redirect.** Rob said the run's purpose was to verify MAT, so Claude listed every place it had improvised or changed the instructions. That list had 17 items, four of which decided whether a run means anything: scenario 6's unfixed prompt and planted paragraph, what a label match means, and Codex's read-only `.git`. Rob asked for drafts, and for item 6 had the grader's names recorded in `MBT_EXAMPLES.md` rather than inferred. Checking those names showed that the run's guessed `<project>` for mini-alien-brain had turned a README paragraph into a false own edit.
- **Scenario 6, rerun.** At Rob's request Claude reran scenario 6 in Codex with the fixed prompt. It reverted the edit again. Rob asked whether OpenCode was the only harness with the defect, and Claude corrected that: Codex was, with OpenCode untested. Rob had both other harnesses run. OpenCode 2 also reverted the edit, and Claude Code kept it.
- **Bundling the fix.** Rob asked how large the check 10 fix was. At one sentence, Rob chose to carry it in #25 rather than review two PRs. Against the fix all three harnesses kept the edit. In the same run OpenCode 2 also applied its own resolution of a template conflict, so Rob had scenario 6 allow changes outside procedure drift that the agent's report names.
- **A stray write.** A Claude Code tested agent mistyped a path and wrote a file beside the scratch directory, outside its allowed directories. Claude deleted it after checking the directory held nothing else. The recipe now checks every run for such writes, and counts a hit only when the agent's transcript shows it, since a broad sweep also caught another session's log.
- **Docker.** Rob asked whether Docker figured in the plans. It didn't, though PR #20 had used it for a macOS-versus-Linux check that retired with its item. Claude added a platform dimension for script scenarios only, since each harness's sign-in lives in the runner's `HOME`. Scenarios 1 and 14 then passed in a Debian container with output identical to the host's. Claude's first script would have written Rob's global git config; the classifier blocked the run, and the script now sets git config for its own process only. At Rob's request it moved to `tests/MBT_SHELL_CHECKS.sh`.
- **How to approve.** Rob asked what would give enough confidence to merge, with multireview or more dry runs as options. Claude recommended two cheap checks over a code review: the other direction of the check 10 fix, and a fresh agent dry-running the recipe, which gives a read not anchored on Claude's. Both passed. The dry run listed 13 guesses, and Rob had the four that would change a run fixed: the brain search, selection by changed files, split-cost scenarios, and scenario 16's wording.
- **Procedure fixes and squashes.** Rob had #25 squashed to one commit, then asked that other procedure defects the run found be fixed now rather than later. Claude fixed them, reran the affected scenarios, and squashed again. Commit hashes in the PR description and this item's plan that a squash removed were replaced with descriptions.
- **What the results verify.** Asked, Claude said the results verify MAT, not 0.73. Scenario 6 last ran before the final procedure changes, #24 isn't included, and much of the battery never ran. 0.73 is verified by a full run after #25 and #24 merge.

## Decisions

- **Second-machine run on local brains only** — Rob.
- **Record each example's grader names in `MBT_EXAMPLES.md`** — Rob, over inferring them.
- **Carry the check 10 fix in #25** — Rob, on Claude's sizing.
- **Scenario 6 allows changes outside procedure drift that the report names** — Rob, from Claude's two options.
- **Linux for script scenarios only, through Docker** — Claude, on Rob's question; Rob had the script shipped in `tests/`.
- **Two cheap checks before merge, instead of a full review** — Claude's recommendation, which Rob took.
- **Fix the dry run's four run-changing gaps now, and leave the other nine for the 0.73 run** — Rob.
- **One commit for #25** — Rob, twice.

## What didn't work

- `timeout`, which macOS lacks, in the sign-in probe.
- Variables expanded in zsh, which doesn't word-split them.
- A scenario 1 script that ran the bad-URL case before the moved-remote case, leaving no install to test.
- A scratchpad script whose `git config --global` would have changed Rob's own config.
- A sweep for stray writes that counted any new file under the temp root.

## Lessons

- **When a run exists to test a test, the improvisations are the result.** Rob's redirect turned a pass/fail report into the list of fixes the recipe needed.
- **A pinned prompt is part of the scenario.** Until scenario 6's prompt was fixed, a failure couldn't be told apart from the wording.
- **A fresh agent finds the gaps the author's context hides.** The dry run found four run-changing gaps after Claude had written every fix.

---

# lamarr-brain's project repo filled in `MBT_EXAMPLES.md`, as PR #27 (2026-11-09)

**Session ID**: `7aa1697a-4c4f-451d-95d1-829c52e64e8e`

Rob's session, with Claude as co-author, run beside the second-machine session above. Rob asked Claude to read this item's status and to prepare the fields missing from `MBT_EXAMPLES.md` without committing, since the other session was still running. One field could be filled, and it landed as PR #27 after #25 merged.

## Turn by turn

- **Status.** Claude found `MBT_EXAMPLES.md` only on #25's branch, and the local branch a squash behind origin. Its project repos column had dashes for lamarr-brain, mini-alien-brain and mini-guardrails-brain.
- **Filling the dashes.** Claude searched the clones on this machine for each brain's hook. The `lamarr` clone carries lamarr-brain's in its `CLAUDE.md`. No clone on hand carries mini-alien-brain's or mini-guardrails-brain's. mini-alien-brain names the codebase it describes, but Claude left it out as unconfirmed and as possibly private project detail. Claude prepared the change as a patch in its scratchpad, with the file at V3, and Rob kept the other two dashes.
- **Applying it.** Rob reset the local branch to origin, and Claude applied the patch. Rob asked for an amend into #25's commit and a force-push. The lease rejected the push: the other session had merged #25 and deleted its branch, and the merged file still had the dash.
- **PR #27.** Rob had Claude carry the change on a new branch from `main` as its own PR, and drop the local #25 branch.

## Decisions

- **Leave mini-alien-brain's and mini-guardrails-brain's project repos as dashes** — Rob.
- **Carry the fix as its own PR once #25 had merged** — Rob, on Claude's proposal.
- **Leave this item's plan citing `MBT_EXAMPLES.md` V2**, since it records what the second-machine run produced — Claude; Rob didn't ask otherwise.

## What didn't work

- An amend for a PR that had merged while the change waited. Only the lease stopped the force-push.

## Lessons

- Fetch and check a PR's state right before amending into it while another session works on it, not just when preparing the change.

---

# PR #25 merged, its branches deleted, and the burndown cut to what remains (2026-11-09)

**Session ID**: `1f667913-3aba-4e55-9e66-626a2c41a789`

Rob's session, with Claude as co-author, continuing after the second-machine entry above. Claude brought #25's description in line with the final commit, and Rob merged it. Claude then deleted the item's branches and rewrote the unfilled burndown. At Rob's direction it was cut to the work that remains, and later dropped the examples item that #27 and Rob's call had settled.

## Turn by turn

- **Description.** Rob asked whether #25's description needed updates. The change list matched the final commit. "Not yet" lacked two gaps: scenario 6 hadn't run since the last procedure changes, and the fold rule hadn't run at all. The description also didn't say the results verify the battery rather than 0.73. Claude added both, updated the cost, and tidied the second-machine list. Rob then merged #25.
- **Branches.** Claude confirmed the merged commit held exactly the branch's content, then deleted `minimum-acceptance-testing` on GitHub and locally, along with two local backup branches made before the squashes.
- **Burndown.** The burndown was still the unfilled scaffold. Claude rewrote it with the PR's completed stages and the open work. Rob said a burndown holds no history, so the completed stages came out. Claude had dated two stages wrongly before checking them against the PR and this log.
- **Examples.** A pull brought in #27 from a parallel session. It filled lamarr-brain's project repo, and recorded Rob's call to leave mini-alien-brain's and mini-guardrails-brain's as dashes. That settled the burndown's examples item, so Claude removed it and deleted #27's branch. Rob reviewed each burndown edit before Claude committed it.

## Decisions

- **A burndown holds only open work** — Rob.
- **Review burndown edits before they're committed** — Rob.

## Lessons

- **Check what a pull brings in against the open burndown.** A parallel session had already settled one of its items.

---

# Scenario 12's first run, against #24 (2026-11-09)

**Session ID**: `1f667913-3aba-4e55-9e66-626a2c41a789`

Rob's session, with Claude as co-author, retesting TEMPLATE_DRIFT's #24 and recorded in full in that item's log. The consequence for this item: scenario 12 ran for the first time, in Codex, and passed in both release cases. Its run surfaced three things for the recipe.

- **The release check reads the runner's install.** It looks at the standard install paths, so a run that leaves `HOME` alone compares the runner's own clone. The run pointed `HOME` at a scratch home holding a controlled clone at `~/mini-brain-toolkit`, and kept Codex's sign-in through `CODEX_HOME`. Claude Code's sign-in doesn't survive a moved `HOME`, so this way of running scenario 12 is Codex's until another is found.
- **The planted `working/` file needs reasoning in it.** The fixture's plan held none, so neither run could inline it, and each flagged the reference instead. With reasoning in the file, the leakage check's fix can be graded too.
- **Phase 3 can't research from Codex's sandbox.** Both runs left checkable SCOPE claims unverified and called external research inapplicable.
