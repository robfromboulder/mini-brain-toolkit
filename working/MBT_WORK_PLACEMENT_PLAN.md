# Work-Item Placement: Implementation Plan

## Objective

Settle which lobe owns a work item, at intake and after. Give work setup a method for deriving the owning lobe, so an item lands where the work's reach puts it rather than where the conversation started. Settle what happens when an item outgrows that lobe: it does not move, it retires as superseded and a successor opens in the correct lobe. Deliver a top-down derivation step in setup's intake section, a supersede retirement in work closeout, and a predecessor line in the FINDINGS scaffold. No move procedure.

Landable now — no depth requirement and no dormancy. The six-lobe prototype is enough to tell a defensible placement from an indefensible one, and every multi-lobe brain exercises this on every work item it opens.

## Context

See `MBT_WORK_PLACEMENT_FINDINGS.md` in this directory for the decision record and alternatives considered.

`MBT_LOBES.md` carries the three things the derivation depends on: the registry's routing terms it reads, the nearest-common-ancestor placement rule that setup's owning-lobe definition mirrors, and the lobespace-ownership constraint that bounds how high an item may sit and decides a successor's document names.

## What changes

- `templates/WORK_SETUP.md`, intake step — the owning-lobe bullet becomes a derivation: name the lobes the work will concern by matching it against the registry's routing terms, then walk up to their nearest common ancestor. It states that an item stays in its opening lobe for life, and that a corrected owner means opening a successor that names its predecessor. The sentence that a brain with one lobe skips the step stays.
- `templates/WORK_CLOSEOUT.md`, retire step — a second retirement reason: superseded rather than concluded. Archive the working documents without folding what they hold, merge the log entries as normal, and record the successor's slug.
- `templates/work/FINDINGS.md` — a predecessor line, filled only when the item supersedes another.

## Interaction with existing docs

| Existing doc | Interaction | Risk |
|---|---|---|
| `templates/WORK_SETUP.md` audit step | It reads the owning lobe's `working/` and never `archive/` | A retired predecessor is invisible to setup, so a successor whose intake conversation omits it is scaffolded with no link back and the predecessor's reasoning is silently orphaned |
| `templates/WORK_SETUP.md` alignment step | It reads the PLAN and FINDINGS of open items in the lobes the work concerns, the owning lobe and its ancestors, so it reaches a predecessor only while that item is still in `working/` | Whether alignment sees the predecessor depends on the order of the two steps, which nothing fixes |
| `templates/WORK_CLOSEOUT.md` | Its target walk and fold run before its retire step, and a supersede retirement skips both for everything but the log | A reader follows the standard flow and folds an unsettled item's decisions into canonical documents |
| `MBT_LOBES.md` | The registry's routing terms are the derivation's only input, and a supersession applies the nearest-common-ancestor rule again with better information | Stale routing terms silently misplace every item opened against them, with no signal that anything went wrong |
| `templates/SESSION_CLOSEOUT.md` | It routes a session part by part, sends a part owned by an item closing in that session to the owning lobe's canonical log, and states a decision spanning several items once | None expected: a session spanning a supersession splits into the predecessor's parts and the successor's. The simulated supersession confirms it |
| `MBT_TESTING.md` | Its work-setup and work-closeout scenarios test the two procedures this item changes | The scenarios pass on the old behavior and say nothing about the new |

## Testing approach

**Derivation.** Run intake against a disposable copy of the six-lobe prototype for three shaped cases: work belonging clearly to one lobe, work spanning two siblings, and work spanning two subtrees. Acceptance: each case lands on the lobe the nearest-common-ancestor rule names, and no case requires opening a lobe's documents to decide.

**Supersession.** Simulate one on the multi-lobe fixture `tests/MBT_SEED_FIXTURE.py --lobes` seeds — a hub and two child lobes are enough, since the policy has no ancestor walk to exercise. Open an item in a child lobe, supersede it into the hub, and verify four things: nothing the archived documents hold was folded into a canonical document, the successor's FINDINGS names its predecessor, the predecessor's log entries landed in the *original* owner's canonical log under their original session IDs, and the session's own entries landed where session closeout routes them — the predecessor's part in its lobe's canonical log, since that item closed in the session, and the successor's part in its working log.

Then run the check procedure on the result; acceptance is a clean structural pass with both items visible in their respective lobes.

At closeout the cases worth repeating join `MBT_TESTING.md` as scenarios.

## Implementation sequence

1. Draft the derivation step against the prototype's registry, and state the stays-for-life policy beside it.
2. Add the supersede retirement to work closeout's retire step.
3. Add the predecessor line to the FINDINGS scaffold.
4. Run the three intake cases.
5. Simulate a supersession end to end and run the check procedure.

## Scope boundary — what this does NOT include

- Any move procedure. The policy exists to remove the need for one.
- Knowledge placement at closeout, which is settled and unaffected by where an item lived.
- The registry's own upkeep — routing terms going stale is the dream cycle's problem, not this derivation's.
- The multi-lobe dream cycle and cross-repository migrations, which are their own work items.

## Open issues

1. Whether the derivation is prose the agent follows or an explicit checklist it walks.
2. How hard the procedure should push back when the answer comes out at the hub. That is a legitimate result for genuinely cross-cutting work and also the exact signature of an inflated walk, and the procedure cannot tell them apart from the answer alone.
3. Which comes first, opening the successor or retiring the predecessor. Opening first lets setup's alignment step read the predecessor's PLAN and FINDINGS while they are still in `working/`; retiring first leaves the intake conversation as the only carrier.
4. Whether a superseded item's PLAN and FINDINGS are archived as they stand or get a closing note saying why they stopped.
5. Whether an item superseded before it produced anything worth keeping is archived at all, or is a scaffold that should simply be removed — against the standing move-don't-delete convention.
6. Whether the successor inherits the predecessor's branch declaration or declares its own.
7. `templates/WORK_CLOSEOUT.md` already uses *supersede* for a knowledge-edit classification — reconcile-supersede against append-log. Adding a superseded *retirement reason* to the same document gives one word two meanings in one place. Either the retirement reason takes a different name, or both uses are disambiguated where they appear.
8. Overlap with MULTI_LOBE_DREAM: this derivation trusts the registry's routing terms, and that item is what keeps them fresh. Until it lands, nothing maintains the derivation's only input.
