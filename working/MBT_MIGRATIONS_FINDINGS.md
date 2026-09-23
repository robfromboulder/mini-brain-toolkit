# Cross-Repository Migrations: Decision Record

## Problem

Three of the four restructuring moves in `MBT_LOBES.md` reshape a brain within its own repository. One crosses a repository boundary — a child lobe leaving to become its own brain — and the table marks it incomplete: it names what the departing subtree lacks without saying how to supply it. The subtree lacks an entrypoint and a maintenance set, both hub property; its SCOPE and APPROACH carry the upstream parent references the exemption table sanctioned, which dangle once the parent is a different repository; and "replace its registry row with a pointer" has no semantics — neither what the row holds nor how routing treats a child that has left.

The inverse motion has no row at all. An existing standalone brain becoming a child lobe of another is a move the table cannot express.

**Absorption is not extraction reversed**, which is why it is work rather than a symmetry that comes free:

- Extraction **mints** what the subtree lacks. Absorption **sheds** what the incoming brain has too much of — its own entrypoint and its full maintenance set both yield to the absorbing hub's, since maintenance documents live at the hub.
- Its lobespace was brain-wide and becomes a child's, re-declared in the registry and checked against the lobespace-ownership rule in both directions: the incoming lobespace must not sit as a longer prefix over an existing lobe's documents, nor an existing lobespace over its own.
- Its SCOPE was authored as a hub SCOPE, referencing nothing because it had no parent. As a child's SCOPE it may now reference its parent's, and the absorbing hub's SCOPE must name the new part without elaborating it.
- Its `archive/` arrives populated, against the convention that a child's `archive/` begins with its own first retirement.
- Its logs meet the absorbing brain's — the same two-logs-one-brain problem the collapse has.

## Preferred approach: one kit, both directions

- **Extraction kit** — mint the new brain's entrypoint and maintenance set, resolve the parent references its SCOPE and APPROACH carried, and define the pointer row.
- **Absorption row** — the move the table lacks: shed the incoming entrypoint and maintenance set, re-declare the lobespace as a child's under the ownership rule, re-home the SCOPE and APPROACH references onto the new parent, and merge the logs.
- **Pointer semantics** — settled once and used by both: what the registry row holds for a departed child, and how routing treats it.

## Alternatives considered

- **State absorption as "extraction, reversed"** — rejected on the asymmetry above. The two moves share a boundary crossing and nothing else; the documents one mints are the documents the other discards.
- **Leave absorption out and keep the table at four rows** — rejected: extraction already lets a child lobe leave, so a brain can reach a shape it has no sanctioned way to undo.

## What this doesn't solve

- **The collapse's log merge** — settled, and stated in the restructuring table. Absorption inherits that rule rather than re-deciding it.
- **The three internal-reshape moves**, which are unaffected by anything here.
