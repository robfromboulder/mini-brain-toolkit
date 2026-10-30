---
name: mini-brain-toolkit
description: Create a new mini-brain for a project, or check an existing mini-brain against the pattern.
argument-hint: create | check
disable-model-invocation: true
---

# Mini-Brain Toolkit: Skill

Read the procedure for the command the user asked for, and follow it:

| Command | Procedure |
|---|---|
| `create` | `MBT_CREATE_BRAIN.md` |
| `check` | `MBT_CHECK_BRAIN.md` |

If the user named neither, ask which to run.

Resolve every `MBT_*.md` file and every `templates/` path against the directory that holds this file. Every other path names a file in the brain or project the procedure is working on.
