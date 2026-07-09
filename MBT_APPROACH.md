# Mini-Brain Toolkit: Technical Approach

> V4, 2026-07-09.

This document describes the approach for addressing the problems defined in `MBT_SCOPE.md`. It covers the strategic approach and key design decisions — not delivery sequence.

---

## 1. Strategic Approach

### 1.1 Dogfood the pattern

The toolkit is itself a mini-brain, and its subject is the mini-brain pattern (`MBT_SCOPE.md` 2.5). This is the load-bearing strategic choice: a toolkit that defined the pattern while not following it would be its own counterexample. Dogfooding makes the repo a worked example a reader can inspect end to end — the read index, the version headers, the append-only log, the orthogonal SCOPE/APPROACH split are all *demonstrated*, not just described — and it is the strongest available test that the templates and procedures are actually usable, because building the toolkit exercised them.

The one wrinkle dogfooding creates is that two kinds of top-level knowledge file coexist: the toolkit's *own* brain (`MBT_SCOPE`, `MBT_APPROACH`, …) and the *pattern it defines* as a consumable product (`MBT_PATTERN`, `MBT_CREATE_BRAIN`, `MBT_CHECK_BRAIN`). The read index in `CLAUDE.md` resolves this by ordering the two in blocks rather than interleaving them.

### 1.2 Distill from live exemplars, do not invent

The pattern already works in production brains. The toolkit's job is to *capture* what those brains do, not to design a pattern from first principles. Every template and every procedure step is derived from the ground-truth exemplars — a content-stage brain and a mature brain — so the toolkit inherits conventions that survived real use rather than conventions that sounded good on paper. Where the exemplars carry project-specific detail (test suites, eval numbers, platform splits), the toolkit generalizes it to placeholders while preserving the mechanics that give the convention its value.

### 1.3 Separate the reference from the procedures

The definition and the two procedures are split into three documents rather than one (`MBT_SCOPE.md` 2.1–2.3): a canonical reference (`MBT_PATTERN.md`) that says *what a mini-brain is and why*, and two procedure documents (`MBT_CREATE_BRAIN.md`, `MBT_CHECK_BRAIN.md`) that say *how to build one* and *how to judge one*. This mirrors how the live brains separate a standalone reference from action-oriented runbooks, and it pays off in two ways: each document is well-sized (principle 9) and loads only when its question is being asked (principle 3), and establishment and assessment — genuinely different activities — don't get tangled in one document. Both procedures cite the pattern reference instead of restating it, so the definition has exactly one home.

### 1.4 Templates as the single source of truth

Establishment is a copy-and-substitute operation against `templates/` (`MBT_SCOPE.md` 2.4), never a copy from whichever neighbor was nearest. Centralizing the base files in one directory is what turns "propagate the pattern" from imitation-with-drift into a mechanical, repeatable step — and it gives the sync problem (`MBT_SCOPE.md` 4.2) a single place to be solved when it's solved.

---

## 2. Key Design Decisions

### 2.1 Namespace token `MBT`

The toolkit follows its own principle 4 and carries a namespace token like any other brain. `MBT` was chosen over mirroring the repo name (`TOOLKIT`) or the subject (`BRAIN`): it is short, unambiguous, and — because the toolkit is frequently loaded *alongside* the very brains it assesses — must not collide with a target brain's files. `BRAIN` risked conceptual collision in exactly that scenario; `MBT` cannot.

### 2.2 Keep the archived docs as source material, distill a canonical reference

The philosophical description stays in `archive/` and is treated as source, exactly as a content-stage brain keeps its originating design docs in `archive/` and distills them into SCOPE/APPROACH. `MBT_PATTERN.md` is the distilled, current, operational reference; the archived philosophical doc remains the fuller "why" for anyone who wants it. This avoids two live copies of the definition drifting apart — the philosophy doc is deliberately kept out of the read index. The improvement roadmap gets the same treatment: the archived source stays in `archive/`, distilled into the living `MBT_RESEARCH.md`.

### 2.3 Split the product into three documents

Chosen over a single combined instructions document. A combined doc would be simpler to find but longer to load and would fuse the neutral reference with two opposed procedures. The split keeps each piece selectively loadable and lets establish and assess stay orthogonal, at the cost of three files where the reader must know which one they want — mitigated by the grouped read index.

### 2.4 Checking produces opportunities, not grades, and never edits the target

`MBT_CHECK_BRAIN.md` is a diagnostic that leads with what's working and frames gaps as ranked opportunities, and it is observe-only. This matches the pattern's stance that adherence is a target, not a gate, and keeps a clean line between reading a brain (check), building one (create), and maintaining one (the dream cycle). The observe-only boundary is deliberately conservative; whether a mechanical-fix mode is warranted is left open (`MBT_SCOPE.md` 4.3).

### 2.5 Templates are un-namespaced

Template files use bare names and placeholders so the copy-and-substitute step is obvious. `README.md` in a new repo is merged into rather than overwritten, since it is a repo artifact that may already exist.

### 2.6 Defer mature machinery when establishing

A new brain gets the seed only. The mature-lifecycle docs are real read-index entries a reader must skip on every load, so scaffolding them empty is a cost paid every session for machinery not yet in use. Establishment therefore defers them until the work justifies them — the same shrink-toward-what's-needed discipline the pattern applies to content, applied to structure.
