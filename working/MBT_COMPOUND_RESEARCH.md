# Component Layer: Research

The open design work, decisions, and questions for the component layer — `MBT_COMPONENTS.md` and the templates that enact it, on branch `component-brains`. 2026-07-31, Rob's direction, Claude (Fable 5) as author. Working doc — unversioned, point-in-time; supersede rather than maintain.

The layer has had zero live executions: every confidence score below is prior to first contact, and the overarching next step is to **seed the virtual-view-brain** (`../virtual-view-brain/VV_BOOTSTRAP_PLAN.md`) as the living test. The seeding path — spec, create procedure, entrypoint template, session closeout, work bookends, project hook — is ready. The seed's acceptance test is the round trip: load the brain from each project repo, confirm the registry routes correctly, and confirm a session lands in the right unit without reading the others.

## Confidence by area

Confidence per the toolkit's idiom: a proxy for remaining unknowns; below ~70 means design or fix before trusting.

| Area | Confidence | What caps it |
|---|---|---|
| Backwards compat & simple-brain cost | 93 | Exemplars untouched and valid; single-unit brains carry a few dormant guarded sentences and one runtime variable |
| Core model (units, recursion, opt-in layering) | 90 | Zero live executions |
| VV structure as canonical exemplar | 85 | The hub-SCOPE thinness question below is its one open doubt |
| Entrypoint (grammar, registry, routing) | 85 | The registry has no assigned maintainer |
| Placement & log routing | 85 | Hub accretion is a real risk with no stated boundary of applicability |
| Naming & token ownership | 85 | The naming guardrails are advisory at naming time; detection happens at check time |
| Session closeout | 85 | Zero live executions in a multi-log brain |
| Work setup / closeout | 80 | No re-homing path when an item outgrows its owner |
| Restructuring migrations | 70 | The collapse and extraction moves each have an unresolved hole |
| Dream cycle | 45 | The template is single-unit; the component design is unwritten |

## Open items

**1. Design the component dream cycle.** The one workflow with no component story, and the one where component brains differ most from flat ones. `templates/DREAM_CYCLE.md` assumes a single unit throughout: its structural checks sweep top-level `*.md` only (in the virtual-view-brain they would audit the hub's seven files and silently skip the other twenty); its filename-leakage check treats "listed in the read index" as the definition of a legitimate mention, which flags every component canonical file by construction; its scope-verification phase checks one SCOPE against one codebase, where a component brain has one SCOPE per unit and a project repo per registry row; and its extraction phase reads one LOG/FINDINGS pair, where a component brain has one per unit plus a class of rot the flat pattern never had — a hub finding about how two units interact, invalidated by a change inside either unit, that no per-unit pass looks up to see. Design decisions the cycle needs: per-unit fan-out and its agent budget; which checks run per unit versus once over the tree; cross-level reconciliation; whether the split test (the port-tell in `MBT_COMPONENTS.md`) runs here on cadence, since the check procedure runs it only on request; and the dream log staying at the hub. Design it against a living VV, not on paper — the shape of real drift should drive the phases.

**2. Work-item re-homing.** The owning unit is settled at intake as the nearest common ancestor of the units the work *will* concern — a prediction. When mid-flight scope growth invalidates it (an agent-owned item turns out to need mcp changes, so the owner should have been `viewmapper/`), there is no move procedure: re-homing means `git mv` plus a token rename across every doc plus the runbook's branch declaration, and nothing says so. Worse, re-running work setup with the corrected owner silently scaffolds a duplicate, because the setup audit lists only the new owner's directories. Needs either a small re-homing procedure or, at minimum, a setup-audit rule that searches other units' `working/` for the slug before creating anything.

**3. Registry maintenance.** The component registry is canonical content with no assigned maintainer. Routes-on terms go stale as units evolve; the Also-holds cell must change when a unit gains a document beyond the doctype set; the Project-repo cell when a repo appears or moves. No procedure names the registry as a target: work closeout's target walk covers the owning unit's docs but not the entrypoint, and the dream cycle — the registry's natural cadence home — is unwritten. Routing quality is the whole cold-start story; silent registry rot degrades the layer's core benefit. Fold the cadence half into the dream-cycle design; the event half (a closeout that adds an extra doc updates Also-holds) is one clause in the closeout walk.

**4. Migration hole: components → one problem.** Folding the hub's documents into the last surviving component has no answer for the logs. "LOG files are append-only — never archived" makes every option contradictory: appending the hub log's old entries after the survivor's newer ones breaks chronology, interleaving breaks append-only, archiving breaks never-archived. Decide the log-fold semantics before any brain runs this move; candidates include keeping the retired hub log in place as a closed sibling, or folding it in as a single dated historical entry.

**5. Migration hole: component → its own brain.** The extracted subtree leaves home without an entrypoint or any maintenance document — both are hub property — and its SCOPE and APPROACH may carry their sanctioned upstream references to the former parent, which then dangle across repositories. The move's "replace its registry row with a pointer" also leaves the pointer's semantics unspecified: what the row holds, and how routing treats it. Needs an extraction kit: mint the new brain's entrypoint and maintenance set, rewrite or absorb the parent references, and define the pointer row.

**6. State the layer's boundary of applicability.** Nearest-common-ancestor placement plus the sibling prohibition means densely-coupled components push most knowledge to the hub — a brain whose components interact many-to-many quietly rebuilds the monolith there. That is graceful degradation, not failure, but it is nowhere stated. One sentence in `MBT_COMPONENTS.md`'s applicability test would carry it: the layer pays off when the problem decomposes tree-like, and an intermediate parent (the virtual-view plan's `viewmapper/`) is the mitigation done right.

**7. Open question: do all four doctypes always earn their keep at the hub?** The grammar obliges every unit to carry SCOPE, APPROACH, FINDINGS and LOG, and seeding creates them all so the grammar never promises a missing file. For a hub whose components compose loosely, the hub SCOPE may have nothing to say that the component scopes don't — the virtual-view plan itself doubts its own. If living hubs bear that out, the grammar-never-lies invariant and every-claim-earns-its-keep pull against each other and need a ruling. Watch VV; don't pre-solve.

**8. Decision: the guardrails brain's shape.** The check procedure's shape check flags a unit that authored one target's documents first and ported the second against them — and the guardrails brain is that case, so any check run against it will carry a standing recommendation to restructure into components. The flat-split-to-components migration row covers the mechanics, including authoring the per-platform SCOPEs and APPROACHes a flat split never had. Decide whether to run that migration, or to accept the recommendation as a known-and-declined flag.

**9. Minor.**

- "The platform runbook" in the work-item scaffolds is flat-split vocabulary; in a component brain it loosely means the owning unit's canonical runbook. The scaffold hedges ("if the brain has one") — let VV's first work item show whether it needs sharper wording.
- The instantiated-brain templates state that any log-appending procedure cites the session-closeout doc as the entry-format authority; the toolkit's own `CLAUDE.md` maintenance-doc boundary lacks that clause and could adopt the same sentence for consistency.

## Sequencing

Seed the virtual-view-brain first and run its round-trip acceptance test. Items 1–3 are stage-3 design work best done once VV has real work items and real drift — the first work item makes re-homing risk live, and the first drift review demands the dream cycle. Items 4–5 block only the migrations they describe, and no brain is near either move. Items 6–8 are a sentence and two decisions, landable any time.