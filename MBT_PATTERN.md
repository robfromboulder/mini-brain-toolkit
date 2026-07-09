# Mini-Brain Toolkit: The Mini-Brain Pattern

> V5, 2026-07-09.

This document is the operational definition of a mini-brain: what it *is*, the file set it's made of, and the lifecycle that keeps it true and small.

---

## 1. What a mini-brain is

A **mini-brain** is a small, curated set of plain-text documents that holds a project's hard-won knowledge: the decisions, the reasons behind them, the paths tried and rejected, and the lessons learned — the things the project's code, git history, and tickets *can't* tell you on their own. It is kept deliberately small and maintained over time, so an AI agent or a new teammate can get oriented in minutes and trust what they read.

It is not a wiki, an architecture manual, or a second copy of the docs. Its defining bet is the inverse of "write everything down": **capture only what would otherwise be lost, and let everything else stay where it already lives.** A shrinking mini-brain is converging on its irreducible core, not decaying.

The reader is usually an AI agent loading files into a limited context window, and sometimes a new teammate. That reader is the reason the brain stays small, keeps each document to a single topic, puts an index at the front, and lives in its own repository loaded on demand by reading its `CLAUDE.md`. The principles below follow from it.

---

## 2. The principles

Ten principles define the pattern, ordered from most to least important. `MBT_CHECK_BRAIN.md` scores a repo against them; `MBT_CREATE_BRAIN.md` builds them in. Each is a target, not a gate — partial adherence is normal.

1. **Keep only what can't be re-derived.** Record the decisions, reasons, rejected paths, and lessons that the code, its version-control history, and the project's tickets do not already contain. Leave everything derivable where it lives. Expect the brain to shrink as content becomes re-derivable — that is health, not decay.

2. **Store the mini-brain in its own repository, separate from the code it describes.** The brain records how and why the product was built, so it must not be embedded in, versioned with, or shipped as part of the product. It sits beside the product repositories, is loaded on demand, and outlives any single one of them.

3. **Organize knowledge into orthogonal documents.** Give each document one dimension of the project — problem, approach, findings, session history — with no overlap between documents. Orthogonality lets each question map to exactly one file, lets each document be judged on its own terms, and keeps any one file small enough to load without the rest.

4. **Separate the append-only log from the distilled documents.** Keep one time-stamped log that records what happened each session and is never edited after the fact. Keep the rest — the *canonical documents* — as living current-state summaries, rewritten freely as understanding improves. The log preserves lineage; the canonical documents preserve conclusions.

5. **Provide an entrypoint with a read index.** Put one file (`CLAUDE.md`) that a reader always opens first — the entrypoint — and have it carry a read index: a table listing every document, what each is for, and which are current. The reader consults the index and loads only the documents a given question needs.

6. **Namespace every knowledge file with a SCREAMING_SNAKE_CASE token.** Prefix each file with one uppercase token unique to the brain (`GUARDRAILS_SCOPE.md`, `NEBULA_APPROACH.md`). The token makes the brain's files unmistakable in a mixed directory and prevents collisions when two brains load in the same session. `CLAUDE.md` and `README.md` are exempt.

7. **Version and date every canonical document.** Open each canonical document with `> V<N>, YYYY-MM-DD.` Bump the number and set the date on each substantive edit. This gives readers a citable version and a freshness signal; full history stays in version control, not in duplicate in-tree copies. The append-only log is exempt.

8. **Keep work-in-progress separate from settled knowledge.** Put experiments and a feature's in-flight documents in a `working/` area, apart from the canonical documents a reader is meant to trust. Nothing in `working/` is authoritative until it is folded into a canonical document.

9. **Open and close each unit of work the same way.** Use one defined ritual to scaffold a feature's working documents at the start, and a matching ritual at the end to fold their durable lessons into the canonical documents and retire (move, not delete) the working files. This keeps every effort's structure identical and stops its lessons from being stranded.

10. **Reflect on a schedule to keep the brain true and small.** Run a periodic maintenance pass that re-checks claims against current reality, merges overlapping content, deletes what has become re-derivable, and flags gaps. Without it, a brain only grows and drifts from the truth.

