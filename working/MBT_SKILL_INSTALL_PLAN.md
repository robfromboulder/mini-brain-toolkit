# Skill Install: Implementation Plan

## Objective

Let a user create or check a brain by running the toolkit's skill with a `create` or `check` argument, with the toolkit installed and updated by one pasteable line per harness, and let brains created from any supported harness load in that harness.

The work lands in two PRs. Part 1, PR #17, installs the toolkit as a Claude Code skill and runs it by path from other harnesses; it merged ahead of PR #18. Part 2, PR #19, adds Codex and OpenCode 2.

## Context

See `MBT_SKILL_INSTALL_FINDINGS.md` in this directory for the decision record and alternatives considered.

## Part 1: Claude Code (PR #17)

### What changes

- `SKILL.md` (new) — dispatches `create` and `check` to `MBT_CREATE_BRAIN.md` and `MBT_CHECK_BRAIN.md`, and asks when the user named neither. `MBT_*.md` files and `templates/` paths resolve against the directory holding `SKILL.md`; every other path belongs to the brain or project the procedure works on.
- `CLAUDE.md` — `SKILL.md` joins the read index and the file-naming and version-header exemptions, and is declared a dispatcher that references only the two procedures and sets where their toolkit paths resolve.
- `MBT_DREAM_CYCLE.md` — `SKILL.md` counts as product, and the namespace check excludes it. The read index lists it, so the orphan check needs no exemption.
- `README.md` — install, create and check sections each open with a paragraph describing the step, then give one command under a **Claude Code** heading and one under **Other harnesses**. Other harnesses clone to `~/mini-brain-toolkit` and run `Read ~/mini-brain-toolkit/SKILL.md and run create` (or `check`).

### Interaction with existing docs

| Existing doc | Interaction | Risk |
|---|---|---|
| `MBT_CREATE_BRAIN.md`, `MBT_CHECK_BRAIN.md` | Their toolkit paths resolve against the directory holding `SKILL.md`, set only in `SKILL.md` | A toolkit file outside `MBT_*.md` and `templates/` would resolve into the target brain |
| `MBT_CHECK_BRAIN.md` namespace check | Its exempt list names `CLAUDE.md`, `README.md` and `CONTRIBUTING.md` | Running the check on a copy of the toolkit flags `SKILL.md`; other target brains are unaffected. Part 2 reads the exemptions the target's `CLAUDE.md` declares |
| `SKILL.md`'s path rule | It sends every `MBT_*.md` file to the install, which is safe only while no target shares the `MBT` lobespace | Checking a copy of the toolkit reads that copy's `MBT_*.md` files from the install, where approved fixes could also land. Part 2 forbids writes under the install |
| PR #18 | Both bump `MBT_DREAM_CYCLE.md`'s version | #18 rebased onto #17 at V24 |

### Testing approach

Install from the branch: `git clone --branch skill-install https://github.com/robfromboulder/mini-brain-toolkit ~/.claude/skills/mini-brain-toolkit`, and start a new Claude Code session in a project repo.

Acceptance has five parts. `check` against an existing brain reads `MBT_PATTERN.md` and the procedure's other citations from the install without the user naming a path. `create` against a scratch brain repo copies from the install's `templates/` and edits the new brain's `CLAUDE.md`, not the install's. The skill with no argument asks which procedure to run. The README's install line, rerun, updates the clone. `Read ~/mini-brain-toolkit/SKILL.md and run check`, from a clone at that path, runs the check. Both install lines already passed in zsh and bash against a scratch `HOME`.

### Implementation sequence

