# Mini-Brain Toolkit: Create a New Mini-Brain

> V18, 2026-08-08.

This document is the procedure for standing up a new mini-brain from `templates/`.

The output of a first run is a **stage-1 seed** (the first of the stages defined in `MBT_PATTERN.md`): a working brain with an entrypoint, empty canonical docs, and the working/archive structure — ready to be filled. Filling SCOPE and APPROACH (stage 2) and adding lifecycle machinery (stage 3) are later steps in this same document.

This procedure is **additive and idempotent**: it creates only what's missing and never overwrites existing work, so it's safe to re-run as the brain grows.

---

## 1. The intake conversation

Before creating anything, settle these with the user. Establishment turns a decision into files; it does not invent the project.

- **Project** — what the brain is *about*. One line: the system whose un-derivable knowledge this will hold.
- **Components** — whether the knowledge divides. Ask whether one SCOPE can state the problem honestly, or whether writing it would force two or more coexisting problems onto the page. If it divides, the brain is component-structured and `MBT_COMPONENTS.md` governs its layout; ask again of any component whose own problem divides. For each component, also settle the terms that should route a question to it — the registry's **Routes on** cell. Most brains hold one problem and answer no. Settle this before the token, because the answer changes how many tokens there are.
- **Namespace token** — the SCREAMING_SNAKE_CASE token every knowledge file carries (principle 6). Short, distinctive, unlikely to collide with another brain loaded in the same session. Mirror the project name where natural (`orchard` → `ORCHARD`); pick an acronym when the name is long (`customer-data-platform` → `CDP`). Confirm it with the user — it touches every filename and is churn to change later. A component-structured brain settles one token for the hub and one for each component, each under the same collision test.
- **Location** — the repo (principle 2: the brain is its own repository, not a folder inside a project repo). Convention is a sibling repo named `mini-<project>-brain`, so a coding session in a project repo can load it with `Read ../mini-<project>-brain/CLAUDE.md for instructions`.
- **Project repos (optional)** — the repos whose coding sessions should load the brain. Each gets the hook merged into its `CLAUDE.md` (§3). A brand-new project may have none yet; add the hook to each repo as it appears — this procedure is safe to re-run. In a component-structured brain, note which component each repo maps to; its hook names that component.
- **Source material (optional)** — existing docs the SCOPE/APPROACH will be distilled from (design docs, PRDs, tickets, prior wikis). If they exist, they go in `archive/` as source, not into the canonical docs verbatim.
- **Platforms (optional)** — if the project targets more than one platform that will need platform-specific docs later, note it now; it affects the namespace layering (`<PLATFORM>_<PREFIX>_*` etc.) but not the seed. Platforms are one problem delivered across several targets; targets holding different problems are the components question above.

Don't gather more than this for a seed.

---

## 2. Audit what exists

Before writing, list the target directory — every unit directory, in a component-structured brain. Classify each seed file:

- **Missing** — create it from the template (§3).
- **Exists** — leave it. Never overwrite.

A brand-new repo has nothing but perhaps a `README.md`, `LICENSE`, and `.git`; all seed files are created. A repo you're formalizing (e.g. a stray `NOTES.md`) gets only its missing pieces, and existing notes are treated as source material to fold in later, not clobbered.

---

## 3. Create the seed file set

For each missing file, copy the corresponding file from `templates/` and substitute the placeholders:

- `<PREFIX>` → the namespace token (e.g. `ORCHARD`). In a component-structured brain, the token of the unit each copy serves: a component's for its own doctype set, the hub's for everything else.
- `<Project>` → the project's display name (Title Case, e.g. `Orchard`).
- `<project>` → the lowercase name used in prose/README (e.g. `orchard`).
- `<date>` → today's date, `YYYY-MM-DD`.

Substitute only these. `<TOKEN>` and `<WORK>` are runtime variables, not creation placeholders — the procedures resolve them later, per owning unit and per work item — so leave them intact wherever a template carries them. Two spots are creation-time despite carrying `<TOKEN>`: the component registry's placeholder rows and the project hook's component paragraph are filled from the intake conversation when this procedure instantiates them, and only there.

