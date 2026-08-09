# Enforced Terms: Implementation Plan

## Objective

Give the pattern a way to reserve terminology: a small registry of words a brain has taken, each stated with the near-miss it must not be confused with, wired into the four points where prose is written, checked, maintained, and merged. Deliver the registry's shape and its anti-growth rules, the four enforcement hooks, and this brain's own first rows.

Landable now, and it needs no living example — the mechanism is one table plus four short hooks, and the assertion pass below has already earned this brain's first rows. It is stage-3 machinery: a new brain adopts nothing, because it has not yet used any word enough to collide, and a registry with zero rows is the normal state for most of a brain's life.

## Context

See `MBT_ENFORCED_TERMS_FINDINGS.md` in this directory for the decision record and alternatives considered.

`MBT_PATTERN.md` carries both things this depends on: the orthogonality principle that creates the collision (documents authored without their siblings in view) and the stage model that decides when a brain takes the machinery on.

## What changes

- `templates/CLAUDE.md` and `templates/COMPONENTS_CLAUDE.md` — an empty registry section in the conventions block, carrying the row shape and the three anti-growth rules; and one line in the writing rules making a reserved term binding at write time. A component brain's registry sits at the hub with the other conventions.
- `CLAUDE.md` — the same section, filled with the rows settled from the slate below.
- `MBT_CHECK_BRAIN.md` — the one-term-one-meaning bullet becomes two-mode: a per-term grep where the brain declares terms, the existing by-eye set read where it declares none, with a repeated collision becoming a recommendation to declare the term. This is also the reversal the decision record names.
- `MBT_DREAM_CYCLE.md` and `templates/DREAM_CYCLE.md` — three hooks rather than one pass, because the work splits across phases that already exist: the per-row re-grep joins the mechanical structural checks, harvesting new candidates joins the extraction phase that already reads the log, and retiring a row removes substance, so it is flagged for the user rather than applied — as the cycle's own guiding principle requires.
- `templates/WORK_CLOSEOUT.md` and `templates/work/FINDINGS.md` — a coined-or-repurposed-term callout beside the existing one naming the canonical claim an item reverses; both are things only the author knows and a wording-based grep cannot find at merge.
- `MBT_CREATE_BRAIN.md` — the stage-3 growth step gains the registry, with the harvest-never-author rule stated at the point where an operator would otherwise be tempted to seed a vocabulary.
- `MBT_PATTERN.md` — a stage-3 file-set row, if the registry is judged to be part of the file set rather than a convention the entrypoint carries (open issue 5).

## The candidate rows for this brain

The slate below was asserted against current top-level and template content. The result is worth stating plainly: **the content is not as clean as assumed.** Six words already carry two senses, several of them inside the very documents that reserve them, and one of the six ships verbatim in two templates. These are the rows closest to what this brain already is — not invented vocabulary.

**Reserve now — live collision in current content.**

