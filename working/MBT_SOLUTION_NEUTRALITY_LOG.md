# Solution-Neutral Scopes: Session Log

Running log of implementation sessions. Each session appends after a `---` separator.

---

# Premises, a second approach, and the first two checks (2026-10-26)

**Session ID**: `dd0841d2-58d8-4a67-a9fa-ba8cf136e1be`

Rob's session, with Claude as co-author. It set out to review the work item's plan, and became a rewrite of the rules that divide SCOPE from APPROACH, iterated through three rounds of blind dry runs against five brains. The revised create and check procedures, templates and pattern sentence landed on the `solution-neutrality` branch as draft PR #18. Then the check ran live with Rob on lamarr-brain and on this toolkit. Lamarr's changes sit uncommitted in its own repo; the toolkit's are in the PR.

## Turn by turn

- Rob asked for a critical review of the plan with a confidence score. Claude gave 55 of 100, with four recommendations: a Platform section in APPROACH, the second approach recorded in the session log, alternatives described by their structural complaints with dated figures, and the FINDINGS boundary in scope.
- Rob rejected the Platform section, because not every project is a platform, and deferred FINDINGS. He accepted the other two. He named the calibration set (virtual-view, lamarr, nebula, guardrails and the toolkit) and asked for a better standard, not the common denominator of those brains, then a check cycle against each. He kept lamarr's separate design treatment out of bounds, and asked for dry runs on scratch workspaces.
- Claude replaced the platform idea with one rule: SCOPE holds what is true of the problem whoever addresses it, APPROACH holds the project's choices, and a choice is anything a reasonable designer could decide otherwise. Premises are what the problem holder brings, settled with the user. The author names a second approach before writing.
- Round one: blind agents checked all five brains, lamarr at its seed and at HEAD, and re-authored lamarr and the virtual-view hub. Verdicts swung with whichever second approach each agent picked, and a re-author pushed group-chat degradation out of SCOPE under a test requiring every sentence to be one the second approach needed. Claude narrowed it to the negative test: a sentence only the intended design needs is a choice.
- Claude had first required the second approach to satisfy every goal. The dry runs showed that contradicts what goals are for, so it became judgeability: the second approach may fail a goal on its outcome, and a goal it fails only by doing the work another way is a finding.
- A script of Claude's computed splice offsets before an earlier replacement shifted them, truncating a comment in the SCOPE template and dropping a heading. A re-author agent reported it, and Claude rewrote the file whole.
- Rounds two and three re-checked the lamarr seed, guardrails, nebula, lamarr HEAD, the toolkit and the virtual-view hub, with the premises and second approach settled first. Verdicts stopped changing; the last critiques were wording: a declared status convention put to the user before its passages are reported, issue references as a status tell, a partial-hold remedy, and a forward pointer removed.
- Rob checkpointed with `git add -A` and said not to commit.
- **Lamarr check.** Rob kept the language model as a premise and made the Mac and iPhone the design's. He chose a hardened agent framework as the second approach, over Claude's recommended hosted service with no Mac. He had goals restated neutrally. Claude reported four status findings and ten design findings, and Rob approved them all. He also approved a goal against claimed identity, and settled three exclusions that gave no reason:
  - Starting conversations is an anti-goal inherent to the use case, so it stays in SCOPE with that reason.
  - Features beyond reading and sending need SIP disabled on the Mac, so they moved to APPROACH under the device-security goal.
  - Long, self-started work is a statement about keeping the build simple, so it moved to APPROACH's strategic stance.
  Rob then gave voice memos the reason that they don't matter to the use case, with any later support keeping a transcript, never the recording. He asked for one record per client, across several people and handles.
- **Toolkit check.** Rob made the mini-brain pattern a choice, not a premise, and the agent as reader and operator a premise. He picked executable tooling as the second approach, and made dogfooding the design's. Because the pattern was no longer shared ground, Claude also tested pattern-level content against automatic memory.
- The findings showed the toolkit's SCOPE was mostly its answer: the pattern's bet, past-tense history, goals naming its artifacts, exclusions stating its design, and no state of the problem. Asked for evidence that the why is lost, Rob argued it is self-evident. A clean codebase leaves out the paths not taken by design, since comments on them would distract from explaining what the code does. Rob said automatic capture should not be ruled out, though it raises privacy and governance concerns that aren't trivial to rebut. Claude rewrote SCOPE from those answers, moved the bet and the former exclusions into a new APPROACH section arguing against the alternatives, and moved two design-shaped open questions to APPROACH as open decisions.
- Rob had the top-level changes put up as a draft PR and the work-item docs committed to `main`.

