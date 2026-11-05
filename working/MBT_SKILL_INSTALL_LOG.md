# Skill Install: Session Log

Running log of implementation sessions. Each session appends after a `---` separator.

The first entry, and every one after it, follows the entry format and content rules in `MBT_SESSION_CLOSEOUT.md` — that spec is the authority, not the prior entry, since a fresh LOG file has none to copy.

---

# Toolkit shipped as a Claude Code skill, draft PR opened (2026-10-26)

**Session ID**: `3e32922d-200a-40f8-8d86-ddfcaadc0d94`

Rob's session, with Claude as co-author. Rob asked how hard it would be to replace the README's `Read ../mini-brain-toolkit/…` prompts with `/mini-brain-toolkit create` and `/mini-brain-toolkit check`. Claude found the change small, Rob chose the root-`SKILL.md` option, and it landed as draft PR #17 with the install line tested and the skill itself not yet run.

## Turn by turn

- Claude read the README and both procedures and grepped the top-level docs and templates for the toolkit's clone path. Only the two README prompts depend on it: the project hook locates the brain beside the project's main checkout, and created brains need no toolkit at runtime. Claude offered two packagings — the repo root as a personal skill, matching Rob's syntax, or a plugin with namespaced commands — and the convention costs of the first: naming and version-header exemptions for `SKILL.md` and a declared boundary for it.
- Rob chose the root skill. Implementing it, Claude found the toolkit's own dream cycle would flag `SKILL.md` as an orphan and an un-namespaced file, so its checks gained the exemption and its product list gained the file. `MBT_PATTERN.md` and the templates were left alone, since users' brains carry no `SKILL.md`.
- Rob pointed out that the README's `git clone` line installs but doesn't update an existing install. Claude replaced it with an `if`/`else` that pulls with `--ff-only` when the clone exists, and tested both paths against a scratch `HOME`.
- Rob pointed out that the multi-line `if` block couldn't be copied and pasted, and asked for one line or continuators. Claude collapsed it to one line with the path in a variable, and tested both paths in zsh and bash.
- Rob asked for a draft PR. Claude branched to `skill-install`, committed without an attribution trailer per `CLAUDE.md`, and left the PR body unattributed to match the repo's prior PRs. The PR records what was tested and what wasn't.
- Rob asked for a work item and a closeout to it, which opened `SKILL_INSTALL` after the change had already landed on its branch.

## Decisions

- **Root `SKILL.md`, not a plugin** — Rob, for the unnamespaced command syntax and the git-based update path.
- **Procedures unchanged** — Claude: one sentence in `SKILL.md` supplies the toolkit root they already assume.
- **One-line install-or-update** — Rob's requirement; the `if` test over `pull || clone` and `--ff-only` were Claude's.

## Lessons

- A README command is copied, not read, so judge it by whether it pastes and whether it reruns cleanly. The first two versions failed one test each, and Rob caught both.
- The toolkit's own maintenance checks enumerate exempt filenames, so a new exempt repo file has to be added to the dream cycle as well as to `CLAUDE.md`.

---

# Commits split, skill extended to OpenCode and Codex (2026-10-26)

**Session ID**: `3e32922d-200a-40f8-8d86-ddfcaadc0d94`

Rob's session, with Claude as co-author, continued after the work item opened. Rob had the work-item docs moved to `main` so PR #17 could be reviewed without them, kept the single-skill shape, and broadened the install from Claude Code to Claude Code, OpenCode and Codex. The README went through several layouts before Rob settled one, and the branch ended as a single squashed commit. The skill has still not been run in any harness.

## Turn by turn

