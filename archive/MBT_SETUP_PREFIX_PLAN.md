# Enforce the Work-Item Token Prefix: Implementation Plan

## Objective

Make `WORK_SETUP` always produce token-prefixed work-item filenames (`<TOKEN>_<WORK>_*`) by turning the currently-buried prepend rule into an explicit name → slug → filename transform at the point a name is handed in, with the handed-name ambiguity (bare vs already-prefixed) resolved in the instruction. Confined to `templates/WORK_SETUP.md`. No new invariants, no changes to the glob, the ownership model, or the naming law.

## Context

See `MBT_SETUP_PREFIX_FINDINGS.md` in this directory for the decision record and the rejected Option A.

Key references in the owning unit:
- `MBT_SCOPE.md` — problem space this fits into
- `MBT_FINDINGS.md` — relevant prior decisions
- `MBT_APPROACH.md` — design constraints

## What changes

- `templates/WORK_SETUP.md` §2 (slug) and §3 (generate the docs): add the explicit transform — the produced filenames are always `<TOKEN>_<WORK>_*`; a bare handed name is always prefixed; a handed name already leading with the unit's token is stripped before use so it is never double-prefixed. State it as an imperative at the decision point, not woven into the prefix-distinctness prose.

Exact wording and placement settled at implementation.

## Interaction with existing code

| Existing code | Interaction | Risk |
|---|---|---|
| `templates/WORK_SETUP.md` glob `<TOKEN>_<WORK>_*` | Unchanged — the fix makes reality match what the glob already assumes | None |
| Inlined `WORK_SETUP` copies in existing brains | Not updated by this change; propagates to newly seeded brains only | Low — known limitation, recorded in FINDINGS |

## Testing approach

Behavioral, no automated suite: run the setup procedure against sample handed names — a bare name, an already-token-prefixed name, and (mentally) a component-brain case — and confirm the resulting filenames are always `<TOKEN>_<WORK>_*` with no double prefix. Manual steps live in `MBT_SETUP_PREFIX_TESTING.md`.

## Implementation sequence

1. Draft the §2/§3 edit to `templates/WORK_SETUP.md`; confirm it reads as one imperative, not a second copy of the prefix-distinctness rule.
2. Dry-run the three sample names against the revised text.

## Scope boundary — what this does NOT include

- Dropping the token from working files (Option A) — explicitly rejected in FINDINGS.
- Any edit to `WORK_CLOSEOUT`, `SESSION_CLOSEOUT`, `PROJECT_HOOK`, `MBT_COMPONENTS.md`, the `<TOKEN>_<WORK>_*` glob, or the `CLAUDE.md` naming law.
- Retro-patching existing exemplar brains' inlined `WORK_SETUP` copies.
- The pattern-wide redesign to retire the token-in-name redundancy (make the directory the sole ownership signal) — a separate work item if pursued.

## Open issues

1. Exact wording and placement of the transform in §2 vs §3 — one imperative, avoiding a duplicated statement of the prepend rule.
2. Whether a one-line pointer belongs in the intake step (§1) so the name is captured cleanly before slug derivation — decide at implementation.