1. Add `SKILL.md` and the `CLAUDE.md` and dream cycle exemptions. Done.
2. Rewrite the README's install, create and check sections. Done.
3. Open the draft PR. Done (#17).
4. Reframe to Claude Code and other harnesses, fix `SKILL.md`'s path rule, and index `SKILL.md`. Done.
5. Retitle and redescribe PR #17, run the acceptance tests, then mark it ready. Done.
6. Address the code review of PR #17: the README's install intro no longer says every line configures a skill, `CLAUDE.md` adds that `SKILL.md` sets where toolkit paths resolve, and the dream cycle drops `SKILL.md`'s orphan exemption. Done.
7. Merge PR #17, ahead of #18. Done. The README's install line, run from `main` against a scratch `HOME` in zsh and bash, cloned the merged toolkit and reported up to date on a rerun.
8. Run the installed skill from `main` in Claude Code. Rob, pending.

## Part 2: Codex and OpenCode 2 (PR #19)

### What changes

- `README.md` — a Codex block and an OpenCode 2 block between Claude Code and Other harnesses in each section, with no other change to the structure. Codex and OpenCode 2 install into `~/.agents/skills`; the commands are `$mini-brain-toolkit` and `@mini-brain-toolkit`. The OpenCode 2 label in create and check says to select the skill from the `@` menu rather than paste the command. The intro prose names no single harness; the diagrams and badge are unchanged.
- `templates/PROJECT_HOOK.md`, `MBT_CREATE_BRAIN.md` — the hook merges into the project repo's `AGENTS.md`, and the repo's `CLAUDE.md` carries `@AGENTS.md`. Either file is created if missing and never overwritten.
- A brain-side `AGENTS.md` template — one line telling the agent to read `CLAUDE.md` and follow it, copied when the brain lacks the file and merged into one that doesn't already point there. The toolkit repo gains the same file.
- `templates/SESSION_CLOSEOUT.md`, `MBT_SESSION_CLOSEOUT.md` — the session ID is the running harness's own environment variable, still asking when it isn't set.
- `templates/README.md`, `templates/SESSION_CLOSEOUT.md` — "Claude session" and "Claude as co-author" stop naming one harness.
- `agents/openai.yaml` (new) — `policy.allow_implicit_invocation: false`.
- `MBT_PATTERN.md`, `MBT_CHECK_BRAIN.md`, `MBT_DREAM_CYCLE.md`, `templates/DREAM_CYCLE.md`, `CLAUDE.md` — `AGENTS.md` joins the file set and the exemptions. The check reads naming exemptions from the target's `CLAUDE.md` instead of a hard-coded list, and a new loading-reach check flags a hook or entrypoint that reaches only `CLAUDE.md`. Its fix, and `create` on an existing brain, also add `AGENTS.md` to the brain's `CLAUDE.md` exemptions and its dream cycle's exclusions. "Explore agents" become "read-only subagents" in the check and the template dream cycle.
- `SKILL.md` — never write to a file under the install.
- `MBT_APPROACH.md`, `MBT_RESEARCH.md`, `MBT_COMPARABLES.md` — the hook lives in the project repo's `AGENTS.md`, and harness-neutrality no longer rests on one filename.

### Testing approach

The part 1 acceptance, in Codex and OpenCode 2. Plus: a brain created in each harness loads from a project repo on the trigger phrase, in that harness and in Claude Code; text after `$mini-brain-toolkit` and `@mini-brain-toolkit` reaches the skill; and in OpenCode 2 a skill with `disable-model-invocation` still resolves by `@` from `~/.agents/skills`. Also: the Other harnesses prompt's `~` path resolves outside Claude Code, and `check` told to apply every fix to a copy of the toolkit leaves the install unchanged.

### Implementation sequence

1. Probe each harness for install location, invocation, arguments, instruction files and session IDs. Done, in Claude Code 2.1.318, Codex 0.166.0 and OpenCode 2.2.5.
2. Move the hook to `AGENTS.md`, add the brain's `AGENTS.md`, the loading-reach check, the session ID variables and `agents/openai.yaml`, and add the README blocks. Done.
3. Run the acceptance in Codex and OpenCode 2. Done; every part passed.
4. Relocate the OpenCode menu note from install to the create and check labels, and replace `SKILL.md`'s toolkit-copy rule with the install guard, both at Rob's direction. Re-test the guard in Codex and OpenCode 2 with a control. Done.
5. Open PR #19. Done.
6. Address Rob's review of PR #19: check 8's fix and `create` add `AGENTS.md` to an existing brain's exemptions and dream-cycle exclusions; an existing brain `AGENTS.md` is merged into, not overwritten; APPROACH, RESEARCH and COMPARABLES follow the hook to `AGENTS.md`; principle 7 exempts `AGENTS.md`; `MBT_SESSION_CLOSEOUT.md` credits the coding agent; the template dream cycle builds its namespace exemptions from `CLAUDE.md`. Done. Retested in Claude Code 2.1.318 on a brain and project repo seeded from the `2aebc68` templates: `check` applied the loading-reach fix, a second `check` reported nothing for `AGENTS.md`, and the install stayed unchanged. Not yet run in Codex or OpenCode 2.
7. Merge PR #19.

## Scope boundary — what this does NOT include

- Plugin packaging.
- Moving existing sibling clones into a skills directory.
- Harnesses beyond Claude Code, Codex and OpenCode 2 having their own block.
- OpenCode 1, which has no user invocation of skills.

## Open issues

1. Whether to add plugin packaging later, for install and update through `/plugin` and a menu entry per command, at the cost of namespaced commands.
2. Whether the README offers a symlink from `~/.claude/skills` to the `~/.agents/skills` clone, which Claude Code follows, giving one clone for all three harnesses.
3. Whether the next release notes tell existing users how to move from the sibling clone to the skill.
4. Whether create's "if on the default branch, branch first" step should apply only when committing. In Codex and OpenCode 2 it branched both repos before writing, and Codex's sandbox refused the write to `.git`.
