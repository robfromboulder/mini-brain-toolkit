# <project> 🧠

This [mini-brain](https://github.com/robfromboulder/mini-brain-toolkit) allows all <project> knowledge and history to be used from any Claude session, and provides standard workflows to maintain and improve this knowledge over time.

This is not a "second brain" with the goal of capturing all <project> knowledge -- this mini-brain only maintains information that cannot be derived from the codebase.

## Knowledge files

All knowledge is stored in Markdown files. Each file captures an orthogonal dimension of knowledge about <project>: its scope, technical approach, working features, work log, and so on.

CLAUDE.md provides a read index so that Claude can discover and apply knowledge that is relevant to the active chat session.

Knowledge files in this mini-brain are `<PREFIX>_`-namespaced. This convention lets you load more than one mini-brain into the same coding session without filename collisions or confusion during updates.

## Usage

#### 1. Use <project> knowledge from a sibling repo directory:

> Read ../mini-<project>-brain/CLAUDE for instructions

#### 2. Save notes about this Claude session:

> Read <PREFIX>_SESSION_CLOSEOUT and append to <PREFIX>_LOG