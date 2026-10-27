# Skill Install: Decision Record

## Problem

Creating or checking a brain meant cloning the toolkit beside the project repo and pasting `Read ../mini-brain-toolkit/MBT_CREATE_BRAIN` or `MBT_CHECK_BRAIN` into a session. The prompt is a file path the user has to know, and it works only from a session whose working directory sits beside the clone.

Those two README prompts are the toolkit's only dependency on where it is cloned. Brains it creates stand alone: the project hook locates `mini-<project>-brain` beside the project's main checkout, and the create procedure inlines the work-item scaffolds so the brain needs no toolkit at runtime. The procedures name toolkit files relative to the toolkit root and say nothing about where that root is.

## Preferred approach: the repo root is the skill

A `SKILL.md` at the repo root makes a clone in `~/.claude/skills/mini-brain-toolkit` a personal skill, invoked as `/mini-brain-toolkit create` or `/mini-brain-toolkit check`. It dispatches the argument to the matching procedure and states once that toolkit paths resolve against the skill's base directory, because the working directory is the user's project repo. The procedures need no edits, since that one sentence supplies the root they already assume.

`disable-model-invocation: true` keeps the skill to explicit invocation. Create and check are always started by the user, and an auto-invoked skill would compete with the project hook's own trigger phrases.

The toolkit's own conventions absorb the new file in `CLAUDE.md`: `SKILL.md` is exempt from the `MBT` lobespace because Claude Code fixes its name, and from the version header because its frontmatter must open the file. The dream cycle excludes it from the orphan and namespace checks and counts it as product. `MBT_PATTERN.md` and `templates/` are unchanged, because the brains they describe carry no `SKILL.md`.

Install and update are one pasteable line. It runs `git -C "$d" pull --ff-only` when the clone exists and clones otherwise. An `if` test is used rather than `pull || clone`, because a failed pull would fall through to a clone that fails on the existing directory with a misleading error. `--ff-only` makes an install someone has edited stop with an error instead of gaining a merge commit.

## Alternatives considered

- **A plugin.** `.claude-plugin/plugin.json` and a marketplace file, with `skills/create/` and `skills/check/`, would install and update through `/plugin`. Rejected for now: plugin skills are namespaced, so the commands would read `/mini-brain-toolkit:create` rather than the requested `/mini-brain-toolkit create`, and the git-based install keeps the update path the sibling clone already had. The namespacing was not verified against current Claude Code docs.
- **A `skill/` subdirectory as the skill root.** Rejected. Every procedure path would resolve one level up from the skill's base directory, and the clone could no longer be installed directly into the skills directory.
- **Dropping the `Read` prompts.** Rejected. They remain the only route for agents without Claude Code skills, so the README keeps them as the fallback.

## What this doesn't solve

- **Discoverability.** A user still has to learn the command from the README; the skill appears in the slash-command list only after it is installed.
- **Existing sibling clones.** They keep working through the fallback prompts, but nothing moves them to the skills directory.
