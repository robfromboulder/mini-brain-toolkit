# Mini-Brain Toolkit: The Multi-Lobe Layer

> V9, 2026-09-21.

This document is the layout convention for a mini-brain whose knowledge divides into several lobes. It is opt-in: a brain with one problem never uses it, and the file set in `MBT_PATTERN.md` applies unchanged.

---

## 1. When the layer applies

A **lobe** is any node in the brain's tree — the hub or any of its children, at any depth. Every lobe carries at least the four knowledge documents — SCOPE, APPROACH, FINDINGS, LOG — with the meanings `MBT_PATTERN.md` gives them, and may carry more (§3).

A lobe holds **child lobes** when one SCOPE cannot state its problem honestly: writing it forces two or more problems onto the page that merely coexist. Each of those problems becomes a child lobe. A lobe whose problem states cleanly in a single SCOPE has no children, and a brain with no children does not use this layer at all.

Apply the test to each child lobe in turn. A child whose own problem splits again holds its own children, and everything below applies to it exactly as it applies to the hub.

The layer pays off when the problem decomposes tree-like. Placement (§4) sends every fact spanning two lobes to the lobe above them, so lobes that interact many-to-many push most of their knowledge to the hub — graceful degradation, not failure, but a brain shaped that way quietly rebuilds the monolith there; grouping the tightly-coupled lobes under an intermediate parent is the mitigation.

The doctypes mean the same thing at every level. A lobe with children therefore has a design that includes how those children compose: its APPROACH describes their interfaces and why they fit together, never their internals, which belong to the children. This is why the layer adds no document type — a parent is not a new kind of thing, only a lobe whose problem happens to decompose.

---

## 2. Naming

```
[<path>/] [working/] <LOBESPACE> [_<WORK>] _<DOCTYPE>.md
    ↑          ↑          ↑           ↑         ↑
  lobe     in-flight   declared    work item  doc kind
 (nested)             per lobe
```

Directories carve lobes; the trailing slot carves work items. Hub documents take no path.

Every lobe declares one lobespace, the hub's in the entrypoint's opening line and each child's in the registry (§3). Because the lobespace is declared rather than inferred, it may contain underscores — `ORCHARD_PRESS` is a single lobespace, not `ORCHARD` plus a qualifier.

**Lobespace ownership.** A document belongs to the lobe whose declared lobespace its name begins with in full, taking the longest match when more than one qualifies. Lobespaces may nest as prefixes, so a shorter lobespace matching proves nothing: `orchard/ORCHARD_PRESS_SCOPE.md` begins with `ORCHARD`, and is nonetheless a misplaced document belonging to `orchard/press/`. Ownership constrains naming in return: never name a document so that another lobe's lobespace is a longer prefix of its name than the owning lobe's — the trap is a parent whose name continues into a child's lobespace, as an `orchard/` work item slugged `PRESS_ERRORS` would yield `ORCHARD_PRESS_ERRORS_PLAN.md` and hand its files to `orchard/press/`.

**Every lobe owns its `working/` and `archive/`.** The hub's pair is created at seeding, as in any brain; a child's is created when it first has in-flight work or retired material, never ahead of need. Source material gathered at seeding lands in the hub's `archive/`, whichever child it describes — a child's `archive/` begins with its own first retirement. A lobe's `working/` inherits its lobespace, so `orchard/press/working/ORCHARD_PRESS_YIELD_PLAN.md` stays as parseable as a canonical document. A lobe's `archive/` does not: retired files keep the basename they were retired under, as in any brain, and need not be markdown.

---

## 3. The entrypoint

The brain's `CLAUDE.md` states the hub lobespace, then carries four things and never a list of every document:

1. **Hub index** — one row per hub document, as in any brain.
2. **Doctype grammar** — one row per doctype, saying what it holds. Every child lobe carries the full set.
3. **Lobe registry** — one row per child lobe: directory, lobespace, the terms that should route a question to it, an **Also holds** cell, and the project repository where one exists — a path into an ancestor's repository, for a child whose code lives inside one. Sub-lobes are rows indented under their parent.
4. **Conventions** — as in any brain, plus the placement rules in §4.

A reader resolves a document's path from the grammar and the registry rather than from an enumeration: the registry gives the directory and lobespace, the grammar gives the rest. The registry's routing terms are what a session matches its question against to choose a lobe before reading anything; questions about how lobes fit together, and questions no lobe's terms claim, are hub-level.

Because the hub index no longer lists every current document, an entrypoint that carried the usual "only files in this table are current" now says that of the hub's documents alone, and points at the registry and grammar for the rest. Left unchanged, that line tells a reader every child document is stale.

Seeding creates the full doctype set for every child lobe, so the grammar never promises a file that does not exist. Documents *beyond* the standard set are named in that child's **Also holds** cell. When the cell outgrows a line or two, that child earns a local read index — `<LOBESPACE>_CLAUDE.md`, never a bare `CLAUDE.md`, which a harness would load unbidden — and the cell becomes a pointer to it.

**Maintenance and procedure documents live at the hub.** Session closeout — and work setup, work closeout and the dream cycle when the brain grows them — govern the whole brain, so one of each serves every lobe and none is namespaced to a child. The in-flight documents those procedures scaffold land in the `working/` of whichever lobe owns the work.

---

## 4. Placement

