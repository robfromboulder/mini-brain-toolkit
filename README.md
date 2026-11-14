# mini-brain-toolkit 🧠

[![Claude Code](https://img.shields.io/badge/Built%20with%20Claude%20Code-6366f1?logo=claude&logoColor=white)](https://claude.ai/code)
[![Contributing](https://img.shields.io/badge/contributions-welcome-green.svg)](https://github.com/robfromboulder/mini-brain-toolkit/blob/main/CONTRIBUTING.md)
[![License](https://img.shields.io/github/license/robfromboulder/mini-brain-toolkit)](https://github.com/robfromboulder/mini-brain-toolkit/blob/main/LICENSE)

Using a **mini-brain** with your codebase helps you iterate and triage faster, and gives your coding agent better context to make changes autonomously. This free toolkit provides skills for creating and checking mini-brains.

Contents:

* [What is a mini-brain?](#what-is-a-mini-brain)
* [Installing the toolkit](#installing-the-toolkit)
* [Creating a mini-brain](#creating-a-mini-brain)
* [Checking a mini-brain](#checking-a-mini-brain)
* [Inside a mini-brain](#inside-a-mini-brain)

## What is a mini-brain?

There are many good tools for giving AI agents memory and context, but too many merely accumulate. Every interaction adds to the knowledge store or "second brain", and this grows and drifts over time.

A mini-brain only captures knowledge about your software project that **can't be derived from code or commit history**: what inspires the work, why decisions went one way and not another, what was tried and discarded, what was surprising. A mini-brain doesn't repeat anything your codebase already knows, but curates important details that are easily forgotten or scattered across tickets, wikis, and project documentation.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset=".github/images/curate-not-accumulate-dark.svg">
  <img src=".github/images/curate-not-accumulate-light.svg" alt="Chart: memory that only accumulates grows steadily, while a mini-brain shrinks at each work item closeout and dream cycle and levels off">
</picture>

**Using a mini-brain is just chatting with your coding agent.** Mention the mini-brain in any session, and a hook in your project repo loads it on demand. Your agent reads only the parts it needs, and uses them for research, coding, or triage. At a natural stopping point, you'll be prompted to optionally save what the session decided and learned. There are no formats to learn, no files to copy, and you never leave the repo you're working in.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset=".github/images/what-goes-where-dark.svg">
  <img src=".github/images/what-goes-where-light.svg" alt="A project repo of code and tests, commit history, and tickets and PRs is always treated as ground truth; a separate mini-brain repo holds experimental results, findings, approach, and scope, loaded into sessions on demand by a hook, with session and work item closeouts capturing new facts and decisions back into it">
</picture>

**Mini-brains are self-improving.** On a schedule, a mini-brain dreams: verifying its claims against the code, pruning what's become derivable, and doing follow-on research. The brain stays small enough to read completely, and curious about what it doesn't know. Each dream cycle re-evaluates drift between the codebase, the mini-brain, and the tools and platforms they depend on.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset=".github/images/lifecycle-dark.svg">
  <img src=".github/images/lifecycle-light.svg" alt="Lifecycle: chat with Claude, optionally close out so Claude updates the brain with what was learned, which feeds the next session directly, while a scheduled dream cycle verifies, prunes, and distills the brain">
</picture>

**Mini-brains are built for software teams.** Each feature, bug fix, or support case can be a *work item* with its own working notes, so several teammates can research at once without stepping on each other. When a work item closes out, what it learned is folded into the team's shared knowledge through a PR, reviewable like any other code. A mini-brain is just Markdown files in a dedicated git repo alongside your project repos, and teammates and their agents all work from the same brain.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset=".github/images/team-curation-dark.svg">
  <img src=".github/images/team-curation-light.svg" alt="Three developers each research their own work item at the same time, a new feature, a bug fix, and a support case; as each work item closes out, what it learned flows up into the shared team mini-brain that every session loads">
</picture>

## Installing the toolkit

Use the command below for your harness to install the toolkit skills, or to update to the latest release.

**Claude Code**

```sh
d=~/.claude/skills/mini-brain-toolkit; if [ -d "$d" ]; then git -C "$d" fetch -q --tags; else git clone -q https://github.com/robfromboulder/mini-brain-toolkit "$d"; fi && git -C "$d" checkout -q "$(git -C "$d" tag --sort=-v:refname | head -1)"
```

**Codex**

```sh
d=~/.agents/skills/mini-brain-toolkit; if [ -d "$d" ]; then git -C "$d" fetch -q --tags; else git clone -q https://github.com/robfromboulder/mini-brain-toolkit "$d"; fi && git -C "$d" checkout -q "$(git -C "$d" tag --sort=-v:refname | head -1)"
```

**OpenCode 2**

```sh
d=~/.agents/skills/mini-brain-toolkit; if [ -d "$d" ]; then git -C "$d" fetch -q --tags; else git clone -q https://github.com/robfromboulder/mini-brain-toolkit "$d"; fi && git -C "$d" checkout -q "$(git -C "$d" tag --sort=-v:refname | head -1)"
```

**Other harnesses**

```sh
d=~/mini-brain-toolkit; if [ -d "$d" ]; then git -C "$d" fetch -q --tags; else git clone -q https://github.com/robfromboulder/mini-brain-toolkit "$d"; fi && git -C "$d" checkout -q "$(git -C "$d" tag --sort=-v:refname | head -1)"
```

## Creating a mini-brain

The `create` command helps seed a new mini-brain, whether you're starting a brand new project or adding a mini-brain to an existing codebase. It asks a few questions, configures knowledge files in a dedicated repo for the mini-brain, and hooks the brain into your project repos.

**Claude Code**

```
/mini-brain-toolkit create
```

**Codex**

```
$mini-brain-toolkit create
```

**OpenCode 2** (select the skill from the menu `@` opens, rather than copying and pasting)

```
@mini-brain-toolkit create
```

**Other harnesses**

```
Read ~/mini-brain-toolkit/SKILL.md and run create
```

## Checking a mini-brain

The `check` command evaluates your mini-brain and suggests how to improve its structure and function. It asks which brains to check, then walks you through the recommendations it finds. It also brings the brain's procedures up to date with the installed toolkit, so updating the toolkit and running `check` is the whole upgrade.

**Claude Code**

```
/mini-brain-toolkit check
```

**Codex**

```
$mini-brain-toolkit check
```

**OpenCode 2** (select the skill from the menu `@` opens, rather than copying and pasting)

```
@mini-brain-toolkit check
```

**Other harnesses**

```
Read ~/mini-brain-toolkit/SKILL.md and run check
```

## Inside a mini-brain

Most knowledge systems handle storing and retrieving knowledge, and leave its structure to you. A mini-brain comes with its structure already decided: which document each kind of fact belongs in, how a work item merges into those documents, and how a brain divides when a project holds several problems.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset=".github/images/inside-a-mini-brain-dark.svg">
  <img src=".github/images/inside-a-mini-brain-light.svg" alt="Inside a mini-brain. Every fact has exactly one home: CLAUDE.md is a read index opened first, so an agent loads only the documents a question needs; SCOPE holds the problem and its goals with no solutions in it, APPROACH the chosen design and the decisions behind it, FINDINGS what building it revealed that the code doesn't show, and LOG what each session did, appended and never edited. A work item's in-flight documents live in working/, and its closeout classifies each piece: a claim proved false updates SCOPE, a changed design decision updates APPROACH, a non-obvious decision goes to FINDINGS, and anything the code now states is omitted, which is how a mini-brain shrinks. When one SCOPE can't hold a project's problem, the brain splits into lobes with the full document set each; a fact about two lobes lives in their nearest common ancestor, and siblings never reference each other.">
</picture>
