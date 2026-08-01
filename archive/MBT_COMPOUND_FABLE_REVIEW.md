# Component Layer - Fable Review

Fable-powered review of the `component-brains` branch (one commit: `MBT_COMPONENTS.md` and `templates/COMPONENTS_CLAUDE.md` new; pattern, create/check procedures, entrypoint and maintenance templates edited). 2026-07-31, Rob's request, Claude (Fable 5, max effort) as reviewer. Reference exemplar for structure: `../virtual-view-brain/VV_BOOTSTRAP_PLAN.md` — its proposed tree only, not its seed-content or issue-mapping claims. Compatibility references: `../../starburstdata/mini-nebula-brain` and `../../starburstdata/mini-guardrails-brain`. Working doc — unversioned, point-in-time; supersede rather than maintain.

---

## Verdict

Nothing found contraindicates the layer. The unit recursion, declared tokens, grammar+registry entrypoint, and nearest-common-ancestor placement rule held up against every workflow case constructed during review. Weaknesses cluster in three places: one concrete cross-cutting defect (the `<PREFIX>` placeholder now means two different things in the maintenance templates), the dream cycle (entirely un-adapted — the only workflow with no component story), and the restructuring table (three of five migrations have holes). Everything scoring below 70 is stage-3 machinery the virtual-view-brain won't exercise at seed, so the seeding path is nearly ready as-is.

## Confidence scorecard

Confidence per the toolkit's own idiom: a proxy for remaining unknowns; below ~70 means fix or design before trusting.

| Area | Confidence | One-line read |
|---|---|---|
| Backwards compat & simple-brain cost | 92 | Exemplars untouched and still valid; single-unit brains gain ~6 dormant, guarded sentences |
| Core model (units, recursion, opt-in layering) | 90 | Clean recursion, no new doctype; reuses the discovery-by-grammar mechanism proven at the work-item layer |
| VV structure as canonical exemplar | 85 | Exercises nesting, compound tokens, cross-module ownership, hub-vs-unit items; asks the right open questions |
| Entrypoint (grammar, registry, routing) | 80 | Solid mechanics; routing-term quality has no assigned maintainer |
| Placement & log routing (NCA rule) | 78 | Decidable and enforceable; "units the session touched" is undefined |
| Naming & token ownership | 75 | Longest-match works; one deterministic misattribution hazard with no guardrail |
| Work setup / closeout | 70 | Component-aware in the right places; no re-homing path, and hit by the substitution defect |
| Session closeout | 65 | NCA fallback landed correctly; work-item routing signals corrupt under substitution in a component brain |
| Restructuring migrations | 55 | Right set of five moves; three contain holes |
| Dream cycle | 40 | Not updated at all — contradicts "maintenance documents govern the whole brain" |

---

## Defects

### 1. `<PREFIX>` carries two meanings in the maintenance templates

`templates/SESSION_CLOSEOUT.md`, `templates/WORK_SETUP.md`, and `templates/WORK_CLOSEOUT.md` use `<PREFIX>` both as the brain's token (substituted at creation) and as *the owning unit's token* (a runtime variable). `MBT_CREATE_BRAIN.md` substitutes `<PREFIX>` → the namespace token unconditionally — the hub token, for a component brain. Instantiating the virtual-view-brain would produce:

- `VV_SESSION_CLOSEOUT.md` whose work-item routing signals (session-content and current-branch rules) read `working/VV_<WORK>_*` and `VV_<WORK>_CLAUDE.md` — patterns matching nothing, since items carry unit tokens in unit `working/` dirs. Both signals go dead in the letter; every session falls through to the no-match rule.
- `VV_WORK_SETUP.md` whose owning-unit intake bullet reads "its token becomes their `VV`" — the sentence that *defines* the runtime variable, destroyed by substitution.
- `VV_WORK_CLOSEOUT.md` instructing moves and dangling-reference greps of `VV_<WORK>_*` names that don't exist.

`templates/work/*` is unaffected — those substitute at setup time with the owning unit's token, which is correct. Fix: adopt the split `templates/COMPONENTS_CLAUDE.md` already uses — `<PREFIX>` substituted, `<TOKEN>` surviving as the runtime unit-token variable — in the three maintenance templates, plus one sentence defining `<TOKEN>` = the brain's token for single-unit brains; or have the create procedure declare a substitution exemption. Fix before seeding VV — session closeout is the most-executed procedure in the pattern.

