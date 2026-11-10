# Mini-Brain Toolkit: Acceptance Testing

> V12, 2026-11-09.

The acceptance scenarios to run before a release, and how to run them on whatever machine is at hand. It takes its example brains from `MBT_EXAMPLES.md`, seeds fixtures with `tests/MBT_SEED_FIXTURE.py`, grades drift with `tests/MBT_DRIFT_COMPARE.py`, snapshots repositories with `tests/MBT_SNAPSHOT.sh`, and runs the shell-sensitive script scenarios with `tests/MBT_SHELL_CHECKS.sh`. This is a recipe: each scenario states its setup and the outcome it expects, and the running agent works out the steps.

Run it when asked to run the acceptance tests or to test a release. The commit under test is this checkout's `HEAD` unless the runner names another. Coverage is whatever the machine allows. No run's results are kept, and nothing a run produces is committed.

## 1. Probe

Find, and print as the report's header:

- The commit under test, `git describe --tags` for it, and the newest release tag.
- Each supported harness on `PATH`, with its version: Claude Code (`claude`), Codex (`codex`) and OpenCode 2 (`opencode`). OpenCode 1 isn't supported.
- The shells present, from zsh, bash and sh.
- The platforms: the host's OS, and Linux when `docker info` succeeds.
- Each brain in `MBT_EXAMPLES.md` that the runner can reach. Look for each by its name under the runner's home directory, four levels deep (`find ~ -maxdepth 4 -type d -name <brain>`). For each one not found, ask the runner for its path, or whether to clone it, and accept "none" only as their answer.

Then ask the runner for a token budget, in any form ("small", "about an hour", "everything"). Confirm each harness can reach its model with a one-line headless prompt that gets an answer, run with stdin from `/dev/null`: `claude -p`, `codex exec --skip-git-repo-check -s read-only`, or `opencode run`. A harness that fails is skipped for this run, with its error as the reason, and a sign-in warning it prints goes in the report's header.

## 2. Select

Each scenario in §6 declares what it needs:

- **Harness:** *none*, *any* (one harness, rotated across the ones found, so different scenarios exercise different harnesses), or *each* (once in every harness found).
- **Brain:** *fixture* (§4), *multi-lobe fixture*, *example* (a reachable brain from `MBT_EXAMPLES.md`), or *none*.
- **Platform:** *host*, or *host and Linux* for a script scenario whose commands differ between BSD and GNU tools. Without Docker, the Linux half is skipped.
- **Cost:** *script* (no model tokens), *dry run* (an agent reads, nothing executes), or *headless* (an agent runs a procedure). A scenario with a script half and a headless half is picked as two: its script half with the script scenarios, and its headless half on its own.

Skip each scenario whose needs the machine can't meet, and give the reason. Then pick within the budget, in this order:

1. every script scenario;
2. scenario 6, the upgrade from the last release;
3. the scenarios under each §6 heading whose procedure changed since the newest release tag, by `git diff --stat <tag>..HEAD`: Install for `README.md` or `SKILL.md`; Create for `MBT_CREATE_BRAIN.md` or `templates/`; Check for `MBT_CHECK_BRAIN.md` or `templates/`; Dream cycle for `templates/DREAM_CYCLE.md` or `MBT_DREAM_CYCLE.md`; Work items and sessions for the work-item or session-closeout templates;
4. the rest, by number;
5. scenario 17 last.

For scale, in Claude Code: scenario 6's two runs cost about $5, a report-only check of a fixture about $0.50, scenario 16 about $0.15, and scenario 2 under $0.10. Codex and OpenCode 2 on a subscription report no cost.

Tell the runner what was picked and what the budget left out, and wait for their go-ahead before spending model tokens.

## 3. Run