| Term | Reserved meaning | Must not mean | What the assertion found |
|---|---|---|---|
| **unit** | A brain's hub or any of its components, at any depth. | A quantum of work; a test scope. | Four independent generic uses: `MBT_PATTERN.md` in both principle 9 ("each unit of work") and principle 3 ("as a whole unit"), `MBT_CHECK_BRAIN.md`'s scorecard row for principle 9 ("open/close of a work unit"), and `MBT_FINDINGS.md` ("the unit of tracked work"). Also `templates/work/PLAN.md` ("unit vs. integration"), where the test sense is idiomatic and probably survives. |
| **token** | The SCREAMING_SNAKE_CASE namespace token a unit declares. | A unit of LLM context. | The writing rules in `CLAUDE.md` — "every token is load-bearing, and every spare one is a question they must resolve" — sitting in the same file that reserves the word, and shipped verbatim in `templates/CLAUDE.md` and `templates/COMPONENTS_CLAUDE.md`. Also `MBT_DREAM_CYCLE.md` ("token cost"). The strongest row on the slate: two senses, one file, and it propagates to every seeded brain. |
| **finding** | An entry in a FINDINGS document — a durable, non-obvious decision. | Anything a check or maintenance pass surfaces. | Seven generic uses across four files: `MBT_DREAM_CYCLE.md` three times ("itself a finding to flag", "absence is itself a finding", "the finding that breaks a load-bearing verdict"), `MBT_RESEARCH.md` twice ("absence is itself a finding", "a question it can't answer is the finding"), and one each in `MBT_CHECK_BRAIN.md` ("is not a finding") and `MBT_CREATE_BRAIN.md` ("a finding about that document"). Its report sections are also headed "Structural findings" and "Substance findings", neither of which is a FINDINGS entry. Two further grep hits are the *verb* ("finding files by guesswork") and are not collisions at all — which puts this term nearer to *working* than the rest of the slate, and is evidence for open issue 4. |
| **supersede** | The closeout knowledge-edit classification: rewrite an existing statement in place. | A work item's retirement reason. | Already found by hand, already unresolved, already recorded as an open issue on another work item. It is the proof case: a real collision, caught late, by one person noticing, in a document about to acquire the second sense deliberately. |
| **registry** | The entrypoint's component table. | A fact table refreshed on a cadence. | Three senses live at once. `MBT_COMPARABLES.md` and `MBT_BIOLOGY.md` both title themselves registries and are described as such throughout `MBT_DREAM_CYCLE.md` and `MBT_RESEARCH.md`; the component registry is the entrypoint's; and this work item would add a third. One sense has to yield (open issue 2). |
| **canonical** | A current, trusted top-level document, as against `working/` and `archive/`. | Authoritative or original in the ordinary sense. | `MBT_COMPARABLES.md` carries a "Canonical source" column — a URL to an external system's home — in four tables a maintenance pass rewrites every cycle, and `MBT_SCOPE.md` states the goal as "one canonical, operational definition". The mildest of the six; the ordinary sense is close enough to the reserved one that a reader is rarely misled. |

**Reserve preventively — clean here, hostile downstream.**

| Term | Reserved meaning | Must not mean | Why it earns a row anyway |
|---|---|---|---|
| **component** | A unit whose problem is one of several its parent's problem divides into. | A software module, service, or UI component. | No generic use exists in current content — this brain is clean. The word is nonetheless a term of art in the domain most brains describe, so any brain documenting software collides with it on contact. This is what a healthy row looks like: reserved before the collision, not after. |
| **work item** | Work that gets its own branch and PR, opened and closed by the setup and closeout rituals. | A ticket, a task, or an issue. | Clean today, and the reserved meaning was already fought for once when it displaced "feature". The generic pull is strong enough that a sibling work item — the TASKS-to-BURNDOWN rename — exists because a neighbouring document's name reads as *ticket*. |

**Rejected, and the reasons are part of the deliverable.** Each shows one of the three rules doing its job, so the slate should ship with them recorded rather than silently dropped.

- **working** — the everyday participle is everywhere ("what's working", "working with the brain", "working in the mini-brain") and entirely harmless. A grep cannot separate the senses, so the row would fail the enforcement it exists for. **Constraint discovered: reserve a word whose ordinary form is rare, not one whose ordinary form is ubiquitous.**
- **stage** — a genuine second sense exists (`MBT_BIOLOGY.md` on sleep stages) alongside the reserved seed/content/mature sense, but it sits in a registry about an adjacent science where the domain shift is obvious to any reader. The Not cell is empty in practice, and an empty Not cell is a delete.
- **archive, session, hub, doctype, placement** — swept and single-sense today, with no plausible near-miss. Leaving them out is precisely what keeps the registry from becoming a glossary; each would be a defensible dictionary entry and none would prevent anything.
- **exemplar** — single-sense across all ten of its uses, so rejected on the same test, but it exposes the mirror defect this mechanism cannot see. `MBT_SCOPE.md` heads a section "Keeping templates and *reference brains* in sync" and closes that same paragraph with "between the toolkit and its *exemplars*", while three other documents say *exemplar* throughout. Two words for one concept costs a reader what one word for two costs, and no Not cell can express it.

## Interaction with existing docs

