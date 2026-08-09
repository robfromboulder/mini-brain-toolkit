# Work-Item Placement: Implementation Plan

## Objective

Give work setup a method for deriving the owning unit, so an item lands where the work's reach puts it rather than where the conversation started. Deliver a top-down derivation step in the intake section, and fold the search for an existing item into that walk.

Landable now — no depth requirement and no dormancy. The six-unit prototype is enough to tell a defensible placement from an indefensible one, and every component brain exercises this on every work item it opens.

## Context

See `MBT_WORK_PLACEMENT_FINDINGS.md` in this directory for the decision record and alternatives considered.

`MBT_COMPONENTS.md` carries the three things the walk depends on: the registry's routing terms it reads, the nearest-common-ancestor rule it applies, and the token-ownership constraint that bounds how high an item may sit.

## What changes

- `templates/WORK_SETUP.md`, intake step — the owning-unit bullet becomes a derivation: name the units the work will concern by matching it against the registry's routing terms, then walk up to their nearest common ancestor.
- `templates/WORK_SETUP.md`, audit step — the audit searches the tree by slug rather than one unit by token, and reports a match in another unit as a probable predecessor rather than as an error.

## Interaction with existing docs

| Existing doc | Interaction | Risk |
|---|---|---|
| `templates/WORK_SETUP.md` audit step | Its pattern anchors on the owner's token, not the slug | A tree-wide search that keeps the token anchor still misses every doc filed under a different owner's token, and looks like it passed |
| `MBT_COMPONENTS.md` | The registry's routing terms are the walk's only input | Stale routing terms silently misplace every item opened against them, with no signal that anything went wrong |
| `templates/WORK_CLOSEOUT.md` | A predecessor the audit finds is the other half of the supersede path | The link gets recorded at setup and nothing consumes it at closeout |

## Testing approach

Run intake against the six-unit prototype for three shaped cases: work belonging clearly to one component, work spanning two siblings, and work spanning two subtrees. Then plant a same-slug item in an unrelated unit and run a fourth.

Acceptance is three things: each case lands on the unit the nearest-common-ancestor rule names, no case requires opening a unit's documents to decide, and the planted item is surfaced as a probable predecessor.

## Implementation sequence

1. Draft the derivation step against the prototype's registry.
2. Rework the audit to search by slug and report predecessors.
3. Run the three intake cases and the planted-slug case.

## Scope boundary — what this does NOT include

- What happens when a placement turns out wrong, which is the relocation item.
- Knowledge placement at closeout, which is settled and unaffected by where an item lived.
- The registry's own upkeep — routing terms going stale is the dream cycle's problem, not this walk's.

## Open issues

1. Whether the derivation is prose the agent follows or an explicit checklist it walks.
2. How hard the procedure should push back when the answer comes out at the hub. That is a legitimate result for genuinely cross-cutting work and also the exact signature of an inflated walk, and the procedure cannot tell them apart from the answer alone.
3. Whether a single-unit brain skips the step entirely or reads one sentence confirming there is nothing to derive.