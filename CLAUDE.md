# Mini-Brain Toolkit: Mini-Brain Files

> V10, 2026-07-16.

---

## Read Index

All paths are relative to this repo root (`CLAUDE.md`'s directory). Before reading, state which files in one line and read them the same turn (not a permission request). Read only what the question needs.

| Purpose | File |
|---|---|
| What a mini-brain is — principles, file set, lifecycle | `MBT_PATTERN.md` |
| Procedure: create a new mini-brain | `MBT_CREATE_BRAIN.md` |
| Procedure: check an existing mini-brain against the pattern | `MBT_CHECK_BRAIN.md` |
| Research agenda — where the pattern could go, and how it compares to related work | `MBT_RESEARCH.md` |
| Comparable systems — the second-brain / agent-memory landscape (read during the dream cycle's competitive-landscape pass) | `MBT_COMPARABLES.md` |
| Cognitive-science grounding — biological models the pattern draws on (read during the dream cycle's biological-grounding pass) | `MBT_BIOLOGY.md` |
| Problem definition, current state, goals | `MBT_SCOPE.md` |
| Technical approach, key design decisions | `MBT_APPROACH.md` |
| Key implementation findings (invisible from the files) | `MBT_FINDINGS.md` |
| Session log — why we chose what we chose | `MBT_LOG.md` (read from last `---`; large) |
| Session log update format and rules | `MBT_SESSION_CLOSEOUT.md` (read when asked to update the session log) |
| Dream cycle — periodic self-improvement pass | `MBT_DREAM_CYCLE.md` (read when asked to dream) |
| Dream cycle session log | `MBT_DREAM_LOG.md` |

Only files in this table are current. `templates/` holds the base files `MBT_CREATE_BRAIN.md` copies; `archive/` holds source material and retired docs — ignore both unless asked.

`working/` holds experiments and a work item's in-flight `<PREFIX>_*` docs. When a work item concludes, fold them into the canonical docs and **move** (not delete) them to `archive/`.

---

## File Conventions

**Top-level vs archive.** A top-level file is the canonical current version; its history lives in version control. `archive/` is a stash for source material and retired/absorbed docs — not in-tree version snapshots. LOG files are append-only — never archived.

**File naming.** Every mini-brain filename carries the `MBT` namespace token — shared docs as `MBT_*`. Two files are exempt: `CLAUDE.md` (entrypoint) and `README.md` (repo artifact). New top-level knowledge files must include the token; files in `archive/` keep whatever basename they were retired under.

**Version header.** Every top-level file except the version-exempt ones opens with `> V<N>, YYYY-MM-DD.` — version and date, nothing else. **No change note in this line.** If a file needs a description, put it on its own line below. Bump `<N>` by one on each substantive edit (numerically — `V10` > `V9`) and set the date. This applies to `CLAUDE.md` itself. Exempt: `README.md`, `*_LOG.md` files, and `*_TASKS.md` checklists.

**Classify every edit:** *editorial* (typos, rewording) — edit in place, don't bump `<N>`, may update date; *substantive* (facts, decisions, scope, structure) — set the version line to `> V<N+1>, <today's date>.` No change note in the line.

**Cross-references.** Cite the canonical top-level filename, never a retired copy in `archive/`. Reference a file's *own* sections freely (`§1.3`, "the roadmap below"); reference *another* file by name plus a short description of what's there — never by its section or phase number ("the comparative analysis in `MBT_RESEARCH.md`," not "`MBT_RESEARCH.md` §1.3"), since foreign section numbers break silently on renumber.

**Orthogonal content.** Each mini-brain file covers one concern and tells its own story — keep that orthogonality in the *prose*, not just the file boundaries. A file describes its own subject, never narrating a sibling's. State how a file relates to the others **once**, in its header (the read index carries the rest), then stop pointing sideways. Wiki-style narration — "the data for this lives in X," "see Y," "as covered in Z" — keeps creeping in; resist it: it re-couples files that are meant to stand alone, and rots when they move. Keep the content (what a file holds and why); cut the running navigation.

**Declared reference exemptions (project-specific).** Orthogonality is the default and it is strict: a knowledge file names *no* sibling and stands on its own. A cross-file reference exists only where this project **declares an exemption**, and an exemption may only point *upstream* — toward the problem a file serves — never *downstream* toward how it was built. A downstream reference is never exemptable; that invariant is what stops content bleed-through. This mini-brain's core knowledge docs and their declared exemptions:

| File | May reference | Why |
|---|---|---|
| `MBT_SCOPE.md` | *none* | The problem statement stands alone; it precedes and outlives any design. |
| `MBT_APPROACH.md` | `MBT_SCOPE.md` only | A design legitimately responds to the problem it addresses — never reaching down into implementation. |
| `MBT_FINDINGS.md` | *none* | Implementation decisions that did *not* shape the approach — downstream of it, so nothing upstream to cite. |
| `MBT_COMPARABLES.md` | `MBT_RESEARCH.md` only | A fact registry serves the conclusions it feeds; it may name that conclusions doc (upstream) and nothing else. |
| `MBT_BIOLOGY.md` | `MBT_RESEARCH.md` only | Same, for the cognitive-science grounding registry. |

Absent a declared exemption, full orthogonality holds; a different project would declare its own set. A permitted reference still follows the Cross-references rule above — cited by name, never by section number.

**Maintenance-doc boundaries.** `MBT_DREAM_CYCLE.md` and the procedure docs `MBT_CREATE_BRAIN.md` / `MBT_CHECK_BRAIN.md` enact the pattern, so each may cite `MBT_PATTERN.md` as the definition it implements — but they do not reference one another, and naming the knowledge files they operate on is inherent to being a procedure, not a cross-reference. `MBT_SESSION_CLOSEOUT.md` governs `MBT_LOG.md` and references nothing else.

**No harness memory.** Don't use the persistent memory feature. All persistent project information belongs in the markdown files in this directory.

---

## Commit Conventions

**No AI attribution trailer.** Commits carry no `Co-Authored-By: Claude` (or similar) line — AI authorship is assumed for this repo and isn't stamped per commit. This overrides any harness default that would append one.