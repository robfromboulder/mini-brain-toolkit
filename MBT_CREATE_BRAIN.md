# Mini-Brain Toolkit: Create a New Mini-Brain

> V5, 2026-07-09.

This document is the procedure for standing up a new mini-brain from `templates/`.

The output of a first run is a **stage-1 seed** (see `MBT_PATTERN.md` §3): a working brain with an entrypoint, empty canonical docs, and the working/archive structure — ready to be filled. Filling SCOPE and APPROACH (stage 2) and adding lifecycle machinery (stage 3) are later steps in this same document, run when the work justifies them, never ahead of need.

This procedure is **additive and idempotent**: it creates only what's missing and never overwrites existing work, so it's safe to re-run as the brain grows.

---

## 1. The intake conversation

Before creating anything, settle these with the user. Establishment turns a decision into files; it does not invent the project.

- **Project** — what the brain is *about*. One line: the system whose un-derivable knowledge this will hold.
- **Namespace token** — the SCREAMING_SNAKE_CASE token every knowledge file carries (principle 6). Short, distinctive, unlikely to collide with another brain loaded in the same session. Mirror the project name where natural (`orchard` → `ORCHARD`); pick an acronym when the name is long (`customer-data-platform` → `CDP`). Confirm it with the user — it touches every filename and is churn to change later.
- **Location** — the repo (principle 2: the brain is its own repository, not a folder inside the product). Convention is a sibling repo named `mini-<project>-brain`, so a coding session in the product repo can load it with `Read ../mini-<project>-brain/CLAUDE for instructions`.
- **Source material (optional)** — existing docs the SCOPE/APPROACH will be distilled from (design docs, PRDs, tickets, prior wikis). If they exist, they go in `archive/` as source, not into the canonical docs verbatim.
- **Platforms (optional)** — if the project targets more than one platform that will need platform-specific docs later, note it now; it affects the namespace layering (`<PLATFORM>_<PREFIX>_*` etc.) but not the seed.

Don't gather more than this for a seed. SCOPE and APPROACH content is filled in §4, not here.

---

## 2. Audit what exists

Before writing, list the target directory. Classify each seed file:

- **Missing** — create it from the template (§3).
- **Exists** — leave it. Never overwrite. If it's an empty/partial canonical doc, it will be filled in §4, not recreated here.

A brand-new repo has nothing but perhaps a `README.md`, `LICENSE`, and `.git`; all seed files are created. A repo you're formalizing (e.g. a stray `NOTES.md`) gets only its missing pieces, and existing notes are treated as source material to fold in later, not clobbered.

---

## 3. Create the seed file set

For each missing file, copy the corresponding file from `templates/` and substitute the placeholders:

- `<PREFIX>` → the namespace token (e.g. `ORCHARD`).
- `<Project>` → the project's display name (Title Case, e.g. `Orchard`).
- `<project>` → the lowercase name used in prose/README (e.g. `orchard`).
- `<date>` → today's date, `YYYY-MM-DD`.

| Create from template | To | Notes |
|---|---|---|
| `templates/CLAUDE.md` | `CLAUDE.md` | Read index + conventions. The read index lists only the seed canonical docs at first; extend it as files are added. |
| `templates/README.md` | `README.md` | If a README already exists (repo artifact), *merge* the mini-brain usage section in rather than overwriting. |
| `templates/SCOPE.md` | `<PREFIX>_SCOPE.md` | Section skeleton with `*To be filled in.*` placeholders. |
| `templates/APPROACH.md` | `<PREFIX>_APPROACH.md` | Section skeleton with `*To be filled in.*` placeholders. |
| `templates/FINDINGS.md` | `<PREFIX>_FINDINGS.md` | Header + `*No findings recorded yet.*` |
| `templates/LOG.md` | `<PREFIX>_LOG.md` | Header only; first entry is appended at first session closeout. |
| `templates/SESSION_CLOSEOUT.md` | `<PREFIX>_SESSION_CLOSEOUT.md` | The authoritative LOG-entry format. |

Then create the two directories: `archive/` (drop any source material here) and `working/`. Git won't track empty directories — add a `.gitkeep` to `working/` if it would otherwise be empty, and remove it once real content lands.

All canonical docs open with `> V1, <date>.`; apply `CLAUDE.md`'s version convention and exemptions.

---

## 4. Fill SCOPE and APPROACH (stage 2)

Seeding produces skeletons; this step turns them into content. Do it in order — APPROACH argues against SCOPE, so SCOPE settles first.

**SCOPE — the problem, objectively.** Author `<PREFIX>_SCOPE.md`: problem statement, current state, goals (as outcomes, not deliverables), what's not in scope, and open questions. Keep it **solution-neutral** — it describes the problem space so any approach can be judged against it. If distilling from source material in `archive/`, strip strategy/tactics/vendor choices out of the goals; those belong in APPROACH. Then **fact-check every falsifiable claim against the actual codebase** — a scope authored from management docs drifts from the code in predictable ways (it overstates uniformity, mislabels by name, lags the code's evolution). Correct what the code contradicts; bump the version.

**APPROACH — the chosen design.** Author `<PREFIX>_APPROACH.md`: strategic approach, architecture, key design decisions (with alternatives weighed), and what gets built. This is where solution commitments live. Cite SCOPE goals by section so each design choice traces to a problem it solves. Keep APPROACH and SCOPE orthogonal: if you find yourself faulting SCOPE for not matching an APPROACH decision, that's importing solution bias into the problem statement — stop.

Record the reasoning and course-corrections of this authoring work in the LOG at session closeout (§6). The *decisions* that are invisible from the resulting docs go in FINDINGS as they arise.

---

## 5. Grow into the mature lifecycle (stage 3)

Add these **only when the work justifies them** (see `MBT_PATTERN.md` §3) — typically when the brain starts tracking feature branches across many sessions. Each is copied from `templates/`, namespaced, added to the read index, and bumps `CLAUDE.md`.

- `templates/FEATURE_SETUP.md` → `<PREFIX>_FEATURE_SETUP.md` and `templates/FEATURE_CLOSEOUT.md` → `<PREFIX>_FEATURE_CLOSEOUT.md` — the open/close bookends for feature work. They reference the per-feature working set in `templates/feature/`.
- `templates/DREAM_CYCLE.md` → `<PREFIX>_DREAM_CYCLE.md` plus a `<PREFIX>_DREAM_LOG.md` (header only) — the periodic reflection pass.

Don't scaffold these into a stage-1 brain. An empty dream cycle and unused feature bookends are read-index clutter that the reader must skip; add them the first time a real feature or a real drift-review need appears.

---

## 6. Close out and hand off

1. Append the first LOG entry per `<PREFIX>_SESSION_CLOSEOUT.md`, recording what this establishment session did and decided (namespace choice, source material, fact-check corrections).
2. Run the structural check from `MBT_CHECK_BRAIN.md` §"Structural checks" — read index ↔ disk, version headers, cross-references, namespace prefix — and fix anything it flags.
3. Report to the user: the namespace token used, which files were **created** vs. already **existed**, what stage the brain is at, and the natural next step (fill SCOPE, or add lifecycle machinery).

Do not commit unless the user asks. If the repo is on its default branch, branch first.
