# Skill Install: Implementation Plan

## Objective

Let a user create or check a brain with `/mini-brain-toolkit create` and `/mini-brain-toolkit check` from any project repo, with the toolkit installed and updated by one pasteable line.

Implemented in draft PR #17 on branch `skill-install`; the skill itself has not yet been run.

## Context

See `MBT_SKILL_INSTALL_FINDINGS.md` in this directory for the decision record and alternatives considered.

## What changes

- `SKILL.md` (new) — dispatches `create` and `check` to `MBT_CREATE_BRAIN.md` and `MBT_CHECK_BRAIN.md`, asks when the argument names neither, and resolves toolkit paths against the skill's base directory.
- `CLAUDE.md` — `SKILL.md` joins the file-naming and version-header exemptions, and is declared a dispatcher that references only the two procedures.
- `MBT_DREAM_CYCLE.md` — `SKILL.md` counts as product, and the orphan and namespace checks exclude it.
- `README.md` — an install section with the one-line install-or-update command, the slash commands for create and check, and the `Read` prompts as the fallback for other agents.

## Interaction with existing docs

| Existing doc | Interaction | Risk |
|---|---|---|
| `MBT_CREATE_BRAIN.md`, `MBT_CHECK_BRAIN.md` | Their toolkit paths now resolve against the skill's base directory, set only in `SKILL.md` | A procedure that names a path relative to the working directory would resolve into the user's project repo |
| `MBT_CHECK_BRAIN.md` namespace check | Its exempt list names `CLAUDE.md`, `README.md` and `CONTRIBUTING.md` | Running the check on the toolkit itself flags `SKILL.md`; target brains are unaffected |

## Testing approach

Install from the branch with `git clone --branch skill-install https://github.com/robfromboulder/mini-brain-toolkit ~/.claude/skills/mini-brain-toolkit` and start a new session in a project repo.

Acceptance has four parts. `/mini-brain-toolkit check` against an existing brain reads `MBT_PATTERN.md` and the procedure's other citations from the install without the user naming a path. `/mini-brain-toolkit create` against a scratch brain repo copies from the install's `templates/`. `/mini-brain-toolkit` with no argument asks which procedure to run. The README's install line, rerun, updates the clone. The install line already passed in zsh and bash against a scratch `HOME`.

## Implementation sequence

1. Add `SKILL.md` and the `CLAUDE.md` and dream cycle exemptions. Done.
2. Rewrite the README's install, create and check sections. Done.
3. Open the draft PR. Done (#17).
4. Run the acceptance tests, then mark the PR ready.

## Scope boundary — what this does NOT include

- Plugin packaging.
- Edits to the procedures, `MBT_PATTERN.md` or `templates/`.
- Moving existing sibling clones into the skills directory.

## Open issues

1. Whether to add plugin packaging later, for install and update through `/plugin`, at the cost of namespaced commands.
2. Whether a symlink from `~/.claude/skills/mini-brain-toolkit` to an existing sibling clone is a working install, which would let a developer keep one clone for both uses.
3. Whether the next release notes tell existing users how to move from the sibling clone to the skill.