| Existing doc | Interaction | Risk |
|---|---|---|
| `MBT_CHECK_BRAIN.md` one-term-one-meaning check | The registry converts a substance check needing a whole-set read into a structural check a grep drives | Two checks for one defect, disagreeing on a brain that declares some terms and not others |
| `CLAUDE.md` writing rules | The sentence that would carry the write-time rule uses *token* in the unreserved sense | The convention ships carrying a violation of itself, in the file that declares it |
| `MBT_COMPARABLES.md`, `MBT_BIOLOGY.md` | Both name themselves registries and carry a "Canonical source" column | Reserving two of the six forces renames in the documents a maintenance pass rewrites most often, so the churn lands where drift is likeliest |
| `templates/COMPONENTS_CLAUDE.md` | The component registry is already in the entrypoint, and the terms registry would sit beside it | Two tables called registries in one document, which is the collision demonstrating itself |
| `templates/WORK_CLOSEOUT.md` | The coined-term callout is the same shape as the existing reversal callout | A second author-only callout that the closeout walk cannot derive, so it is skipped exactly as often as the first one is |

## Testing approach

No code. Three dry runs on a disposable copy, plus one decay check.

Seed this brain's registry with the rows settled above and run the check procedure's term pass over the canonical set. **Re-running a grep over the same corpus is not a test** — it is the assertion pass a second time, and it passes by construction. Acceptance is therefore two things the assertion pass cannot give itself: a *planted* collision is caught (take a reserved term and misuse it deliberately in a document that does not currently misuse it), and a reader who did not write the slate, following only the documented procedure, arrives at the same rows. The first tests the check; the second tests whether the rows encode a procedure or this session's judgment. Measure the false-positive volume per term alongside both — a term that buries its real hits under ordinary English is evidence the row should be rejected, not that the check needs tuning.

Then run the same pass against a brain with an empty registry and confirm it is silent and raises no gap.

Then a write-time trial: author one new document against the filled registry and confirm the reserved sense is what comes out, and that the writer is not tempted into defining the concepts rather than using them.

The decay check runs the three rules against *stage* and *working* and confirms both are rejected — the rules have to be able to say no, or the registry only ever grows.

## Implementation sequence

1. Settle the row shape and the three anti-growth rules; place the empty registry in both entrypoint templates.
2. Settle each row on the slate, including which sense of *registry* and *canonical* yields.
3. Wire the four enforcement points — write, check, maintain, closeout.
4. Fix the collisions the filled registry now forbids, starting with the writing rules' own use of *token*.
5. Run the three dry runs and the decay check.

## Scope boundary — what this does NOT include

- Any project's domain vocabulary. The registry governs the brain's own prose; reserving the product's terms would pull the brain toward being a wiki for the product.
- Definitions of the reserved concepts, which stay in their home documents. A row disambiguates and points.
- Term coordination between two brains co-loaded in one session, which is an open question the pattern already carries.
- Adding or renumbering a principle. The registry serves the orthogonality principle; whether that principle's wording changes is a user-level call.

## Open issues

1. Whether the registry stays a section in the entrypoint at every size or graduates to its own document past a stated threshold, and what that threshold is.
2. Whether *registry* can be reserved at all. The two research fact tables have called themselves registries since long before the word was contested, and the component registry is named in the entrypoint grammar — one of the three senses has to yield, and which one is editorial rather than derivable.
3. Whether a reserved term binds `archive/` content. Retired documents keep the wording they were retired under, so a repo-wide grep hits them and every term pass would carry permanent noise unless the check is scoped.
4. Whether the term pass is a structural check (mechanical, pass/fail) or a substance check with a mechanical aid. *working* proves some terms cannot be judged mechanically at all, so a single classification may not hold for the whole registry.
5. Whether the registry earns a row in the pattern's stage-3 file set, or is a convention the entrypoint carries with no file of its own — which decides whether it is one of the pattern's documents or one of its rules.
6. What this work item's own deliverable is called. The slate reserves *registry* for the entrypoint's component table while both documents here call the deliverable "the registry" throughout — so the pair has already pre-committed to the third sense that open issue 2 holds open. Either the reserved meaning waits on issue 2, or the deliverable takes a working name now (*reserved-terms table*) so that settling issue 2 does not mean rewriting the pair. This is the mechanism failing to catch itself in the document proposing it, which is the cheapest evidence available that the mechanism is needed.
