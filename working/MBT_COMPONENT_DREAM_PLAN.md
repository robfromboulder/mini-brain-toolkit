# Component Dream Cycle: Implementation Plan

## Objective

Give the dream cycle a component story: redesign `templates/DREAM_CYCLE.md` so every phase handles a multi-unit brain, and make the cycle the component registry's assigned maintainer. No new document types, and no change to what single-unit brains instantiate. Deliberately dormant until the living multi-component prototype accumulates real drift — the design is driven by observed rot, not anticipated rot.

## Context

See `MBT_COMPONENT_DREAM_FINDINGS.md` in this directory for the decision record and alternatives considered.

Key references in the mini-brain:
- `MBT_COMPONENTS.md` — the layer whose maintenance this designs
- `MBT_FINDINGS.md` — relevant prior decisions
- `MBT_APPROACH.md` — design constraints

## What changes

Stub until design begins, per the trigger below. Expected surface: `templates/DREAM_CYCLE.md` (per-unit awareness in every phase), `MBT_COMPONENTS.md` (its maintenance-documents paragraph currently promises a whole-brain dream cycle nothing redeems), and `MBT_CREATE_BRAIN.md` (drop the don't-instantiate-unadapted caveat once the template earns it).

## Interaction with existing code

| Existing doc | Interaction | Risk |
|---|---|---|
| `MBT_CHECK_BRAIN.md` | Shares the structural checks; the two must keep flagging the same things | Divergent verdicts on the same brain |
| `templates/WORK_CLOSEOUT.md` | Owns the event-driven Also-holds update this plan excludes | Registry maintenance falls between the two |

## Testing approach

Run the redesigned cycle against the living component prototype and against a single-unit exemplar for no-regression. Acceptance: structural checks cover every unit, raise no false positives on component canonical files, and the registry pass catches a seeded stale routes-on term.

## Implementation sequence

1. Gather the real drift the prototype has accumulated.
2. Settle fan-out, budgets, and the tree-level/unit-level split.
3. Rewrite the template; align spec and create procedure.
4. Run against both brain shapes.

## Scope boundary — what this does NOT include

- Work-item re-homing (its own work item).
- The restructuring migration holes (their own work item).
- The event half of Also-holds maintenance (one clause in the work-closeout walk).

## Open issues

1. Per-unit fan-out agent budget at high unit counts.
2. Whether the split test runs on cadence here or stays on-request in the check procedure.
3. Do all four doctypes earn their keep at the hub? Seeding creates them all so the grammar never promises a missing file, but a loosely-composing brain's hub SCOPE may have nothing to say that the component scopes don't — the prototype's own bootstrap plan doubts its own. If living hubs bear that out, the grammar-never-lies invariant and every-claim-earns-its-keep pull against each other and need a ruling. Watch the prototype; don't pre-solve.
4. Cross-level reconciliation mechanics — what triggers a re-check of a hub finding.