- Rob asked for the commits refactored so the work-item docs land on `main` first and the PR holds only the implementation. Claude cherry-picked the work-item commit onto `main` and pushed it, rebuilt `skill-install` on the new `main` with only the implementation commit, and force-pushed with lease.
- Rob asked whether the skill shows `create` and `check` as menu items. Claude's understanding, unverified: `argument-hint` shows them only as hint text, and separate entries would take two skills, cleanest as the namespaced plugin. Rob kept it as is.
- Rob found the install section Claude-only and the instruction to replace each command buried, and asked for install options for Claude Code, Codex and OpenCode, with create and check always run as documented. Claude checked the Codex and OpenCode docs: Codex reads `~/.agents/skills` and invokes with `$`; OpenCode reads `~/.claude/skills` among others and ignores `disable-model-invocation`. Claude wrote three install options, dropped the `Read` fallback, and reworded `SKILL.md` off `$ARGUMENTS` and "base directory". The OpenCode and Codex install paths were tested against an empty `HOME`.
- Rob asked whether the README should instead ask the agent to install the skill from the repo URL. Claude agreed it fit and named what the prompt would still have to state: the whole repo is the skill, a git clone, a user-level install. Rob then raised a bootstrapping problem and kept explicit install lines.
- Rob folded Claude Code and OpenCode into one option, since OpenCode reads Claude Code's skills directory, and asked for both command forms in create and check. Claude put them as two lines in one quote. Rob rejected that layout and asked for create and check to mirror the install section: an opening paragraph for the step, then a heading per harness. Rob's own example labeled the `/` form "Claude Code and Codex"; Claude read it as OpenCode.
- Rob changed the install wording to "your preferred harness" and asked for "harness" in all three sections, then reworked the create and check paragraphs. Claude proposed restoring "run it in your project repo"; Rob pointed out that a brand-new project creates its brain before any project repo exists, which the create procedure's intake already allows, and Claude dropped it.
- Rob asked whether "This skill helps…" used terms accurately. No enforced term covers "skill", but there is one skill with two commands, and "maintain" overstated a one-off evaluation. Rob had both paragraphs reworded to "The `create` command" and "The `check` command … evaluates".
- Rob had the changes committed and pushed, the PR retitled and redescribed for all three harnesses, and the two branch commits squashed into one.

## Decisions

- **Work-item docs on `main`, implementation alone on the PR** — Rob, to review the PR without the work item.
- **One skill, argument as hint text** — Rob, over a plugin's per-command menu entries.
- **Explicit install lines, not an install prompt** — Rob.
- **Two options: Claude Code or OpenCode, and Codex** — Rob, since OpenCode reads Claude Code's skills directory.
- **Every section shaped as an opening paragraph, then a heading per harness** — Rob, so no command is rewritten by the reader.
- **No `Read` fallback** — Claude proposed dropping it to avoid the replace instruction; Rob's layout kept it out.

## What didn't work

- Two command forms as lines in one quote block, each with the harness in parentheses: Rob found it unclear next to the install section's structure.
- An install prompt handed to the agent: the prompt would carry most of what the lines spell out, and Rob judged it to have a bootstrapping problem.

## Lessons

- A README that serves several harnesses reads best when every step has the same shape; a note telling the reader to adapt a command is the thing to remove, not to place better.
- "Skill" names the installed unit and "command" the argument it takes; the README's paragraphs each describe a command.

---

# Skill install split into two PRs, Claude Code half tested and ready (2026-10-30)

**Session ID**: `b749aeb1-ac6c-4678-9211-27eef0e29cc8`

Rob's session, with Claude as co-author, which ran over two days. It started from a review of PR #17 and Rob's question about how harness support should shape the README. Checking the harness docs showed that Codex and OpenCode needed more than install lines: brains created there would never load. Rob reframed the work item as two PRs. PR #17 now covers Claude Code plus a fallback for other harnesses that reads `SKILL.md` by path. It passed acceptance in Claude Code and is ready for review. Codex and OpenCode wait for a second PR after #18.

## Turn by turn

- Rob had Claude read the work item and check out `skill-install`. The branch sat on the commit that opened the work item, six commits behind `main`.
- Rob pointed to the review of PR #17 and asked for recommendations on harness support. Claude checked the OpenCode and Codex skills docs. OpenCode's main docs describe skills loaded only by the model, so `/mini-brain-toolkit` would fail there, and OpenCode reads both `~/.claude/skills` and `~/.agents/skills`. Codex documents `agents/openai.yaml` for turning off implicit invocation. Claude recommended:
  - grouping install lines by directory;
  - a `description` guard against auto-invocation;
  - an "Other agents" fallback through `SKILL.md`;
  - command wording that works however the command arrives;
  - no shallow clone.
