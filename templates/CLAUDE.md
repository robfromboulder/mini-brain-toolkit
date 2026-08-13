# <Project>: Mini-Brain Files

> V1, <date>.

---

## Read Index

All paths are relative to this repo root (`CLAUDE.md`'s directory). Before reading, state which files in one line and read them the same turn (not a permission request). Read only what the question needs.

| Purpose | File |
|---|---|
| Problem definition, the world it exists in, goals | `<PREFIX>_SCOPE.md` |
| Technical approach, what we build | `<PREFIX>_APPROACH.md` |
| Key implementation findings (invisible from code) | `<PREFIX>_FINDINGS.md` |
| Session log — why we chose what we chose | `<PREFIX>_LOG.md` (read from last `---`; large) |
| Session log update format and rules | `<PREFIX>_SESSION_CLOSEOUT.md` (read when asked to update the session log) |

Only files in this table are current. `archive/` holds source material, retired/absorbed docs, and retired work-item working files — ignore it unless asked.

`working/` holds experiments and a work item's in-flight `<PREFIX>_<WORK>_*` docs. When a work item concludes, fold them into the canonical docs and **move** (not delete) them to `archive/`. The item's PLAN, once consumed (converted to code), may move there early at the developer's request — walk its significant unaddressed items with the developer first.

<!-- As the brain matures, add the lifecycle docs to this index:
| Work setup — scaffold a work item's working docs | `<PREFIX>_WORK_SETUP.md` |
| Work closeout — fold working docs into the mini-brain | `<PREFIX>_WORK_CLOSEOUT.md` |
| Periodic health check and content refresh | `<PREFIX>_DREAM_CYCLE.md` |
| Dream cycle session log | `<PREFIX>_DREAM_LOG.md` |
-->

---

## File Conventions

**Top-level vs archive.** A top-level file is the canonical current version; its history lives in version control. `archive/` is a stash for source material and retired/absorbed docs — not in-tree version snapshots.

**Append-only logs.** LOG files are never archived and never edited after the fact. Append-only governs an entry's content, not its position: once written, an entry is never revised, split, or merged. New entries go at the end. The one exception is folding another log into this one, which places that log's entries whole and in date order among the existing ones, so the last separator still holds the most recently written entry.

**File naming.** Every mini-brain filename carries the `<PREFIX>` namespace token — shared docs as `<PREFIX>_*`. Two files are exempt: `CLAUDE.md` (entrypoint) and `README.md` (repo artifact). New top-level knowledge files must include the token; files in `archive/` keep whatever basename they were retired under.

**Version header.** Every top-level file except the version-exempt ones opens with `> V<N>, YYYY-MM-DD.` — version and date, nothing else. **No change note in this line.** If a file needs a description, put it on its own line below. Bump `<N>` by one on each substantive edit (numerically — `V10` > `V9`) and set the date. This applies to `CLAUDE.md` itself. Exempt: `README.md`, `*_LOG.md` files, and `*_BURNDOWN.md` checklists.

**Classify every edit:** *editorial* (typos, rewording) — edit in place, don't bump `<N>`, may update date; *substantive* (facts, decisions, scope, structure) — set the version line to `> V<N+1>, <today's date>.` No change note in the line.

**Cross-references.** Cite the canonical top-level filename, never a retired copy in `archive/`. Reference a file's *own* sections freely (`§2`, "the section below"); reference *another* file by name plus a short description of what's there — never by its section number ("the constraints in `<PREFIX>_SCOPE.md`," not "`<PREFIX>_SCOPE.md` §2"), since foreign section numbers break silently on renumber.

**Orthogonal content.** Each mini-brain file covers one concern and tells its own story — keep that orthogonality in the *prose*, not just the file boundaries. A file describes its own subject, never narrating a sibling's (`<PREFIX>_SCOPE.md` states the problem; it does not recap the design that lives in `<PREFIX>_APPROACH.md`). State how a file relates to the others **once**, in its header (the read index carries the rest), then stop pointing sideways. Wiki-style narration — "the data for this lives in X," "see Y," "as covered in Z" — keeps creeping in; resist it: it re-couples files that are meant to stand alone, and rots when they move. Keep the content (what a file holds and why); cut the running navigation.

**Declared reference exemptions (project-specific).** Orthogonality is the default and it is strict: a knowledge file names *no* sibling and stands on its own. A cross-file reference exists only where this project **declares an exemption**, and an exemption may only point *upstream* — toward the problem a file serves — never *downstream* toward how it was built. A downstream reference is never exemptable; that invariant is what stops content bleed-through. This mini-brain's core design docs and their declared exemptions:

| File | May reference | Why |
|---|---|---|
| `<PREFIX>_SCOPE.md` | *none* | The problem statement stands alone; it precedes and outlives any design. |
| `<PREFIX>_APPROACH.md` | `<PREFIX>_SCOPE.md` only | A design legitimately responds to the problem it addresses — never reaching down into implementation. |
| `<PREFIX>_FINDINGS.md` | *none* | Implementation decisions that did *not* shape the approach — downstream of it, so nothing upstream to cite. |

Absent a declared exemption, full orthogonality holds; add a row here only when the brain grows a knowledge doc that genuinely needs one. A permitted reference still follows the Cross-references rule above — cited by name, never by section number.

<!-- As the brain matures and gains the lifecycle docs, add their boundary rule:
**Maintenance-doc boundaries.** Any procedure that appends a log entry cites `<PREFIX>_SESSION_CLOSEOUT.md` as the entry-format authority. Beyond that, `<PREFIX>_DREAM_CYCLE.md` references no other maintenance doc, and `<PREFIX>_WORK_SETUP.md` / `<PREFIX>_WORK_CLOSEOUT.md` are bookends that may reference each other, but only by that relationship.
-->

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