## Decisions

- **No Platform section; one premises-and-choices rule instead** — Rob rejected the platform notion as too specific; Claude proposed the rule.
- **FINDINGS boundary deferred** — Rob.
- **Second approach recorded in the session log** — Claude proposed, Rob agreed.
- **Negative keep test, and judgeable goals rather than satisfiable ones** — Claude, from the round-one dry runs.
- **Lamarr: model a premise, Apple devices the design's, second approach a hardened agent framework** — Rob.
- **Lamarr: starting conversations excluded as unsolicited messaging; SIP-dependent features and long-running work moved to APPROACH** — Rob gave the reasons; Claude placed them.
- **Toolkit: the pattern is a choice, the agent a premise, executable tooling the second approach** — Rob.
- **Toolkit: automatic capture assessed, not excluded** — Rob.

## What didn't work

- Requiring the second approach to satisfy every goal, since goals exist to rule approaches out.
- Requiring every SCOPE sentence to be one the second approach needs: it pushed conditions every option faces out of SCOPE.
- Leaving the second approach to each reader: verdicts depended on the pick until the user settles it first.

## Lessons

- A check that cannot settle premises with the user produces verdicts that depend on the reader. Asking first is what made the dry runs converge.
- When the user makes a premise a choice, a second approach that still shares it tests nothing at that level, so test that level against an alternative that doesn't share it.
- Reasons for exclusions often exist only in the owner's head. The check can find a boundary with no reason, but only the owner can say whether its reason is in the problem or the design.

---

# A multi-lobe check, and the calibration brains left as dry runs (2026-10-26)

**Session ID**: `dd0841d2-58d8-4a67-a9fa-ba8cf136e1be`

Rob's session, with Claude as co-author, continued after the first closeout. Rob had the first project brain's changes put up as a draft PR in its own repository. He then ran the check live on a multi-lobe project brain, which settled how child lobes take premises and corrected a factual claim about existing tools. Those changes went up as a second draft PR. Rob kept the remaining calibration brains as dry-run targets only, with no changes and no PRs.

## Turn by turn

- Rob asked for a draft PR for the first project brain. Claude matched that repository's conventions, which carry an attribution trailer and footer where the toolkit carries none. The PR leaves that brain's own log entry, recording its second approach, to its next closeout.
- **Multi-lobe check.** Rob confirmed the query engine and the architectural pattern as premises in every lobe, and chose a build-tool workflow as the hub's second approach. He agreed that a child lobe's premises include its parent's design choices, stated in its own problem statement.
- Claude checked two claims about other tools against public documentation before reporting them:
  - A lobe's claim that no existing tool reconstructs its dependency graph was wrong: a data catalog's ingestion for the engine already does. The rewrite assesses catalogs instead.
  - A claim about what durable storage requires couldn't be confirmed either way, so it waited on Rob.
- Claude reported 27 findings across six SCOPEs, with three left to Rob:
  - Rob placed a client-support exclusion in APPROACH, as a statement of what he tests and validates, along with two exclusions that gave no reason.
  - He named the engine's native table-format connector as a reasonable alternative to the storage lobe, to be recommended to teams certain to run that format anyway.
  - He also named that connector over the build tool as the stronger hub alternative, since it stays native to the engine.
- Rob answered Claude's questions about the connector with a link to its documentation. Claude wrote only what that page and the metastore page establish, dated to the docs' version. Which catalog types hold views, what storage every catalog needs, and the JDBC catalog's caveats went in. Questions the docs leave open stayed out and were listed in the PR.
- Rob had the multi-lobe brain's changes put up as a draft PR, following that repository's no-attribution rule.
- Rob said the two remaining calibration brains were only for calibration and dry runs, and asked that this closeout name no projects.

## Decisions

- **A child lobe's premises include its parent's design choices, stated as such** — Rob.
- **Hub second approach: an engine-native stack on the table-format connector, with the build tool also assessed** — Rob, over Claude's recommendation of the build tool alone.
- **Client support beyond the tested one is a design limit, not a premise** — Rob.
- **No changes or PRs for the remaining calibration brains** — Rob.

