# Mini-Brain Toolkit: The Component Layer

> V3, 2026-08-02.

This document is the layout convention for a mini-brain whose knowledge divides into several components. It is opt-in: a brain with one problem never uses it, and the file set in `MBT_PATTERN.md` applies unchanged.

---

## 1. When the layer applies

A **unit** is a brain's hub or any of its components, at any depth. Every unit carries at least the four knowledge documents — SCOPE, APPROACH, FINDINGS, LOG — with the meanings `MBT_PATTERN.md` gives them, and may carry more (§3).

A unit holds **components** when one SCOPE cannot state its problem honestly: writing it forces two or more problems onto the page that merely coexist. Each of those problems becomes a component. A unit whose problem states cleanly in a single SCOPE has no components, and a brain with no components does not use this layer at all.

Apply the test to each component in turn. A component whose own problem splits again holds sub-components, and everything below applies to it exactly as it applies to the hub.

The doctypes mean the same thing at every level. A unit with children therefore has a design that includes how those children compose: its APPROACH describes their interfaces and why they fit together, never their internals, which belong to the children. This is why the layer adds no document type — a parent is not a new kind of thing, only a unit whose problem happens to decompose.

---

## 2. Naming

```
[<path>/] [working/] <TOKEN> [_<WORK>] _<DOCTYPE>.md
    ↑          ↑        ↑         ↑         ↑
component  in-flight declared  work item  doc kind
 (nested)           per unit
```

Directories carve components; the trailing slot carves work items. Hub documents take no path.

Every unit declares one namespace token, the hub's in the entrypoint's opening line and each component's in the registry (§3). Because the token is declared rather than inferred, it may contain underscores — `VMR_AGENT` is a single token, not `VMR` plus a qualifier.

**Token ownership.** A document belongs to the unit whose declared token its name begins with in full, taking the longest match when more than one qualifies. Tokens may nest as prefixes, so a shorter token matching proves nothing: `viewmapper/VMR_AGENT_SCOPE.md` begins with `VMR`, and is nonetheless a misplaced document belonging to `viewmapper/agent/`. Ownership constrains naming in return: never name a document so that another unit's token is a longer prefix of its name than the owning unit's — the trap is a parent whose name continues into a child's token, as a `viewmapper/` work item slugged `AGENT_ERRORS` would yield `VMR_AGENT_ERRORS_PLAN.md` and hand its files to `viewmapper/agent/`.

**Every unit owns its `working/` and `archive/`.** Create them when the unit first has in-flight work or retired material, never ahead of need. A unit's `working/` inherits its token, so `viewmapper/agent/working/VMR_AGENT_COLUMN_LINEAGE_PLAN.md` stays as parseable as a canonical document. A unit's `archive/` does not: retired files keep the basename they were retired under, as in any brain, and need not be markdown.

---

## 3. The entrypoint

The brain's `CLAUDE.md` states the hub token, then carries four things and never a list of every document:

1. **Hub index** — one row per hub document, as in any brain.
2. **Doctype grammar** — one row per doctype, saying what it holds. Every component carries the full set.
3. **Component registry** — one row per component: directory, token, the terms that should route a question to it, an **Also holds** cell, and the project repository where one exists. Sub-components are rows indented under their parent.
4. **Conventions** — as in any brain, plus the placement rules in §4.

A reader resolves a document's path from the grammar and the registry rather than from an enumeration: the registry gives the directory and token, the grammar gives the rest. The registry's routing terms are what a session matches its question against to choose a component before reading anything; questions about how components fit together, and questions no component's terms claim, are hub-level.

Because the hub index no longer lists every current document, an entrypoint that carried the usual "only files in this table are current" now says that of the hub's documents alone, and points at the registry and grammar for the rest. Left unchanged, that line tells a reader every component document is stale.

Seeding creates the full doctype set for every component, so the grammar never promises a file that does not exist. Documents *beyond* the standard set are named in that component's **Also holds** cell. When the cell outgrows a line or two, that component earns a local read index — `<TOKEN>_CLAUDE.md`, never a bare `CLAUDE.md`, which a harness would load unbidden — and the cell becomes a pointer to it.

**Maintenance and procedure documents live at the hub.** Session closeout, work setup and closeout, and the dream cycle govern the whole brain, so one of each serves every unit and none is namespaced to a component. The in-flight documents those procedures scaffold land in the `working/` of whichever unit owns the work.

---

## 4. Placement