**The placement rule.** A fact about two lobes belongs to their nearest common ancestor. Sibling references are forbidden — a sibling is neither upstream nor downstream — so knowledge spanning two lobes lives in the lobe above them and never in either one. Placement is therefore decidable rather than a matter of taste: name the lobes a fact concerns and walk up to where they meet. The ancestor fixes which lobe holds the fact; the fact's own nature fixes which document, composition that was designed going to APPROACH and interaction that implementation revealed going to FINDINGS.

**A parent names what a child elaborates, and stops.** A parent whose problem decomposes has to state the parts in order to state its own problem at all, so some restatement is inherent and is not duplication. What is duplication is the parent continuing past naming a part into explaining it — describing *why* a child's problem is hard, or how it is solved, in the parent's own words. The line is that a reader of the parent should learn that the part exists and where it fits; a reader who wants to know what makes it hard goes to the child. When the same explanation would be at home in either document, it belongs in the child.

**An open question belongs to exactly one lobe: the one whose work would resolve it.** The same question standing in a parent and a child means neither owns it, and both copies will drift as the answer develops. Ask which lobe's session would close the question, and put it there.

**Log routing** is the same rule applied to lineage. A session logs to the nearest common ancestor of the lobes its work concerned — not every lobe it read: one that worked inside a single lobe logs there, one whose work crossed lobes logs above them, however far apart in the tree they sit.

**Declared reference exemptions**, stated per doctype so the table stays fixed-size at any lobe count or depth:

| Doctype | May reference | Why |
|---|---|---|
| `<LOBESPACE>_SCOPE.md` | its parent's SCOPE only | A child's problem is part of the problem its parent states, which precedes and outlives it. The hub's SCOPE has no parent and so references nothing. |
| `<LOBESPACE>_APPROACH.md` | its own SCOPE and its parent's APPROACH | A design answers its own problem and the design it composes into — both upstream. |
| `<LOBESPACE>_FINDINGS.md` | *none* | Implementation decisions downstream of the approach, with nothing upstream to cite. |
| Any document | its own child lobes **by name**, never their files | Naming a part of your own subject is not a downstream reference; reaching into that part's documents is. |

A permitted reference is cited by name, never by section number. Two classes stand outside the table. **Logs** record what a session touched, filenames included, so naming another lobe's documents is their job. **Maintenance and procedure documents** name the knowledge files they operate on, which is inherent to being a procedure.

---

## 5. Restructuring

The first three migrations preserve every knowledge document's filename, so no cross-reference resolves differently and no log is rewritten; their real work is authoring the documents the new shape requires, named per row. Maintenance documents are the exception: they live at the hub under its lobespace, so the one migration that gives the hub a new lobespace renames them to it. The last two need no new SCOPE, and collapsing to one problem is the single case that retires knowledge filenames, since folding the hub's documents into the survivor leaves one set of names standing.

A **flat platform split** is the base pattern's convention for one problem delivered across several targets: documents that differ per target take a leading platform qualifier and shared ones do not, with no directories involved.

| From | To | The move |
|---|---|---|
| One problem | Multi-lobe | `git mv` the knowledge documents into a child directory — the brain's lobespace, now taken, becomes that child's — then declare a fresh hub lobespace, rename the maintenance documents (and the hub references inside them) to it, author the hub's documents at the root, and replace the entrypoint's file table with the four parts in §3. A brain that already runs a dream cycle comes out of this move with one that assumes a single lobe: its structural checks are scoped to the root and will pass while never examining a child. Treat that cycle as unadapted until it is redesigned. |
| Flat platform split | Multi-lobe | Move each platform's documents into a directory named for it and declare its existing compound prefix as that child's lobespace. Shared documents stay at the root as the parent, whose lobespace is unchanged. Author each new lobe's missing doctypes — a platform family typically arrives with findings and a log but no SCOPE or APPROACH of its own. |
| Child lobe | Sub-lobes | The child gains its own child directories, each seeded with its full doctype set; its own documents stay put and become the parent layer, ceding to each grandchild the content that was really that grandchild's. |
| Multi-lobe | One problem | The reverse of the first, folding the hub's documents into the last remaining child. Each of the hub's logs merges into the survivor's counterpart: entries move whole and in date order, placed among the survivor's rather than after them. Entries sharing a date may sit in either order — the headings carry no finer precision. |
| Child lobe | Its own brain | **Incomplete — do not run this move yet.** `git mv` the directory to a new repository and replace its registry row with a pointer; the subtree already carries its `working/` and `archive/`, so it moves whole. What is unspecified is everything the subtree lacks on arrival: an entrypoint and a maintenance set, both hub property, and a SCOPE and APPROACH whose sanctioned parent references now dangle across repositories. The pointer's own semantics — what the row holds, and how routing treats a child that has left — are undefined. |

---

## 6. Noticing that a lobe should have split

The lobe test runs when a brain is created and is easy never to run again. A brain that should have split is internally consistent either way, so no structural check can see the omission — the shared SCOPE it ends up with looks settled rather than provisional.

**A port is the tell.** When a lobe finds itself authoring one target's documents first and porting a second target against them, those targets hold different problems. The porting is what a single SCOPE looks like when it is really one target's SCOPE wearing a shared name.

The signal is never volume. How much a lobe accumulates depends on how tightly its children couple, not on whether the split was right — a parent whose APPROACH stays short may simply own children that rarely touch. Re-run the test when the test itself stops discriminating, never because a document came out thinner than expected.
