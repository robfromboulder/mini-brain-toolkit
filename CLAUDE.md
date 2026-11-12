@AGENTS.md

# Claude Instructions for Mini-Brain Toolkit

Mini-Brain Toolkit is an agent skill that creates a mini-brain for a project and checks an existing mini-brain against the pattern.

## Repo Layout

This repo is the skill: a clone placed in a harness's skills directory is the install, so every file committed here ships in every install.

- `SKILL.md` — the skill entrypoint; dispatches `create` and `check`, and sets where the toolkit's paths resolve
- `agents/openai.yaml` — Codex's invocation policy for the skill
- `MBT_PATTERN.md` — what a mini-brain is: principles, file set, lifecycle
- `MBT_LOBES.md` — the layout convention for a brain whose knowledge divides into several lobes
- `MBT_CREATE_BRAIN.md`, `MBT_CHECK_BRAIN.md` — the two procedures
- `templates/` — the files `create` copies into a brain and `check` compares a brain against

**One namespace across two repos.** `MBT_` names one namespace that spans this repo and the mini-brain. Each `MBT_` name lives in exactly one of the two and is never duplicated in the other.

## Branching

- Each work item is built on its own branch, the one its runbook in the mini-brain names
- PRs target `main`; merging to `main` means the change is ready to ship in the next release
- PRs merge by rebase only, so every commit on a branch lands on `main` as is: shape a branch's commits before review, and update a branch by rebasing onto `main`, never by merging `main` into it

## Product Files

These rules govern `SKILL.md`, `MBT_PATTERN.md`, `MBT_LOBES.md`, `MBT_CREATE_BRAIN.md` and `MBT_CHECK_BRAIN.md`.

**No version line.** These files carry no `> V<N>` line; their history is this repo's commits and release tags. A template in `templates/` that carries a `> V1, <date>.` line keeps it through every edit, because that line is the version a newly seeded brain starts from.

**Cross-references.** Reference a file's *own* sections freely; reference *another* file by name plus a short description of what's there — never by its section number, since foreign section numbers break silently on renumber.

**Orthogonal content.** Each file covers one concern and tells its own story — keep that orthogonality in the *prose*, not just the file boundaries. A file describes its own subject, never narrating a sibling's. State how a file relates to the others **once**, in its header, then stop pointing sideways. Wiki-style narration — "the data for this lives in X," "see Y," "as covered in Z" — keeps creeping in; resist it: it re-couples files that are meant to stand alone, and rots when they move.

**Declared reference exemptions.** A file names no other of these files, except where an exemption below allows it. An exemption may only point *upstream*, toward the definition a file serves, never *downstream* toward what enacts it.

| File | May reference | Why |
|---|---|---|
| `MBT_PATTERN.md` | *none* | The canonical definition stands alone; it precedes the procedures that enact it and reaches down to neither. |
| `MBT_LOBES.md` | `MBT_PATTERN.md` only | An optional layout layer serves the definition it extends — upstream — and reaches down to no procedure. |

**Procedure boundaries.** `MBT_CREATE_BRAIN.md` and `MBT_CHECK_BRAIN.md` enact the pattern, so each may cite `MBT_PATTERN.md` and `MBT_LOBES.md` as the definitions it implements; they do not reference each other, and naming the templates they copy or compare is inherent to being a procedure. `SKILL.md` dispatches to the two procedures, sets where their paths resolve, and references nothing else.

## Writing Docs and Instructions

All prose in this repo is read like a proof or a program, not a wiki. The reader is adversarial: every token is load-bearing, and every spare one is a question they must resolve.

- **Say it once.** Each fact has exactly one home. Duplication isn't emphasis; it's a second copy to keep in sync and a sign the first statement didn't land.
- **Define before use.** Introduce a thing where the reader first needs it, in dependency order. A forward pointer ("see Step 3", "as below") means the content is in the wrong place — move it, don't link to it.
- **No sideways narration.** A section explains its own subject and never recaps a sibling section's; pointing (`§3`) is fine, restating is not. Across files, the Orthogonal content rule above governs.
- **Every claim earns its keep.** State only what the reader must act on and what you could defend if challenged. Decorative rationale, benefits, and history are cut.
- **Resolve, don't provoke.** A detail that raises a question it doesn't answer is a net loss — prefer omission to a half-explanation.
- **One job per sentence.** A sentence tells the reader what to do or explains why — never several at once.
- **No hard wrapping.** Write each markdown paragraph and list item as one continuous line and let it soft-wrap; manual line breaks inside a paragraph make noisy diffs and fight reflow.
- **Enforced terms bind.** Use each term the mini-brain enforces in its enforced sense, or choose a different word.

When a line's contribution isn't obvious, it isn't contributing — delete it.

## Commit Conventions

**No AI attribution.** Commits carry no `Co-Authored-By: Claude` (or similar) line, and PR descriptions carry no "Generated with" footer — AI authorship is assumed for this repo and isn't stamped per commit or PR. This overrides any harness default that would append one.