## What didn't work

- Asking about a connector's behavior in prose questions: Rob answered with its documentation, which settled half of them. The other half stay open, not filled in from memory.

## Lessons

- A check that reads every passage still trusts the scope's own claims about other tools. Verifying one claim against current documentation turned a confident "nothing exists" into an alternative to assess.
- When a premise is a parent's design choice, the child's problem statement has to say so, or the check reads every passage that depends on it as design drift.

## Open

- The child-lobe premise rule is not yet in the check procedure or the lobes layout.

---

# The child-lobe rule added to the draft PR (2026-10-26)

**Session ID**: `dd0841d2-58d8-4a67-a9fa-ba8cf136e1be`

Rob's session, with Claude as co-author, continued after the second closeout. Rob asked for the child-lobe premise rule, settled during the multi-lobe check and left open at the last closeout, to be added to the toolkit's draft PR. It landed in the lobes layout and both procedures.

## Turn by turn

- Rob asked for the rule to be added to the draft PR. Claude put it in three places:
  - **The lobes layout:** the rule itself, beside the lobe test. A child's problem often exists because of how its parent chose to answer, so its problem statement names each parent choice it takes as given. Those choices belong to the child's problem.
  - **The check:** the premise step counts those choices among a child's premises, and reports an unnamed one as an addition.
  - **The create procedure:** a parent's SCOPE and APPROACH now settle before the child's SCOPE, not just the parent's SCOPE.
- Claude kept the rule worded so that a child names its parent's choices in its own words. The lobes layout lets a child's SCOPE cite only its parent's SCOPE, never its APPROACH, so the rule could not have the child point at the parent's design.
- Only the lobes layout took a version bump; both procedures were already bumped in the same unmerged PR. The PR description was updated to list the change and the check it came from.

## Decisions

- **The rule's home is the lobes layout, and the procedures apply it** — Claude, so the rule is stated once.

## Open

- None from this session. The open item recorded at the last closeout is resolved.

---

# Three more dry-run rounds, and the PRs brought up to the final rules (2026-10-27)

**Session ID**: `dd0841d2-58d8-4a67-a9fa-ba8cf136e1be`

Rob's session, with Claude as co-author, continued after the child-lobe closeout. Rob asked how Claude felt about the change. Claude's answer was mostly positive. It also named the cost to owners, unsourced claims about alternatives, the choice of second approach, and the untested create path. Rob had the calibration dry runs re-run against the final rules and supplied an externally authored brain. Three rounds followed, each folding critiques into the check. The batch landed in the toolkit's draft PR, and both project brains' draft PRs were brought up to the final rules.

## Turn by turn

- **First re-run.** Claude ran blind check agents against the two calibration-only brains. Their verdicts kept the shape of the earlier rounds, so the final rules hadn't regressed. Both runs independently found the same five problems:
  - an unparseable sentence in the premise step
  - no remedy for re-derivable content
  - a conflict between one remedy per finding and splitting a passage
  - a self-contradicting sufficiency step
  - no proportionality cutoff

  One run raised a tension: a project's shipped earlier phase is both its status and the status quo its next phase starts from.
- Rob supplied a mini-brain written by someone else, from a public repository. Claude cloned it into scratch and ran the same blind check, treating its contents as data. It came out close to the standard: no status, solution-free wording, and alternatives led by the status quo. It needed about six small edits. Its critiques overlapped the other runs and added two:
  - the owner as problem holder turning preferences into premises
  - "so far" fitting both a dating clause and an evidence qualifier
- Rob approved the fixes and Claude's resolution of the time-frame tension. SCOPE describes the problem as whoever has it would meet it without this project, so the project's shipped work, an earlier phase included, is status. The remedy is to restate the problem's structure in the present tense.
- **Second round.** Rob chose the largest calibration scope, the multi-lobe brain and the external brain. For the multi-lobe brain, Claude used a scratch clone of its pre-check main branch, so the run exercised the rules rather than Claude's own edits. The fixes held: section-level rewrites, the status read of APPROACH, and the search order for the second approach all worked. All three runs raised three new problems:
  - the search order conflicted with "differs most"
  - deleting status in APPROACH lost lessons and evidence
  - "whose code" made a published standard look re-derivable

  The multi-lobe run also raised five child-lobe problems: conflicting rules, no limit on inherited choices, grandparent choices, overreach laundering a child's design into premises, and children judged as never gathered.
