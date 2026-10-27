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

## Preferred approach: lead with alternatives, and test relevance against a second approach

The state of the problem describes what a person with the problem would weigh: the alternatives, their tradeoffs, and their chief complaints. A fact about the environment earns a place only when it binds every plausible approach. In `lamarr-brain`, those were group chats degrading to their least capable member, spoofable identity outside iMessage, and the expectation that AI discloses itself. Every one of them binds a Twilio design as much as a Mac design.

The second-approach test enforces this. The author names one approach materially different from the intended one before writing. Each sentence must serve a designer of either. The test has to be concrete, because "solution-neutral" in the abstract is what the seeded version already claimed to be. Naming an actual second approach is what gave the developer's correction its force.

Goals then answer the gaps. The alternatives' complaints are the reason the project exists, so a goal that answers none of them, or a gap the project takes on with no goal, is a defect visible only when the two sections are read against each other. Ordering goals by impact on whoever has the problem keeps that reading honest.

## Alternatives considered

- **Rename the heading to "State of the Market."** Rejected. It fits a product with commercial alternatives and misfits an internal library, and the check already treats a heading as cosmetic. The content rule does the work.
- **Rely on the read-back pass, with its question sharpened.** Rejected as the whole answer. A leak caught at read-back costs a rewrite of the section the scope leads with, as it did in `lamarr-brain`. The test belongs where the sentences are written, and the read-back pass keeps it as a second line.
- **Forbid platform facts in SCOPE outright.** Rejected. Some environment facts bind every approach and are part of the problem. The test admits them by what they constrain, not by what they describe.

## What this doesn't solve

- **Choosing the second approach.** A strawman second approach passes everything. The test depends on the author naming one that a reasonable designer would pursue.
- **Source material's own shape.** A design treatment organized around its design still pulls a scope toward it. The existing rule on source material addresses that, and this item leaves it unchanged.
