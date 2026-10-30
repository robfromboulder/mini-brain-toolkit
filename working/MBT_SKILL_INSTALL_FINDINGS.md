# Skill Install: Decision Record

## Problem

Creating or checking a brain meant cloning the toolkit beside the project repo and pasting `Read ../mini-brain-toolkit/MBT_CREATE_BRAIN` or `MBT_CHECK_BRAIN` into a session. The prompt is a file path the user has to know, and it works only from a session whose working directory sits beside the clone.

Those two README prompts are the toolkit's only dependency on where it is cloned. The procedures name toolkit files relative to the toolkit root and say nothing about where that root is, and they do not depend on the project hook: create and check run the same whether or not a project repo loads the brain.

The brains create produces depend on Claude Code. The project hook merges into the project repo's `CLAUDE.md`, the brain's entrypoint is `CLAUDE.md`, and the closeout finds the session ID under `~/.claude/projects/`. A harness that reads only `AGENTS.md` runs create and check but never loads the brain they produce.

## Harness facts

Verified against each harness's docs on 2026-10-29 and 2026-10-30.

| | Claude Code | Codex | OpenCode 2 |
|---|---|---|---|
| Global skill directories | `~/.claude/skills` | `~/.agents/skills` | `~/.config/opencode/skills`, `~/.claude/skills`, `~/.agents/skills` |
| User invocation | `/name args` | `$name`, or the `/skills` menu | `@name` |
| Suppressing model invocation | `disable-model-invocation: true` | `agents/openai.yaml`: `policy.allow_implicit_invocation: false` | `disable-model-invocation: true`, or `metadata.opencode/autoinvoke: false` |
| Duplicate skills | — | Not merged; both appear | Resolved by ID from the folder name; the later source wins, and `~/.agents/skills` registers after `~/.claude/skills` |
| Instruction file | `CLAUDE.md`, which can import `@AGENTS.md` | `AGENTS.md`, plus names in `project_doc_fallback_filenames` | `AGENTS.md`; a `CLAUDE.md` fallback when it is absent is documented but reported removed |

OpenCode 1 has no user invocation of skills; the model loads them through its `skill` tool. Neither Codex nor OpenCode 2 documents whether text after the mention reaches the skill.

## Preferred approach: the repo root is the skill

A `SKILL.md` at the repo root makes a clone in a harness's skills directory a skill named `mini-brain-toolkit`. It dispatches the command the user asked for to the matching procedure, a wording that serves `/`, `$` and `@` invocation and a plain `Read` alike. It resolves `MBT_*.md` files and `templates/` paths against the directory holding `SKILL.md` and every other path against the brain or project being worked on, because the procedures also name files of the target brain, such as its `CLAUDE.md`, that would otherwise resolve into the install. The procedures need no edits. `disable-model-invocation: true` stays, because create and check are always started by the user and an auto-invoked skill would compete with the project hook's trigger phrases.

The toolkit's own conventions absorb the new file in `CLAUDE.md`: `SKILL.md` is exempt from the `MBT` lobespace because the agents that load skills fix its name, and from the version header because its frontmatter must open the file. The dream cycle excludes it from the orphan and namespace checks and counts it as product.

Each install line runs `git -C "$d" pull --ff-only` when the clone exists and clones otherwise. An `if` test is used rather than `pull || clone`, because a failed pull would fall through to a clone that fails on the existing directory with a misleading error. `--ff-only` makes an install someone has edited stop with an error instead of gaining a merge commit.

The README's install, create and check sections each open with a paragraph saying what the step does, then give a command under a heading per harness. The reader runs the command shown for their harness and never rewrites one. **Other harnesses** is the last block in every section: the toolkit clones to `~/mini-brain-toolkit` and runs by `Read ~/mini-brain-toolkit/SKILL.md and run create`. Each harness added later is a block inserted before it, with nothing else in the section changing.

### Two PRs

Part 1 ships Claude Code and other harnesses; part 2 adds Codex and OpenCode 2. A README that lists a harness promises that the brain create produces works there, and for Codex that needs changes to the create procedure and templates that PR #18 also edits. Part 1 touches only `SKILL.md`, `CLAUDE.md`, `MBT_DREAM_CYCLE.md` and `README.md`, needs acceptance in one harness, and merges ahead of #18. Other harnesses ship in part 1 although the brain loads only where `CLAUDE.md` is read: the procedures run there, and part 2 closes the loading gap for every harness that reads `AGENTS.md`.

### Part 2 design

- **Project hook in `AGENTS.md`, imported by `CLAUDE.md`.** Claude Code imports `@AGENTS.md`; Codex and OpenCode read `AGENTS.md`. The hook keeps one home.
- **Brain entrypoint stays `CLAUDE.md`, with a one-line `AGENTS.md`** telling the agent to read it. The pattern, the lobe layout and every template name `CLAUDE.md`, so renaming the entrypoint would touch all of them.
- **Codex and OpenCode 2 install into `~/.agents/skills`**, the one directory both read. A user with both installs gets the `~/.agents` copy in OpenCode 2, the one the README assigns it.
- **`agents/openai.yaml` with `allow_implicit_invocation: false`.** Codex is the only one of the three that ignores `disable-model-invocation`, and once the hook reaches `AGENTS.md` its trigger phrases would compete with the skill.
- **Closeout names each harness's transcript location**, keeping the fallback of asking.

## Alternatives considered

- **A plugin.** `.claude-plugin/plugin.json` and a marketplace file, with `skills/create/` and `skills/check/`, would install and update through `/plugin`, and would list each command separately in the slash menu. Rejected for now: plugin skills are namespaced, so the commands would read `/mini-brain-toolkit:create` rather than `/mini-brain-toolkit create`, and the git-based install keeps the update path the sibling clone already had. The namespacing was not verified against current Claude Code docs.
- **A `skill/` subdirectory as the skill root.** Rejected. Every procedure path would resolve one level up from the skill's directory, and the clone could no longer be installed directly into a skills directory.
- **Asking the agent to install the skill from the repo URL.** One prompt would serve every harness. Rejected: the prompt must still state what a URL cannot — that the whole repo is the skill, that it is a git clone so updating is a pull, and that it installs for the user rather than the project — and a wrong install surfaces only when the command first fails in a new session.
- **Per-procedure `Read` prompts as a fallback.** Rejected. Reading `SKILL.md` serves both commands from one path the install line fixes.
- **"Without installing" as the fallback heading.** Rejected: the fallback still installs a clone, at a fixed path.
- **Codex and OpenCode in PR #17.** Rejected: listing them before brains load there promises what create does not deliver, and making it deliver widens #17 into the files #18 edits.
- **The hook written into both `CLAUDE.md` and `AGENTS.md`.** Rejected: two copies to keep in sync.
- **A plain-language command for OpenCode.** Rejected: OpenCode 2's `@` invocation replaces it, and OpenCode 1 is out of scope.
- **`--depth 1` on the install.** Rejected: the packed repo is about 344 KB, and a shallow clone complicates later pulls.

## What this doesn't solve

- **Discoverability.** A user still has to learn the command from the README; the skill appears in a harness's command list only after it is installed, and its argument appears only as hint text.
- **Existing sibling clones.** Nothing moves them to a skills directory.
