# Cross-Repository Migrations: Decision Record

## Problem

Four of the five restructuring moves in `MBT_COMPONENTS.md` reshape a brain within its own repository. One crosses a repository boundary — a component leaving to become its own brain — and it is the only one stated as a single sentence. It understates what the departing subtree lacks: an entrypoint and a maintenance set, both hub property; SCOPE and APPROACH carrying the upstream parent references the exemption table sanctioned, which dangle once the parent is a different repository; and a "replace its registry row with a pointer" whose semantics are never given — neither what the row holds nor how routing treats a component that has left.

The inverse motion has no row at all. An existing standalone brain becoming a component of another is a move the table cannot express.

**Absorption is not extraction reversed**, which is why it is work rather than a symmetry that comes free:

- Extraction **mints** what the subtree lacks. Absorption **sheds** what the incoming brain has too much of — its own entrypoint and its full maintenance set both yield to the absorbing hub's, since maintenance documents live at the hub.
- Its token was brain-wide and becomes a component token, re-declared in the registry and checked against the naming rule in both directions: the incoming token must not sit as a longer prefix over an existing unit's documents, nor an existing token over its own.
- Its SCOPE was authored as a hub SCOPE, referencing nothing because it had no parent. As a component SCOPE it may now reference its parent's, and the absorbing hub's SCOPE must name the new part without elaborating it.
- Its `archive/` arrives populated, against the convention that a component's `archive/` begins at its own first retirement.
- Its logs meet the absorbing brain's — the same two-logs-one-brain problem the collapse has.

## Preferred approach: one kit, both directions

- **Extraction kit** — mint the new brain's entrypoint and maintenance set, resolve the parent references its SCOPE and APPROACH carried, and define the pointer row.
- **Absorption row** — the move the table lacks: shed the incoming entrypoint and maintenance set, re-declare the token as a component token under the naming rule, re-home the SCOPE and APPROACH references onto the new parent, and merge the logs.
- **Pointer semantics** — settled once and used by both: what the registry row holds for a departed component, and how routing treats it.

## Alternatives considered

- **State absorption as "extraction, reversed"** — rejected on the asymmetry above. The two moves share a boundary crossing and nothing else; the documents one mints are the documents the other discards.
- **Leave absorption out and keep the table at five rows** — rejected: extraction already lets a component leave, so a brain can reach a shape it has no sanctioned way to undo.

## What this doesn't solve

- **The collapse's log merge** — settled, and stated in the restructuring table. Absorption inherits that rule rather than re-deciding it.
- **The four internal-reshape moves**, which are unaffected by anything here.