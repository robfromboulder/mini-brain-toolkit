# Mini-Brain Toolkit: Technical Approach

> V7, 2026-07-27.

This document describes the approach for addressing the problems defined in `MBT_SCOPE.md`. It covers the strategic approach and key design decisions — not delivery sequence.

---

## 1. Strategic Approach

### 1.1 Dogfood the pattern

The toolkit is itself a mini-brain, and its subject is the mini-brain pattern — exemplifying the pattern it defines is one of the goals in `MBT_SCOPE.md`. This is the load-bearing strategic choice: a toolkit that defined the pattern while not following it would be its own counterexample. Dogfooding makes the repo a worked example a reader can inspect end to end — the read index, the version headers, the append-only log, the orthogonal SCOPE/APPROACH split are all *demonstrated*, not just described — and it is the strongest available test that the templates and procedures are actually usable, because building the toolkit exercised them.

The one wrinkle dogfooding creates is that two kinds of top-level knowledge file coexist: the toolkit's *own* brain (its problem, design, and findings) and the *pattern it defines* as a consumable product (the reference and the two procedures). The read index resolves this by grouping the two in blocks rather than interleaving them.

### 1.2 Distill from live exemplars, do not invent

The pattern already works in production brains. The toolkit's job is to *capture* what those brains do, not to design a pattern from first principles. Every template and every procedure step is derived from the ground-truth exemplars — a content-stage brain and a mature brain — so the toolkit inherits conventions that survived real use rather than conventions that sounded good on paper. Where the exemplars carry project-specific detail (test suites, eval numbers, platform splits), the toolkit generalizes it to placeholders while preserving the mechanics that give the convention its value.

### 1.3 Separate the reference from the procedures

The definition and the two procedures are split into three documents rather than one, matching the three goals in `MBT_SCOPE.md`: a standalone reference that says *what a mini-brain is and why*, and two procedure documents that say *how to build one* and *how to judge one*. A single combined document would be simpler to find, but it would fuse the neutral reference with two opposed procedures. The split mirrors how the live brains separate a standalone reference from action-oriented runbooks, and it pays off in two ways: each document stays small and loads only when its question is being asked, and establishment and assessment — genuinely different activities — don't get tangled in one document. The cost is three files where the reader must know which one they want, mitigated by the grouped read index. The definition lives in the reference alone, cited rather than restated, so it has exactly one home.

### 1.4 Templates as the single source of truth

Establishment is a copy-and-substitute operation against `templates/` (the base-template goal in `MBT_SCOPE.md`), never a copy from whichever neighbor was nearest. Centralizing the base files in one directory is what turns "propagate the pattern" from imitation-with-drift into a mechanical, repeatable step — and it gives the template/reference sync problem (an open question in `MBT_SCOPE.md`) a single place to be solved when it's solved.

---

## 2. Key Design Decisions

### 2.1 Namespace token `MBT`

The toolkit carries a namespace token like any other brain. `MBT` was chosen over mirroring the repo name (`TOOLKIT`) or the subject (`BRAIN`): it is short, unambiguous, and — because the toolkit is frequently loaded *alongside* the very brains it assesses — must not collide with a target brain's files. `BRAIN` risked conceptual collision in exactly that scenario; `MBT` cannot.

### 2.2 Keep the archived docs as source material, distill a canonical reference

The philosophical description stays in `archive/` and is treated as source, exactly as a content-stage brain keeps its originating design docs in `archive/` and distills them into SCOPE/APPROACH. The distilled, current, operational reference is what the read index carries; the archived philosophical doc remains the fuller "why" for anyone who wants it. This avoids two live copies of the definition drifting apart — the philosophy doc is deliberately kept out of the read index. The improvement roadmap gets the same treatment: the archived source stays in `archive/`, distilled into a living current-state document.

### 2.3 Checking produces opportunities, not grades, and never edits the target

The assessment procedure is a diagnostic that leads with what's working and frames gaps as ranked opportunities, and it is observe-only. This matches the pattern's stance that adherence is a target, not a gate, and keeps a clean line between reading a brain, building one, and maintaining one. The observe-only boundary is deliberately conservative; whether a mechanical-fix mode is warranted is left open (an open question in `MBT_SCOPE.md`).

### 2.4 Templates are un-namespaced

Template files use bare names and placeholders so the copy-and-substitute step is obvious. `README.md` in a new repo is merged into rather than overwritten, since it is a repo artifact that may already exist.

### 2.5 Defer mature machinery when establishing

A new brain gets the seed only. The mature-lifecycle docs are real read-index entries a reader must skip on every load, so scaffolding them empty is a cost paid every session for machinery not yet in use. Establishment therefore defers them until the work justifies them — the same shrink-toward-what's-needed discipline the pattern applies to content, applied to structure.

### 2.6 The project-repo hook is merged, not copied

Where a developer works migrates over a project's life: before project code exists, work items are thought through in the brain itself; once the project is established, iteration happens in a project repo, and switching directories to use the brain is friction that kills the habit. The hook template answers this — a section merged into each project repo's `CLAUDE.md` that loads the brain into that repo's sessions on demand and has the agent proactively offer a session closeout at natural stopping points — so the brain's workflows run wherever the developer already is, in both directions and at every stage. It was distilled from the exemplar where it emerged, where the closeout prompt measurably increased brain use. Because the target `CLAUDE.md` belongs to the project repo and may already exist, the hook is merged in as a section, never copied over — the same rule as `README.md`.
