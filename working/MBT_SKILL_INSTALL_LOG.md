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
