# Skill Install: Implementation Plan

## Objective

Let a user create or check a brain from Claude Code, OpenCode or Codex by running the toolkit's skill with a `create` or `check` argument, with the toolkit installed and updated by one pasteable line per harness.

Implemented in draft PR #17 on branch `skill-install`; the skill itself has not yet been run in any harness.

## Context

See `MBT_SKILL_INSTALL_FINDINGS.md` in this directory for the decision record and alternatives considered.

## What changes

- `SKILL.md` (new) — dispatches `create` and `check` to `MBT_CREATE_BRAIN.md` and `MBT_CHECK_BRAIN.md`, asks when there is no argument or it names neither, and resolves toolkit paths against the directory holding `SKILL.md`.
- `CLAUDE.md` — `SKILL.md` joins the file-naming and version-header exemptions, and is declared a dispatcher that references only the two procedures.
- `MBT_DREAM_CYCLE.md` — `SKILL.md` counts as product, and the orphan and namespace checks exclude it.
- `README.md` — install, create and check sections each open with a paragraph describing the step, then give one command under a heading for Claude Code or OpenCode and one for Codex. The `Read` prompts are removed.

## Interaction with existing docs

| Existing doc | Interaction | Risk |
|---|---|---|
| `MBT_CREATE_BRAIN.md`, `MBT_CHECK_BRAIN.md` | Their toolkit paths now resolve against the directory holding `SKILL.md`, set only in `SKILL.md` | A procedure that names a path relative to the working directory would resolve into the user's project repo |
| `MBT_CHECK_BRAIN.md` namespace check | Its exempt list names `CLAUDE.md`, `README.md` and `CONTRIBUTING.md` | Running the check on the toolkit itself flags `SKILL.md`; target brains are unaffected |

## Testing approach

Install from the branch in each harness's skills directory — `git clone --branch skill-install https://github.com/robfromboulder/mini-brain-toolkit ~/.claude/skills/mini-brain-toolkit` for Claude Code and OpenCode, the same into `~/.agents/skills/mini-brain-toolkit` for Codex — and start a new session in a project repo.

Acceptance, in each of Claude Code, OpenCode and Codex, has four parts. `check` against an existing brain reads `MBT_PATTERN.md` and the procedure's other citations from the install without the user naming a path. `create` against a scratch brain repo copies from the install's `templates/`. The skill with no argument asks which procedure to run. The README's install line, rerun, updates the clone. Argument passing is the least certain part: OpenCode's slash invocation of skills and Codex's text after a `$` mention are inferred from their docs. Both install lines already passed in zsh and bash against a scratch `HOME`.

## Implementation sequence

1. Add `SKILL.md` and the `CLAUDE.md` and dream cycle exemptions. Done.
2. Rewrite the README's install, create and check sections. Done.
3. Open the draft PR. Done (#17).
4. Extend `SKILL.md` and the README to OpenCode and Codex. Done.
5. Run the acceptance tests in all three harnesses, then mark the PR ready.

## Scope boundary — what this does NOT include

- Plugin packaging.
- Edits to the procedures, `MBT_PATTERN.md` or `templates/`.
- Moving existing sibling clones into a skills directory.
- Harnesses beyond Claude Code, OpenCode and Codex.

## Open issues

1. Whether to add plugin packaging later, for install and update through `/plugin` and a menu entry per command, at the cost of namespaced commands.
2. Whether a symlink from a skills directory to an existing sibling clone is a working install, which would let a developer keep one clone for both uses.
3. Whether the next release notes tell existing users how to move from the sibling clone to the skill, now that the README no longer documents the `Read` prompts.
4. Whether to add an `agents/openai.yaml` with `allow_implicit_invocation: false`, so Codex also keeps the skill to explicit invocation.