- Rob found OpenCode's V2 docs, which Claude had missed. V2 invokes a skill with `@name`, honors `disable-model-invocation`, takes a skill's ID from its folder name, and resolves duplicates by registration order, so the `~/.agents` copy wins. Claude revised: OpenCode 2 gets its own `@` heading, the `description` guard drops to optional, and Codex's yaml stays.
- Rob had the README and `SKILL.md` changed without committing. Claude added a Codex-or-OpenCode-2 install into `~/.agents/skills`, `@` command blocks, and Other agents blocks. It also fixed the review's path-rule bug: only `MBT_*.md` files and `templates/` paths resolve against the install, so a procedure's bare `CLAUDE.md` names the target brain's. Rob hadn't asked for that fix, and Claude flagged it.
- Rob asked why the yaml was needed. Claude found that the project hook goes only into `CLAUDE.md`, which Codex never reads. So the conflict the yaml guards against can't happen in Codex, and neither can loading a brain at all. Rob ruled that Codex support that doesn't work has no place in the project, and widened the scope.
- Claude proposed an `AGENTS.md` hook imported by `CLAUDE.md`, a one-line `AGENTS.md` in the brain, harness-aware session-ID lookup, and a check for hooks that reach only `CLAUDE.md`. Rob chose the import and at first kept everything in one PR. Claude compared the planned edits with PR #18: they share the create and check procedures, `MBT_PATTERN.md` and the dream cycle, with mostly version-line conflicts and one adjacent edit in the create intake.
- Rob reframed the work. #17 became "install the toolkit as a Claude skill", shown under Claude Code and Other harnesses, and merges before #18. Codex and OpenCode follow as part 2 once #18 merges. Claude agreed, and proposed renaming the fallback "Without installing", because a brain created from another harness still won't load there. Rob kept "Other harnesses": the fallback does install a clone, the structure leaves room for Codex and OpenCode blocks in part 2, and create and check never depend on the hook. Rob accepted the loading gap until part 2, and decided one work item would carry both PRs.
- Claude trimmed the branch to `README.md`, `SKILL.md` and `CLAUDE.md` and added `SKILL.md` to the read index. It kept `CLAUDE.md` at V27 with a new date rather than bumping a version the unmerged PR had already bumped. It rewrote the plan and findings on `main` in a separate worktree. The force-push to amend the branch's one commit was blocked by the permission classifier, so the narrowing landed as a second commit. Claude retitled and redescribed the PR.
- Rob had the acceptance tests run in Claude Code. Claude installed the branch into `~/.claude/skills` and drove headless `claude -p` sessions against scratch copies with no remote:
  - no argument asked which command to run;
  - `check` on a copy of lamarr-brain read the procedure and pattern from the install and the brain's own `CLAUDE.md`;
  - `create` from a scratch project read every template from the install and wrote the new brain and the project's `CLAUDE.md`, leaving the install clean;
  - the install line, rerun on a clone moved one commit back, fast-forwarded it;
  - the `Read ~/mini-brain-toolkit/SKILL.md` form ran the check from that clone instead of the installed skill.
- Rob had the PR's testing section replaced with those results and the PR marked ready.

## Decisions

- **Two PRs, one work item** — Rob. #17 ships Claude Code and Other harnesses and merges before #18; Codex and OpenCode follow it.
- **No harness in the README until brains created there load there** — Rob.
- **Project hook in `AGENTS.md`, imported by `CLAUDE.md`** for part 2 — Rob, over writing the hook into both files.
- **"Other harnesses", not "Without installing"** — Rob.
- **OpenCode 2 targeted through `@`, OpenCode 1 left out** — Claude, after Rob found the V2 docs.
- **Path rule narrowed to `MBT_*.md` and `templates/`** — Claude, from the review; it shipped in part 1.
- **Merge order #17, then #18** — Rob.

## What didn't work

- Recommending from OpenCode's main docs: they describe OpenCode 1, and V2 changed invocation, auto-invocation and duplicate handling.
- Treating `agents/openai.yaml` as a fix on its own: the conflict it guards against needs a hook Codex never reads.
- Amending the branch's single commit: the force-push was refused, so the branch carries two commits.

