# Work-Item Placement: Decision Record

## Problem

The owning-unit rule is blast radius; nothing enacts it. Work setup defines the owning unit as the nearest common ancestor of the units the work will concern, then tells the reader to settle it first and moves on without a method — no walk, no enumeration, no prompt to consider units the intake conversation has not already named. What the procedure actually produces is the unit the conversation was sitting in: inception point, not reach.

That was tolerable while a wrong placement had a cheap correction. It no longer does. Correcting an owner now means retiring the item and re-authoring it in its new home, so intake is the cheap moment and the only one.

## Preferred approach: derive the owner top-down, from the registry

Placement starts at the root and works down: name the units the work will concern by matching it against the registry's routing terms, then walk up to their nearest common ancestor. It never starts from whichever unit the conversation is already in.

Three constraints the derivation has to respect:

- **Read the registry, not the units.** The routing terms exist so a session can choose a component before reading anything. A walk that opens each unit to judge relevance re-imports precisely the cost the component layer was built to shed, and gets worse with depth.
- **Will, not could.** Almost any work *could* touch any unit, so a top-down prompt phrased as "could this reach X?" drifts every item toward the hub. The rule already says *will concern*; the procedure has to hold that line explicitly or the walk inflates.
- **Over-placement has a specific cost.** An item sitting at a unit whose token is a prefix of its children's is next to the naming trap, where a slug that continues into a child's token hands the item's files to that child. Placing too high is not merely untidy.

The search for an existing item falls out of the walk rather than needing its own guard: a traversal already covering the tree surfaces a same-slug item wherever it lives, and reports it for linking.

## Alternatives considered

- **Leave placement to the intake conversation and correct afterward.** Rejected: there is no cheap correction to fall back on, so the cost lands on a path that has to re-author two documents.
- **A standalone audit guard on the setup audit.** Rejected as the answer: it catches a duplicate scaffold at the moment placement has already gone wrong, and it performs a traversal the derivation walk performs anyway. Worth doing only as part of the walk.

## What this doesn't solve

- **Mis-predicted reach.** A better-informed decision at intake is still a prediction; work whose scope grows mid-flight still needs the relocation path.
- **Knowledge placement**, which closeout settles by reach when the item concludes, independent of where the item lived.