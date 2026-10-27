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