## Lessons

- Listing a harness is a promise about the brains create produces, not only about running the procedures. Check the whole loop — install, invoke, then load the created brain — before offering a harness.
- Harness docs version underneath you. Check the version a page describes before recommending from it.
- "Already up to date" does not test an update path. Roll the clone back first.

---

# PR #17 reviewed, squashed and merged; #18 rebased onto it (2026-10-30)

**Session ID**: `ecf1ef40-2322-4c2c-af99-a36c53dacd10`

Rob's session, with Claude as co-author. It started by reading the work item and ended with PR #17 merged and #18 rebased onto it. A code review of #17 produced three wording fixes and moved two gaps in checking the toolkit itself into part 2. Along the way Claude edited stale copies of the work-item docs on the branch, which put #17 in conflict with `main` until those edits were reversed.

## Turn by turn

- Rob asked Claude to read the work item. Claude read it from the `skill-install` checkout and reported the docs out of date against the branch's latest commit. They were out of date only on the branch: the previous session had moved the work-item docs to `main`, and the branch carried the copies from where it forked.
- Rob had the plan and findings updated without touching the log. Claude rewrote the branch's copies from the latest commit and from the PR description. It noted that the dream cycle's orphan check still excluded `SKILL.md`, though the read index now lists it. Rob had the exclusion dropped in part 1, and had the change committed, pushed and reflected in the PR description.
- Rob ran a medium code review of #17, which returned eight findings. Claude's first triage recommended fixing two, and Rob asked for each to be confirmed and thought through. Checking each against the files:
  - the path rule sends a target's `MBT_*.md` files to the install, so checking a copy of the toolkit, the one target sharing the `MBT` lobespace, reads the install's files instead — real but narrow, deferred to part 2;
  - the check's namespace test flags `SKILL.md` — real, already in part 2, where `main`'s plan has the check read the target's declared exemptions rather than name `SKILL.md`;
  - the path rule living only in `SKILL.md`, and the install line treating any existing directory as a clone — accurate, dismissed;
  - the `~` path in the Other harnesses prompt — untested outside Claude Code, added to part 2's testing;
  - `CLAUDE.md` saying `SKILL.md` "references nothing else" — weaker than Claude first stated, reworded anyway;
  - the README's install intro promising every line configures a skill — reworded;
  - no migration note for clones beside a project — left to the release notes.
- Rob had the fixes made, committed, pushed and reflected in the PR description.
- Asked what review remained, Claude found #17 conflicting with `main` in the two work-item docs, and `main`'s versions current and fuller than the branch's. Claude named the mistake and proposed the recovery, which Rob approved: a new commit reset the branch's copies to the merge base, the review's content went into `main`'s docs through a worktree, and GitHub reported #17 mergeable.
- Rob asked for the branch squashed. The force-push was blocked by the permission classifier, so Claude squashed locally and Rob pushed.
- Asked about remaining review tasks, Claude ran the toolkit's mechanical checks on the branch — namespace, read index, version headers, and references to the old clone-beside-the-project route — and all passed. A trial merge of #18 onto #17 conflicted only on the dream cycle's version line, so Claude corrected #17's description to say #18 takes V24.
- Rob merged #17. Claude ran the README's install line from `main` against a scratch `HOME` in zsh and bash: it cloned the merged toolkit, and a rerun reported up to date. Running the skill needs a real install, which Rob kept to do personally, and Claude removed the scratch installs.
- Rob had #18 rebased. Three of its commits bump the dream cycle, and Claude raised each by one. After the second resolution both sides read V23, so git applied the third commit cleanly and dropped its bump; Claude amended the last commit to V24. Rob force-pushed, and Claude updated #18's description, whose version numbers all predated its review rounds.
- Rob had this entry written and the work item's landing on `main` verified.

## Decisions

- **Drop `SKILL.md`'s orphan exemption in part 1** — Rob.
- **Wording fixes in part 1; the toolkit's self-check gaps and the `~` path in part 2; the rest dismissed or left to release notes** — Rob, on Claude's per-finding triage.
- **Work-item docs stay on `main`; the branch's copies reset by a new commit, not a force-push** — Claude, approved by Rob.
- **#17 merged as one squashed commit** — Rob.
- **Running the installed skill from `main` is Rob's to test** — Rob.

