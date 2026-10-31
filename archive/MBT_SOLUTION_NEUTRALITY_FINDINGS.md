# Solution-Neutral Scopes: Decision Record

## Problem

The create procedure asks for a solution-neutral SCOPE and then tells the author to fill the state of the problem with "what the platform or environment already provides and withholds" and "who has the problem and what they already hold." The comment on §2 of `templates/SCOPE.md` says the same. Those instructions presuppose a platform, and the only platform in view while authoring is the one the design will use.

`lamarr-brain` shows the result. Its seeded SCOPE opened with the owner's Mac, iPhone and accounts, then catalogued what macOS and Messages withhold, down to database fields and scripting grants. The alternatives the owner would actually weigh came last, as a table marked secondhand. The developer had to correct it: the state of the problem should assess the better-known alternatives and their complaints, the goals should answer those complaints, and reading SCOPE should let someone imagine a Twilio-based approach as easily as the Mac one. After the restructure, SCOPE led with ten categories of alternatives and kept only three conditions that bind every option. The platform facts moved to a new Platform section in APPROACH.

Four gaps in the toolkit let the seeded version through:

- **The neutrality test checks truth, not relevance.** The read-back pass asks whether a claim would still hold if the design had gone another way. A fact about a platform is true whatever gets built, so it passes. The question that catches it is whether a different approach would still need it.
- **The different-design test covers only goals.** The create procedure applies it to each goal and never to the state of the problem.
- **Displaced content has no home.** The APPROACH template has no section for facts about the chosen platform, so an author holding them puts them in the only section that asks for them.
- **The check cannot see it.** The status-drift check looks for version numbers and release status. An accurate, current catalogue of one platform's internals has neither, and passes.

The same session needed less correction on the APPROACH–FINDINGS boundary: duplicates, one contradiction, and four entries reasoning about unbuilt work. The developer observed that the toolkit's existing guidance holds this boundary better.

## Preferred approach: SCOPE holds premises, APPROACH holds choices

A choice is anything a reasonable designer of the problem could decide otherwise, however early it was made. What stays in SCOPE is what no designer could: the conditions every option faces, the evidence, and the premises the problem holder brings. Something the problem holder already has is a premise only when the problem requires every approach to use it. Only the problem holder can say which premises are theirs, so the author settles them with the user and states each in the problem statement. In `lamarr-brain`, the owner's one number is a premise, because clients know it. The Mac and the Claude subscription are choices, which is why the developer moved them to APPROACH.

The second approach makes the line visible. It is the reasonable alternative to the whole design that differs from it most while honoring the premises, and SCOPE assesses it among the alternatives. A sentence only the intended design needs is a choice. The test has to be concrete, because the seeded scope already claimed to be neutral; naming Twilio is what gave the developer's correction its force. A premise the two approaches share unstated, such as a model, goes untested, so it is tested against an alternative that does not share it.

The state of the problem leads with the alternatives, the status quo and doing it by hand among them. Goals answer the gaps those alternatives and the shared conditions leave, and they are stated so any approach can be judged against them. The second approach may fail a goal, since ruling approaches out is what goals are for.

The calibration brains showed one rule covers what looked like separate defects. These are a chosen platform presented as the world (lamarr's seeded scope, viewzoo's plugin interface), a boundary justified by what the design can test (VV's Trino-only exclusion), a problem framed by its answer (guardrails' "layer" that evaluates content, this toolkit's list of its own deliverables as the gap), and goals and open questions written in the design's terms (all five).

## Alternatives considered

- **Rename the heading to "State of the Market."** Rejected. It fits a product with commercial alternatives and misfits an internal library, and the check already treats a heading as cosmetic. The content rule does the work.
- **Rely on the read-back pass, with its question sharpened.** Rejected as the whole answer. A leak caught at read-back costs a rewrite of the section the scope leads with, as it did in `lamarr-brain`. The test belongs where the sentences are written, and the read-back pass keeps it as a second line.
- **Forbid platform facts in SCOPE outright.** Rejected. Some environment facts bind every approach and are part of the problem. The test admits them by what they constrain, not by what they describe.
- **A Platform section in APPROACH.** Rejected by the developer: not every project is a platform. The strategic approach opens with the choices SCOPE leaves open, including what the design builds on.
- **Require the second approach to satisfy every goal.** Rejected after the first dry runs. Goals exist to rule approaches out; the test that holds is whether a goal is stated in terms another design could be judged against.
- **Require every sentence to be one the second approach would also need.** Rejected after a blind re-author pushed group-chat degradation out of lamarr's scope, a condition most alternatives face. Only the negative form holds: a sentence only the intended design needs is a choice.
- **Narrow the status test to the project's own releases, and leave market figures free.** Rejected for figures. Alternatives are described by what they require and how they charge, which survives a price change, and a figure kept is dated.

## What the dry runs showed

- **Blind readers converge once the premises are settled first.** In round one, verdicts swung with the reader's choice of second approach. Once the check required listing the premises and confirming the second approach with the user, readers of the same scope agreed on which premises were the problem holder's and which were the design's.
- **A blind re-author reproduces the developer's correction.** Working from lamarr's seeded scope alone, it led with the alternatives and moved the Messages internals to APPROACH. Under the first draft it kept the owner's Mac and subscription as conditions; the premise rule moved them in the second draft.
- **The status check reached only one section.** Status hides in goal status lines, resolutions recorded under open questions, roadmap notes and clauses like "not yet".

## What this doesn't solve

- **The premises themselves.** The check surfaces them; only the problem holder can settle them, and a brain whose owner calls every holding a premise keeps its design in SCOPE.
- **Source material's own shape.** A design treatment organized around its design still pulls a scope toward it. The existing rule on source material addresses that, and this item leaves it unchanged.