**The placement rule.** A fact about two units belongs to their nearest common ancestor. Sibling references are forbidden — a sibling is neither upstream nor downstream — so knowledge spanning two components lives in the unit above them and never in either one. Placement is therefore decidable rather than a matter of taste: name the units a fact concerns and walk up to where they meet. The ancestor fixes which unit holds the fact; the fact's own nature fixes which document, composition that was designed going to APPROACH and interaction that implementation revealed going to FINDINGS.

**A parent names what a child elaborates, and stops.** A parent whose problem decomposes has to state the parts in order to state its own problem at all, so some restatement is inherent and is not duplication. What is duplication is the parent continuing past naming a part into explaining it — describing *why* a child's problem is hard, or how it is solved, in the parent's own words. The line is that a reader of the parent should learn that the part exists and where it fits; a reader who wants to know what makes it hard goes to the child. When the same explanation would be at home in either document, it belongs in the child.

**An open question belongs to exactly one unit: the one whose work would resolve it.** The same question standing in a parent and a child means neither owns it, and both copies will drift as the answer develops. Ask which unit's session would close the question, and put it there.

**Log routing** is the same rule applied to lineage. A session logs to the nearest common ancestor of the units its work concerned — not every unit it read: one that worked inside a single unit logs there, one whose work crossed units logs above them, however far apart in the tree they sit.

**Declared reference exemptions**, stated per doctype so the table stays fixed-size at any component count or depth:

| Doctype | May reference | Why |
|---|---|---|
| `<TOKEN>_SCOPE.md` | its parent's SCOPE only | A component's problem is part of the problem its parent states, which precedes and outlives it. The hub's SCOPE has no parent and so references nothing. |
| `<TOKEN>_APPROACH.md` | its own SCOPE and its parent's APPROACH | A design answers its own problem and the design it composes into — both upstream. |
| `<TOKEN>_FINDINGS.md` | *none* | Implementation decisions downstream of the approach, with nothing upstream to cite. |
| Any document | its own sub-components **by name**, never their files | Naming a part of your own subject is not a downstream reference; reaching into that part's documents is. |

Two classes stand outside the table. **Logs** record what a session touched, filenames included, so naming another unit's documents is their job. **Maintenance and procedure documents** name the knowledge files they operate on, which is inherent to being a procedure.

---

## 5. Restructuring

The first three migrations preserve every knowledge document's filename, so no cross-reference resolves differently and no log is rewritten; their real work is authoring the documents the new shape requires, named per row. Maintenance documents are the exception: they live at the hub under its token, so the one migration that gives the hub a new token renames them to it. The last two need no new SCOPE, and collapsing to one problem is the single case that retires knowledge filenames, since folding the hub's documents into the survivor leaves one set of names standing.

A **flat platform split** is the base pattern's convention for one problem delivered across several targets: documents that differ per target take a leading platform qualifier and shared ones do not, with no directories involved.

| From | To | The move |
|---|---|---|
| One problem | Components | `git mv` the knowledge documents into a component directory — the brain's token, now taken, becomes that component's — then declare a fresh hub token, rename the maintenance documents (and the hub references inside them) to it, author the hub's documents at the root, and replace the entrypoint's file table with the four parts in §3. |
| Flat platform split | Components | Move each platform's documents into a directory named for it and declare its existing compound prefix as that component's token. Shared documents stay at the root as the parent, whose token is unchanged. Author each new unit's missing doctypes — a platform family typically arrives with findings and a log but no SCOPE or APPROACH of its own. |
| Component | Sub-components | The component gains child directories, each seeded with its full doctype set; its own documents stay put and become the parent layer, ceding to each child the content that was really that child's. |
| Components | One problem | The reverse of the first, folding the hub's documents into the last remaining component. |
| Component | Its own brain | `git mv` the directory to a new repository and replace its registry row with a pointer. The subtree already carries its `working/` and `archive/`, so it moves whole. |

---

## 6. Noticing that a unit should have split

The component test runs when a brain is created and is easy never to run again. A brain that should have split is internally consistent either way, so no structural check can see the omission — the shared SCOPE it ends up with looks settled rather than provisional.

**A port is the tell.** When a unit finds itself authoring one target's documents first and porting a second target against them, those targets hold different problems. The porting is what a single SCOPE looks like when it is really one target's SCOPE wearing a shared name.

The signal is never volume. How much a unit accumulates depends on how tightly its components couple, not on whether the split was right — a parent whose APPROACH stays short may simply own components that rarely touch. Re-run the test when the test itself stops discriminating, never because a document came out thinner than expected.