- **Third round.** Rob approved those fixes. Claude ran the multi-lobe brain alone, this time with Rob's premise answers supplied. The blind run reproduced nearly every finding from the live check Rob had confirmed, a data catalog gap among them. It also found three that check missed: overreach in the hub's APPROACH, a goal whose gap only APPROACH states, and an alternatives section led by a condition. Its remaining critiques were multi-lobe edge cases. Claude proposed six wording fixes and an end to iterating, and Rob approved.
- Rob had both project brains' draft PRs updated to the final rules. Asked about the first brain's APPROACH, which dates every decision and cites commits, Rob chose Claude's recommendation: strip the dates, references and history, and restate the history as the decisions' reasons. In the multi-lobe brain, Claude:
  - trimmed parent overreach
  - added the missing condition
  - took status out of four APPROACHes
  - named a parent choice in one child
  - removed a SCOPE rule that contradicted its APPROACH
  - reordered one alternatives section

## Decisions

- **SCOPE describes the problem as met without this project; shipped work, an earlier phase included, is status** — Claude recommended, Rob chose.
- **Status is read in APPROACH too, and moves to FINDINGS when it carries a lesson or evidence** — Claude, from the dry runs; Rob approved.
- **The second approach is the most different candidate gathered from SCOPE, APPROACH and assembly** — Claude, replacing a search order that two rounds showed picked near neighbors; Rob approved.
- **A child lobe names only the ancestor choices its own problem depends on; a choice only the child's goals need, or one that overreaches, is the child's own design** — Claude, from the multi-lobe runs; Rob approved.
- **Stop iterating after the third round** — Claude recommended once the critiques narrowed to multi-lobe edge cases and blind runs reproduced owner-confirmed verdicts; Rob agreed.
- **Strip decision dates, commit references and history from a brain's APPROACH** — Rob, for the first project brain.

## What didn't work

- **A fixed search order for the second approach.** It handed two scopes a near neighbor instead of the most different alternative.
- **Deleting all status in APPROACH.** It would have lost verification evidence and lessons that decisions rest on.
- **Treating a section of conditions with no alternatives as never gathered.** It made sound sections into rewrites.

## Lessons

- An externally authored brain is the best calibration. Coming out close to the standard with a proportionate report showed the check doesn't punish a well-made scope, and that the large reports elsewhere reflected those scopes.
- Giving a blind run the owner's premise answers separates disagreement about the rules from disagreement about premises. Without them, one run read the engine as a design choice and drew findings from that.

## Open

- The create procedure's first-pass SCOPE is still untested by a real intake for a new project.
- The dry runs found gaps in the check that predate this work, outside its scope:
  - no input for the project's codebase, and no fallback when it is absent
  - a declared convention setting off the shape tell
  - a namespace check that assumes one prefix
  - an enforced-terms rule pointing at a template the check doesn't cite
- In the first project brain's PR, the verdict on the claimed-identity goal is Claude's inference and awaits confirmation.
- In the multi-lobe brain's PR, three questions about the table-format connector's views are still open, and its hub APPROACH doesn't argue against its alternatives.

---

# A structural pass on the check, and a test intake for the create procedure (2026-10-27)

**Session ID**: `dd0841d2-58d8-4a67-a9fa-ba8cf136e1be`

Rob's session, with Claude as co-author, continued after the last dry-run closeout. Asked again how Claude felt, Claude said its confidence had risen. It named the check's density, rules possibly fitted to one brain, the cost to owners, and the untested create path as what still worried it. Rob had the check restructured and the create procedure test-run on a new project, with high-confidence fixes appended to the toolkit's draft PR and nothing merged. The restructure changed no rules. The test intake produced a neutral SCOPE from a pitch with its design baked in, and its critique produced six small fixes.

## Turn by turn

