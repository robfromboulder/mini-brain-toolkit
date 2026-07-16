# Mini-Brain Toolkit: Mini-Brain Files

> V7, 2026-07-15.

---

## Read Index

All paths are relative to this repo root (`CLAUDE.md`'s directory). Before reading, state which files in one line and read them the same turn (not a permission request). Read only what the question needs.

| Purpose | File |
|---|---|
| What a mini-brain is — principles, file set, lifecycle | `MBT_PATTERN.md` |
| Procedure: create a new mini-brain | `MBT_CREATE_BRAIN.md` |
| Procedure: check an existing mini-brain against the pattern | `MBT_CHECK_BRAIN.md` |
| Research agenda — where the pattern could go, and how it compares to related work | `MBT_RESEARCH.md` |
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

**Cross-references.** Always cite the canonical top-level filename, never a retired copy in `archive/`.

**No harness memory.** Don't use the persistent memory feature. All persistent project information belongs in the markdown files in this directory.