In short: a mini-brain **lives in its own repository and stores only what the code can't tell you, split into orthogonal documents with the log kept apart from the distilled documents, fronted by a read index, and pruned on a schedule so it stays both true and small.**

---

## 3. The file set

A mini-brain grows in three stages. Not every brain reaches stage 3, and that's fine — grow the machinery when the work justifies it, never ahead of need.

### Stage 1 — Seed (every brain starts here)

The minimum viable brain. `MBT_CREATE_BRAIN.md` produces exactly this from `templates/`.

| File | Role | Namespaced? |
|---|---|---|
| `CLAUDE.md` | Entrypoint: read index + file conventions (principle 5). | Exempt |
| `README.md` | Repo artifact: what this is and how to load it. | Exempt |
| `<PREFIX>_SCOPE.md` | The problem, current state, goals — objective, solution-free. | Yes |
| `<PREFIX>_APPROACH.md` | The chosen design and key decisions that address SCOPE. | Yes |
| `<PREFIX>_FINDINGS.md` | Implementation findings invisible from the code; starts empty. | Yes |
| `<PREFIX>_LOG.md` | Append-only session log — the lineage (principle 4). | Yes |
| `<PREFIX>_SESSION_CLOSEOUT.md` | The authoritative format/rules for LOG entries. | Yes |
| `archive/` | Source material and retired docs. | — |
| `working/` | Experiments and in-flight feature docs (principle 8). | — |

SCOPE and APPROACH are deliberately **orthogonal** (principle 3): SCOPE describes the problem space without bias toward any solution; APPROACH makes the case for a specific design against that neutral problem statement. Keeping them separate is what lets each be judged on its own terms.

### Stage 2 — Content

Same file set, now filled. SCOPE and APPROACH are authored (often distilled from source material parked in `archive/`, then fact-checked against the real codebase), the LOG accumulates session entries, and FINDINGS starts collecting the non-obvious. This is where a brain spends most of its life.

### Stage 3 — Mature lifecycle

Added when a brain tracks real feature work across many sessions and needs rituals to stay coherent (principles 9 and 10).

| File | Role |
|---|---|
| `<PREFIX>_FEATURE_SETUP.md` | Scaffolds a feature's `working/<FEATURE>_*` docs from an intake conversation. |
| `<PREFIX>_FEATURE_CLOSEOUT.md` | Folds a merged feature's working docs into the canonical store; retires them to `archive/`. |
| `<PREFIX>_DREAM_CYCLE.md` | The periodic reflection pass: structural checks, claim verification, findings extraction. |
| `<PREFIX>_DREAM_LOG.md` | Append-only log of dream-cycle runs. |
| Per-feature working set | `working/<FEATURE>_{PLAN,FINDINGS,LOG,TASKS,CLAUDE,TESTING}.md` — unversioned, out of the read index. |

Brains that serve more than one target platform also split some docs by platform (`<PLATFORM>_<PREFIX>_*`), keeping shared findings in the un-prefixed file and platform-specific ones in the platform files.

---

## 4. The lifecycle

- **A session** starts by reading `CLAUDE.md` and only the indexed files the question needs. It ends (when there's durable lineage worth keeping) by appending one entry to the LOG per `<PREFIX>_SESSION_CLOSEOUT.md`.
- **A feature** opens with `FEATURE_SETUP` (scaffold `working/` docs), runs across sessions logging to its own `<FEATURE>_LOG.md`, and closes with `FEATURE_CLOSEOUT` (fold durable knowledge into canonical docs, move working files to `archive/`).
- **Maintenance** runs on a cadence via `DREAM_CYCLE`: verify SCOPE's factual claims against the code, refresh APPROACH's external assumptions, promote LOG entries into FINDINGS, prune what's now re-derivable, and flag anything that needs human judgment.

The through-line across all three: knowledge is captured as lineage in the LOG, distilled into the living docs on a known cadence, and continuously pruned toward the irreducible core.