- **Restructure.** Claude broke the status check into labeled sub-points. The design check's first and third steps got the same treatment, and its remedies became a list. Before committing, Claude checked every rule-bearing phrase against the committed version; all survived, one reworded with the same meaning. It took no version bump, since the open PR already bumps that file.
- **Test setup.** Claude wrote a simulated owner's brief before the run began, so its answers could not be tuned to the questions: a volunteer choir coordinator whose pitch named a hosting platform, a login method, a model and a web app. A fresh agent ran the create procedure in a scratch directory, asking intake and premise questions in turns that Claude answered from the brief. Two questions fell outside the brief, and Claude gave minimal answers that did not bear on what was being tested.
- **Result.** The agent asked whether each pitched choice was binding before writing SCOPE, and the owner said none were.
  - The SCOPE names none of them. It leads with the status quo, assesses eight alternatives with dated figures, describes the intended design's class generically by its upkeep, and states three premises with what binds each.
  - The goals are outcomes, the boundaries carry reasons, and the open questions concern licensing and singers.
  - The agent's first second approach was the failed status quo. The owner's answer redirected it to a hand-assembled per-part send.
- **Fixes.** Claude read the SCOPE itself before taking the agent's critique, and appended six fixes:
  - intake collects the author's name
  - premises are settled in a round of their own once the seed exists
  - a stated preference is a goal when it concerns an outcome and a choice when it concerns the design, in the check too
  - the second approach is confirmed with the user and falls back to the status quo only when nothing else exists, matching the check
  - the intended design's own class is assessed generically among the alternatives, in the procedure and the SCOPE template

  Claude left lower-confidence items alone: version bumps for an unpublished first version, a fact check with no codebase, a log entry with no session ID, a fixed repository name in the README template, and tracing premises in APPROACH.
- Claude mistakenly launched an empty agent while resuming the test, and it did nothing. A request to resend a message also paused the test agent mid-research until Claude released it.

## Decisions

- **Restructure without changing rules, verified phrase by phrase** — Claude, at Rob's direction.
- **Fix the create procedure only where the test was unambiguous, without merging** — Rob set the bar; Claude chose the six fixes.

## Lessons

- Fixing a simulated owner's answers before the run is what makes a create test meaningful. Answers written after seeing the questions would test the tester.
- The intended design's own class is the most direct route for a design into SCOPE. Assessing it generically, by what it requires, kept the pitched choices out.

## Open

- The create procedure's first pass is now tested by one intake, on a single-lobe project with a simulated owner. A multi-lobe intake and a real owner remain untested.

---

# Six review rounds, a settled test, and a four-brain dry run (2026-10-30)

**Session ID**: `c0b8b268-e845-4487-8346-f144ad51ce91`

Rob's session, with Claude as co-author. Rob ran `/code-review` on PR #18 repeatedly and had Claude fix each round. He then moved from review rounds to settling the toolkit's own test and dry-running the rules against real brains. The PR ended as one squashed commit that met a merge criterion Rob accepted: no rule misfiring on owner-approved content, no opposite verdicts between create and check, and nothing that stops an unattended run.

## Turn by turn

