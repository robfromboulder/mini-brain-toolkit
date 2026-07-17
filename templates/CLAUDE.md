# <Project>: Mini-Brain Files

> V1, <date>.

---

## Read Index

All paths are relative to this repo root (`CLAUDE.md`'s directory). Before reading, state which files in one line and read them the same turn (not a permission request). Read only what the question needs.

| Purpose | File |
|---|---|
| Problem definition, current state, goals | `<PREFIX>_SCOPE.md` |
| Technical approach, what we build | `<PREFIX>_APPROACH.md` |
| Key implementation findings (invisible from code) | `<PREFIX>_FINDINGS.md` |
| Session log — why we chose what we chose | `<PREFIX>_LOG.md` (read from last `---`; large) |
| Session log update format and rules | `<PREFIX>_SESSION_CLOSEOUT.md` (read when asked to update the session log) |

Only files in this table are current. `archive/` holds source material, retired/absorbed docs, and closed work-item working files — ignore it unless asked.

`working/` holds experiments and a work item's in-flight `<WORK>_*` docs. When a work item concludes, fold them into the canonical docs and **move** (not delete) them to `archive/`.

<!-- As the brain matures (see MBT_CREATE_BRAIN.md §5), add the lifecycle docs to this index:
| Work setup — scaffold a work item's working docs | `<PREFIX>_WORK_SETUP.md` |
| Work closeout — fold working docs into the mini-brain | `<PREFIX>_WORK_CLOSEOUT.md` |
| Periodic health check and content refresh | `<PREFIX>_DREAM_CYCLE.md` |
| Dream cycle session log | `<PREFIX>_DREAM_LOG.md` |
-->

---

## File Conventions

**Top-level vs archive.** A top-level file is the canonical current version; its history lives in version control. `archive/` is a stash for source material and retired/absorbed docs — not in-tree version snapshots. LOG files are append-only — never archived.

**File naming.** Every mini-brain filename carries the `<PREFIX>` namespace token — shared docs as `<PREFIX>_*`. Two files are exempt: `CLAUDE.md` (entrypoint) and `README.md` (repo artifact). New top-level knowledge files must include the token; files in `archive/` keep whatever basename they were retired under.

**Version header.** Every top-level file except the version-exempt ones opens with `> V<N>, YYYY-MM-DD.` — version and date, nothing else. **No change note in this line.** If a file needs a description, put it on its own line below. Bump `<N>` by one on each substantive edit (numerically — `V10` > `V9`) and set the date. This applies to `CLAUDE.md` itself. Exempt: `README.md`, `*_LOG.md` files, and `*_TASKS.md` checklists.

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
**Maintenance-doc boundaries.** `<PREFIX>_DREAM_CYCLE.md` is standalone — it references no other maintenance doc. `<PREFIX>_WORK_SETUP.md` and `<PREFIX>_WORK_CLOSEOUT.md` are bookends and may reference each other, but only by that relationship.
-->

**No harness memory.** Don't use the persistent memory feature. All persistent project information belongs in the markdown files in this directory.