### 2. The dream cycle has no component story

`templates/DREAM_CYCLE.md` was not touched; every phase assumes a single unit:

- Phase 1's checks operate on top-level `*.md` only — in VV they audit the hub's files and silently skip the other twenty. The filename-leakage check defines legitimate mentions as "listed in the `CLAUDE.md` read index," but component canonical files are deliberately *not* listed there, so every legitimate mention of one (in the hub LOG, say) is flagged as leakage — false positives by construction.
- Phase 2 verifies one SCOPE against one codebase. VV has six SCOPEs verified against five different project repos. The registry's Project-repo column carries exactly the data this phase needs; nothing consumes it.
- Phase 4 extracts from one LOG into one FINDINGS. VV has six pairs, plus a problem the flat pattern never had: a hub finding about how two units interact can be rotted by a change inside either unit, and no per-unit pass looks upward. Cross-level reconciliation is a novel maintenance task.

Compounding: `MBT_COMPONENTS.md` declares the dream cycle a hub document governing the whole brain — a promissory note nothing redeems. And the toolkit's own `MBT_DREAM_CYCLE.md` has the same blind spot: its teaching-artifact consistency sweep enumerates the pattern, the two procedures, and `templates/` — so the `MBT_COMPONENTS.md` ↔ `templates/COMPONENTS_CLAUDE.md` pair, which duplicates the grammar, ownership rule, placement rule, and exemption table nearly verbatim by necessity, sits outside the only mechanism keeping spec and template in sync. Highest-drift-risk duplication in the repo right now. Also undecided: the check procedure's new Shape check re-runs the split test on request; the dream cycle is the natural cadence home for it and doesn't run it.

Deferrable debt (VV reaches stage 3 later), but treat the component dream cycle as a design task — per-unit fan-out, agent budgets, cross-level reconciliation — not sentence-patching. Extending the toolkit's own Phase 2 sweep to cover the new pair is cheap and immediate.

### 3. Restructuring-table holes

The migration table in `MBT_COMPONENTS.md` is the right set of five moves, and blessing the flat platform split as a base-pattern convention is what keeps guardrails valid. Three holes:

- **One problem → components breaks its own headline claim.** "The first three migrations preserve every filename" is false for maintenance docs: the seed's `<OLD>_SESSION_CLOSEOUT.md` begins with the old token, which after migration belongs to the new component by longest-match ownership — yet maintenance docs must live at the hub under no component's token. It must be renamed to the new hub token, and the hub needing a *new* token (the old one is taken) is unaddressed friction. The check procedure's own token-ownership check would flag the un-renamed file as misplaced.
- **Flat split → components arrives violating the grammar invariant.** Guardrails' platform families have FINDINGS/LOG/PHASES/TESTING/CLAUDE but no SCOPE or APPROACH; "every unit carries the full doctype set" fails on arrival. The preamble's "authoring the SCOPE the new shape requires" (singular) doesn't own up to authoring a SCOPE *and* an APPROACH per migrated unit.
- **Components → one problem has no answer for the logs.** "LOG files are append-only — never archived" makes folding the hub's LOG into the survivor's contradictory: appending old entries after newer ones breaks chronology, interleaving breaks append-only, archiving breaks never-archived. Mirror understatement in component → own brain: the extracted subtree leaves without an entrypoint or any maintenance doc (hub property), and its SCOPE/APPROACH may carry now-cross-repo parent references the exemption table sanctioned.

---

## Under-specified seams

Each is a sentence or two of fix.