## What didn't work

- Reading the work item from the PR branch: it carried the copies from where it forked, and two commits edited them before the conflict exposed it.
- Force-pushing from the session: the classifier blocked both the squash and the #18 rebase, so Rob ran each push.
- Trusting a rebase to carry a chain of version bumps: once both sides held the same number, git merged cleanly and a bump vanished.

## Lessons

- A work item whose docs live on `main` is read from `main`, not from a feature branch. Check `origin/main` for the item's docs before reading or editing them.
- After resolving version-line conflicts across a rebase, check the final number against the count of bumps; a clean merge can hide a lost one.
- A first triage of review findings can overstate one. Checking each against the files changed a recommendation.

---

# Part 2 probed in each harness, revised by Rob, and opened as PR #19 (2026-11-04)

**Session ID**: `2321d25a-038a-4c05-abd6-4ec4f6cd8116`

Rob's session, with Claude as co-author, on a machine running Claude Code, Codex and OpenCode 2. Rob asked Claude to drive part 2 by experiment until the toolkit installed, loaded and worked in each harness. Claude probed each harness, built the planned changes on `skill-install-part-2`, and ran the acceptance in Codex and OpenCode 2, which passed. Rob then moved the OpenCode menu instruction and replaced the toolkit-copy rule with an install guard. A re-test with a control passed, and the work went up as PR #19.

## Turn by turn

- Claude read the work item from `main` and asked one question: whether the README's intro, diagrams and badge should stop naming Claude. Rob chose prose only.
- Claude probed each harness with a throwaway skill, `zz-probe`:
  - Codex passes the text after `$name` through, and ignores `disable-model-invocation`, which `agents/openai.yaml` overrides.
  - OpenCode 2 attached the skill neither from `opencode run '@zz-probe'` nor from a mention typed out in the TUI. Claude drove the TUI through a pty and the server API, and found the skill attaches only when picked from the `@` menu.
  - OpenCode 2 has no `CLAUDE.md` fallback, and Claude Code follows a symlink in `~/.claude/skills`.
  - Each harness exports its session ID as a variable. OpenCode 2 keeps sessions in SQLite, which ruled out the planned transcript lookup.
- Claude implemented the plan's part 2 list, with two additions:
  - a loading-reach check;
  - "read-only subagents" in place of "Explore agents", since OpenCode and Codex have subagents of other names.
- In the acceptance, a toolkit copy tested whether `check` stayed out of the install. That led to a `SKILL.md` rule resolving every path against the copy.
- Claude reported, and Rob asked two questions:
  - whether the OpenCode note between the install blocks earned its place;
  - whether the toolkit-copy rule positioned forking the toolkit as a user story.
- Claude answered both:
  - a pasted `@mini-brain-toolkit` silently fails, so the note steers away from a real failure;
  - the toolkit-copy rule came from part 1's deferred finding, not a fork story.
  
  Claude moved the note under the create command and proposed a general guard against writes to the install.
- Rob directed:
  - the instruction goes in the OpenCode 2 label of both create and check, since a reader copies a command without rereading install, and may run check without reading create;
  - the guard goes in general form.
  
  Claude made both changes.
- Rob asked for a re-test before the PR. Claude planted a missing version header in a toolkit copy and a writable test install, and told `check` to apply every fix:
  - With the guard, Codex and OpenCode 2 fixed only the copy.
  - On an ordinary brain wired the old way, Codex applied the loading-reach fix, moving the hook rather than copying it.
  - A control with `main`'s `SKILL.md` also fixed only the copy.
  
  The install stayed byte-identical throughout.
- Rob had the branch committed, pushed and opened as PR #19, and the work item updated on `main`.

## Decisions

- **README intro prose names no single harness; diagrams, alt text and badge unchanged** — Rob.
- **Session ID from the running harness's own variable** — Claude, on the OpenCode 2 finding.
- **OpenCode 2 menu instruction in the create and check labels, not after the install blocks** — Rob.
- **A general install-write guard in `SKILL.md`, not a rule for toolkit copies** — Rob, on Claude's proposal. The reason was to avoid framing a copy of the toolkit as an expected workflow.
- **No symlink in the README for now, and create's branch-first wording left alone** — Claude, raised with Rob as open issues.

