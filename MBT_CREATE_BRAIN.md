# Mini-Brain Toolkit: Create a New Mini-Brain

> V32, 2026-10-30.

This document is the procedure for standing up a new mini-brain from `templates/`.

The output of a first run is a **stage-1 seed** (the first of the stages defined in `MBT_PATTERN.md`): a working brain with an entrypoint, empty canonical docs, and the working/archive structure — ready to be filled. Filling SCOPE and APPROACH (stage 2) and adding lifecycle machinery (stage 3) are later steps in this same document.

This procedure is **additive and idempotent**: it creates only what's missing and never overwrites existing work, so it's safe to re-run as the brain grows.

---

## 1. The intake conversation

Before creating anything, settle these with the user. Establishment turns a decision into files; it does not invent the project.

- **Project** — what the brain is *about*. One line: the system whose un-derivable knowledge this will hold.
- **Lobes** — whether the knowledge divides. Ask whether one SCOPE can state the problem honestly, or whether writing it would force two or more coexisting problems onto the page. If it divides, the brain is multi-lobe and `MBT_LOBES.md` governs its layout; ask again of any lobe whose own problem divides. For each child lobe, also settle the terms that should route a question to it — the registry's **Routes on** cell. Most brains hold one problem and answer no. Settle this before the lobespace, because the answer changes how many lobespaces there are.
- **Lobespace** — the SCREAMING_SNAKE_CASE lobespace every knowledge file carries (principle 6). Short, distinctive, unlikely to collide with another brain loaded in the same session. Mirror the project name where natural (`orchard` → `ORCHARD`); pick an acronym when the name is long (`customer-data-platform` → `CDP`). Confirm it with the user — it touches every filename and is churn to change later. A multi-lobe brain settles one lobespace for the hub and one for each child lobe, each under the same collision test.
- **Location** — the repo (principle 2: the brain is its own repository, not a folder inside a project repo). Convention is a repo named `mini-<project>-brain` beside the project repo's main checkout, where a coding session in that project repo — or any of its worktrees — finds it.
- **Project repos (optional)** — the repos whose coding sessions should load the brain. Each gets the hook merged into its `CLAUDE.md` (§4). A brand-new project may have none yet; add the hook to each repo as it appears — this procedure is safe to re-run. In a multi-lobe brain, note which lobe each repo maps to; its hook names that lobe.
- **Author** — the name of the human author, which the first session log entry names.
- **Source material (optional)** — existing docs the SCOPE/APPROACH will be distilled from (design docs, PRDs, tickets, prior wikis). If they exist, they go in `archive/` as source, not into the canonical docs verbatim.

Don't gather more than this for a seed.

---

## 2. Establish the brain repo

Verify that the target location from §1 exists and is a git repository. If either check fails, tell the user what's needed — the repo name and location settled in the intake — so they can create it (`gh repo create` for a hosted repo, or `mkdir` + `git init` for local-only). Don't create the repo yourself; hosting and visibility are the user's call.

When the brain accompanies an existing project, this procedure creates the brain's files in the brain repo; the project repo receives only the loading hook (§4).

---

## 3. Audit what exists

Before writing, list the target directory — every lobe directory, in a multi-lobe brain. Classify each seed file:

- **Missing** — create it from the template (§4).
- **Exists** — leave it. Never overwrite.

A brand-new repo has nothing but perhaps a `README.md`, `LICENSE`, and `.git`; all seed files are created. A repo you're formalizing (e.g. a stray `NOTES.md`) gets only its missing pieces, and existing notes are treated as source material to fold in later, not clobbered.

---

## 4. Create the seed file set

For each missing file, copy the corresponding file from `templates/` and substitute the placeholders:

- `<HUB>` → the hub's lobespace (e.g. `ORCHARD`); in a brain with one lobe, the brain's own. One value per brain, and every instance is creation-time — it marks the documents that live only at the hub.
- `<LOBESPACE>` → the lobespace of the lobe whose document you are seeding: the brain's own in a single-lobe brain, each child's own in its doctype set. Leave it intact in the doctype grammar, which names documents generically and is resolved per lobe at read time.
- `<Project>` → the project's display name (Title Case, e.g. `Orchard`). In a multi-lobe brain, a child's own doctype set takes that child's display name instead, so each lobe's documents name their own subject rather than the whole project's.
- `<project>` → the lowercase name used in prose/README (e.g. `orchard`).
- `<date>` → today's date, `YYYY-MM-DD`.

Substitute only these. `<WORK>` is always a runtime variable, not a creation placeholder — the procedures resolve it later, per work item — so leave it intact wherever a template carries it. Two spots are creation-time despite carrying `<LOBESPACE>`: the lobe registry's placeholder rows and the project hook's lobe paragraph are filled from the intake conversation when this procedure instantiates them, and only there.

