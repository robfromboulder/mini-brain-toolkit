# <Project>: Session Closeout Instructions

> V1, <date>.

---

Governs `<PREFIX>_LOG.md` (and each feature's working `<FEATURE>_LOG.md`, once the brain has feature machinery). **This format is the authority; do not imitate the previous entry** — a fresh file has none, and copying a neighbor lets the structure drift one merge at a time. Match sibling entries only where this spec is silent.

**Purpose.** The log is the work's lineage, traceable to each coding session, and the home for what **cannot be deduced from the codebase alone**: key findings, decision points (and who made each call), what was tried and didn't work, and the course-corrections that kept the work on track. It's a log, not a design doc — don't restate scope or strategy; give the turn-by-turn account of each session start to finish and what was learned.

**Reading** (never read this large file in full): `grep -n '^---$' <PREFIX>_LOG.md | tail -1` gives the last separator's line `L`; read from `offset` `L`.

**Appending:**
1. Add a `---` at the end of the file, then the entry below it. **Append only — never revise or correct prior sessions.**
2. Entry shape: an H1 with a short title and date (`# <title> (YYYY-MM-DD)`); a `` **Session ID**: `<uuid>` `` line; a one-paragraph lead (what the session set out to do and what landed); then `##` subsections for the turn-by-turn lineage, decisions, what didn't work, and lessons — chosen per session, not a fixed template.
3. Session ID = newest transcript filename minus `.jsonl`, taken from the current session's project dir under `~/.claude/projects/`. That dir is derived from the directory the session was launched in: implementation work runs from the product repo and logs there; mini-brain-only work runs from this repo and logs under its own project dir. Pick the transcript for the session you're recording — e.g. `ls -t ~/.claude/projects/<this-session's-project-dir>/*.jsonl | head -1`. Ask if it can't be determined.

**Content rules:** trace the lineage turn-by-turn (don't summarize the destination); class/method names are fine but no line numbers or other drift-prone specifics; skip anything re-derivable from the codebase; don't restate feature scope or implementation strategy.
