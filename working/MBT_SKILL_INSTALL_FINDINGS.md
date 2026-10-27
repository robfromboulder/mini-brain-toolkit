# Skill Install: Decision Record

## Problem

Creating or checking a brain meant cloning the toolkit beside the project repo and pasting `Read ../mini-brain-toolkit/MBT_CREATE_BRAIN` or `MBT_CHECK_BRAIN` into a session. The prompt is a file path the user has to know, and it works only from a session whose working directory sits beside the clone.

Those two README prompts are the toolkit's only dependency on where it is cloned. Brains it creates stand alone: the project hook locates `mini-<project>-brain` beside the project's main checkout, and the create procedure inlines the work-item scaffolds so the brain needs no toolkit at runtime. The procedures name toolkit files relative to the toolkit root and say nothing about where that root is.

## Preferred approach: the repo root is the skill

A `SKILL.md` at the repo root makes a clone in a harness's skills directory a skill named `mini-brain-toolkit`, invoked with a `create` or `check` argument. It dispatches the argument to the matching procedure and states once that toolkit paths resolve against the directory holding `SKILL.md`, because the working directory is the user's project repo. The procedures need no edits, since that one sentence supplies the root they already assume.

`SKILL.md` uses only what Claude Code, OpenCode and Codex all honor. It names "the argument the user invoked this skill with" instead of `$ARGUMENTS`, which Codex does not substitute, and "the directory that holds this file" instead of Claude Code's "base directory". `disable-model-invocation: true` stays, because create and check are always started by the user and an auto-invoked skill would compete with the project hook's trigger phrases; only Claude Code honors it.

The toolkit's own conventions absorb the new file in `CLAUDE.md`: `SKILL.md` is exempt from the `MBT` lobespace because the agents that load skills fix its name, and from the version header because its frontmatter must open the file. The dream cycle excludes it from the orphan and namespace checks and counts it as product. `MBT_PATTERN.md` and `templates/` are unchanged, because the brains they describe carry no `SKILL.md`.

The README gives two install options: one for Claude Code or OpenCode, cloning into `~/.claude/skills`, which OpenCode also reads, and one for Codex, cloning into `~/.agents/skills`. Each is one pasteable line that runs `git -C "$d" pull --ff-only` when the clone exists and clones otherwise. An `if` test is used rather than `pull || clone`, because a failed pull would fall through to a clone that fails on the existing directory with a misleading error. `--ff-only` makes an install someone has edited stop with an error instead of gaining a merge commit.

Codex invokes skills with `$` where the other two use `/`, so no single command serves every harness. Create and check each open with a paragraph saying what the command does, then give the command under a heading per harness, matching the install section's shape. The reader runs the command shown for their harness and never rewrites one.

## Alternatives considered

- **A plugin.** `.claude-plugin/plugin.json` and a marketplace file, with `skills/create/` and `skills/check/`, would install and update through `/plugin`, and would list each command separately in the slash menu. Rejected for now: plugin skills are namespaced, so the commands would read `/mini-brain-toolkit:create` rather than `/mini-brain-toolkit create`, and the git-based install keeps the update path the sibling clone already had. The namespacing was not verified against current Claude Code docs.
- **A `skill/` subdirectory as the skill root.** Rejected. Every procedure path would resolve one level up from the skill's directory, and the clone could no longer be installed directly into a skills directory.
- **Asking the agent to install the skill from the repo URL.** One prompt would serve every harness, and each harness knows its own skills directory. Rejected: the prompt must still state what a URL cannot — that the whole repo is the skill, that it is a git clone so updating is a pull, and that it installs for the user rather than the project — and a wrong install surfaces only when the command first fails in a new session.
- **Keeping the `Read` prompts as a fallback.** Rejected. Using them meant telling the reader to replace each documented command, which defeats commands that run as written.
- **A separate OpenCode install option.** Rejected. OpenCode reads `~/.claude/skills`, so the Claude Code line installs for both, and a third line invites a duplicate install of the same skill.

## What this doesn't solve

- **Harnesses beyond these three.** They have no documented path; the procedures remain readable by path, but the README no longer says so.
- **Model invocation outside Claude Code.** OpenCode ignores `disable-model-invocation`, and Codex sets the equivalent in a separate `agents/openai.yaml`, so in both the agent may load the skill unasked.
- **Discoverability.** A user still has to learn the command from the README; the skill appears in a harness's command list only after it is installed, and its argument appears only as hint text.
- **Existing sibling clones.** Nothing moves them to a skills directory.
