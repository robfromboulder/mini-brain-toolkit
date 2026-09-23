# Cross-Repository Migrations: Implementation Plan

## Objective

Make a child lobe portable across a repository boundary in both directions: complete the extraction move so a departing child arrives as a working brain, and add the inverse move so an existing standalone brain can be absorbed as a child lobe.

This is capability, not repair. No brain following the table today hits a contradiction — extraction is marked incomplete and runs out of instructions partway, and absorption has no row to follow. Activate when a brain is near either move.

## Context

See `MBT_MIGRATIONS_FINDINGS.md` in this directory for the decision record and alternatives considered.

Key references in the mini-brain:
- `MBT_LOBES.md` — the restructuring table these rows live in, and the lobespace, placement and reference rules both moves must leave intact
- `MBT_FINDINGS.md` — relevant prior decisions
- `MBT_APPROACH.md` — design constraints

## What changes

- `MBT_LOBES.md` — the extraction row stated to the completeness of the others, with its incomplete warning removed; a new absorption row; and the section preamble, which counts rows ("the first two," "the last two") and must be recounted once the absorption row lands.
- Possibly `templates/LOBES_CLAUDE.md`, if the pointer row's shape belongs in the registry's documentation rather than only in the move that creates it.

## Interaction with existing docs

| Existing doc | Interaction | Risk |
|---|---|---|
| `MBT_CHECK_BRAIN.md` | Its checks must pass on every brain either move leaves behind — the diminished parent, the newly independent child, the enlarged absorber | A sanctioned move produces a brain that the brain's own checker flags |
| `templates/LOBES_CLAUDE.md` | The registry's row shape has to express a pointer to a departed child | A pointer row the entrypoint grammar cannot state |
| `templates/SESSION_CLOSEOUT.md` | Log routing must resolve while a child is leaving and after it has gone | Sessions route to a lobe no longer in the tree |

## Testing approach

Dry-run the round trip on disposable copies, since the two moves are each other's undo and the round trip tests both at once: extract a child lobe from the multi-lobe prototype into a fresh repository, then absorb it back. Run the check procedure on every brain each step produces — the diminished parent and the new standalone brain after extraction, the reassembled brain after absorption.

Acceptance is two things: a clean structural pass at every step, and a reassembled brain whose shape matches where the round trip started, logs included.

## Implementation sequence

1. Specify the extraction kit and settle the pointer semantics.
2. Author the absorption row and recount the preamble's rows.
3. Dry-run the round trip and run the check procedure on each resulting brain.

## Scope boundary — what this does NOT include

- The three moves that reshape a brain inside its own repository.
- Log-merge semantics — already settled in the restructuring table; absorption inherits the rule rather than re-opening it.
- Work-item relocation and the multi-lobe dream cycle, which are their own work items.

## Open issues

1. Pointer semantics: what the registry row holds for a departed child, and whether routing treats it as a dead end or as a redirect a reader is expected to follow.
2. Whether an absorbed brain's populated `archive/` moves with it or stays behind in its original repository.
3. Whether extraction and absorption are two rows or one bidirectional row — the table's other entries are all one-directional, so a bidirectional row would be a new kind of entry.
