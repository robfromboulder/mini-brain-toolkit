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
