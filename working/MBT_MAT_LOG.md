# Minimum Acceptance Testing: Session Log

Running log of implementation sessions. Each session appends after a `---` separator.

The first entry, and every one after it, follows the entry format and content rules in `MBT_SESSION_CLOSEOUT.md` — that spec is the authority, not the prior entry, since a fresh LOG file has none to copy.

---

# MAT replanned as a recipe that fits each machine (2026-11-08)

**Session ID**: `9dd62b33-2b95-4dd2-b2de-07c645e0d576`

Rob's session, with Claude as co-author. With 0.73 close, Rob gave feedback on the scaffolded plan. Contributors won't all have a Mac, every harness, every example brain or unlimited tokens. The battery should run what each machine allows, keep no record of results, print a short report that is loud on failure, and be a recipe rather than a script. Claude rewrote the PLAN, FINDINGS and TESTING docs to match, and Rob refined them over several turns. The docs were committed to `main`.

## Turn by turn

- **Research.** Claude read the scaffolded docs, the 0.72 preflight entries in `MBT_LOG.md`, and the testing sections of PRs #19, #20, #22, #23 and #24. It also read the testing approaches of the four other open items in `working/`. The machine has Claude Code but not Codex or OpenCode, and holds lamarr-brain and virtual-view-brain.
- **Rewrite.** The plan became a five-part recipe: probe, select, run, grade and report. Selection follows a budget the runner states, and a scenario needing any one harness rotates across the harnesses found. The nine TEMPLATE_DRIFT tests became seed scenarios covering install, create, check, the dream cycle, work items and session closeout. Every scenario runs on fixtures seeded from release tags, so a contributor with no examples can still run the battery. FINDINGS gained the rejected full matrix, the rejected per-release record, and a deferred golden machine. Most of the old open issues were settled in the plan.
- **Rob's answers.** Rob treated the clash with `CLAUDE.md`'s no-testing-doc binding, which PR #23 had flagged, as housekeeping: the binding goes, and `_TESTING` docs fold into `MBT_TESTING.md`. He asked where the drift-grading script would live if it didn't ship, since the battery has to run on several machines, and it moved to `tests/`. He accepted the three fixed release blockers. He added lamarr-brain and `starburstdata/mini-alien-brain` to the examples.
- **`tests/` or `archive/`.** Rob asked whether a new top-level directory would need excluding from other instructions, and whether `archive/` would be simpler. Claude found that `archive/` conflicts with the cross-reference rule and with the dream cycle's leakage check, which would try to inline the script into `MBT_TESTING.md`. Rob kept `tests/`.
- **Comparison with 0.72.** Asked how the plan compares with 0.72's testing, Claude found the plan covers far more of the toolkit. It also found that most of 0.72's fixes came from transcripts showing agents improvising, which a fixed expectation would pass. It had no equivalent for the blind check of virtual-view-brain judged against Rob's own PR. Rob had both added: transcript notes in grading, reported as notes rather than failures, and an optional judgment scenario.
- **Read-back.** Rob asked for a read-back of the PLAN for accuracy. Claude corrected its earlier claim that `tests/` needs no exclusion: the dream cycle's cross-reference check would flag `MBT_TESTING.md` naming the script, so `MBT_DREAM_CYCLE.md` joined the changes. It also corrected "the 0.72 fixes" to "most of", and fixed several scenario details against the procedures. Two gaps went into open issues. PR #24's pinned lines and release check merge only after the 0.73 tag, and installing the commit under test would overwrite the runner's own install.
- **Scratch `HOME`.** Rob chose a scratch `HOME` for the install. Claude added the model login as a caveat, which Rob questioned, since the testing is local. Claude explained that agent scenarios call hosted models through each harness's own login, which a scratch `HOME` can hide. The wording became "model login", and where each harness keeps it is left to verify on the first run.

## Decisions

- **Coverage fits each machine, with no full matrix, no recorded results and a short local report** — Rob.
- **`_TESTING` docs fold into `MBT_TESTING.md` once it exists** — Rob, as housekeeping.
- **The drift-grading script ships in `tests/`, not `archive/`** — Rob, on Claude's analysis.
- **Three fixed release blockers: a failed upgrade from the last release, a write to the install, and a report-only run that changes a repository** — Rob, accepting Claude's proposal.
- **Grade transcripts for improvisation as notes, and add an optional judgment scenario** — Rob, on Claude's recommendation.
- **Agent scenarios run under a scratch `HOME`** — Rob.

## What didn't work

- Claude's first answer on `tests/` said none of the dream cycle's mechanical checks would touch it. Only the read-back against the cycle's text caught that the cross-reference check would.

## Lessons

- Fixed expectations test mechanics, while the 0.72 preflight's fixes came from reading how agents got there. A battery needs both.
- A claim about what an instruction ignores should come from reading every rule in it, not from the rules that look relevant.
