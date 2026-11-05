# Template Drift: Implementation Plan

## Objective

Make upgrading a brain the same act every release: run `check` and follow its recommendations. Deliver a `check` step that compares each procedure file a brain holds with the current template it was copied from, reports each difference as a recommendation carrying the template's text, and leaves every change to the owner in the walk-through. Release notes then never carry upgrade steps.

## Context

See `MBT_TEMPLATE_DRIFT_FINDINGS.md` in this directory for the decision record and alternatives considered.

The procedure files and their templates:

| Brain's file | Template |
|---|---|
| `<LOBESPACE>_SESSION_CLOSEOUT.md` | `templates/SESSION_CLOSEOUT.md` |
| `<LOBESPACE>_WORK_SETUP.md` | `templates/WORK_SETUP.md` |
| `<LOBESPACE>_WORK_CLOSEOUT.md` | `templates/WORK_CLOSEOUT.md` |
| `<LOBESPACE>_DREAM_CYCLE.md` | `templates/DREAM_CYCLE.md` |
| The brain's `CLAUDE.md`, conventions sections only | `templates/CLAUDE.md`, or `templates/LOBES_CLAUDE.md` for a multi-lobe brain |
| The "Working in the Mini-Brain" section of each project repo's `CLAUDE.md` | `templates/PROJECT_HOOK.md` |
| The prompts in the brain's `README.md` | `templates/README.md` |

The skill-install work item's second part lands first and changes this table: the hook moves into each project repo's `AGENTS.md`, with its `CLAUDE.md` importing it, and a brain-side `AGENTS.md` template joins the set. Settle the table against those templates as they land.

Knowledge files are never compared, and neither are a work item's docs, which `templates/work/` seeds once per item.

## What changes

- `MBT_CHECK_BRAIN.md`, structural checks — a procedure-drift check: for each file in the table the brain holds, substitute the brain's placeholder values into the current template and compare the two section by section. A section the brain filled in (its read index, exemption table, lobe registry, the hook's lobe paragraph and work-item block) is compared only for the template's own text around it.
- `MBT_CHECK_BRAIN.md`, report — procedure drift gets its own entry among the structural issues: each differing section, with a one-line reading of what the template's current text changes. The report names the toolkit version it compared against.
- `MBT_CHECK_BRAIN.md`, walk-through — an approved update replaces that section with the template's text, keeping the brain's filled-in parts. A declined one stays as it is.
- `templates/DREAM_CYCLE.md` — fix two defects that the drift check would otherwise carry into every brain. Codex and OpenCode 2 each found both independently during the PR #19 retest. Check 6 exempts names carrying `<LOBESPACE>` as placeholder notation, but `create` substitutes the lobespace, so a seeded brain exempts its own real `working/` filenames and lets leaked references through; the exemption must describe placeholder notation in words that `create`'s substitution leaves alone. Checks 1 and 4 don't say to skip read-index rows commented out in HTML, as check 1 in `MBT_CHECK_BRAIN.md` does, so followed literally they flag the rows staged for docs that don't exist yet.
- `templates/DREAM_CYCLE.md` — verify three wording issues Codex raised in the same retest, which haven't yet been checked against the template: the enforced-terms rules when the brain has no enforced-terms file, discoveries that shaped the approach being routed to FINDINGS, and "LOG files are never archived" against retiring merged working logs.
- `MBT_PATTERN.md` — the distinction between knowledge files and procedure files, if the pattern doesn't already draw it in terms `check` can cite.

## Interaction with existing docs

| Existing doc | Interaction | Risk |
|---|---|---|
| `MBT_CREATE_BRAIN.md` placeholder rules | `check` needs the same substitution rules to rebuild what a copy should say | The procedures don't reference one another, so the rules get restated in `check` and the two copies drift; they may need a home in `MBT_PATTERN.md` |
| `SKILL.md` path rule | `templates/` resolves against the install | A stale install compares against stale templates and reports a current brain as clean; the report's toolkit version is the only signal |
| `templates/DREAM_CYCLE.md` | A brain's own dream cycle never sees the toolkit's templates | Drift found only when the owner runs `check`; whether the dream cycle should prompt for one is open |
| `MBT_DREAM_CYCLE.md` | This brain's own maintenance docs differ from their templates by design, since its subject is the pattern | Running the new check on the toolkit reports its own docs as drift; running `check` on the toolkit already misfires (an open issue in the skill-install work item) |
| Release notes | No longer carry upgrade steps | A change `check` can't detect (a renamed file, a moved convention) would have no channel at all |

## Testing approach

Seed a brain in a scratch directory with the toolkit at tag 0.72, before the skill-install work item's second part, then run the new `check` from `main` against it. Acceptance: the walk-through moves the brain's hook from the project repo's `CLAUDE.md` into its `AGENTS.md` and adds the brain-side `AGENTS.md`, keeping the hook's lobe paragraph and work-item block. Every existing brain needs this upgrade for 0.73, so it is the test that matters most.

Then seed one at tag 0.70 and run the same `check`. Acceptance: it reports the 0.71 hook and session-closeout changes and the 0.72 dream-cycle changes once each, with the template's text; it reports no knowledge file; and the walk-through, approving every update, leaves the brain's filled-in placeholders, lobe paragraph and work-item block intact.

Then run it against lamarr-brain, whose copies were updated by hand, a multi-lobe brain (virtual-view-brain), and an externally authored brain (mini-subtitle-wizard-brain). Acceptance: no false drift on lamarr; each remaining difference put to the owner rather than applied; nothing reported for a brain whose procedure files were never copied from a template.

## Implementation sequence

1. Settle where the placeholder rules and the procedure-file list live.
2. Fix the two `templates/DREAM_CYCLE.md` defects, and verify Codex's three wording issues against the template.
3. Write the drift check, report entry and walk-through step in `MBT_CHECK_BRAIN.md`.
4. Run the 0.72-seeded and 0.70-seeded brain tests, then the three existing brains.

## Scope boundary — what this does NOT include

- Knowledge files written to an older standard, which `check`'s substance checks already cover.
- Updating anything without the owner's approval.
- The toolkit's own maintenance docs, which differ from the templates by design.

## Open issues

1. How a brain records an adaptation it keeps, so later checks stop reporting it: a comment in the file, a list in its `CLAUDE.md`, or nothing, re-asking each time.
2. Whether each template should carry a toolkit-version stamp as a cheap first signal that a copy is stale, alongside the comparison.
3. How `check` recognizes a file that started from a template but was reorganized, rather than one that never came from one.
4. Whether a brain's dream cycle should flag that a `check` is due after a toolkit release, since it never reads the templates itself.
5. Whether a change that renames or moves a procedure file needs its own detection, so release notes stay free of upgrade steps.