| Create from template | To | Notes |
|---|---|---|
| `templates/CLAUDE.md` | `CLAUDE.md` | Read index + conventions. The read index lists only the seed canonical docs at first; extend it as files are added. |
| `templates/README.md` | `README.md` | If a README already exists (repo artifact), *merge* the mini-brain usage section in rather than overwriting. |
| `templates/SCOPE.md` | `<PREFIX>_SCOPE.md` | Section skeleton with `*To be filled in.*` placeholders. Each section carries a comment saying what belongs in it; leave those in place at seed time — they are deleted section by section as §4 fills them. |
| `templates/APPROACH.md` | `<PREFIX>_APPROACH.md` | Section skeleton with `*To be filled in.*` placeholders, carrying the same per-section comments. |
| `templates/FINDINGS.md` | `<PREFIX>_FINDINGS.md` | Header + `*No findings recorded yet.*` |
| `templates/LOG.md` | `<PREFIX>_LOG.md` | Header only; first entry is appended at first session closeout. |
| `templates/SESSION_CLOSEOUT.md` | `<PREFIX>_SESSION_CLOSEOUT.md` | The authoritative LOG-entry format. |
| `templates/PROJECT_HOOK.md` | each project repo's `CLAUDE.md` | *Merge* as a section into the existing file (create the file if the repo has none). Skip when no project repo exists yet. |

Then create the two directories: `archive/` (drop any source material here) and `working/`. Git won't track empty directories — add a `.gitkeep` to `working/` if it would otherwise be empty, and remove it once real content lands.

All canonical docs open with `> V1, <date>.`; apply `CLAUDE.md`'s version convention and exemptions.

**For a component-structured brain**, seed the hub's documents at the root under the hub token, create one directory per component — nested where components nest — and seed each component's full doctype set from the same `SCOPE`, `APPROACH`, `FINDINGS` and `LOG` templates under that component's token. Those four are prefix-substituted and work identically at any depth. Use `templates/COMPONENTS_CLAUDE.md` for the entrypoint in place of `templates/CLAUDE.md`, filling its registry from the intake conversation — one row per component, replacing the placeholder rows. Reword the seeded README's namespace sentence to per-unit tokens — the template states one brain-wide token, which a component brain's own registry contradicts. `SESSION_CLOSEOUT` stays at the hub, one per brain, as does every maintenance document added later; `archive/` and `working/` belong to whichever unit first needs them, so create only the hub's now. `MBT_COMPONENTS.md` carries the registry's shape and the naming rules.

---

## 4. Fill SCOPE and APPROACH (stage 2)

Seeding produces skeletons; this step turns them into content. Do it in order — APPROACH argues against SCOPE, so SCOPE settles first. In a component-structured brain, work parents before children as well: a component's problem statement may cite its parent's, so the parent has to settle first.

**SCOPE — the problem, objectively.** Author `<PREFIX>_SCOPE.md`: problem statement, state of the problem, goals (as outcomes, not deliverables), what's not in scope, and open questions. Keep it **solution-neutral** — it describes the problem space so any approach can be judged against it. Four rules make that concrete, and each fails silently when ignored:

- **The state of the problem is not the state of the project.** The problem exists whether zero or many things address it, so this section describes the world the work enters: what the platform or environment already provides and withholds, what alternatives exist and where they stop, who has the problem and what they already hold, and what evidence there is that the problem is real. Version numbers, release status, test counts, maturity labels, benchmarks and issue counts are the project's status, not the problem's — they are re-derivable, they date within weeks, and a scope built from them quietly becomes a changelog. The test: if a sentence would have to change because a release shipped, it does not belong here.
- **A goal names an outcome for whoever has the problem, never a mechanism.** A goal naming an artifact, a format, or a capability is a design commitment wearing a goal's clothes. After writing each one, check that a completely different design could satisfy it; if it could not, the solution is baked in and belongs in APPROACH.
- **Source material carries its own shape.** The documents parked in `archive/` were written for a project repo and are organized around the project — status, features, roadmap — and distilling them preserves that organization unless the problem is deliberately re-derived from them. Read them for the problem they imply, not for what they say about the project, and strip strategy, tactics and vendor choices out of anything headed for the goals. This is the usual reason a scope comes out reading like a status report.
- **Report evidence at the strength it was given.** Sources record what someone did far more often than why. If a source says a team built their own tool, do not write that they built it because nothing else was light enough.