| Create from template | To | Notes |
|---|---|---|
| `templates/CLAUDE.md` | `CLAUDE.md` | Read index + conventions. The read index lists only the seed canonical docs at first; extend it as files are added. |
| `templates/README.md` | `README.md` | If a README already exists (repo artifact), *merge* the mini-brain usage section in rather than overwriting. |
| `templates/SCOPE.md` | `<LOBESPACE>_SCOPE.md` | Section skeleton with `*To be filled in.*` placeholders. Each section carries a comment saying what belongs in it; leave those in place at seed time — they are deleted section by section as §5 fills them. |
| `templates/APPROACH.md` | `<LOBESPACE>_APPROACH.md` | Section skeleton with `*To be filled in.*` placeholders, carrying the same per-section comments. |
| `templates/FINDINGS.md` | `<LOBESPACE>_FINDINGS.md` | Header + `*No findings recorded yet.*` |
| `templates/LOG.md` | `<LOBESPACE>_LOG.md` | Header only; first entry is appended at first session closeout. |
| `templates/SESSION_CLOSEOUT.md` | `<HUB>_SESSION_CLOSEOUT.md` | The authoritative LOG-entry format. |
| `templates/PROJECT_HOOK.md` | each project repo's `CLAUDE.md` | *Merge* as a section into the existing file (create the file if the repo has none). Skip when no project repo exists yet. |

Then create the two directories: `archive/` (drop any source material here) and `working/`. Git won't track empty directories — add a `.gitkeep` to `working/` if it would otherwise be empty, and remove it once real content lands.

All canonical docs open with `> V1, <date>.`; apply `CLAUDE.md`'s version convention and exemptions.

**For a multi-lobe brain**, seed the hub's documents at the root under the hub lobespace, create one directory per child lobe — nested where lobes nest — and seed each child's full doctype set from the same `SCOPE`, `APPROACH`, `FINDINGS` and `LOG` templates under that child's lobespace. Those four are substituted per lobe — `<LOBESPACE>` with the lobe's lobespace, `<Project>` with its display name — and work identically at any depth. Use `templates/LOBES_CLAUDE.md` for the entrypoint in place of `templates/CLAUDE.md`, filling its registry from the intake conversation — one row per child lobe, replacing the placeholder rows. Reword the seeded README's namespace sentence to per-lobe lobespaces — the template states one brain-wide lobespace, which a multi-lobe brain's own registry contradicts. `SESSION_CLOSEOUT` stays at the hub, one per brain, as does every maintenance document added later; `archive/` and `working/` belong to whichever lobe first needs them, so create only the hub's now. `MBT_LOBES.md` carries the registry's shape and the naming rules.

---

## 5. Fill SCOPE and APPROACH (stage 2)

Seeding produces skeletons; this step turns them into content. Do it in order — APPROACH argues against SCOPE, so SCOPE settles first. In a multi-lobe brain, work parents before children as well: a child's problem statement may cite its parent's and works within its ancestors' design choices, so the parent's SCOPE and APPROACH settle before the child's SCOPE.

**SCOPE — the problem, objectively.** Author `<LOBESPACE>_SCOPE.md`: problem statement, state of the problem, goals (as outcomes, not deliverables), what's not in scope, and open questions. Keep it **solution-neutral**: SCOPE holds what is true of the problem whoever addresses it, and APPROACH holds the project's choices. A choice is anything a reasonable designer of this problem could decide otherwise — a platform, a mechanism, an audience narrower than whoever has the problem — however early it was made and however settled it feels. What stays in SCOPE is what no designer could decide otherwise: the conditions every option faces, the evidence, the goals, which are the problem holder's outcomes, and the premises the problem holder (whoever has the problem the scope states) brings, such as a system every approach must work within or a commitment the problem holder made outside this project. Something the problem holder already has is a premise only when the problem requires every approach to use it; one the intended design merely uses is a choice. Only the problem holder can say which premises are theirs, so settle them with the user, in a round of questions of their own once the seed is in place, and state each in the problem statement with what makes it binding; for a commitment, that the problem holder made it is reason enough. A preference the user states is a goal when it concerns an outcome, and a choice when it concerns the design.

Before writing, research the alternatives someone with the problem would weigh. Source material lists what its author considered, which is rarely everything a problem holder would weigh, so research them rather than only distilling them. Then **name a second approach**: the reasonable alternative to the whole intended design that differs from it most while still honoring the problem statement's premises, taken from those alternatives or assembled for the purpose. Confirm it with the user; the status quo serves only when no other reasonable alternative exists. It is one of the alternatives the state of the problem assesses. Read each sentence as that approach's designer: a sentence only the intended design needs is a choice that belongs in APPROACH. A premise the two approaches share without the problem statement stating it, such as a platform or a model, goes untested by that comparison, so test it against an alternative that does not share it. The test has to be concrete, because a scope that leaks a design already reads as neutral to its author. Seven rules make neutrality concrete, and each fails silently when ignored:

