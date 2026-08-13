# Burndown: Implementation Plan

## Objective

Rename a work item's TASKS document to BURNDOWN and reframe it as the second half of a two-document pair: the plan gets the code written, the burndown gets the code pushed upstream. Deliver the renamed scaffold with a positive scope statement in place of a category list, the early plan-archival move that reframing makes safe, and the rename across every site that names the old file.

Landable now. It touches no component machinery and needs no living example — the reading failures it corrects have already happened in seeded brains, and the correction is a name plus a scope.

## Context

See `MBT_BURNDOWN_FINDINGS.md` in this directory for the decision record and alternatives considered.

`MBT_PATTERN.md` carries the two things this depends on: the version-header exemption stated in terms of what the document is, and the stage-3 working set that fixes which documents a work item carries.

## What changes

Sixteen sites across ten files. Twelve are found by grepping `TASKS`; four are not — the scaffold's filename, its heading, its opening line, and work setup's one reference to the document by description. Three of the bullets below also carry new content rather than a rename: the scaffold's scope statement, work setup's statement of the pair, and work closeout's early-archival mechanic.

- `templates/work/TASKS.md` → `templates/work/BURNDOWN.md` — three sites, none of which a `TASKS` grep finds: the filename, the heading (`# <Work-Item Name>: Burndown`), and the opening line, which becomes a positive scope statement — a finishing checklist for everything between working code and a merged PR — in place of the category list. The body splits into routine and custom items, with routine items as inheritable defaults each brain refines; the closeout-notes bullet stays as it is.
- `templates/WORK_SETUP.md` — four sites: the working-doc table row (name and role), the intake bullet that says the testing approach "seeds the TASKS checklist", the base-template list naming `TASKS.md`, and the scope paragraph's "rather than being forced through the PR checklist" — which names the document by description, so a grep-driven rename misses it. Setup also gains the statement of what the pair is for, since that is what a scaffolding reader needs before the documents exist.
- `templates/WORK_CLOSEOUT.md` — the closeout-notes reference naming `<TOKEN>_<WORK>_TASKS.md`, and the early-archival mechanic: user-requested, with a guided review of any significant unaddressed plan items before the plan moves. Its enumerate-what-exists rule already tolerates a missing plan ("a doc was implemented and retired mid-development (often the PLAN)"), so closeout half-anticipates this move and never says how to make it safe.
- `MBT_PATTERN.md` — two sites: principle 7's exemption phrase ("task checklists") and the stage-3 working-set list `{PLAN,FINDINGS,LOG,TASKS,CLAUDE,TESTING}`.
- `CLAUDE.md`, `templates/CLAUDE.md`, `templates/COMPONENTS_CLAUDE.md` — the version-exemption list, written as the glob `*_TASKS.md` in each.
- `MBT_CHECK_BRAIN.md`, `MBT_DREAM_CYCLE.md`, `templates/DREAM_CYCLE.md` — the same glob inside each version-header check.

## Interaction with existing docs

| Existing doc | Interaction | Risk |
|---|---|---|
| `templates/WORK_CLOSEOUT.md` | Already tolerates a missing plan as an incidental case, without saying how one may go missing | Early archival stays an informal habit rather than a defined move, so the guided review that makes it safe is the step people skip |
| Version-exemption globs in seven documents | The exemption is written as a filename pattern, not as a doctype name | A renamed file silently becomes version-required, and every brain's checker starts flagging a document that is exempt by design |
| `MBT_PATTERN.md` stage-3 working set | Fixes the six doctypes a work item carries, by name | The spec and the templates disagree about what a work item is made of, which is the drift the toolkit exists to prevent |
| `templates/work/TESTING.md` | Has the same lifetime property — manual checks outlive the plan | Deliberately excluded here, so half the lifetime problem is solved and the other half is left looking like an oversight unless it is named |

## Testing approach

No code. One end-to-end dry run on a disposable copy, one adoption check, and one back-test.

Scaffold a work item from the changed templates and walk it through plan → code → PR. Mid-way, request early plan archival. Acceptance is three things: the guided review surfaces unaddressed items and the developer decides per-item what belongs in the burndown, the burndown reads completely with the plan absent from `working/`, and closeout finds and retires the burndown by its new name.

Then run the check procedure against a brain carrying the new name and confirm the version-header check does not flag the burndown — the exemption glob is the site most likely to be missed, because nothing else fails when it is.

Then the back-test that justifies the rename: re-read the two known misreadings — the master list and the plan summary — against the new scaffold, and ask whether either is still a defensible reading of it. If a reader could still produce a master list without contradicting anything the document says, the scope statement is not doing the work and the name alone will not save it.

## Implementation sequence

1. Rewrite the scaffold: rename the file, replace the category list with the scope statement, split routine from custom with routine items as inheritable defaults.
2. State the pair and its handoff in work setup; state the early-archival move and its guided review in work closeout.
3. Apply the rename to the remaining thirteen sites, exemption globs last so they can be checked against the finished set.
4. Run the dry run, the adoption check, and the back-test.

## Scope boundary — what this does NOT include

- The manual test plan, which shares the lifetime property and is a separate call.
- Any change to how work items are scaffolded, routed, or retired. This renames one document and defines one new retirement move for another.
- The plan scaffold's own structure is unchanged.
- A mechanism for verifying that a burndown is complete.
- Migration of existing brains carrying `*_TASKS.md`. No check validates work-item doc names, so a legacy file passes the check procedure silently; migration is a separate effort.

