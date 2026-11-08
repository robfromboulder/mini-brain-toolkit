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

---

# MAT's examples, recipe, fixture seeder and grader land on the work branch (2026-11-08)

**Session ID**: `9dd62b33-2b95-4dd2-b2de-07c645e0d576`

Rob's session, with Claude as co-author, continuing after the replan above. Rob had plan steps 1–4 and 7 carried out: `MBT_EXAMPLES.md`, the move of the drift grader to `tests/`, its check against check 10, `MBT_TESTING.md`, and a fixture seeding script. Rob directed the split: plan and log changes go to `main`, and the toolkit changes go to branch `minimum-acceptance-testing`.

## Turn by turn

- **`tests/` again.** Rob asked whether a hidden `.tests` would mean fewer exclusions. Claude found it would remove none: the cross-reference check is triggered by the path written in `MBT_TESTING.md`, not by the directory's visibility. A hidden directory would also hide the grader from `ls` and from search tools. Rob kept `tests/`.
- **`MBT_EXAMPLES.md`.** Claude gathered provenance from the local clones, the Codeberg repo and the toolkit's logs. A seeding release is the newest tag at a brain's first commit. Claude found `mini-okx-brain` as well, and Rob left it out. Claude widened the plan's "name and holder only" rule for private brains, since author, release and shape say nothing about a project and scenario selection needs the shape. Claude first left the read-index row for plan step 7, and Rob pointed out that this breaks the pattern. The row and a declared-exemptions row went in with the file.
- **Moving the grader.** A failed `git checkout` inside a chained command left the plan edit unrun and a stray commit on the branch. Claude redid both before anything was pushed.
- **Checking the grader against check 10.** Claude found three divergences and confirmed each with a test: tables outside `CLAUDE.md` went unpaired, a literal hub name in a multi-lobe runtime slot matched, and pre-0.70 `<PREFIX>` copies showed false own edits. Rob asked for fixes and reruns. Claude then compared the old and new grader on every example brain. That showed the multi-lobe fix had turned a correctly behind paragraph in virtual-view into an own edit, because `create` at `d66dddf` filled `<LOBESPACE>` with the hub's name. Claude made earlier template versions accept that fill too.
- **`MBT_TESTING.md`.** Claude wrote the recipe, with fixtures as a part of their own. It also wired the doc into `CLAUDE.md` and the dream cycle in the same commit, applying Rob's read-index point to step 7.
- **Fixtures.** Claude generalized the single-tag seeding scripts TEMPLATE_DRIFT left in an earlier scratchpad into `tests/MBT_SEED_FIXTURE.py`, following each ref's own create rules. Seeding 0.70, 0.71, 0.72, `8ad8deb` and HEAD in both shapes, and grading every procedure file, found one more grader gap. Create at 0.70–0.72 filled every `<LOBESPACE>` in a multi-lobe hub's procedure files, work-item slots included. With that fixed, HEAD fixtures came out fully current, and no fixture showed an own edit.
- **Whole-brain grading.** Rob had the caller's preparation folded into the grader as `--brain`. Real brains showed that virtual-view, which predates 0.70, labels each scaffold with a bare doc name, and the scaffold cutter was widened to match.
- **Nebula.** Claude's summary blamed nebula's many own edits on a compound prefix. Rob questioned it. Nebula's work files are plain `NEBULA_<WORK>_*`, and word-level diffs showed the own edits are owner adaptations over older template text. Claude corrected the claim in the plan.

## Decisions

- **Keep `tests/` visible** — Rob.
- **Leave `mini-okx-brain` out of the examples** — Rob.
- **A top-level doc gets its read-index row in the commit that adds it** — Rob.
- **Plan and log on `main`, and `CLAUDE.md`, `MBT_EXAMPLES.md` and the rest of the toolkit change on the work branch** — Rob.
- **Fold the caller's preparation into the grader** — Rob, on Claude's offer.

## What didn't work

- A shell command chained across a heredoc kept running after a failed `git checkout`, and committed the plan edit to the wrong branch.
- Claude's first multi-lobe grader fix was checked only against the targeted test, and regressed a real brain.
- Claude passed on the old log's compound-prefix line about nebula without checking it against the brain.

## Lessons

- Run a grader change against every example brain before and after, and diff the two runs. The targeted tests passed on the change that regressed virtual-view.
- Seeding fixtures at every ref and grading them tests the grader and the seeder together. A HEAD fixture must come out fully current, and no fixture may show an own edit.
- A claim about a brain's shape should come from the brain, not from a log entry about it.
