# <Project>: Mini-Brain Files

> V1, <date>.

The hub's namespace token is `<PREFIX>`. Each component declares its own in the registry below.

---

## Read Index

All paths are relative to this repo root (`CLAUDE.md`'s directory). Before reading, state which files in one line and read them the same turn (not a permission request). Read only what the question needs.

### Hub documents

| Purpose | File |
|---|---|
| Problem definition, the world it exists in, goals — the system as a whole | `<PREFIX>_SCOPE.md` |
| How the components compose, and the decisions spanning them | `<PREFIX>_APPROACH.md` |
| Findings that cross components (invisible from code) | `<PREFIX>_FINDINGS.md` |
| Session log for hub work and sessions that crossed components | `<PREFIX>_LOG.md` (read from last `---`; large) |
| Session log update format and rules | `<PREFIX>_SESSION_CLOSEOUT.md` (read when asked to update a session log) |

These are the current hub documents. Components' documents are **resolved** from the grammar and registry below rather than listed — a document not derivable that way does not exist.

<!-- As the brain matures, add the lifecycle docs to this index:
| Work setup — scaffold a work item's working docs | `<PREFIX>_WORK_SETUP.md` |
| Work closeout — fold working docs into the mini-brain | `<PREFIX>_WORK_CLOSEOUT.md` |
| Periodic health check and content refresh | `<PREFIX>_DREAM_CYCLE.md` |
| Dream cycle session log | `<PREFIX>_DREAM_LOG.md` |
-->

### Doctype grammar

Every component directory carries all four, where `<TOKEN>` is that component's declared token:

| Doctype | Holds |
|---|---|
| `<TOKEN>_SCOPE.md` | That unit's problem, the world it exists in, goals — objective, solution-free. |
| `<TOKEN>_APPROACH.md` | That unit's chosen design, including how its own sub-components compose. |
| `<TOKEN>_FINDINGS.md` | Implementation findings invisible from its code. |
| `<TOKEN>_LOG.md` | Append-only session log for work that stayed inside that unit (read from last `---`; large). |

A component may carry more; anything beyond these four is named in its **Also holds** cell. When that cell outgrows a line or two, the component earns its own `<TOKEN>_CLAUDE.md` read index — never a bare `CLAUDE.md`, which a harness would load unbidden — and the cell becomes a pointer to it.

### Component registry

| Component | Directory | Token | Routes on | Also holds | Project repo |
|---|---|---|---|---|---|
| <Component> | `<dir>/` | `<TOKEN>` | the terms that should send a question here | — | `../<repo>` |
| — <Sub-component> | `<dir>/<sub>/` | `<SUBTOKEN>` | … | — | `../<repo>/<path>` |

Match a question's terms against **Routes on** to choose a component *before* reading anything. A question about how components fit together, or one no component's terms claim, is hub-level — start at the hub documents. Sub-components are indented under their parent. A component whose code lives inside an ancestor's repository points its project-repo cell at that path (`../<repo>/<path>`); leave the cell empty for a component with no repository presence at all.

`archive/` holds source material and retired docs — not in-tree version snapshots; ignore unless asked. `working/` holds experiments and in-flight work-item docs; when a work item concludes, fold them into the canonical docs and **move** (not delete) them to the owning unit's `archive/`. Every unit owns its own pair — the hub's sit at the repo root from seeding; a component creates its own when it first needs them. Seed-time source material all lands in the hub's `archive/`, whichever component it describes.

---

## File Conventions

**File naming.** Every filename follows `[<path>/] [working/] <TOKEN> [_<WORK>] _<DOCTYPE>.md` — directories carve components, the trailing slot carves work items. Hub documents take no path and use `<PREFIX>`. `CLAUDE.md` and `README.md` are exempt. Because each token is *declared* rather than inferred, a token may contain underscores; it is one token, not a shorter token plus a qualifier.

**Token ownership.** A document belongs to the unit whose declared token its name begins with in full, longest match winning. Tokens may nest as prefixes, so a shorter token matching proves nothing — a document whose name begins with a child's token is misplaced if it sits in the parent's directory. Ownership constrains naming in return: never name a document so that another unit's token is a longer prefix of its name than the owning unit's — a parent's work-item slug that continues into a child's token hands the item's files to that child.

**Working and archive.** A unit's `working/` inherits that unit's token, so in-flight documents stay as parseable as canonical ones. A unit's `archive/` does not: retired files keep the basename they were retired under and need not be markdown.

**Append-only logs.** LOG files are never archived and never edited after the fact. Append-only governs an entry's content, not its position: once written, an entry is never revised, split, or merged. New entries go at the end. The one exception is folding another log into this one, which places that log's entries whole and in date order among the existing ones, so the last separator still holds the most recently written entry.

**Maintenance documents live at the hub.** Session closeout — and work setup, work closeout and the dream cycle when the brain grows them — govern the whole brain, so one of each serves every unit and none is namespaced to a component. The in-flight documents those procedures scaffold land in the `working/` of whichever unit owns the work.

<!-- As the brain matures and gains the lifecycle docs, add their boundary rule:
**Maintenance-doc boundaries.** Any procedure that appends a log entry cites `<PREFIX>_SESSION_CLOSEOUT.md` as the entry-format authority. Beyond that, `<PREFIX>_DREAM_CYCLE.md` references no other maintenance doc, and `<PREFIX>_WORK_SETUP.md` / `<PREFIX>_WORK_CLOSEOUT.md` are bookends that may reference each other, but only by that relationship.
-->

**Version header.** Every canonical document opens with `> V<N>, YYYY-MM-DD.` — version and date, nothing else. **No change note in this line.** If a file needs a description, put it on its own line below. Bump `<N>` by one on each substantive edit (numerically — `V10` > `V9`) and set the date. This applies to `CLAUDE.md` itself. Exempt: `README.md`, `*_LOG.md` files, and `*_TASKS.md` checklists.

**Classify every edit:** *editorial* (typos, rewording) — edit in place, don't bump `<N>`, may update date; *substantive* (facts, decisions, scope, structure) — set the version line to `> V<N+1>, <today's date>.` No change note in the line.

**Cross-references.** Cite the canonical filename, never a retired copy in `archive/`. Reference a file's *own* sections freely (`§2`, "the section below"); reference *another* file by name plus a short description of what's there — never by its section number, since foreign section numbers break silently on renumber.

**Orthogonal content.** Each file covers one concern and tells its own story — keep that orthogonality in the *prose*, not just the file boundaries. A file describes its own subject, never narrating a sibling's. State how a file relates to the others **once**, in its header (the read index carries the rest), then stop pointing sideways. Wiki-style narration — "the data for this lives in X," "see Y," "as covered in Z" — keeps creeping in; resist it: it re-couples files that are meant to stand alone, and rots when they move.

**Placement.** A fact about two units belongs to their nearest common ancestor. Sibling references are forbidden — a sibling is neither upstream nor downstream — so knowledge spanning two components lives in the unit above them and never in either one. Name the units a fact concerns and walk up to where they meet: the ancestor fixes which unit holds it, and the fact's own nature fixes which document, composition that was designed going to APPROACH and interaction that implementation revealed going to FINDINGS.

**A parent names what a child elaborates, and stops.** A parent whose problem decomposes has to state the parts in order to state its own problem at all, so some restatement is inherent and is not duplication. What is duplication is the parent continuing past naming a part into explaining it — describing *why* a child's problem is hard, or how it is solved, in the parent's own words. The line is that a reader of the parent should learn that the part exists and where it fits; a reader who wants to know what makes it hard goes to the child. When the same explanation would be at home in either document, it belongs in the child.

**An open question belongs to exactly one unit: the one whose work would resolve it.** The same question standing in a parent and a child means neither owns it, and both copies will drift as the answer develops. Ask which unit's session would close the question, and put it there.

**Log routing** is the same rule applied to lineage. A session logs to the nearest common ancestor of the units its work concerned — not every unit it read: one that worked inside a single unit logs there, one whose work crossed units logs above them, however far apart in the tree they sit.

**Declared reference exemptions.** Orthogonality is the default and it is strict: a knowledge file names *no* sibling and stands on its own. A cross-file reference exists only where an exemption is declared, and an exemption may only point *upstream* — toward the problem a file serves — never *downstream* toward how it was built. A downstream reference is never exemptable; that invariant is what stops content bleed-through. Stated per doctype, so this table stays the same size at any component count or depth:

| Doctype | May reference | Why |
|---|---|---|
| `<TOKEN>_SCOPE.md` | its parent's SCOPE only | A component's problem is part of the problem its parent states, which precedes and outlives it. The hub's SCOPE has no parent and so references nothing. |
| `<TOKEN>_APPROACH.md` | its own SCOPE and its parent's APPROACH | A design answers its own problem and the design it composes into — both upstream. |
| `<TOKEN>_FINDINGS.md` | *none* | Implementation decisions downstream of the approach, with nothing upstream to cite. |
| Any document | its own sub-components **by name**, never their files | Naming a part of your own subject is not a downstream reference; reaching into that part's documents is. |

A permitted reference still follows the Cross-references rule above — cited by name, never by section number. Two classes stand outside the table. **Logs** record what a session touched, filenames included, so naming another unit's documents is their job. **Maintenance and procedure documents** name the knowledge files they operate on, which is inherent to being a procedure.

**No harness memory.** Don't use the persistent memory feature. All persistent project information belongs in the markdown files in this directory.

---

## Writing Docs and Instructions

All prose in this repo is read like a proof or a program, not a wiki. The reader is adversarial: every token is load-bearing, and every spare one is a question they must resolve.

- **Say it once.** Each fact has exactly one home. Duplication isn't emphasis; it's a second copy to keep in sync and a sign the first statement didn't land.
- **Define before use.** Introduce a thing where the reader first needs it, in dependency order. A forward pointer ("see Step 3", "as below") means the content is in the wrong place — move it, don't link to it.
- **No sideways narration.** A section explains its own subject and never recaps a sibling section's; pointing (`§3`) is fine, restating is not. Across files, the Orthogonal content rule above governs.
- **Every claim earns its keep.** State only what the reader must act on and what you could defend if challenged. Decorative rationale, benefits, and history are cut.
- **Resolve, don't provoke.** A detail that raises a question it doesn't answer is a net loss — prefer omission to a half-explanation.
- **One job per sentence.** A sentence tells the reader what to do or explains why — never several at once.
- **No hard wrapping.** Write each markdown paragraph and list item as one continuous line and let it soft-wrap; manual line breaks inside a paragraph make noisy diffs and fight reflow.

When a line's contribution isn't obvious, it isn't contributing — delete it.
