# Multi-Lobe Dream Cycle: Implementation Plan

## Objective

Give the dream cycle a multi-lobe story: redesign `templates/DREAM_CYCLE.md` so every phase handles a multi-lobe brain, and make the cycle the lobe registry's assigned maintainer. No new document types, and no change to what single-lobe brains instantiate. Deliberately dormant until the living multi-lobe prototype accumulates real drift — the design is driven by observed rot, not anticipated rot.

## Context

See `MBT_MULTI_LOBE_DREAM_FINDINGS.md` in this directory for the decision record and alternatives considered.

Key references in the mini-brain:
- `MBT_LOBES.md` — the layer whose maintenance this designs
- `MBT_FINDINGS.md` — relevant prior decisions
- `MBT_APPROACH.md` — design constraints, including the dream cycle running unattended

## What changes

Stub until design begins, per the trigger below. Expected surface: `templates/DREAM_CYCLE.md` (per-lobe awareness in every phase), `MBT_LOBES.md` (its maintenance-documents paragraph promises a whole-brain dream cycle nothing redeems, and its one-problem-to-multi-lobe row tells the brain to treat its cycle as unadapted), `MBT_CREATE_BRAIN.md` (drop the don't-instantiate-unadapted caveat once the template earns it), `MBT_CHECK_BRAIN.md` (its procedure-drift check stops skipping a multi-lobe brain's dream cycle), `MBT_TESTING.md` (the scenario that expects that skip), and `templates/LOBES_CLAUDE.md` (its copy of the maintenance-documents paragraph).

## Interaction with existing code

| Existing doc | Interaction | Risk |
|---|---|---|
| `MBT_CHECK_BRAIN.md` | Shares the structural checks; the two must keep flagging the same things. Its procedure-drift check skips a multi-lobe brain's dream cycle because the template assumes one lobe | Divergent verdicts on the same brain; a skip that outlives its reason |
| `templates/WORK_CLOSEOUT.md` | Owns the event-driven Also-holds update this plan excludes | Registry maintenance falls between the two |

## Testing approach

Run the redesigned cycle against the living multi-lobe prototype and against a single-lobe exemplar for no-regression. Acceptance: structural checks cover every lobe, raise no false positives on child canonical files, and the registry pass catches a seeded stale routes-on term.

## Implementation sequence

1. Gather the real drift the prototype has accumulated.
2. Settle fan-out, budgets, and the tree-level/lobe-level split.
3. Rewrite the template; align spec and create procedure.
4. Run against both brain shapes.

## Scope boundary — what this does NOT include

- Work-item placement and cross-repository migrations, which are their own work items.
- The event half of Also-holds maintenance (one clause in the work-closeout walk).

## Open issues

1. Per-lobe fan-out agent budget at high lobe counts.
2. Whether the split test runs on cadence here or stays with the check procedure, run when a user asks.
3. Do all four doctypes earn their keep at the hub? Seeding creates them all so the grammar never promises a missing file, but a loosely-composing brain's hub SCOPE may have nothing to say that the child scopes don't — the prototype's own bootstrap plan expected its hub SCOPE to be the shortest in the brain. As of 2026-11-10 it is 69 lines against 58–71 for the three top-level children, which settles length and not whether it says anything theirs don't. If living hubs bear the doubt out, the grammar-never-lies invariant and every-claim-earns-its-keep pull against each other and need a ruling. Watch the prototype; don't pre-solve.
4. Cross-level reconciliation mechanics — what triggers a re-check of a hub finding.
5. Whether the trigger has fired. As of 2026-11-10 the prototype has closed work items in two lobes, open ones in the same two, and no dream cycle of its own.
6. Overlap with WORK_PLACEMENT: its owning-lobe derivation reads the registry's routing terms and nothing else, so the registry pass here is what keeps that derivation honest.
