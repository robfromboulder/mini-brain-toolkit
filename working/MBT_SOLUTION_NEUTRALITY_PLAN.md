# Solution-Neutral Scopes: Implementation Plan

## Objective

Tighten the instructions that divide SCOPE from APPROACH, so the create procedure produces a solution-neutral SCOPE on the first pass and the check procedure catches a SCOPE that carries its design's choices. Then run the revised check against every existing brain and improve each one's SCOPE/APPROACH split with its owner.

The standard is the better line, not the common denominator of the brains it was calibrated on: every one of them fails the revised check somewhere.

## Context

See `MBT_SOLUTION_NEUTRALITY_FINDINGS.md` in this directory for the decision record and alternatives considered.

The evidence is `lamarr-brain`: its SCOPE as seeded under `MBT_CREATE_BRAIN.md` V24 (commit `62f5627`), the developer's restructure (commit `88496f7`), and its session log entry for 2026-10-23. The calibration set is `virtual-view-brain`, `lamarr-brain`, `mini-nebula-brain`, `mini-guardrails-brain` and this toolkit.

## What changes

- `MBT_CREATE_BRAIN.md`, the SCOPE paragraph:
  - **Definitions.** Choices and premises are defined: a choice is anything a reasonable designer could decide otherwise. A premise is something the problem holder brings, and something they already have is a premise only when the problem requires every approach to use it.
  - **Premises.** Premises are settled with the user and stated in the problem statement.
  - **The second approach.** It is named before writing: the most different alternative to the whole design that honors the premises, assessed in SCOPE. A premise it shares with the intended design is tested against an alternative that does not share it.
  - **Seven rules:**
    - The state of the problem leads with the alternatives, the status quo and doing it by hand among them, described by structure and dated where they carry figures.
    - Status has no place in any section of SCOPE.
    - Every boundary carries the problem's reason.
    - Goals answer gaps and are stated in terms any approach can be judged against.
    - Open questions are about the problem.
    - Source material carries its own shape (kept as is).
    - Evidence is reported at its strength (kept as is).
- `MBT_CREATE_BRAIN.md`, the rest:
  - **APPROACH.** It opens with the choices SCOPE leaves open, argues against the alternatives SCOPE assesses with the second approach among them, and states undecided decisions as open.
  - **Read-back pass.** It asks whether that scope's second approach would still need each claim.
  - **Closeout.** The closeout's LOG entry records the second approach.
- `MBT_CHECK_BRAIN.md`:
  - **Status drift.** The check reaches every section and names status's hiding places. It defines "the project" and reports status as a deletion.
  - **New check: "SCOPE drifted into design".** It runs in three steps: settle the premises and the second approach with the user, read as that approach's designer, then read for sufficiency. It names its remedies (delete, move, rewrite, reorder, add, user), and the report section names the new failure.
- `templates/SCOPE.md` and `templates/APPROACH.md`: the comments mirror the rules.
- `MBT_PATTERN.md`, the file-set description: what divides SCOPE from APPROACH is whether a different approach could reuse a piece of content.

## Interaction with existing docs

| Existing doc | Interaction | Risk |
|---|---|---|
| `MBT_CREATE_BRAIN.md` status rule | Kept, widened to every section, and keyed to this project's releases | A market-led scope reads competitors' changes as status unless the test names the project |
| `templates/SCOPE.md` comments | They restate the create procedure's rules | Changing one without the other is the divergence the dream cycle's teaching-artifact check exists to flag |
| `MBT_DREAM_CYCLE.md` and `templates/DREAM_CYCLE.md` | A market-led state of the problem carries claims about other products | Structural description and dated figures keep them from going stale unseen; the dream cycle is unchanged |
| Brains seeded under the current rules | Every calibration brain fails the new check somewhere | Its owner decides each finding; nothing is rewritten unasked |

## Testing approach

Blind dry runs in scratch copies, by fresh agents that see only the procedure and the target, iterated until the critiques stop changing the verdicts:

- **Check runs** against all five brains, with lamarr at both `62f5627` and HEAD.
- **Re-author runs** of lamarr from its seeded SCOPE and APPROACH, and of the VV hub.

Acceptance:
- The check flags lamarr at `62f5627` for the same moves the developer made at `88496f7`, including leading with the alternatives.
- A blind re-author of lamarr moves the platform internals and the owner's holdings to APPROACH, and leads with the alternatives.
- Readers of the same scope agree on the premises to put to the user and on the shape of the verdict.

## Implementation sequence

1. Revise the create rules, templates and pattern sentence. Done, three drafts.
2. Revise the status check and add the design check. Done, three drafts.
3. Dry-run each draft blind and fold in the critiques. Done, three rounds.
4. Run the check cycle against each brain with its owner, as `MBT_CHECK_BRAIN.md` describes, and make the changes the owner approves. Done for the toolkit and the two project brains whose owner took the changes; the other calibration brains served as dry-run targets only.

## Scope boundary — what this does NOT include

- **A Platform section in APPROACH.** Not every project is a platform; the strategic approach states what the design builds on.
- **The APPROACH–FINDINGS boundary.** Deferred to a separate item, along with whether untested reasoning about unbuilt work belongs in FINDINGS.
- **Renaming the "State of the Problem" heading.**
- **Rewriting existing scopes without their owners.**

## Open issues

1. Whether the check's per-passage findings stay proportionate on a large scope. Nebula and guardrails each produce more than ten groups.
2. Whether ordering goals by impact earns its place when the evidence cannot rank them.
