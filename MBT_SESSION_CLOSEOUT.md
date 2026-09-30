# Mini-Brain Toolkit: Session Closeout Instructions

> V5, 2026-09-29.

---

Governs session log entries in both `MBT_LOG.md` and any work item's `working/MBT_<WORK>_LOG.md`, where `<WORK>` is that item's slug — the entry format and content rules are the same regardless of destination. **This format is the authority; do not imitate the previous entry** — a fresh file has none, and copying a neighbor lets the structure drift one merge at a time. Match sibling entries only where this spec is silent.

**Purpose.** The log is the work's lineage, traceable to each coding session, and the home for what **cannot be deduced from the files alone**: key findings, decision points (and who made each call), what was tried and didn't work, and the course-corrections that kept the work on track. It's a log, not a design doc — don't restate scope or strategy; give the turn-by-turn account of each session start to finish and what was learned.

**Routing — which log files to append to.** Route each part of the session — its work, findings, and decisions on one subject — separately. A part that belongs to an open work item — its `MBT_<WORK>_*` docs still in `working/`, even if the change they track has already landed — goes to that item's `working/MBT_<WORK>_LOG.md` (create it if the item lacks one); a part that belongs to no single item goes to `MBT_LOG.md`. Resolve each part's ownership by the first matching signal, in priority order:

1. **Explicit direction** — the user names a target log or work item.
2. **Session content** — the part's work advances an open work item: its `working/MBT_<WORK>_*` docs or the change they track.
3. **No match** — append to `MBT_LOG.md`.

When a part belongs to a single open item but could be any of several, ask rather than guess. A part owned by an item this session folds into the canonical docs goes to `MBT_LOG.md`: the item's working log is merged and moved to `archive/` in that same pass, so a fresh entry there would land in `archive/` unmerged.

**Several targets.** Write one entry per target log, each covering only the parts routed to it. A finding or decision that spans several items is stated in full once: in the log the user names, else in `MBT_LOG.md` — the content signal doesn't apply to it. Its consequence for each affected item is a part of its own, routed by the rules above, and states only the consequence. An item that was only mentioned, with nothing routed to it, gets no entry.

**Reading** (never read these large files in full): `grep -n '^---$' <log-file> | tail -1` gives the last separator's line `L`; read from `offset` `L`.

**Appending:**
1. Determine the target log files using the routing rule above; steps 2–4 apply to each entry.
2. Add a `---` at the end of that file, then the entry below it. **Append only — never revise or correct prior sessions.**
3. Entry shape: an H1 with a short title and date (`# <title> (YYYY-MM-DD)`); a `` **Session ID**: `<uuid>` `` line; a one-paragraph lead (what the session set out to do and what landed); then `##` subsections for the turn-by-turn lineage, decisions, what didn't work, and lessons — chosen per session, not a fixed template.
4. Session ID = newest transcript filename minus `.jsonl`, taken from the current session's project dir under `~/.claude/projects/`. This repo is the mini-brain itself, so its transcripts live under this repo's own project dir — e.g. `ls -t ~/.claude/projects/-Users-rob-dickinson-Projects-robfromboulder-mini-brain-toolkit/*.jsonl | head -1`. Ask if it can't be determined.

**Content rules:** trace the lineage turn-by-turn (don't summarize the destination); filenames and section names are fine but no line numbers, no cross-document section or finding numbers (`§N`, "finding #N"), and no other drift-prone specifics — reference decisions and findings by their substance, which stays readable as the docs are renumbered and re-homed; skip anything re-derivable from the files themselves; don't restate scope or approach.

**Name the people.** The entry must make clear whose session it was: the lead names the human author (with Claude as co-author), and decisions stay attributed to whoever made each call. Don't lean on the Session ID to carry this — it's an opaque UUID.