1. **"Touched" is undefined.** Log routing sends a session to the NCA "of the units the session touched" — read, or worked on? Under the read interpretation, every multi-unit consultation drifts hubward. Should say: the units whose knowledge the session's work concerned.
2. **Work-item log merge: per-entry vs collective.** The closeout template routes merged entries "to the log of the nearest common ancestor of the units the sessions touched, which is usually the owner." If per-entry, an item whose first session stayed inside one child fragments its lineage across logs. Collective NCA over all the item's sessions appears intended (plural "sessions"); one clause pins it.
3. **No work-item re-homing path.** The owning unit is settled at intake as the NCA of the units the work *will* touch — a prediction. When mid-flight scope growth invalidates it (agent-owned item turns out to need mcp changes), there's no move procedure (git mv plus token rename on every doc), and re-running setup silently scaffolds a duplicate in the new owner's `working/` because the audit lists only the new owner's directories.
4. **Child-token capture hazard, no naming-time guardrail.** A parent-owned name extending a child's token is deterministically captured by the child: a viewmapper-owned item slugged `AGENT_ERRORS` yields `viewmapper/working/VMR_AGENT_ERRORS_PLAN.md`, which longest-match assigns to `viewmapper/agent/` — flagged as misplaced by the check procedure. Work-setup's collision guidance covers collisions with other work items, not with child tokens; VV's compound `VMR_AGENT` extending `VMR` makes this live. One sentence in work setup closes it: a `<WORK>` slug must not begin with a child unit's token suffix.
5. **Closeout's target walk only enumerates the owner.** Upward placement (child item pushes a finding to its parent) is stated; downward placement (parent-owned item, child-only finding) is implied by "place by reach" but never structurally walked the way the owner's docs are.
6. **Component-token collision guidance missing.** The create procedure's advice that a token be unlikely to collide with another brain loaded in the same session isn't extended to component tokens, where generic choices (`AGENT`, `MCP`, `CORE`) are now tempting.
7. **The registry has no maintainer.** Routes-on terms go stale as units evolve; Also-holds cells and Project-repo cells change when docs and repos appear. No procedure names the registry as a target — closeout's walk doesn't include the entrypoint, and the dream cycle is absent. Routing quality is the whole cold-start story; silent registry rot degrades the layer's core benefit.

## Structural risks — inherent, worth stating rather than fixing

- **Hub accretion is the boundary of applicability.** NCA placement plus the sibling prohibition means densely-coupled components push most knowledge to the hub — a brain whose components interact many-to-many quietly rebuilds the monolith there. Graceful degradation, not failure; worth one sentence in `MBT_COMPONENTS.md`: the layer pays off when the problem decomposes tree-like. VV's intermediate `viewmapper/` parent is the mitigation done right.
- **Composition questions route one level low.** "How does mcp drive the agent?" matches child terms while the answer lives in the parent's APPROACH. The doctype grammar states where composition lives, so a careful reader recovers; parents' routes-on terms can carry composition vocabulary as cheap mitigation (VV's viewmapper row already does).
- **Forced hub doctypes can run thin.** The grammar obliges every unit to carry all four doctypes; VV's own open question about its hub SCOPE is really a pattern-level question about whether a hub SCOPE always earns its keep. Watch what VV learns; don't pre-solve.

## What holds

- **Backwards compatibility is genuinely clean.** Ten principles untouched; the pattern doc gained one additive paragraph; the flat platform split remains sanctioned; both exemplars parse under the new checks unmodified. Single-unit cost is a handful of dormant, guarded sentences in stage-3 templates — the right trade against a forked template set.
- **The core model is the branch's best idea executed well.** A parent is just a unit; no new doctype; the entrypoint resolves documents from grammar+registry — the mechanism already carrying ninety-six files in guardrails, promoted to the canonical layer. "A document not derivable that way does not exist," backed by the seed-the-full-set rule, is a strong invariant.
- **The check procedure is the best-adapted consumer.** Registry detection at orient, per-unit checks, principles 5/6 rescored against the layer, exact-match token ownership (the substring false-negative was caught and fixed), the archive exemption validated against both exemplars, and the sibling-reference check.
- **The VV structure exercises the sharp edges deliberately**: depth-2 nesting, an underscore-bearing compound token, cross-module items owned by an intermediate parent, sibling items kept apart (the paired security guides) with the hub-owned alternative considered and rejected, and per-unit project repos in the registry.

## Consequence to be aware of

The check procedure's new Shape check ("authored one target's documents first and ported a second against them") now flags guardrails as an undeclared component split — deliberate, per the branch's log entry, but it shifts the toolkit's stance toward guardrails from "conforming" to "conforming, with a standing recommendation to restructure."

## Recommended sequence

1. **Before seeding VV:** fix the `<PREFIX>`/`<TOKEN>` dual-use in the three maintenance templates — the only defect on the seeding path.
2. **Cheap sentence fixes:** define "touched"; pin collective-NCA log merging; forbid `<WORK>` slugs extending a child token; state the missing-doctype authoring and maintenance-doc renames in the migration rows; extend `MBT_DREAM_CYCLE.md`'s consistency sweep to the components pair.
3. **Next design iteration, informed by a living VV:** the component dream cycle (per-unit fan-out, registry maintenance, cross-level reconciliation, where the split test re-runs) and the work-item re-homing procedure.
