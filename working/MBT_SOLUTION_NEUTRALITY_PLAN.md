# Solution-Neutral Scopes: Implementation Plan

## Objective

Make the create procedure produce a solution-neutral SCOPE on the first pass, so the problem statement never needs a developer's nudge to shed the chosen design. Deliver four things: a state-of-the-problem rule that leads with alternatives and admits only conditions binding every approach, a second-approach test applied while authoring, goals that answer the gaps the alternatives leave, and a check that catches a SCOPE that has drifted into design.

Landable now. The evidence is one brain, but the defect traces to the toolkit's own wording rather than to that brain's source material, so every brain seeded from the current rule is exposed to it.

## Context

See `MBT_SOLUTION_NEUTRALITY_FINDINGS.md` in this directory for the decision record and alternatives considered.

The evidence is `lamarr-brain`: its SCOPE as seeded from `MBT_CREATE_BRAIN.md` V24 (commit `62f5627`), the restructure that made it neutral (commit `88496f7`), and its session log entry for 2026-10-23, which records the developer's correction and the test that drove it.

## What changes

- `MBT_CREATE_BRAIN.md`, SCOPE rule on the state of the problem — the section leads with the alternatives a person with the problem would weigh: what each offers, its tradeoffs, and its chief complaints on cost, complexity, security and what it asks of the people involved. A fact about the environment stays only if it binds every plausible approach. Facts about a platform the design picks, and holdings that select which users the design targets, go to APPROACH. The status test stays as it is.
- `MBT_CREATE_BRAIN.md`, new SCOPE rule — before authoring, name one approach materially different from the intended one. Every sentence in SCOPE must be equally useful to a designer of either.
- `MBT_CREATE_BRAIN.md`, SCOPE rule on goals — each goal answers a gap or complaint the state of the problem names, and each gap the project takes on has a goal. Goals are ordered by impact on whoever has the problem.
- `MBT_CREATE_BRAIN.md`, read-back pass over the scopes — the question "would it still hold if the design had gone another way?" becomes "would a different approach still need it?"
- `MBT_CREATE_BRAIN.md`, APPROACH paragraph — its list of sections names the platform section below.
- `templates/SCOPE.md`, comments on §2 and §3 — mirror the revised rules.
- `templates/APPROACH.md` — an optional Platform section after the strategic approach: what the chosen platform requires, provides and withholds.
- `MBT_CHECK_BRAIN.md`, substance checks — a "SCOPE drifted into design" check beside the status-drift check. It applies the second-approach test to the state of the problem and the goals, and reports a section that fails as a rewrite.
- `MBT_PATTERN.md`, file-set description — the demarcation as two questions: whether a different approach could reuse a piece of content separates SCOPE from APPROACH, and whether it shaped the design separates APPROACH from FINDINGS.

## Interaction with existing docs

| Existing doc | Interaction | Risk |
|---|---|---|
| `MBT_CREATE_BRAIN.md` status rule | The status test and the relevance test guard different drifts and share one section | Merging them into one rule loses the status test, which still catches the changelog scope |
| `templates/SCOPE.md` comments | They restate the create procedure's rules | Changing one without the other is the divergence the dream cycle's teaching-artifact check exists to flag |
| `MBT_DREAM_CYCLE.md` and `templates/DREAM_CYCLE.md` | A market-led state of the problem carries prices and product claims that date | The dream cycle checks SCOPE against code and refreshes only APPROACH's external assumptions, so dated market figures in SCOPE go unrefreshed |
| `MBT_CHECK_BRAIN.md` status-drift check | A competitor's release changes market prose, which the status test reads as project status | The two checks contradict each other on every market-led scope unless the status test names the project's own releases |
| Brains seeded under the current rule | The new check flags their scopes | The check reports a rewrite that the brain's owner did not ask for and may not want |

## Testing approach

Re-seed `lamarr-brain`'s SCOPE and APPROACH from its archived design treatment in a fresh session that follows the revised procedure, with no developer nudging. Then run the revised check against the SCOPE at `62f5627`, the SCOPE at `88496f7`, and `MBT_SCOPE.md`.

Acceptance has four parts. The re-seeded SCOPE names no macOS or Messages internals and leads with the alternatives. Each of its goals traces to a gap it names. The check flags the scope at `62f5627` and passes the one at `88496f7`. The check also passes `MBT_SCOPE.md`, which shows the market framing does not misfire on a project without a commercial market.

## Implementation sequence

1. Revise the state-of-the-problem rule and add the second-approach test.
2. Revise the goals rule and the read-back question.
3. Mirror the rules into `templates/SCOPE.md`, and add the Platform section to `templates/APPROACH.md` and the APPROACH paragraph.
4. Add the check, and narrow the status test to the project's own releases.
5. Add the two-question demarcation to `MBT_PATTERN.md`.
6. Run the re-seed and the three check cases.

## Scope boundary — what this does NOT include

- Renaming the "State of the Problem" heading. "State of the Market" fits `lamarr-brain` but not an internal library, and the check already treats a heading as cosmetic.
- Rewriting scopes in existing brains. The check reports them, and their owners decide.
- The boundary between APPROACH and FINDINGS, beyond naming it in `MBT_PATTERN.md`.

## Open issues

1. Whether the Platform section belongs in the APPROACH template, where an unused section must be deleted, or only in the create procedure's APPROACH paragraph.
2. Whether the second approach must be written down, such as in the session log, or only named in the session. A written one makes the test auditable but adds an artifact nothing else reads.
3. Whether the dream cycle refreshes dated market claims in SCOPE, or whether a market section carries an "as of" date and is left to the check.
4. Whether the rule that untested reasoning about unbuilt work is an open question for the work item that will build it, rather than a finding, belongs in `templates/FINDINGS.md`, in `templates/WORK_CLOSEOUT.md`, or in a separate work item.
