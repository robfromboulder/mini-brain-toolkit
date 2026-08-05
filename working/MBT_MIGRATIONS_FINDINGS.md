# Restructuring Migration Completion: Decision Record

## Problem

Two of the five restructuring migrations in `MBT_COMPONENTS.md` have holes.

**Components → one problem** has no answer for the logs. Folding the hub's documents into the last surviving component collides with "LOG files are append-only — never archived": appending the hub log's old entries after the survivor's newer ones breaks chronology, interleaving breaks append-only, and archiving breaks never-archived. Every option contradicts a standing rule.

**Component → its own brain** understates what the extracted subtree lacks. It leaves home without an entrypoint or any maintenance document — both are hub property — and its SCOPE and APPROACH may carry their sanctioned upstream references to the former parent, which then dangle across repositories. The move's "replace its registry row with a pointer" also leaves the pointer's semantics unspecified: what the row holds, and how routing treats it.

## Preferred approach: decide the collapse, kit the extraction

- **Collapse** — decide the log-fold semantics before any brain runs the move. Candidates: keep the retired hub log in place as a closed sibling of the survivor's, or fold it in as a single dated historical entry.
- **Extraction** — an extraction kit: mint the new brain's entrypoint and maintenance set, rewrite or absorb the parent references its SCOPE and APPROACH carried, and define the pointer row.

## Alternatives considered

- **Relax the append-only/never-archived rules for migrations** — rejected: the rules protect lineage everywhere; a migration-shaped exception weakens them for the common case to serve a rare one.

## What this doesn't solve

- The first three migrations, which are fully specified and preserve every knowledge filename.
