# <Project>: Session Closeout Instructions

> V1, <date>.

---

Governs session log entries in every canonical log and in each work item's `working/<TOKEN>_<WORK>_LOG.md` (once the brain has work-item machinery) — the entry format and content rules are the same regardless of destination. `<TOKEN>` throughout is the owning unit's namespace token and `working/` that unit's own directory — in a brain with one unit, both are the brain's. **This format is the authority; do not imitate the previous entry** — a fresh file has none, and copying a neighbor lets the structure drift one merge at a time. Match sibling entries only where this spec is silent.

**Purpose.** The log is the work's lineage, traceable to each coding session, and the home for what **cannot be deduced from the codebase alone**: key findings, decision points (and who made each call), what was tried and didn't work, and the course-corrections that kept the work on track. It's a log, not a design doc — don't restate scope or strategy; give the turn-by-turn account of each session start to finish and what was learned.

**Routing — which log file to append to.** A session that belongs to an open work item — its docs still in `working/`, even if its PR has already merged — appends to that item's `working/<TOKEN>_<WORK>_LOG.md`; all other sessions append to a canonical log. Resolve ownership by the first matching signal, in priority order:

1. **Explicit direction** — the user names a target log or work item.
2. **Session content** — the session's work belongs to an open work item: its PR, branch, code area, or `working/<TOKEN>_<WORK>_*` docs (e.g. addressing review feedback on the item's PR from a different branch, or refining the item's plan in a session run from this repo).
3. **Current branch** — the session runs from a project repo and its checked-out branch matches the branch declared in an open work item's `<TOKEN>_<WORK>_CLAUDE.md` runbook (exact name or glob). A session run from this repo has no branch signal; never take one from a sibling checkout's incidental branch.
4. **No match** — append to `<PREFIX>_LOG.md`. In a brain whose knowledge is divided into components, append instead to the log of the nearest common ancestor of the units the session's work concerned — not every unit it read: a session that worked inside one unit logs there, and one whose work crossed units logs to the unit above them, however far apart in the tree they sit.

When the content and branch signals point at different work items, or either signal is ambiguous, ask rather than guess. The session that runs a work item's closeout appends to the canonical log of the unit that owns the item: the item's `working/<TOKEN>_<WORK>_LOG.md` is merged and retired in that same pass, so a fresh entry there would land in `archive/` unmerged.

**Reading** (never read these large files in full): `grep -n '^---$' <log-file> | tail -1` gives the last separator's line `L`; read from `offset` `L`.

**Appending:**
1. Determine the target log file using the routing rule above.
2. Add a `---` at the end of that file, then the entry below it. **Append only — never revise or correct prior sessions.**
3. Entry shape: an H1 with a short title and date (`# <title> (YYYY-MM-DD)`); a `` **Session ID**: `<uuid>` `` line; a one-paragraph lead (what the session set out to do and what landed); then `##` subsections for the turn-by-turn lineage, decisions, what didn't work, and lessons — chosen per session, not a fixed template.
4. Session ID = newest transcript filename minus `.jsonl`, taken from the current session's project dir under `~/.claude/projects/`. That dir is derived from the directory the session was launched in: implementation work runs from a project repo; mini-brain-only work runs from this repo. Pick the transcript for the session you're recording — e.g. `ls -t ~/.claude/projects/<this-session's-project-dir>/*.jsonl | head -1`. Ask if it can't be determined.

**Content rules:** trace the lineage turn-by-turn (don't summarize the destination); class/method names are fine but no line numbers, no cross-document section or finding numbers (`§N`, "finding #N"), and no other drift-prone specifics — reference decisions and findings by their substance, which stays readable as the docs are renumbered and re-homed; skip anything re-derivable from the codebase; don't restate work-item scope or implementation strategy.

**Name the people.** The entry must make clear whose session it was: the lead names the human author (with Claude as co-author), and decisions stay attributed to whoever made each call. Don't lean on the Session ID to carry this — it's an opaque UUID.
