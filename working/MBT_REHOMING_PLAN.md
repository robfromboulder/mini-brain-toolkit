# Work-Item Re-homing: Implementation Plan

## Objective

Give component brains a safe correction path when a work item outgrows its owning unit: a setup-audit guard that prevents silent duplicate scaffolds, and a small re-homing procedure for moving an item's in-flight docs to the corrected owner. Dormant until the living multi-component prototype opens its first work items — the first live item is what makes the risk concrete.

## Context

See `MBT_REHOMING_FINDINGS.md` in this directory for the decision record and alternatives considered.

Key references in the mini-brain:
- `MBT_COMPONENTS.md` — token ownership and naming rules the move must preserve
- `MBT_FINDINGS.md` — relevant prior decisions
- `MBT_APPROACH.md` — design constraints

## What changes

- `templates/WORK_SETUP.md` — the audit searches every unit's `working/` for the slug before creating anything; a re-homing section covering the move, the token rename, and the branch declaration.
- Possibly the work-item scaffolds, if the first live item shows the wording needs it (see open issues).

## Interaction with existing code

| Existing doc | Interaction | Risk |
|---|---|---|
| `templates/SESSION_CLOSEOUT.md` | Routing signals resolve by slug and branch; both change in a re-home | A session mid-re-home routes to the old home |
| `templates/WORK_CLOSEOUT.md` | Retires items where they live | Closeout during a half-done re-home splits the docs |

## Testing approach

Simulate on a disposable copy of the prototype: scaffold an item in a child unit, re-home it to the parent, and verify the token rename is complete, re-running setup creates no duplicates, and the routing signals resolve to the new home.

## Implementation sequence

1. Land the setup-audit guard (independent of the rest).
2. Draft the re-homing section against the prototype's first live item.
3. Simulate the move end to end.

## Scope boundary — what this does NOT include

- Log-merge semantics — already pinned: merged entries land in the owner's canonical log.
- The component dream cycle and the migration holes (their own work items).

## Open issues

1. "The platform runbook" in the work-item scaffolds is flat-split vocabulary; in a component brain it loosely means the owning unit's canonical runbook. The scaffold hedges ("if the brain has one") — let the prototype's first work item show whether it needs sharper wording.
2. Whether re-homing lives as a section in work setup or earns its own maintenance document.