- **Rounds one to three.** Claude stashed the skill-install branch's uncommitted edits, switched to this branch, and fixed every reported issue, committing and pushing each round at Rob's direction. Round one found create and check contradicting each other on where shipped work goes, the enforced term "finding" used generically, and the toolkit's own SCOPE and APPROACH failing rules the PR added. Each later round found about ten more, a third of them caused by Claude's previous fixes. The count held at ten because the review caps its findings at ten by default.
- **Convergence.** Asked whether the review was converging, Claude said no. The review had become an audit of the whole toolkit against the PR's rules, and Claude had been settling the toolkit's premises, second approach and goals on Rob's behalf, the call the PR reserves for the owner. Asked which changes were churning, Claude measured the commits: procedure and template edits shrank each round and were never reversed, and the churn was in the toolkit's own SCOPE and APPROACH. Rob kept both in one PR, since the toolkit's own documents are the test bed for the pattern changes.
- **Settling the test.** Rob confirmed developers working through coding agents as a binding premise, chose wikis and second brains as the second approach over Claude's pick of automatic memory, and kept the owner-related goals as written. Mid-turn, Rob merged #17 and rebased this branch; the rebase overlapped nothing, and the stash was gone after the merge.
- **Squash and an uncapped review.** Rob had the PR squashed to one commit, and an uncapped review found 22 issues. Rob asked Claude to confirm every claim before changing anything. The top one held: the read-back and the pattern's dividing sentence had restored the positive test this item rejected after the lamarr re-author. Rob also redirected two terms. "Repository" means git, a fair premise for a developer audience, and a store is inherent to the concept rather than a design leak. Claude defined a knowledge store once in SCOPE as wherever a project's why is kept.
- **Confirming as a set.** Rob asked that the next round's claims be confirmed together, since edits applied one by one hide their interactions. Read together, several claims were one problem: create, check, the pattern and both dream cycles each checked a different subset of SCOPE's facts. Rob chose to fold copying and scaffolders into the curated-store class.
- **Scaling back.** The next review showed that Claude's widening of what dream cycles verify would stop unattended cycles on claims nothing can verify, and would send web checks to agents that cannot reach the web. At Rob's direction Claude scaled it back: create and check verify alternatives and evidence with a person present, and dream cycles verify only the systems in reach and list the rest as unverified.
- **PR description.** Rob had Claude check the description against the branch. Two claims were wrong, an overstated goal trace and an unmentioned intake item, and a Still open section was added.
- **Dry run.** Rob had Claude dry-run the rules by hand against lamarr-brain, virtual-view-brain and mini-nebula-brain. Mid-run he added an externally authored brain, mini-subtitle-wizard-brain, which Claude cloned to the scratchpad and only read. Eight places faltered. The worst two misfired on owner-approved scopes: defining an alternative as covering the whole problem misclassified partial options in three of the four brains, and the parent-choice qualifier left virtual-view's portfolio constraint, a parent choice made for no goal, fitting neither branch.
- **Rob's principles.** Rob answered with four:
  - an alternative is the next-best option, stating where it falls short
  - lobes align top-down: ancestors' SCOPE and APPROACH define the space a child inhabits, and changes ripple down
  - the check uses the latest definition, the second approach included
  - APPROACH honors SCOPE's premises and keeps its own assumptions without mirroring them

  Claude applied them, adding an approach check to CHECK, and re-ran the dry run, which met the merge criterion. Asked whether the round reduced the instructions, Claude measured it: 158 words net added, the approach check accounting for all of it, while four conditional rules became two principles.

## Decisions

- **One PR, with the toolkit's own documents as the test bed** — Rob.
- **The premise, wikis and second brains as the second approach, and the owner-related goals as written** — Rob.
- **Git as a premise and a defined knowledge store** — Rob's direction, Claude's wording.
- **Copying and scaffolders folded into the curated-store class** — Rob, on Claude's recommendation.
- **Dream cycles verify only the systems in reach** — Rob, on Claude's recommendation to scale back rather than add rotation and web agents to every brain.
- **Partial alternatives, top-down alignment, an approach check mirroring create, and premises honored by APPROACH** — Rob.
- **Parent overreach stays a defect corrected in the parent, its choice given to the child meanwhile** — Claude's default, accepted by Rob.
- **The merge criterion** — proposed by Claude, accepted by Rob.
- **Declined across rounds:** dropping the Author intake line, which the first log entry uses; unwrapping template comments, which predate the PR; and merging the SCOPE and APPROACH open questions, which ask different things.
- **Deferred:** one home for the definitions, as a follow-up work item; the toolkit's remaining wording issues, to the first dream cycle after merge.

## What didn't work

- Fixing findings one by one. Each round's fixes seeded about a third of the next round's findings, and Claude's choices for the toolkit's test were re-litigated every round until Rob settled them.
- Widening maintenance to verify every kind of SCOPE claim, which would have stopped unattended cycles. It was scaled back a round later.
- An install clause added to a goal to give a gap a home was itself a design leak, and came out the next round.

## Lessons

- A capped review always returns its cap. Only an uncapped run shows whether findings are shrinking.
- Settle the owner's test before reviewing the toolkit's own documents against the rules; otherwise every round tests the reviewer's guesses.
- Confirming review claims as a set catches the interactions that one-by-one fixes create.
- A dry run against real brains is a better merge gate than a review count, because it tests whether the rules work rather than whether the toolkit's own prose survives every rule.
- Conditional qualifiers are where rules misfire. Replacing them with general principles fixed the worst dry-run failures.

## Open

