# Minimum Acceptance Testing: Burndown

Everything between the merged battery and this item's closeout.

## Before closeout

* fix the procedure defects the 0.73 run found, in PR #28:
  * work closeout checks `archive/` for a name collision before it merges anything
  * `templates/WORK_CLOSEOUT.md`'s dream-cycle passage, against the boundary rule in `templates/CLAUDE.md`
  * "Finding" in its generic sense in session closeout, in the template and this repo's copy
  * the toolkit dream cycle: its cross-reference check against append-only logs and `templates/` paths, Phase 3 with no web search, the Phase 3 skip gate, the Phase 4 slice boundary, and the delegation threshold
* fold the 0.73 run's recipe gaps into `MBT_TESTING.md` and `tests/`, in a PR:
  * Codex: `--skip-git-repo-check` in its command, and a sandbox that keeps it out of `/tmp`, which it writes whatever `TMPDIR` says
  * Claude Code: `--add-dir` on a target's parent, an allowlist with `sed`, `head`, pipes, `bash` and the web tools, and a JSON output whose transcript can be read for improvisation
  * the stray-write sweep covers `/tmp` and `/private/tmp`, and no snapshot names a directory together with repos inside it
  * scenario 1: a scratch tag below HEAD, so a pinned install line is told apart from one that pulls `main`
  * scenario 3: `archive/` gets a `.gitkeep` only when nothing else would keep it
  * scenario 12: started with a bare `dream`, under a scratch `HOME` (Codex only), with a scratch tag above the clone's release for the older-release case
  * scenario 13: passes when no instruction would stop a run in the harness the maintainer dreams in; the ambiguities it lists are notes
  * scenario 14: agents audit `working/` with their own tools, so the script half tests commands no agent runs
  * the grader pairs a rewritten paragraph that keeps its bold lead-in, if check 10's wording supports that, and fills virtual-view-brain's hook brain name correctly
* a fresh agent dry-runs the recipe once both PRs are ready, in place of the earlier dry run's nine gaps, which were never recorded; fix what it finds that is real
* rerun the scenarios the fixes touch: 13 and 15, scenario 1's script, and the grader against scenario 8's saved reports

## Closeout

* closeout notes — the battery shipped before its first release run, and #25 also carried four procedure fixes, by Rob's call, rather than leaving them to their own changes
* fold `MBT_MAT_TESTING.md` into `MBT_TESTING.md`, as scenarios worth repeating each release
* retire `MBT_MAT_CLAUDE.md` to `archive/` unfolded, since this brain has no canonical runbook
* overlaps: MIGRATIONS, REHOMING, WORK_PLACEMENT and MULTI_LOBE_DREAM each add scenarios when they land, and MULTI_LOBE_DREAM replaces check 10's multi-lobe dream-cycle skip, which scenario 10 tests
