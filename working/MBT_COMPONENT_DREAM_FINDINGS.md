# Component Dream Cycle: Decision Record

## Problem

The dream cycle is the one lifecycle workflow with no component story, and the one where component brains differ most from flat ones. `templates/DREAM_CYCLE.md` assumes a single unit in every phase: its structural checks sweep top-level `*.md` and `working/` only, so in a component brain they audit the hub's documents and silently skip every component's; its filename-leakage check treats "listed in the read index" as the definition of a legitimate mention, which flags every component canonical file by construction; its scope-verification phase checks one SCOPE against one codebase, where a component brain has one SCOPE per unit and a project repo per registry row; and its extraction phase reads one LOG/FINDINGS pair, where a component brain has one per unit. Component brains also add a rot class the flat pattern never had: a hub finding about how two units interact can be invalidated by a change inside either unit, and no per-unit pass looks upward.

Compounding this, the component registry is canonical content with no assigned maintainer: routes-on terms go stale as units evolve, the Also-holds cell must change when a unit gains a document beyond the doctype set, and the Project-repo cell when a repo appears or moves. Routing quality is the whole cold-start story, and the dream cycle is its natural cadence home. Until this work lands, `MBT_CREATE_BRAIN.md` warns against instantiating the dream-cycle template unadapted into a component-structured brain.

## Preferred approach: design against a living brain

Design the component dream cycle against a living multi-component brain, not on paper — the shape of real drift should drive the phases. The design must settle:

- **Per-unit fan-out and its agent budget** — which passes run per unit, and what that costs at ten or thirty units.
- **Tree-level vs unit-level checks** — which checks run once over the tree (registry ↔ disk, unit references) versus per unit (scope verification, extraction).
- **Cross-level reconciliation** — the pass that re-checks hub findings about unit interactions against changes inside those units.
- **Registry maintenance on cadence** — routes-on freshness, Also-holds accuracy, Project-repo validity.
- **Whether the split test runs here on cadence** — the port-tell in `MBT_COMPONENTS.md`; the check procedure runs it only on request, and the cycle is the natural place for it to recur.
- **The dream log stays at the hub** — one per brain, like every maintenance document.

## Alternatives considered

- **Sentence-patching the existing template per check** — rejected: fan-out, agent budgets, and cross-level reconciliation are new machinery, not wording; patching would ship a cycle that reads component-aware and audits one unit.

## What this doesn't solve

- The event-driven half of registry maintenance (a work closeout that adds a document beyond the doctype set updates the Also-holds cell) belongs to the work-closeout walk, not the cycle.
