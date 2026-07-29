# Mini-Brain Toolkit: Session Closeout Instructions

> V3, 2026-07-29.

---

Governs session log entries in both `MBT_LOG.md` and any work item's `working/<PREFIX>_LOG.md` — the entry format and content rules are the same regardless of destination. **This format is the authority; do not imitate the previous entry** — a fresh file has none, and copying a neighbor lets the structure drift one merge at a time. Match sibling entries only where this spec is silent.

**Purpose.** The log is the work's lineage, traceable to each coding session, and the home for what **cannot be deduced from the files alone**: key findings, decision points (and who made each call), what was tried and didn't work, and the course-corrections that kept the work on track. It's a log, not a design doc — don't restate scope or strategy; give the turn-by-turn account of each session start to finish and what was learned.

**Routing — which log file to append to.** A session that belongs to an open work item — its `<PREFIX>_*` docs still in `working/`, even if the change they track has already landed — appends to that item's `working/<PREFIX>_LOG.md` (create it if the item lacks one); all other sessions append to `MBT_LOG.md`. Resolve ownership by the first matching signal, in priority order:

1. **Explicit direction** — the user names a target log or work item.
2. **Session content** — the session's work advances an open work item: its `working/<PREFIX>_*` docs or the change they track.
3. **No match** — append to `MBT_LOG.md`.

When the session spans an open work item and other work, or could belong to more than one open item, ask rather than guess. The session that folds a concluded work item into the canonical docs appends to `MBT_LOG.md`: the item's working log is merged and moved to `archive/` in that same pass, so a fresh entry there would land in `archive/` unmerged.

**Reading** (never read these large files in full): `grep -n '^---$' <log-file> | tail -1` gives the last separator's line `L`; read from `offset` `L`.

**Appending:**
1. Determine the target log file using the routing rule above.
2. Add a `---` at the end of that file, then the entry below it. **Append only — never revise or correct prior sessions.**
3. Entry shape: an H1 with a short title and date (`# <title> (YYYY-MM-DD)`); a `` **Session ID**: `<uuid>` `` line; a one-paragraph lead (what the session set out to do and what landed); then `##` subsections for the turn-by-turn lineage, decisions, what didn't work, and lessons — chosen per session, not a fixed template.
4. Session ID = newest transcript filename minus `.jsonl`, taken from the current session's project dir under `~/.claude/projects/`. This repo is the mini-brain itself, so its transcripts live under this repo's own project dir — e.g. `ls -t ~/.claude/projects/-Users-rob-dickinson-Projects-robfromboulder-mini-brain-toolkit/*.jsonl | head -1`. Ask if it can't be determined.

**Content rules:** trace the lineage turn-by-turn (don't summarize the destination); filenames and section names are fine but no line numbers, no cross-document section or finding numbers (`§N`, "finding #N"), and no other drift-prone specifics — reference decisions and findings by their substance, which stays readable as the docs are renumbered and re-homed; skip anything re-derivable from the files themselves; don't restate scope or approach.

**Name the people.** The entry must make clear whose session it was: the lead names the human author (with Claude as co-author), and decisions stay attributed to whoever made each call. Don't lean on the Session ID to carry this — it's an opaque UUID.
