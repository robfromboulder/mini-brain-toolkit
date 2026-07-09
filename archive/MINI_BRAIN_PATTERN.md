# The Mini-Brain Pattern

Working document. A portable definition of the mini-brain pattern, written so a human or an AI agent can read it and then assess whether some other project follows the same conventions — and, where it doesn't, suggest how it might benefit.

## What it is

A **mini-brain** is a small, curated set of plain-text documents that holds a project's hard-won knowledge: the decisions, the reasons behind them, the paths that were tried and rejected, and the lessons learned along the way — the things the project's own code, history, and tickets *can't* tell you on their own. It is kept deliberately small and maintained over time, so that an AI agent or a new teammate can get oriented quickly and trust what they read.

The mini-brain is not a wiki, a full architecture manual, or a second copy of the documentation. Its defining bet is the opposite of "write everything down": **capture only what would otherwise be lost, and let everything else stay where it already lives.**

## How to use this for assessment

Read the principles below and walk through the target project one at a time. For each, ask whether the project shows the convention and — more importantly — gets the *value* behind it. A useful verdict for each principle is simply **present / partial / absent / not applicable**, with a one-line note on what you saw.

This is a target, not a gate. Most projects will match some principles and not others; partial adherence is normal and fine. The point is to surface opportunities ("this project keeps a great decision log but has no front-door index, so newcomers can't find it"), not to grade harshly. A project can be a healthy mini-brain without doing all of these, and doing all of them mechanically without the underlying value misses the point.

## The principles

### 1. Keep only what can't be re-derived

The brain holds knowledge a newcomer couldn't reconstruct from the project's own artifacts — the *why* behind choices, not the *what* that the code already shows. It is allowed, even expected, to shrink.

- **Why:** Anything the project already records elsewhere is duplication that quietly drifts out of date. A small store of un-derivable knowledge stays high-signal and cheap to maintain. Shrinking is a sign of convergence, not neglect.
- **Signs of it:** The memory avoids restating what's plainly in the code or README. There's a stated preference for small over comprehensive. Contrast with: a store that grows without bound and mirrors the architecture.

### 2. Separate the log of what happened from the distilled truth

Keep an append-only, time-stamped record of work sessions (never edited after the fact) distinct from living documents that hold the current best understanding (rewritten freely as understanding improves).

- **Why:** The log preserves honest lineage — who decided what, what was attempted — while the living docs stay current without being weighed down by history. You can trace the reasoning without it cluttering the conclusions.
- **Signs of it:** There's an attributed, chronological history *and* a separate set of curated current-state documents. Contrast with: one mutable blob, or an ever-growing log that's never distilled.

### 3. Give it one front door

A single entrypoint lists every document and what it's for, kept current by convention, so a reader can load only what the question at hand needs.

- **Why:** It orients a fresh human or agent in seconds, scales to many files without anyone having to read them all, and provides the one authoritative answer to "what's current versus retired."
- **Signs of it:** There's a maintained index or map. From one file you can tell what to read for a given question. Contrast with: discovering relevant files by guesswork.

### 4. Name the files so they stand out and don't collide

Memory files share a distinctive, consistent naming style that visibly sets them apart from ordinary project files — for example a shared namespace token or prefix.

- **Why:** The names become unmistakable, don't get visually lost among surrounding code, and stay unambiguous even when more than one such memory is loaded at the same time.
- **Signs of it:** You can tell at a glance that a file belongs to the brain. Names wouldn't clash if two brains were combined. Contrast with: generic names that blend into the rest of the repo.

### 5. Make the lasting documents citable and dated

Each canonical document carries a simple, stable marker of its version and date; the detailed history of changes lives in version control rather than as duplicate snapshots in the repo.

- **Why:** It gives people a durable handle to cite, signals at a glance how settled a document is, and avoids keeping drift-prone copies inside the project.
- **Signs of it:** A lightweight version or date stamp on the main documents; history left to the version-control system. Contrast with: undated docs, or many in-tree "old version" copies.

### 6. Keep work-in-progress apart from settled knowledge

Not-yet-agreed material — experiments, and the in-flight notes of whatever is currently being built — lives in a clearly separate working area (one or more subdirectories), distinct from the trusted core.

- **Why:** Work can be messy and provisional without polluting what others rely on, and the boundary between "draft" and "agreed" stays obvious.
- **Signs of it:** A recognizable holding area for drafts and experiments. Contrast with: provisional and canonical content mixed together so you can't tell what's trusted.

### 7. Have a standard way to open and close a unit of work

A defined procedure sets up the documents for a new piece of work, and a matching procedure folds that work's durable lessons back into the lasting store when it finishes — retiring the scratch files rather than discarding them.

- **Why:** Knowledge created during the work doesn't die in a branch or a closed ticket. The lasting store grows deliberately, on a known cadence, instead of by accident — and nothing learned is silently thrown away.
- **Signs of it:** A repeatable setup-and-closeout ritual; finished work visibly harvested into the durable docs. Contrast with: every effort reinventing its own structure and stranding its insights.

### 8. Schedule a reflection pass to keep it true and small

A periodic maintenance routine re-checks the memory against the project's current reality — verifying claims, merging overlap, deleting what has become re-derivable, and flagging what's missing.

- **Why:** Memory rots without upkeep. A regular pass is what lets the brain stay accurate and shrink toward its irreducible core, rather than drifting unnoticed.
- **Signs of it:** A defined, recurring review of the memory itself (not just of the code), that both prunes and looks for gaps. Contrast with: a store that is only ever added to.

### 9. Write for the reader you actually have

Structure and length are tuned to how the memory is really consumed — usually an AI agent loading documents into a limited context window — favoring a few well-sized, well-indexed files over either a swarm of fragments or one giant document.

- **Why:** Matching the format to the consumer keeps the memory concise, loadable, and high signal-per-token. It avoids both the overhead of hundreds of tiny notes and the cost of one unreadable monolith.
- **Signs of it:** Files are sized and organized with the actual reader in mind; there's evidence of caring about what gets loaded and when. Contrast with: filing that's convenient to write but expensive to read.

## The short version

If you remember nothing else: a mini-brain **stores only what the work can't already tell you, keeps the record of what happened separate from the distilled truth, puts one index at the front, and maintains itself on a schedule so it stays both true and small.** Everything else above is in service of those four.
