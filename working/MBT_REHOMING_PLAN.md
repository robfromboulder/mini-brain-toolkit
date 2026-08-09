# Work-Item Relocation: Implementation Plan

## Objective

Settle what happens when a work item outgrows the unit it was opened in: it does not move. The item retires as superseded and re-opens in the correct unit. Deliver the policy statement and the one procedure change it needs — a supersede retirement in work closeout.

Landable whenever wanted. It needs no living example and no particular hierarchy depth, because it removes a procedure rather than adding one — there is no ancestor walk to get wrong and no token rename to verify.

## Context

See `MBT_REHOMING_FINDINGS.md` in this directory for the decision record and alternatives considered.

`MBT_COMPONENTS.md` carries the placement rule a supersession corrects, and the token-ownership rules that decide the successor's document names.

## What changes

- `templates/WORK_CLOSEOUT.md` — a second retirement reason in its retire step: superseded rather than concluded. Archive the working documents without folding their findings, merge the log entries as normal, and record the successor's slug.
- `templates/WORK_SETUP.md` — the intake step states that an item stays in its opening unit for life and that a corrected owner means opening a successor. The audit reports a same-slug item in another unit as a probable predecessor rather than as an error.
- `templates/work/FINDINGS.md` — a predecessor line, filled only when the item supersedes another.

## Interaction with existing docs

| Existing doc | Interaction | Risk |
|---|---|---|
| `templates/WORK_SETUP.md` | Setup runs twice for one line of work — once for the item, once for its successor | The successor is scaffolded as a fresh item with no link back, and the predecessor's reasoning is silently orphaned |
| `MBT_COMPONENTS.md` | Its intake rule settles the owning unit; a supersession is that rule being applied again with better information | The policy reads as licensing careless first placement, when it makes good placement worth more |
| `templates/SESSION_CLOSEOUT.md` | A session that spans the supersession concerned both units | Its entry routes to the successor's unit by default rather than to the ancestor its work actually reached |

## Testing approach

Simulate one supersession on a disposable copy of a two-level component brain — no fixture tree is needed, since the policy has no ancestor walk to exercise. Open an item in a child unit, supersede it into the parent, and verify four things: the archived documents kept their findings unfolded, the successor names its predecessor, the log entries landed in the *original* owner's canonical log under their original session IDs, and setup at the new home reports the predecessor rather than a clean slate.

Then run the check procedure on the result; acceptance is a clean structural pass with both items visible in their respective units.

## Implementation sequence

1. State the policy in work setup's intake step.
2. Add the supersede retirement to work closeout's retire step.
3. Add the predecessor line to the FINDINGS scaffold.
4. Simulate a supersession end to end and run the check procedure.

## Scope boundary — what this does NOT include

- Any move procedure. The policy exists to remove the need for one.
- How intake derives the owning unit in the first place.
- The component dream cycle and cross-repository migrations, which are their own work items.

## Open issues

1. Whether a superseded item's PLAN and FINDINGS are archived as they stand or get a closing note saying why they stopped.
2. Whether an item superseded before it produced any findings is worth archiving at all, or is a scaffold that should simply be removed — against the standing move-don't-delete convention.
3. Whether the successor inherits the predecessor's branch declaration or declares its own.
4. `templates/WORK_CLOSEOUT.md` already uses *supersede* for a knowledge-edit classification — reconcile-supersede against append-log. Adding a superseded *retirement reason* to the same document gives one word two meanings in one place, which is the defect shape a prior review caught in the maintenance templates. Either the retirement reason takes a different name, or both uses are disambiguated where they appear.