## What didn't work

- **`opencode run '@name'`:** it never attaches a skill. Testing OpenCode 2 headlessly needed the server API.
- **An allow-all permission ruleset:** a helper session created with one was blocked by the permission classifier. The default build permissions served.
- **A Codex run from a directory that wasn't a git repo:** it exited without running, so the fixture needed `--skip-git-repo-check`.

## Lessons

- **A note placed before the step it governs fails the reader who copies that step.** Put an instruction beside the command it qualifies, in every section a reader might enter at.
- **A rule written for one collision can frame that case as supported.** A general fail-closed rule covers the hazard without endorsing the case.
- **A guard that passes its test also needs a control.** Here the control showed the models already behaved, which makes the guard a backstop rather than a fix.

---

# PR #19 reviewed by Rob, fixes landed, and the review recorded (2026-11-04)

**Session ID**: `0c40dcd0-74de-49e6-85a5-945479e994cb`

Rob's session, with Claude as co-author. Rob reported that part 2 had been implemented and reviewed in PR #19. Rob's review of `cbdf12e` was posted to the PR as a comment, and `0bd87bf` on `skill-install-part-2`, authored by Rob, fixed every finding. This session recorded the round in the plan and, at Rob's direction, moved the review's substance from the PR comment into this log.

## The review

Rob framed it this way: most findings sit in procedures an agent follows literally, so each one is an instruction that gives a wrong result when followed as written.

- **Blocking: check's loading-reach fix made the next check flag the file it added.** On a brain seeded before part 2, the fix added `AGENTS.md`, but nothing updated that brain's `CLAUDE.md` exemptions. The next check would flag the file as un-namespaced and as missing a version header. The brain's own dream cycle, copied from the old template, would flag it again as an orphan, un-namespaced and unversioned: up to five new findings from following check's advice. Re-running `create` had the same result, since it left an existing `CLAUDE.md` alone. Rob asked whether the dream-cycle exclusions belonged in the same step or in TEMPLATE_DRIFT.
- **Before release: an existing brain `AGENTS.md`.** A brain grown in Codex may already hold its own `AGENTS.md`. `create` kept it, so Codex and OpenCode sessions never reached `CLAUDE.md`, and check's fix read as copying the one-line template over it.
- **Before release: the design docs still put the hook in `CLAUDE.md`.** `MBT_APPROACH.md`'s harness-tie sentence and its hook decision, `MBT_RESEARCH.md`'s harness-neutrality claim and `MBT_COMPARABLES.md`'s `CLAUDE.md` row were outside the diff. Because APPROACH is the design authority, a dream cycle reading it would treat the new behavior as drift. Rob left the "tie to a harness" wording as a judgment call, since Claude Code still needs the import line.
- **Minor: principle 7 omitted `AGENTS.md`.** Principle 6 and both entrypoint templates exempted it from the version header, but principle 7 didn't. Check falls back to principle 7 for a brain that declares no exemptions, so it would flag the `AGENTS.md` it had just added.
- **Minor: `MBT_SESSION_CLOSEOUT.md` still credited Claude and called the session ID a UUID.** The template copy had been updated. With `AGENTS.md` in place, a Codex session closing out this repo would credit Claude in the append-only log.
- **Minor: the template dream cycle's namespace command contradicted its prose.** The prose deferred to `CLAUDE.md`'s exemptions, while the command hard-coded four names. A brain declaring another exemption, as this repo declares `SKILL.md`, would get a false positive, and check and the dream cycle would disagree.

## Resolution

