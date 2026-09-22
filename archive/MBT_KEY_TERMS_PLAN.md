# Key Terms: Implementation Plan

## Objective

Rename three collision-prone pattern terms — unit → lobe, token → lobespace, component → lobe — across the toolkit's canonical docs and templates, so downstream brains inherit vocabulary that does not collide with their product domains. "Component" collapses into "lobe" because a component IS a non-hub unit, which in the new vocabulary is simply a child lobe.

## Context

See `MBT_KEY_TERMS_FINDINGS.md` in this directory for the decision record and alternatives considered. This work item was split from the ENFORCED_TERMS work item, which identified these terms as collision-prone but deferred the rename to keep its own scope bounded.

## What changes

Every file that uses "unit," "token," or "component" in the pattern-specific sense. The rename is mechanical (grep-and-replace) with editorial judgment at each site — some uses are the pattern-specific sense, some are the ordinary-English sense, and a few are ambiguous.

### Pattern-specific "unit" and "component" (→ lobe)

"Component" collapses into "lobe" — a component is a non-hub unit, which in the new vocabulary is a child lobe. "Component-structured brain" becomes "multi-lobe brain." The component registry becomes the lobe registry. `MBT_COMPONENTS.md` becomes `MBT_LOBES.md` (or similar — the file describes the multi-lobe layout convention).

| File | Where |
|---|---|
| `MBT_PATTERN.md` | Principles 3 and 9, the file-set tables, the lifecycle section, component passages |
| `MBT_COMPONENTS.md` | Pervasive — "unit" and "component" are the core concepts; file itself renames |
| `MBT_CHECK_BRAIN.md` | Component-brain checks, scorecard |
| `MBT_CREATE_BRAIN.md` | Component creation, intake conversation |
| `MBT_DREAM_CYCLE.md` | Component-brain maintenance |
| `templates/COMPONENTS_CLAUDE.md` | Pervasive — doctype grammar, registry, placement rules |
| `templates/WORK_CLOSEOUT.md` | Component-brain closeout |
| `templates/DREAM_CYCLE.md` | If component-brain hooks exist |
| `CLAUDE.md` | File conventions, declared exemptions, read index |

### Pattern-specific "token" (→ lobespace)

| File | Where |
|---|---|
| `MBT_PATTERN.md` | Principle 6 |
| `MBT_COMPONENTS.md` | Token ownership, naming rules |
| `MBT_CHECK_BRAIN.md` | Namespace checks |
| `MBT_CREATE_BRAIN.md` | Intake conversation (token selection) |
| `templates/CLAUDE.md` | File naming rule |
| `templates/COMPONENTS_CLAUDE.md` | Token ownership, file naming, registry columns |
| `CLAUDE.md` | File naming rule |

### Vocabulary-alignment walkthrough in the check procedure

`MBT_CHECK_BRAIN.md` gains a step that detects old-vocabulary usage in a target brain and walks the migration when the user opts in. Details in the "Migration of older brains" section below.

### Template placeholders

Both template placeholders represent lobespaces and both rename: `<TOKEN>` → `<LOBESPACE>` (a component's declared namespace) and `<PREFIX>` → `<LOBESPACE>` (the single lobespace in a single-unit brain, or the hub's lobespace in a component brain). A brain with one lobe has one lobespace; the concept is the same at every level.

The create procedure currently relies on the placeholder *name* to distinguish what gets substituted at creation (`<PREFIX>`) from what stays as a runtime variable (`<TOKEN>`). With both becoming `<LOBESPACE>`, the procedure carries that distinction by context — which placeholders to substitute is determined by position (hub docs vs. doctype grammar), not by name.

## Implementation sequence

1. Rename in the pattern definition (`MBT_PATTERN.md`) first — it is the authority.
2. Rename in `MBT_COMPONENTS.md` — the component layer that depends on the pattern.
3. Rename in the procedures (`MBT_CHECK_BRAIN.md`, `MBT_CREATE_BRAIN.md`) and maintenance (`MBT_DREAM_CYCLE.md`).
4. Rename in the templates (`templates/CLAUDE.md`, `templates/COMPONENTS_CLAUDE.md`, `templates/DREAM_CYCLE.md`, `templates/WORK_CLOSEOUT.md`).
5. Rename in this brain's own `CLAUDE.md`.
6. Add the vocabulary-alignment walkthrough to `MBT_CHECK_BRAIN.md`: detect old terms, classify each hit by context, replace or skip unambiguous cases silently, surface ambiguous cases to the user.
7. Verify: grep for remaining pattern-specific uses of "unit," "token," and "component" across all top-level and template files.

## Testing approach

After the rename, run `MBT_CHECK_BRAIN.md` against this repo. The check should pass — the rename changes vocabulary, not structure. Confirm no stale "unit"/"token"/"component" references survive in the pattern-specific sense (generic uses like "unit test" in a PLAN template are fine and expected).

## Migration of older brains

Brains seeded before this rename use the old vocabulary in their own docs and `CLAUDE.md`. The rename doesn't break them — internal vocabulary is self-consistent — but it creates a vocabulary split: the toolkit says "lobe" while the brain says "unit," and a session loading both sees two terms for one concept.

The check procedure (`MBT_CHECK_BRAIN.md`) gains a vocabulary-alignment step. When the check finds a brain using the old terms, it walks every hit, classifies each as pattern-specific or ordinary-English by surrounding context, and acts:

- **Unambiguous pattern-specific** (e.g. "the brain's token is `ORCHARD`") — replaced silently.
- **Unambiguous ordinary-English** (e.g. "token budget" in LLM infrastructure docs) — skipped silently.
- **Genuinely ambiguous** — surfaced to the user to judge.

This keeps the user's time limited to the cases where context doesn't settle the sense. The walkthrough runs as part of the normal check; once a brain's vocabulary aligns, the step produces no hits and is effectively silent on future checks.

The check's stance ("never edit the target brain during a check unless the user explicitly asks") governs: the check flags the vocabulary split as an opportunity and performs the walkthrough only when the user opts in.

## Scope boundary

- The ENFORCED_TERMS work item. It delivers the mechanism and two entries (finding, work item). Neither work item blocks the other.
- `archive/` content. Retired files keep their vocabulary, consistent with the archive-exempt rule.