- **The state of the problem assesses the alternatives.** It leads with what someone with the problem would weigh: the status quo, doing it by hand where that differs from the status quo, and every other alternative a reasonable person would consider beside them. An alternative is any option someone with the problem could take instead, even one that covers only part of it. Few cover every goal, and where each falls short is what the goals answer. For each, say what it offers and where it stops, with its chief complaints on cost, complexity, security, and what it asks of the people involved. Describe each alternative by what it structurally requires and how it charges, which survive a price change, and date any figure worth keeping to when it was read. The intended design's own class is one of them, described generically by what it requires, never by the choices the intended design makes. The section closes with the conditions every option faces and the evidence that the problem is real. A fact about the environment belongs here only as one of those conditions, and only at the depth the problem needs: describe a system by its structure and its gaps, not by the identifiers, settings and counts its code already shows.
- **The scope is not the state of the project.** The problem exists whether zero or many things address it, so SCOPE describes it as whoever has it would meet it without this project: the status quo is what they would have without it, and what the project has shipped, an earlier phase included, is APPROACH's to record as decisions, with what they have proven as the rationale those decisions rest on, never as status. Version numbers, release status, test counts, maturity labels, benchmarks and issue counts are the project's status, not the problem's — they are re-derivable, they date within weeks, and a scope built from them quietly becomes a changelog. The test: if a sentence would have to change because this project shipped a release, it does not belong in SCOPE, whether it sits in a section of its own, in a status line on a goal, in a resolution recorded under an open question, or in a roadmap note. A request from the project's users, phrased against what the project already built, is status too; state the need beneath it.
- **Every boundary carries the problem's reason.** An exclusion, or a narrowing of who has the problem, states a reason that holds whatever gets built. One with no reason, or with a reason about what the design can reach, test or support, is a limit of the design, and belongs in APPROACH, marked against any goal it leaves unmet. A child lobe inherits the boundaries its ancestors set rather than restating them.
- **Goals answer the gaps.** A gap is where an alternative stops or a condition every option faces bites; an alternative that stops by breaking a premise is ruled out by the premise, not a gap. Each gap has a goal, an exclusion whose reason holds whatever gets built, or, where the problem itself leaves it unresolved, an open question. A gap the design leaves unmet keeps its goal, and APPROACH marks that goal unmet. Each goal answers the problem statement or a gap. A goal names an outcome for whoever has the problem, never a mechanism: a goal naming an artifact, a format, a capability or the project itself is a design commitment wearing a goal's clothes. State each goal so that any approach can be judged against it. The second approach may fail a goal, since ruling approaches out is what goals are for, but a goal stated in terms only the intended design has is a mechanism. Order the goals by their impact on whoever has the problem, as far as the evidence ranks them.
- **Open questions are about the problem.** A question that offers design options, presupposes the design, or asks whether the design will hold is an APPROACH question.
- **Source material carries its own shape.** The documents parked in `archive/` were written for a project repo and are organized around the project — status, features, roadmap — and distilling them preserves that organization unless the problem is deliberately re-derived from them. Read them for the problem they imply, not for what they say about the project, and strip strategy, tactics and vendor choices out of anything headed for the goals. This is the usual reason a scope comes out reading like a status report.
- **Report evidence at the strength it was given.** Sources record what someone did far more often than why. If a source says a team built their own tool, do not write that they built it because nothing else was light enough.

