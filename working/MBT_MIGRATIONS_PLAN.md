# Restructuring Migration Completion: Implementation Plan

## Objective

Complete the two restructuring migrations with open holes — log-fold semantics for the collapse to one problem, and an extraction kit for a component leaving as its own brain — so no brain runs either move unspecified. Blocks only those two migrations, and no brain is near either; activate when one is.

## Context

See `MBT_MIGRATIONS_FINDINGS.md` in this directory for the decision record and alternatives considered.

Key references in the mini-brain:
- `MBT_COMPONENTS.md` — the migration table these rows live in
- `MBT_FINDINGS.md` — relevant prior decisions
- `MBT_APPROACH.md` — design constraints

## What changes

- `MBT_COMPONENTS.md` — the collapse and extraction rows in the restructuring table, stated to the same completeness as the other three.
- Possibly `templates/COMPONENTS_CLAUDE.md`, if the pointer row's shape belongs in the registry's documentation.

## Interaction with existing code

| Existing doc | Interaction | Risk |
|---|---|---|
| `MBT_CHECK_BRAIN.md` | Its checks must pass on a just-migrated brain | A sanctioned migration leaves a brain its own check flags |
| `templates/SESSION_CLOSEOUT.md` | Log routing must resolve during and after either move | Sessions log to a retired or not-yet-minted log |

## Testing approach

Dry-run each migration on a disposable copy of the living component prototype, then run the check procedure against the result; acceptance is a clean structural pass on the migrated shape.

## Implementation sequence

1. Decide the collapse's log-fold semantics.
2. Specify the extraction kit and the pointer row.
3. Dry-run both; run the check procedure on the results.

## Scope boundary — what this does NOT include

- No new migration kinds; the table stays five rows.
- No changes to the three fully-specified migrations.

## Open issues

1. Log-fold semantics: closed sibling vs single dated historical entry.
2. Pointer-row semantics: what the row holds, and how routing treats a component that has left.