- One home for premise, choice, alternative and second approach, whose copies differ today.
- Re-gathering a scope under a kept status convention, and nothing prompting a child's revision when an ancestor changes.
- The toolkit's own wording issues listed in the PR, for the first dream cycle after merge.
- `backup/solution-neutrality-pre-squash` is still in this checkout.

---

# A historical and a blind dry run on lamarr (2026-10-30)

**Session ID**: `c0b8b268-e845-4487-8346-f144ad51ce91`

Rob's session, with Claude as co-author, continuing after the closeout entry above. Rob judged that further review would turn up wording issues that don't change interpretation, and asked for dry runs instead. Two runs tested the current check against lamarr-brain as it stood before Rob's hand restructure, the effort that started this work item. Both landed close to what Rob did, and between them they found two gaps in the check, both fixed.

## Turn by turn

- **The criterion.** Rob asked whether preferring dry runs and synthetic tests to abstract review was wrong. Claude agreed: a review checks the text against the rules, while a dry run checks whether the rules reach the owner's verdict on a real brain. Claude proposed blind runs by fresh agents and a set of synthetic brains with planted defects for a later testing work item.
- **Historical dry run.** Rob proposed comparing the check's recommendations on lamarr's pre-restructure state with what he actually did. Claude took the state just before the restructure, wrote 27 predictions before reading any later commit, and scored them against the hand restructure and the later check-guided commits.
  - Every move of the hand restructure matched a named rule, and the later commits covered the rest, so the check would have raised in one report what took four commits over five days.
  - The check went further in three places: the live check's second approach was recorded only in a commit message, no generic entry described the intended design's class, and the model was assumed without a stated reason.
  - It missed one thing. Lamarr's evidence paragraph was lost in a later word-collision fix, and the check never asks for evidence although the create procedure requires it. At Rob's direction Claude added that to the check's sufficiency step.
  - Claude flagged that it had read lamarr's current state earlier in the session, so two predictions might have been steered.
- **Blind check.** Rob asked for a fresh agent. Claude gave it only the procedure's files and an export of the pre-restructure commit, with no history, no toolkit repository and no web access. Claude wrote a simulated owner's answers from Rob's real decisions before the agent started, and relayed only those.
  - Before seeing an answer, the agent proposed the same second approach Rob's live check used.
  - It reproduced about 20 of the 27 predictions, including every design move of the hand restructure apart from the platform facts, which hinged on a premise the simulated answers left open.
  - It did not find the two goals Claude had flagged as possibly steered, which suggests they were.
  - It found three issues neither Rob nor Claude had: a disclosure requirement quoted in SCOPE that APPROACH's closing label never argues it meets, the owner's number restated in APPROACH as a choice, and a goal half with no answering decision.
  - It listed ten places the procedure was unclear. At Rob's direction Claude fixed two, a line each: commit references and decision dates count as status, and the approach check reads SCOPE as the design check's remedies would leave it.

## Decisions

- **Dry runs over further abstract review as the merge evidence** — Rob, with Claude agreeing.
- **Add evidence to the check's sufficiency step** — Rob, on Claude's recommendation from the historical run.
- **Fix two of the blind run's unclear points, one line each, and leave proportion to the testing work item** — Rob, on Claude's recommendation.
- **Leave lamarr-brain unchanged** — its next check should take up the evidence paragraph, the second approach, and the blind run's three new issues.

## Lessons

- A reviewer who knows the answer can't run a check blind. Writing predictions down before reading the history helps, but only a fresh agent with the history withheld shows which predictions were steered.
- Fixing a simulated owner's answers before the run, and relaying nothing else, keeps the tester's judgment out of a blind check.
- A dry run on a brain's own history is a direct test of a procedure: the owner's later fixes are the expected result.

## Open

- The blind run reported 33 issues item by item, despite the check's rule to report a section once when issues cover most of it. Proportion on a large scope stays an open issue for the testing work item.
- The blind run's remaining unclear points (identifiers in a platform vendor's code, by hand versus the status quo, holdings mentioned only implicitly in APPROACH, vendor-specific conditions, published patterns) belong with the definitions and testing work items.
- The blind-run setup can be rebuilt as a seed for synthetic testing: an export of lamarr's pre-restructure commit, the check's four files, and owner answers fixed from the owner's recorded decisions.