Then **fact-check every falsifiable claim** against the codebase and against the current state of whatever else the claim is about — trackers, branches, released artifacts. A scope authored from project documents drifts in predictable ways (it overstates uniformity, mislabels by name, lags the code's evolution), and the source documents themselves are often stale: a feature count that no longer matches, an open ticket asking for work that already shipped. Correct what the evidence contradicts, bump the version, and report the stale sources — a source that has drifted is a finding about that document, not just an obstacle to this one.

**APPROACH — the chosen design.** Author `<PREFIX>_APPROACH.md`: strategic approach, architecture, key design decisions (with alternatives weighed), and what gets built. This is where solution commitments live. Trace each design choice to the SCOPE goal it serves, cited by name. Then read the pair in the other direction: **for every goal, name the decision that answers it.** A goal with no answering decision is either a gap in the design or a goal that was never real, and where the design deliberately leaves a goal unmet, say so — silence reads as "handled". This reverse pass is what catches the defects the forward pass cannot, because a design that traces cleanly to the goals it addresses says nothing about the goals it skipped. Keep APPROACH and SCOPE orthogonal: if you find yourself faulting SCOPE for not matching an APPROACH decision, that's importing solution bias into the problem statement — stop.

**Read the set back before calling it done.** Run this once every document in the set exists, not after each one. Authoring runs document by document, so each one comes out consistent with itself and the defects collect in the seams. They are invisible from inside the document being written and obvious the moment the set is read together, which is why this is a separate pass and not a matter of being careful while authoring. The structural check in §6 catches none of them — every file involved exists, is namespaced, and carries a version header. Two passes, and they are not the same pass:

- **The scopes, as a group.** Read every SCOPE in one sitting and look for what only appears side by side: a term meaning two different things in two units, an open question standing in more than one place, a parent explaining a child's problem rather than naming it, and the same fact stated at two levels. Then re-ask solution-neutrality in a form authoring cannot answer — for each claim about the world, would it still hold if the design had gone another way? A claim that fails that test arrived from a design decision made in some other document and is wearing the clothes of a fact. This is the leak that survives a careful reading for solution bias, because by the time it is written down it reads as a description of reality.
- **Each approach against its own scope, and never against the other approaches.** The pairing is the reverse-trace above, run once the whole set exists. Comparing approaches to *each other* is a mistake: they are siblings, so the comparison invites exactly the coupling the pattern forbids, and it pressures designs that legitimately differ into cosmetic agreement. What matters about an approach is whether it answers its own problem, not whether it resembles its neighbors.

Record the reasoning and course-corrections of this authoring work in the LOG at session closeout (§6). The *decisions* that are invisible from the resulting docs go in FINDINGS as they arise.

---

## 5. Grow into the mature lifecycle (stage 3)

Add these **only when the work justifies them** (the stage model in `MBT_PATTERN.md`) — typically when the brain starts tracking work items across many sessions. Each is copied from `templates/`, namespaced, added to the read index, and bumps `CLAUDE.md`.

- `templates/WORK_SETUP.md` → `<PREFIX>_WORK_SETUP.md` and `templates/WORK_CLOSEOUT.md` → `<PREFIX>_WORK_CLOSEOUT.md` — the open/close bookends for work items (a feature, bug fix, or hardening effort). They reference the per-work-item working set in `templates/work/` — inline those six scaffolds into `<PREFIX>_WORK_SETUP.md` where it points at them, so the brain stands alone without the toolkit.
- `templates/DREAM_CYCLE.md` → `<PREFIX>_DREAM_CYCLE.md` plus a `<PREFIX>_DREAM_LOG.md` (header only) — the periodic reflection pass. The template assumes a single unit; don't instantiate it unadapted into a component-structured brain.

When the brain gains work items, also uncomment the work-item block in each project repo's hook (the maturity comment inside `templates/PROJECT_HOOK.md`).

Don't scaffold these into a stage-1 brain; add them the first time a real work item or a real drift-review need appears.

---

## 6. Close out and hand off

1. Append the first LOG entry per `<PREFIX>_SESSION_CLOSEOUT.md`, recording what this establishment session did and decided (namespace choice, source material, fact-check corrections).
2. Run a structural check — read index ↔ disk, version headers, cross-references, namespace prefix; for a component-structured brain, also registry ↔ disk and each unit's full doctype set and token — and fix anything it flags.
3. Report to the user: the namespace token used — or the unit tree and its per-unit tokens, for a component-structured brain — which files were **created** vs. already **existed**, what stage the brain is at, and the natural next step (fill SCOPE, or add lifecycle machinery).

Do not commit unless the user asks. If the repo is on its default branch, branch first.