- **Test install.** Install the commit under test as a full clone (check 10 reads the toolkit's history), under the skill name `mini-brain-toolkit-mat`: at `~/.claude/skills/mini-brain-toolkit-mat` for Claude Code, and `~/.agents/skills/mini-brain-toolkit-mat` for Codex and OpenCode 2. Set `name: mini-brain-toolkit-mat` in its `SKILL.md`, since each harness finds a skill by that name, and invoke it by that name. Delete its `tests/`: a tested agent that finds the grader runs it in place of the procedure, and the grader then grades itself. The grader runs from this checkout. Stop if either path exists. The runner's own install is never touched, and the test install is removed when the run ends. Each harness keeps its own sign-in and settings, so a tested agent also sees the runner's global instructions.
- **Scratch copies.** Every brain and project a scenario touches is a copy in the scratch directory. Never run against an example in place.
- **Isolation.** Keep answers files, scripts and fixture sources outside the tested agent's working directory. A tested agent reads whatever it can reach.
- **Headless runs.** Start each tested agent fresh, with write access limited to the scratch directory. Give it a temp directory inside the scratch directory, with `TMPDIR` set to it, since check 10 compares copies outside the brain and the install. Run it from the brain, with stdin from `/dev/null`, and keep its transcript in the scratch directory. A report-only run gets the same write access as any other; its snapshots, not its sandbox, show it changed nothing. Each harness:
  - *Claude Code*: `claude -p '/mini-brain-toolkit-mat <request>' --add-dir <each other directory it uses> --allowedTools Read Glob Grep Write Edit WebSearch WebFetch 'Bash(git:*)' 'Bash(python3:*)' 'Bash(ls:*)' 'Bash(find:*)' 'Bash(mkdir:*)' 'Bash(cp:*)' 'Bash(diff:*)' 'Bash(cat:*)' 'Bash(grep:*)' 'Bash(sed:*)' 'Bash(head:*)' 'Bash(tail:*)' 'Bash(wc:*)' 'Bash(sort:*)' --output-format stream-json --verbose`. The other directories include the brain's parent, since Claude Code lists nothing outside the directories it was given, a missing target included. The stream is the transcript, and its last event gives the session ID and cost.
  - *Codex*: `codex exec --skip-git-repo-check -s workspace-write -c sandbox_workspace_write.exclude_slash_tmp=true --add-dir <each other directory it uses> --json -o <last-message file> '$mini-brain-toolkit-mat <request>'`. Without the first flag it won't start outside a git repository, and without the setting its sandbox lets it write `/tmp` whatever `TMPDIR` says. Its sandbox keeps `.git` read-only, so check 9's `git add` fails, and the next check reports that file as untracked.
  - *OpenCode 2*: `opencode run --format json 'Read <test install>/SKILL.md and run <request>'`, with `OPENCODE_CONFIG_CONTENT='{"permission":{"external_directory":{"<test install>/**":"allow","<temp directory>/**":"allow"}}}'` and the other directories it uses added the same way. It attaches a skill only from its interactive `@` menu, so a headless run uses the README's other-harnesses prompt. Its answer is the last `text` part in the JSON events.

  A scenario that needs the owner's answers states them in the prompt or, for a multi-turn intake, resumes the session and answers only from an answers file written before the run. Write each answers file as carefully as the scenario: an answer it doesn't give is "yours to settle", never "not a premise".
- **Linux.** Run a scenario's Linux half in a `debian:stable-slim` container, as `tests/MBT_SHELL_CHECKS.sh`'s header shows, with the toolkit checkout mounted read-only and an empty scratch directory mounted for its work. The container's `sh` is dash. Agent scenarios run on the host only, because each harness's sign-in lives in the runner's `HOME`.
- **Batches.** Run headless jobs two or three at a time. Usage limits stop larger batches partway.
- **Scripts.** Run every command that uses a variable through `bash -c`, and write any loop in bash. Under zsh an unquoted variable isn't word-split, and a line starting with `=` is a command lookup.
- **Before and after.** Before each scenario that runs an agent, run `tests/MBT_SNAPSHOT.sh` on every directory it can reach and on the test install, naming no directory that holds another one named, and save the output. §5 compares it with a second snapshot after. A harness's permissions don't reliably confine writes to the directories it was given, so after each run, also look for files written since it started in the directory holding the scratch directory and at the top of the system temp directory: `find <that directory> -newer <the first snapshot's file> -type f -not -path '<scratch directory>/*'`, and `find /tmp /private/tmp -maxdepth 1 -newer <the first snapshot's file> -type f`. Other sessions write there too, so count a hit only when the agent's transcript shows it wrote that path.

## 4. Fixtures

A fixture is a brain seeded as the toolkit's create would have seeded it at a given ref, so every machine can build one without spending tokens. `tests/MBT_SEED_FIXTURE.py <toolkit> <ref> <outdir>` writes a committed brain, with every procedure file adopted and work setup's scaffolds inline. Beside it, it writes a committed project repo, with its own instructions and the hook placed where that ref's create put it. `--lobes` seeds a multi-lobe fixture, with a hub and two child lobes. At the commit under test, every procedure file in a fresh fixture is current. Build each fixture once per run, and copy it for each scenario that uses it. A scenario that needs a fixture changed by hand, such as a half-applied update, makes the change in its own copy.

## 5. Grade and report

**Grade on disk**, never from the agent's summary.

- A report-only run leaves every snapshot as it was before.
- Every agent scenario leaves the test install's snapshot as it was before, and writes nothing outside the scratch directory.
- In a drift scenario, run `tests/MBT_DRIFT_COMPARE.py --brain` on the brain, naming each project repo with `--project-repo`, and take an example's arguments from `MBT_EXAMPLES.md`. It compares every file check 10 names. A report is graded by its labels: every paragraph the agent names carries the script's label for it, and the agent reports no own edit or dropped paragraph the script doesn't. A walk-through is graded by its end state: the script, run after it, labels every paragraph current apart from those the scenario says to keep. A label that differs is a failure, because either one may be wrong, with one exception: the script pairs a rewritten paragraph only by its words, its opening or its bold lead-in, so where it calls a paragraph missing and the agent calls it an own edit, read both texts, and count a failure only if the agent paired the wrong paragraph. The script compares each top-level list item as a paragraph of its own, as an agent reads a list, so compare items, not counts, where an agent groups a list. Pass `-v` to see each paragraph's label, and name one template and file in place of `--brain` to grade a single file.
- Read each tested agent's transcript for places where it improvised, asked something the procedure doesn't ask, or contradicted itself. Each one is a note, not a failure: it points at a gap in the procedure.

**A major problem** blocks the release. Three failures are always major: scenario 6, any write to the install, and a report-only run that changes a repository. Any other failure is the releaser's call.

**Report.** Print it, and save it in the scratch directory, never in a repository. Lead with what failed. Keep a passing run short:

```
MAT  <commit> (<describe>)  newest release <tag>
     harnesses: <name version, ...>   shells: <...>   platforms: <...>   brains: <fixtures, examples found>

FAIL [MAJOR] 6  Upgrade from 0.72 (claude 2.1.x)
     expected: second check reports no drift
     got:      README's install paragraph reported behind again
     scratch:  <path>

NOTE 3, 14  both agents improvised where work setup doesn't say which lobe owns a cross-lobe item

PASS 12   SKIP 4  2, 5, 16 (codex, opencode not installed); 17 (no owner revision named)
MANUAL     2 in OpenCode 2 (select the skill from the @ menu)
COST       claude $6.10; codex, opencode unmetered
```

## 6. Scenarios

Each scenario states observable outcomes, never a procedure's wording, so an editorial change to a procedure doesn't break it. A defect fixed in the toolkit adds a scenario that would have caught it. A known weak point adds one too.

### Install

1. **Install line.** *Harness: none. Brain: none. Platform: host and Linux. Cost: script.* `tests/MBT_SHELL_CHECKS.sh` runs it, with scenario 14's `find` commands. Make a bare clone of the commit under test, tag its parent commit with a scratch version above the newest release, and point each of the README's install lines at it. Run each line in each shell, with its install path pointed into the scratch directory. A fresh install exits 0 and lands on the scratch tag, not the commit under test. A rerun exits 0 and changes nothing. With a higher scratch tag on the commit under test, a rerun exits 0 and moves the install to it. A bad URL exits non-zero and leaves no install. With the remote moved away, the line exits non-zero and leaves the install as it was. Run the moved-remote case against an existing install, before the bad-URL case removes it.
2. **Invocation.** *Harness: each. Brain: none. Cost: headless.* Run from an empty scratch directory. Invoked with no argument, the skill asks whether to run create or check. Invoked with `check ../no-such-brain`, it starts check and reports that the target doesn't exist. Selecting it from OpenCode 2's `@` menu is a manual step for the runner.

### Create

3. **Blind create.** *Harness: any. Brain: none. Cost: headless.* Use an invented project with a few design notes and an existing `CLAUDE.md` of its own, and an empty brain repo beside it. Drive create through stage 2 from an answers file. It asks about each premise on its own. SCOPE keeps the design's choices out and assesses them only as alternatives. The hook is merged into the project's `AGENTS.md`, and the project's `CLAUDE.md` gains `@AGENTS.md` with its own content kept. Each of `archive/` and `working/` that holds nothing else gets a staged `.gitkeep`. The first log entry names the session ID from the running harness's own variable. Nothing is committed unless the answers say so.
4. **Create and check agree.** *Harness: any. Brain: scenario 3's. Cost: headless.* A fresh check of scenario 3's brain, committed, with the same answers, gives no verdict opposite to create's on premises, the second approach or SCOPE's neutrality.
5. **Loading.** *Harness: each. Brain: scenario 3's. Cost: headless.* From the project repo, the hook's trigger phrase makes the agent read the brain's `CLAUDE.md`. From inside the brain repo, the agent reaches `CLAUDE.md` through `AGENTS.md`.

### Check

6. **Upgrade from the last release.** *Harness: any. Brain: fixture at the newest release tag, with one own edit planted and committed. Cost: headless.* Plant it by rewording, within the same rule, the enforced-terms rule that opens "An empty disambiguation is a delete". Before the run, confirm that the grader labels that paragraph an own edit and nothing else in the file differently. Run check with this request: `check this brain. Its project repo is ../fix. Then walk me through every recommended next step: I approve each recommendation, so make each change without asking. Do not commit.` Run the second check with: `check this brain and report only: change nothing in it or in ../fix.` Before any fixes, the report lists only behind, missing and dropped paragraphs, plus the planted own edit, and names the install's release position. After a walk-through that approves every recommended change:
   - every procedure file matches the current template, apart from the planted own edit, which is unchanged, and any paragraph changed by an approved recommendation that isn't procedure drift, which the agent's report names;
   - the hook sits in the project's `AGENTS.md`, and the project's own instructions are where they were;
   - work setup's scaffolds are intact.

   A second check reports no missing, behind or dropped paragraph, reports the planted edit and each paragraph changed outside procedure drift as own edits, and changes nothing. When the budget allows, repeat from an older tag.
7. **Drift edge cases.** *Harness: none, or any when headless. Brain: fixture. Cost: script, or headless.*
   - A multi-lobe `CLAUDE.md` seeded at 0.71 shows the paragraph 0.72 added as missing.
   - A dream cycle with half of a release's changes applied by hand shows exactly the other half. Build it from the newest release's fixture: split its dream cycle and a commit-under-test fixture's into blank-line blocks, and replace every other block that differs with its closest counterpart from the commit under test.
   - Procedure files copied at `8ad8deb`, between releases, show no own edits.
   - Headless only: a walk-through that declines one added paragraph and one rewrite, and approves the rest. A second check reports both declined changes again.
   - Headless, report-only: a fixture at the commit under test cut back to stage 1, with its lifecycle docs removed and create's staged comments deleted rather than uncommented. The check reports no drift.
8. **Example brains.** *Harness: none, or any when headless. Brain: each example. Cost: script, or headless report-only.* Every difference is behind, missing, dropped or an own edit. Known own edits are reported as own edits: lamarr-brain's clone name, mini-subtitle-wizard-brain's fixed clone path and its pull-request rule, and virtual-view-brain's fixed clone path. By script, the other examples only show that the grader runs on them; a headless run is graded against the grader's labels. A headless run changes nothing.
9. **Loading reach.** *Harness: any. Brain: scenario 6's fixture before fixes. Cost: headless report-only.* Check flags that only `CLAUDE.md` reaches the hook. When scenario 6 runs, its first report covers this.
10. **Skips.** *Harness: any. Brain: see below. Cost: headless report-only.*
    - With a full clone of the commit under test as the target, `tests/` included, check 10 is skipped, and the report names `SKILL.md` and `MBT_CHECK_BRAIN.md` as the reason.
    - With a multi-lobe fixture that has a dream cycle, the dream-cycle comparison is skipped, and the template's full dated history is listed.
    - With a brain directory that isn't a git repository, check 9 is reported as unchecked.
11. **Install guard.** *Harness: any. Brain: a toolkit copy. Cost: headless.* Plant a missing version header in both a copy of the toolkit and the writable install. Check the copy and approve every fix. Only the copy changes.

### Dream cycle

12. **Template dream cycle.** *Harness: Codex. Brain: fixture beside a small code repo, with a file in `working/` that holds the reasoning behind a decision, and a top-level doc that cites it. Cost: headless.* The release check reads the toolkit clone at a standard install path, so run with `HOME` pointed at a scratch home holding a clone at `~/mini-brain-toolkit` whose origin is a scratch bare clone, keeping Codex's sign-in through `CODEX_HOME`; Claude Code's sign-in doesn't survive a moved `HOME`. Run the cycle twice: once with the clone at the newest release and a scratch tag above it on the remote, and once with the clone at the commit under test. Start each with a bare `dream` from the brain, not through the skill, which would ask whether to create or check. It runs every phase unattended and asks nothing. Its leakage check flags the citation of the `working/` file. It flags claims it can't verify and carries on, edits no premise, and verifies SCOPE's claims rather than the project's code. Its release check raises an item when the install sits on an older release than the remote's newest, and says it skipped when the install is off-release.
13. **Toolkit dream cycle.** *Harness: Claude Code. Brain: this repo. Cost: dry run.* Give the agent the clone's parent directory too, as a run would have it. A dry run of `MBT_DREAM_CYCLE.md` edits nothing and finds no instruction that would stop a run in Claude Code, the harness the maintainer dreams in. Each ambiguity it lists is a note, since a dry run of a long procedure always finds some.

### Work items and sessions

14. **Work setup.** *Harness: any. Brain: fixture, and a multi-lobe fixture holding a conflicting open item. Platform: host, and host and Linux for the script. Cost: headless, plus script.* Setup creates the item's scaffolds and audits only `working/`. In the multi-lobe fixture it records the overlap with the other open item. A headless run passes whichever way it audits, since an agent may use its own file tools. By script (`tests/MBT_SHELL_CHECKS.sh`), the procedure's `find` commands give the same output and exit code in each shell, on the host and on Linux, for an agent that runs them.
15. **Work closeout.** *Harness: any. Brain: fixture holding a finished scratch item. Cost: headless.* The item's docs fold into the canonical docs, and its log entries merge into the canonical log in date order. Run again with a file of the same name already in `archive/`: closeout stops and asks for a new slug, and overwrites nothing.
16. **Session closeout.** *Harness: each. Brain: fixture. Cost: headless.* The request gives the session's content: `I am Rob, the brain owner. In this session we decided that Fix stores its job queue in SQLite rather than flat files, because two workers writing flat files at once corrupted each other; we rejected a JSON-lines file as too slow to query. Read CLAUDE.md and follow it, then update the session log for this session. Do not commit or push.` Start each harness's run from the runner's own shell, so that every tested agent inherits the runner's session variable. The agent appends one entry after a `---` at the end of the log, in the entry format, with the running harness's own session ID, not the inherited one.

### Judgment

17. **Blind check against an owner's revision.** *Harness: any. Brain: an example with a known owner revision. Cost: headless.* The runner names a revision, such as a merged PR that reworked SCOPE or APPROACH. Check the brain as it stood just before it, with an answers file drawn from the revision's description. Report how much of the revision the check reproduced, where it placed content differently, and what it removed that the owner kept. No score passes or fails; the releaser judges.