Then **fact-check every falsifiable claim** against the current state of what it describes: an alternative, a system the problem holder works within, or the evidence. A scope authored from project documents drifts in predictable ways (it overstates uniformity, mislabels by name, lags the systems' evolution), and the source documents themselves are often stale: a feature count that no longer matches, an open ticket asking for work that already shipped. Correct a claim about the world that the evidence contradicts. Delete a claim the evidence shows is the project's status, and an identifier, setting or count a system's own code is the source of, rather than correcting either. Bump the version, and report the stale sources — a source that has drifted is an observation about that document, not just an obstacle to this one.

**APPROACH — the chosen design.** Author `<LOBESPACE>_APPROACH.md`: strategic approach, architecture, key design decisions (with alternatives weighed, and any decision not yet made stated as open), and what gets built. This is where solution commitments live. The strategic approach opens with the choices SCOPE leaves open: whom the design serves, where that is narrower than whoever has the problem, and what it builds on beyond SCOPE's premises, with what each foundation requires, provides and withholds. It honors SCOPE's premises without restating them as its own choices, and the assumptions it adds are its own and stay in APPROACH. It then says why this approach beats the alternatives SCOPE assesses, naming the second approach as such. Trace each design choice to the SCOPE goal it serves, cited by name. Then read the pair in the other direction: **for every goal, name the decision that answers it.** A goal with no answering decision is either a gap in the design or a goal that was never real, and where the design deliberately leaves a goal unmet, say so — silence reads as "handled". This reverse pass is what catches the defects the forward pass cannot, because a design that traces cleanly to the goals it addresses says nothing about the goals it skipped. Keep APPROACH and SCOPE orthogonal: if you find yourself faulting SCOPE for not matching an APPROACH decision, that's importing solution bias into the problem statement — stop.

**Read the set back before calling it done.** Run this once every document in the set exists, not after each one. Authoring runs document by document, so each one comes out consistent with itself and the defects collect in the seams. They are invisible from inside the document being written and obvious the moment the set is read together, which is why this is a separate pass and not a matter of being careful while authoring. The structural check in §7 catches none of them — every file involved exists, is namespaced, and carries a version header. Two passes, and they are not the same pass:

- **The scopes, as a group.** Read every SCOPE in one sitting and look for what only appears side by side: a term meaning two different things in two lobes, an open question standing in more than one place, a parent explaining a child's problem rather than naming it, and the same fact stated at two levels. Then re-ask solution-neutrality in a form authoring cannot answer — for each claim about the world, does only that scope's intended design need it, or could a reasonable designer of this problem have decided it otherwise? A claim that only the intended design needs, or that a designer of this problem could have decided otherwise, arrived from a design decision made in some other document and is wearing the clothes of a fact. This is the leak that survives a careful reading for solution bias, because by the time it is written down it reads as a description of reality.
- **Each approach against its own scope, and never against the other approaches.** The pairing is the reverse-trace above, run once the whole set exists. Comparing approaches to *each other* is a mistake: they are siblings, so the comparison invites exactly the coupling the pattern forbids, and it pressures designs that legitimately differ into cosmetic agreement. What matters about an approach is whether it answers its own problem, not whether it resembles its neighbors.

Record the reasoning and course-corrections of this authoring work in the LOG at session closeout (§7). The *decisions* that are invisible from the resulting docs go in FINDINGS as they arise.

---

## 6. Grow into the mature lifecycle (stage 3)

Add these **only when the work justifies them** (the stage model in `MBT_PATTERN.md`) — typically when the brain starts tracking work items across many sessions. Each is copied from `templates/`, namespaced, added to the read index, and bumps `CLAUDE.md`.

- `templates/WORK_SETUP.md` → `<HUB>_WORK_SETUP.md` and `templates/WORK_CLOSEOUT.md` → `<HUB>_WORK_CLOSEOUT.md` — the open/close bookends for work items (a feature, bug fix, or hardening effort). They reference the per-work-item working set in `templates/work/` — inline those six scaffolds into `<HUB>_WORK_SETUP.md` where it points at them, so the brain stands alone without the toolkit.
- `templates/DREAM_CYCLE.md` → `<HUB>_DREAM_CYCLE.md` plus a `<HUB>_DREAM_LOG.md` (header only) — the periodic reflection pass. The template assumes a single lobe; don't instantiate it unadapted into a multi-lobe brain.
- `templates/ENFORCED_TERMS.md` → `<HUB>_ENFORCED_TERMS.md` — the brain's reserved vocabulary. Add it the first time a term collision is found, not before — a brain with no collisions has no enforced terms, and seeding a vocabulary up front is the authoring failure the mechanism's first rule prevents.

When the brain gains work items, also uncomment the work-item block in each project repo's hook (the maturity comment inside `templates/PROJECT_HOOK.md`).

Don't scaffold these into a stage-1 brain; add them the first time a real work item or a real drift-review need appears.

---

## 7. Close out and hand off

1. Append the first LOG entry per `<HUB>_SESSION_CLOSEOUT.md`, recording what this establishment session did and decided (namespace choice, source material, the premises the user settled and the second approach SCOPE was tested against, fact-check corrections).
2. Run a structural check — read index ↔ disk, version headers, cross-references, namespace prefix; for a multi-lobe brain, also registry ↔ disk and each lobe's full doctype set and lobespace — and fix anything it flags.
3. Report to the user: the lobespace used — or the lobe tree and its per-lobe lobespaces, for a multi-lobe brain — which files were **created** vs. already **existed**, what stage the brain is at, and the natural next step (fill SCOPE, or add lifecycle machinery).

Do not commit unless the user asks. If the repo is on its default branch, branch first.
