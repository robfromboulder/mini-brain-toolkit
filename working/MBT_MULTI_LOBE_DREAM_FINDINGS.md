# Multi-Lobe Dream Cycle: Decision Record

## Problem

The dream cycle is the one lifecycle workflow with no multi-lobe story, and the one where multi-lobe brains differ most from single-lobe ones. `templates/DREAM_CYCLE.md` assumes a single lobe in every phase: its structural checks sweep top-level `*.md` and `working/` only, so in a multi-lobe brain they audit the hub's documents and silently skip every child's; its scope-verification phase checks one SCOPE against one codebase, where a multi-lobe brain has one SCOPE per lobe and a project repo per registry row; and its extraction phase reads one LOG/FINDINGS pair, where a multi-lobe brain has one per lobe. Multi-lobe brains also add a rot class a single-lobe brain never had: a hub finding about how two lobes interact can be invalidated by a change inside either lobe, and no per-lobe pass looks upward.

Compounding this, the lobe registry is canonical content with no assigned maintainer: routes-on terms go stale as lobes evolve, the Also-holds cell must change when a lobe gains a document beyond the doctype set, and the project-repo cell when a repo appears or moves. Routing quality is the whole cold-start story, and the dream cycle is its natural cadence home. Until this work lands, `MBT_CREATE_BRAIN.md` warns against instantiating the dream-cycle template unadapted into a multi-lobe brain, and `MBT_LOBES.md` tells a brain that becomes multi-lobe to treat its existing cycle as unadapted.

## Preferred approach: design against a living brain

Design the multi-lobe dream cycle against a living multi-lobe brain, not on paper — the shape of real drift should drive the phases. The design must settle:

- **Per-lobe fan-out and its agent budget** — which passes run per lobe, and what that costs at ten or thirty lobes.
- **Tree-level vs lobe-level checks** — which checks run once over the tree (registry ↔ disk, cross-lobe references) versus per lobe (scope verification, extraction).
- **Cross-level reconciliation** — the pass that re-checks hub findings about lobe interactions against changes inside those lobes.
- **Registry maintenance on cadence** — routes-on freshness, Also-holds accuracy, project-repo validity.
- **Whether the split test runs here on cadence** — the port tell in `MBT_LOBES.md`. The check procedure runs it only when a user asks for a check, and the cycle is the natural place for it to recur. The cycle runs unattended, so it can only surface a port as a needs-human-decision item; the split itself stays the user's call.
- **One decision list at any size** — every per-lobe judgment call lands in the cycle log's single needs-human-decision list, which at thirty lobes needs a shape a reader can act on.
- **The dream log stays at the hub** — one per brain, like every maintenance document.

## Alternatives considered

- **Sentence-patching the existing template per check** — rejected: fan-out, agent budgets, and cross-level reconciliation are new machinery, not wording; patching would ship a cycle that reads multi-lobe-aware and audits one lobe.

## What this doesn't solve

- The event-driven half of registry maintenance (a work closeout that adds a document beyond the doctype set updates the Also-holds cell) belongs to the work-closeout walk, not the cycle.
