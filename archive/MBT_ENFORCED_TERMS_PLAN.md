# Enforced Terms: Implementation Plan

## Objective

Give the pattern a way to enforce terminology: a standalone document listing a brain's enforced terms, wired into the four points where prose is written, checked, maintained, and merged. Deliver the document template and its anti-growth rules, the four enforcement hooks, and this brain's own first entries.

## Context

See `MBT_ENFORCED_TERMS_FINDINGS.md` in this directory for the decision record and alternatives considered.

## What changes

- `templates/ENFORCED_TERMS.md` — NEW. The skeleton: header text explaining what enforced terms are, the entry format (prose paragraphs: bold term, definition, disambiguation), the three anti-growth rules, and the instruction to check every use of a listed term against its entry.
- `templates/CLAUDE.md` and `templates/LOBES_CLAUDE.md` — a read-index row pointing to `<PREFIX>_ENFORCED_TERMS.md` (hub documents section in the lobe-level template). One line in the writing rules making an enforced term binding at write time.
- `CLAUDE.md` — the same read-index row and write-time rule. A declared-exemption row for `MBT_ENFORCED_TERMS.md`.
- `MBT_ENFORCED_TERMS.md` — NEW. This brain's own enforced terms, filled with the entries settled below.
- `MBT_CHECK_BRAIN.md` — the one-term-one-meaning bullet becomes two-mode: a per-term grep where the brain declares enforced terms, the existing by-eye set read where it declares none, with a repeated collision becoming a recommendation to declare the term. The reversal identified in the decision record is reconciled here.
- `MBT_DREAM_CYCLE.md` and `templates/DREAM_CYCLE.md` — three hooks across phases that already exist: the per-entry re-grep joins the mechanical structural checks, harvesting new candidates joins the extraction phase that already reads the log, and retiring an entry is flagged for the user rather than applied.
- `templates/WORK_CLOSEOUT.md` and `templates/work/FINDINGS.md` — a coined-or-repurposed-term callout beside the existing one naming the canonical claim an item reverses.
- `MBT_CREATE_BRAIN.md` — the stage-3 growth step gains the enforced terms file, with the harvest-never-author rule stated at the point where an operator would otherwise be tempted to seed a vocabulary.
- `MBT_PATTERN.md` — a stage-3 file-set row for the enforced terms file.

## The enforced terms for this brain

Two entries. Each is a prose paragraph per the settled format.

**Finding** is an entry in a FINDINGS document: a durable, non-obvious decision or discovery worth preserving beyond the session that produced it. It is not anything a check, maintenance pass, or procedure surfaces — those are observations or issues, not findings in the enforced sense. Where the generic sense is needed, write "observation," "issue," or "result."

**Work item** is work that gets its own branch and PR, opened and closed by the setup and closeout rituals, with its own `working/` documents. It is not a ticket, a task, or an issue. The phrase is among the most generic available for a unit of tracked effort and pulls toward the ticket/task/issue senses without the reservation.

### Terms considered and not included

Each demonstrates one of the three anti-growth rules doing its job.

- **working** — the everyday participle is everywhere ("what's working", "working with the brain") and entirely harmless. A grep cannot separate the senses, so the entry would fail the enforcement it exists for. *Constraint: reserve a word whose ordinary form is rare, not one whose ordinary form is ubiquitous.*
- **stage** — a second sense exists (sleep stages in the biology content) alongside the seed/content/mature sense, but it sits in content about an adjacent science where the domain shift is obvious. The disambiguation is empty in practice. *Rule: an empty disambiguation is a delete.*
- **supersede** — appears only parenthetically in the closeout procedure's merge classifications ("Reconcile (supersede)"), not as a standalone term in active use. No writer would confuse it because no writer uses it independently. *Rule: an empty disambiguation is a delete.*
- **canonical** — the ordinary dictionary meaning (authoritative, standard) is close enough to the pattern's meaning (a current, trusted top-level document) that a reader is rarely misled. The more frequent term for the pattern's sense is "top-level." *Rule: an empty disambiguation is a delete.*
- **archive, session, hub, doctype, placement** — single-sense today with no plausible near-miss. *Rule: an empty disambiguation is a delete.*
- **exemplar** — single-sense across all uses, but exposes the mirror defect the mechanism cannot see: two words for one concept ("exemplar" vs. "reference brain") costs a reader what one word for two costs, and no disambiguation can express it.
- **unit, token, component** — were load-bearing in the pattern but their everyday forms (unit test, auth token, LLM token, software component) are ubiquitous, so enforcement by grep would have generated more noise than signal. Left unenforced; the collision was resolved by renaming to "lobe" and "lobespace" (PR #5).

## Collision fixes

Reserving "finding" requires fixing generic uses in current content. The assertion pass found seven generic uses across four files:

- `MBT_DREAM_CYCLE.md` — "itself a finding to flag", "absence is itself a finding", "the finding that breaks a load-bearing verdict"
- `MBT_RESEARCH.md` — "absence is itself a finding", "a question it can't answer is the finding"
- `MBT_CHECK_BRAIN.md` — "is not a finding"; also the report section headings "Structural findings" and "Substance findings"
- `MBT_CREATE_BRAIN.md` — "a finding about that document"

Each generic use is reworded to an unambiguous alternative. The report section headings in the check procedure are renamed to avoid confusion with FINDINGS entries.

"Work item" is clean in current content — no collision fixes needed.

Archive content is exempt: retired files keep the form they were retired under and are never edited for enforced-terms compliance.

## Implementation sequence

1. Create `templates/ENFORCED_TERMS.md` — the skeleton with format, rules, and instructions.
2. Add read-index rows and write-time rules to both entrypoint templates and this brain's `CLAUDE.md`. Add the declared-exemption row to `CLAUDE.md`.
3. Wire the four enforcement hooks — check, dream cycle (both the toolkit's own and the template), closeout, and work FINDINGS template.
4. Add the enforced terms file to `MBT_CREATE_BRAIN.md`'s stage-3 growth step and `MBT_PATTERN.md`'s stage-3 file set.
5. Create `MBT_ENFORCED_TERMS.md` with this brain's three entries.
6. Fix the "finding" collisions in current content.

## Testing approach

No code. Three dry runs.

1. Seed this brain's enforced terms with the three entries and run the check procedure's term pass over the canonical set. Acceptance: a *planted* collision is caught (misuse a reserved term deliberately in a document that does not currently misuse it), and a reader following only the documented procedure arrives at the same entries without prior knowledge of the slate. Measure false-positive volume per term — a term burying its real hits under ordinary English is evidence the entry should be rejected.
2. Run the same pass against a brain with an empty enforced terms file and confirm it is silent and raises no gap.
3. A write-time trial: author one new document against the filled enforced terms file and confirm the enforced sense is what comes out, and that the writer is not tempted into defining the concepts rather than using them.

## Scope boundary

- Any project's domain vocabulary. The enforced terms govern the brain's own prose; enforcing the product's terms would pull the brain toward being a wiki for the product.
- Definitions of the enforced concepts, which stay in their home documents. An entry disambiguates and points.
- Term coordination between two brains co-loaded in one session, which is an open question the pattern already carries.
- Renaming pattern vocabulary. The enforced terms mechanism governs the brain's own prose; changes to the pattern's core terms are a separate concern.