- Check's loading-reach fix now has three parts: the brain entrypoint, the brain conventions and the project hook. The conventions part adds `AGENTS.md` to the target `CLAUDE.md`'s naming and version-header exemptions, and to the dream cycle's exclusions in both prose and commands. It then reruns the affected structural checks. That answered Rob's question: the dream cycle is patched in the same step, not deferred to TEMPLATE_DRIFT.
- `create` on an existing brain applies the same exemption updates. Its idempotence statement now covers merges into existing files, and its report distinguishes files that were created, updated and left unchanged.
- An existing brain `AGENTS.md` is merged into, keeping its instructions, unless it already points to `CLAUDE.md`. Both `create` and check say so.
- APPROACH's hook decision now merges into the project repo's `AGENTS.md`, with an `@AGENTS.md` import in `CLAUDE.md`. The "one tie to a harness is a filename" sentence was cut rather than reworded. RESEARCH says loading still depends on each harness's instruction-file discovery and import conventions. COMPARABLES calls `CLAUDE.md` the brain's entrypoint filename, which in project repos imports the `AGENTS.md` holding the hook.
- Principle 7, `MBT_SESSION_CLOSEOUT.md` and the template dream cycle's namespace command were fixed as the review asked. The command builds its exempt list from `CLAUDE.md`, the same way check does.

## This session

- Claude read the plan, the PR and the fix commit, and confirmed that each finding was addressed. It then recorded the round in the plan's change list and implementation sequence, leaving the merge of PR #19 as the open step.
- Claude first offered to log only what this session did, on the grounds that the fixes came from another session. Rob pointed out that the review findings had been written to the PR as comments rather than to the work item log, so this entry records them here.
- Claude listed what was left on the work item. The review had asked for a retest of the loading-reach fix, and no record showed one had been run.
- Rob asked for the retest. Codex and OpenCode were not on this machine's PATH, so it ran in Claude Code 2.1.318, headless:
  - **Fixture.** Claude seeded a brain from the `2aebc68` templates. It had a dream cycle, and a sibling project repo held the hook in `CLAUDE.md`. A baseline of the old structural checks was clean.
  - **First run.** `check` ran from the PR branch's `SKILL.md`, told to apply every fix. Loading reach was its only structural finding, and the fix did the following:
    - added the brain's `AGENTS.md`;
    - added `AGENTS.md` to the brain's naming and version-header exemptions in `CLAUDE.md`;
    - added it to the dream cycle's orphan and namespace exclusions, in prose and in the command;
    - moved the project hook to `AGENTS.md`, behind an `@AGENTS.md` import.

    It then reran the affected checks.
  - **Second run.** A report-only `check` flagged nothing for `AGENTS.md`, and the install worktree was byte-identical throughout.
  - **Out-of-scope findings.** The second run also reported drift from the current templates: the closeout's transcript-based session ID, and "Explore agents" wording in the dream cycle. That belongs to TEMPLATE_DRIFT. It also noted that `archive/` was missing from git, since the old `create` puts a `.gitkeep` only in `working/`. That predates this PR.
- Rob had the retest folded into this entry, the work item committed on `main`, and the scratch worktrees removed.

## Lessons

- **A review's findings are lineage.** A PR comment lives outside the brain, so a review whose findings shaped the work belongs in the work item's log too.

---

# Loading-reach retest handed off for Codex and OpenCode 2 (2026-11-04)

**Session ID**: `0c40dcd0-74de-49e6-85a5-945479e994cb`

Rob's session, with Claude as co-author, continuing past this session's earlier entry. That entry was already committed, so this follow-on is a new entry rather than an edit to it. Rob wanted to repeat the loading-reach retest on another machine that has Codex and OpenCode 2. He asked for the instructions as a comment on PR #19, and then a closeout.

## Turn by turn

- Claude turned the retest's manual seeding into a standalone `seed.sh`. The script clones the toolkit at `2aebc68` and at the PR branch, then seeds the brain and project repo.
- Claude ran the script in a scratch directory and diffed the result against the fixture the Claude Code retest had used. The first draft also substituted the `<LOBESPACE>_<WORK>` placeholders in the session closeout, which the tested fixture had left intact. Claude limited those substitutions to the files they had touched in the tested run. One difference was kept on purpose: the script adds an `archive/.gitkeep`, so the second run doesn't report a missing `archive/`.
- Claude posted the comment to PR #19. It holds the script, the two `check` prompts, the pass criteria for each run, the noise to ignore, and a final check that the install is untouched.

## Lessons

- **A handed-off test script should be checked against the fixture it reproduces.** A substitution written for convenience can change what is under test without anyone noticing.
