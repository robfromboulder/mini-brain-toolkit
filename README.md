# mini-brain-toolkit 🧠

[![Claude Code](https://img.shields.io/badge/Built%20with%20Claude%20Code-6366f1?logo=claude&logoColor=white)](https://claude.ai/code)
[![License](https://img.shields.io/github/license/robfromboulder/mini-brain-toolkit)](https://github.com/robfromboulder/mini-brain-toolkit/blob/main/LICENSE)

Using a **mini-brain** with your codebase helps you iterate and triage faster, and gives Claude better context to make changes autonomously. This free toolkit provides agentic tools for creating and improving mini-brains.

## What is a mini-brain?

A mini-brain only captures knowledge about your software project that **can't be derived from code or git history**: what inspires the work, why decisions went one way and not another, what was tried and discarded, what was surprising. Normally these details live in your team's heads or are scattered across tickets, wikis, and project docs. A mini-brain curates these details so every Claude session understands the problem statement, the technical approach, the design tradeoffs, and the implementation decisions behind your codebase.  

**Using a mini-brain is just chatting with Claude.** Your coding sessions are the raw material. At each natural stopping point, you'll be prompted to optionally save what the session decided and learned. There's nothing to file, no format to learn, and you never leave the repo you're working in. Even creating a new mini-brain is done by chatting with Claude.

**Mini-brains are built for software teams.** A mini-brain is just Markdown files in a dedicated git repo, alongside your regular project repos. Changes to a mini-brain are made through commits and PRs, reviewable like any other code. This knowledge belongs to the team, and teammates and AI agents all work from the same brain.

**Mini-brains are self-improving.** On a schedule, a mini-brain dreams: verifying all claims against the codebase, pruning what's become derivable, and doing follow-on research. The brain stays small enough to read completely, and curious about what it doesn't know. Each dream cycle re-evaluates drift between the codebase, the mini-brain, and their surroundings.

## Creating a mini-brain

Paste this into a Claude session — works whether you're starting a new project or adding a mini-brain to an existing codebase:

> Read ../mini-brain-toolkit/MBT_CREATE_BRAIN

This asks a few questions, sets up a new dedicated repo for the mini-brain, generates seed files, and hooks the brain into your project repos.

## Improving a mini-brain

A new brain starts small — run this to see where it stands and what to add next as it matures:

> Read ../mini-brain-toolkit/MBT_CHECK_BRAIN

This asks which brains to check, then walks you through the recommendations it finds.

## Why a mini-brain?

There are many good tools for giving AI agents memory and context: instruction files, production memory systems, knowledge-management patterns like ADRs and Zettelkasten. But most of them merely accumulate. Every interaction adds to the store, and it grows over time.

A mini-brain makes the opposite bet: **store only what the code can't tell you, and shrink as knowledge becomes derivable.** Decisions, rejected paths, and surprising findings stay. Anything the codebase or git history can already answer gets pruned. The result is a small, high-trust store that an AI agent can load incrementally and a new teammate can read in minutes.

If you're curious about the design:
- [MBT_PATTERN.md](MBT_PATTERN.md) — the principles, file set, and lifecycle
- [MBT_RESEARCH.md](MBT_RESEARCH.md) — how mini-brains compare to related approaches
- [MBT_BIOLOGY.md](MBT_BIOLOGY.md) — the cognitive-science models the pattern draws on
