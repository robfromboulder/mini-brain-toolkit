# Mini-Brain Toolkit: Session Closeout Instructions

> V2, 2026-07-17.

---

Governs `MBT_LOG.md`. **This format is the authority; do not imitate the previous entry** — a fresh file has none, and copying a neighbor lets the structure drift one merge at a time. Match sibling entries only where this spec is silent.

**Purpose.** The log is the work's lineage, traceable to each coding session, and the home for what **cannot be deduced from the files alone**: key findings, decision points (and who made each call), what was tried and didn't work, and the course-corrections that kept the work on track. It's a log, not a design doc — don't restate scope or strategy; give the turn-by-turn account of each session start to finish and what was learned.

**Reading** (never read this large file in full): `grep -n '^---$' MBT_LOG.md | tail -1` gives the last separator's line `L`; read from `offset` `L`.

**Appending:**
1. Add a `---` at the end of the file, then the entry below it. **Append only — never revise or correct prior sessions.**
2. Entry shape: an H1 with a short title and date (`# <title> (YYYY-MM-DD)`); a `` **Session ID**: `<uuid>` `` line; a one-paragraph lead (what the session set out to do and what landed); then `##` subsections for the turn-by-turn lineage, decisions, what didn't work, and lessons — chosen per session, not a fixed template.
3. Session ID = newest transcript filename minus `.jsonl`, taken from the current session's project dir under `~/.claude/projects/`. This repo is the mini-brain itself, so work on it logs under this repo's own project dir — e.g. `ls -t ~/.claude/projects/-Users-rob-dickinson-Projects-robfromboulder-mini-brain-toolkit/*.jsonl | head -1`. Ask if it can't be determined.

**Content rules:** trace the lineage turn-by-turn (don't summarize the destination); filenames and section names are fine but no line numbers, no cross-document section or finding numbers (`§N`, "finding #N"), and no other drift-prone specifics — reference decisions and findings by their substance, which stays readable as the docs are renumbered and re-homed; skip anything re-derivable from the files themselves; don't restate scope or approach.

**Name the people.** The entry must make clear whose session it was: the lead names the human author (with Claude as co-author), and decisions stay attributed to whoever made each call. Don't lean on the Session ID to carry this — it's an opaque UUID.
