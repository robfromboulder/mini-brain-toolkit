# Template Drift: Implementation Plan

## Objective

Make upgrading a brain the same act every release: run `check` and follow its recommendations. Deliver a `check` step that merges each procedure template's change since a brain's copy was last brought up to date into that copy, reports each change as a recommendation carrying the template's text, and leaves every change to the owner in the walk-through. Release notes then never carry upgrade steps.

## Context

See `MBT_TEMPLATE_DRIFT_FINDINGS.md` in this directory for the decision record, the evidence and the alternatives considered. `MBT_TEMPLATE_DRIFT_EXPERIMENT.py` in this directory runs the comparison by script.

The procedure files and their templates:

| Brain's file | Template |
|---|---|
| `<HUB>_SESSION_CLOSEOUT.md` | `templates/SESSION_CLOSEOUT.md` |
| `<HUB>_WORK_SETUP.md` | `templates/WORK_SETUP.md`, plus the six `templates/work/` scaffolds it inlines |
| `<HUB>_WORK_CLOSEOUT.md` | `templates/WORK_CLOSEOUT.md` |
| `<HUB>_DREAM_CYCLE.md` | `templates/DREAM_CYCLE.md` |
| The brain's `CLAUDE.md`: the template's text in its Read Index and conventions sections | `templates/CLAUDE.md`, or `templates/LOBES_CLAUDE.md` for a multi-lobe brain |
| The hook's paragraphs, wherever they sit in each project repo's `AGENTS.md` or `CLAUDE.md` | `templates/PROJECT_HOOK.md` |
| The prompts in the brain's `README.md` | `templates/README.md` |

`templates/AGENTS.md` is not in the table. Check 8 (loading reach) in `MBT_CHECK_BRAIN.md` owns the brain's `AGENTS.md`, the `AGENTS.md` exemptions in the brain's `CLAUDE.md` and dream cycle, and the hook's move from a project repo's `CLAUDE.md` into its `AGENTS.md`. The drift check reports none of these.

Knowledge files are never compared, and neither are a work item's docs. The scaffolds inlined in `<HUB>_WORK_SETUP.md` are procedure text and are compared against `templates/work/`. The template's sentence locating them in `templates/work/` is not drift, since a brain's copy inlines them by design.

## What changes

- `MBT_CHECK_BRAIN.md`, structural checks — a procedure-drift check. For each file in the table the brain holds:
  - Read its base from its stamp, or for an unstamped file, take the tagged release whose template differs least from it and confirm that with the user.
  - Take the base and current templates from the install's git history (`git -C <install> show <ref>:templates/<file>`).
  - Normalize all three texts: fold the brain's lobespace back to `<LOBESPACE>`, read `<HUB>` as `<LOBESPACE>`, fill the display and lowercase names, and drop version lines.
  - Merge paragraph by paragraph. A paragraph only the template changed is a recommendation; one both changed is a conflict; one only the brain changed is not reported.
  - Split work setup's inlined scaffolds out by content, whatever their heading or fence, and merge each against its `templates/work/` file.
  - Match the hook's paragraphs by content in the project repo's instruction files.
  - Skip the paragraphs check 8 rewrites.
  - Without git history in the install, compare two ways and put every difference to the user.
- `MBT_CHECK_BRAIN.md`, report — procedure drift gets its own entry among the structural issues: each recommendation with a one-line reading of what the template's text changes, then each conflict with both texts. The report names the toolkit version it compared against and each file's base.
- `MBT_CHECK_BRAIN.md`, walk-through — check 8's fix runs before drift updates. An approved recommendation or a resolved conflict replaces that paragraph, filling placeholders as the brain's copy fills them around it. A declined one stays as it is. Once every recommendation in a file is decided, its stamp advances to the current version.
- `MBT_CHECK_BRAIN.md`, check 8 — in a brain copied from the templates, the conventions fix takes the current template's wording for the paragraphs it changes, so the drift check finds them current rather than in conflict.
- `MBT_CHECK_BRAIN.md`, check 3 — skip HTML-commented content, as check 1 does. A seeded brain's `CLAUDE.md` names its staged lifecycle docs in comments, so check 3 followed literally flags files that don't exist yet.
- `MBT_CREATE_BRAIN.md` and each procedure template — a stamp line under the version header, `<!-- Toolkit: <toolkit-version> -->`, with `<toolkit-version>` joining the creation placeholders as the install's `git describe --tags`. The hook and README templates carry it inside the merged section.
- `templates/DREAM_CYCLE.md` — fix two defects that the drift check would otherwise carry into every brain. Codex and OpenCode 2 each found both independently during the PR #19 retest. Check 6 exempts names carrying `<LOBESPACE>` as placeholder notation, but `create` substitutes the lobespace, so a seeded brain exempts its own real `working/` filenames and lets leaked references through. The exemption becomes "a name carrying an angle-bracketed variable such as `<WORK>`", which survives `create`'s substitution and still exempts `working/ORCHARD_<WORK>_PLAN.md` while flagging `working/ORCHARD_FOO_PLAN.md`. Checks 1 and 4 don't say to skip read-index rows commented out in HTML, as check 1 in `MBT_CHECK_BRAIN.md` does, so followed literally they flag the rows staged for docs that don't exist yet.
- `templates/DREAM_CYCLE.md`, Phase 5 — with no enforced terms file, the drift pass still proposes a term by "the enforced terms file's rule for adding an entry", which doesn't exist. `MBT_CHECK_BRAIN.md` falls back to `templates/ENFORCED_TERMS.md`, but a brain's dream cycle never sees the toolkit, so the rule must be stated in the dream cycle itself.
- `templates/DREAM_CYCLE.md`, Phase 4 — extraction promotes "discoveries that reframed the problem" to FINDINGS, which the template's exemption table defines as implementation decisions that did not shape the approach. Extraction must route by that definition.
- `templates/CLAUDE.md`, `templates/LOBES_CLAUDE.md`, `CLAUDE.md` — "LOG files are never archived" contradicts work closeout's retire step, which moves a work item's working log to `archive/`. Scope the rule to canonical logs.
- `MBT_PATTERN.md` — the distinction between knowledge files and procedure files, which the pattern does not yet draw.

## Interaction with existing docs

| Existing doc | Interaction | Risk |
|---|---|---|
| `MBT_CHECK_BRAIN.md` check 8 | Owns the loading path through `AGENTS.md`, including paragraphs of the brain's `CLAUDE.md`, its dream cycle and the project hook that the drift check also compares | If check 8's fix words a paragraph differently from the current template, the next drift check reports it as a conflict |
| `MBT_CREATE_BRAIN.md` placeholder rules | The walk-through fills placeholders in the template text it applies | Filling by the brain's own surrounding text can't follow a rule the copy never exercised; a new placeholder needs the user |
| `SKILL.md` path rule | Templates and their history resolve against the install | A stale install compares against stale templates and reports a current brain as clean; the report's toolkit version is the only signal |
| `templates/DREAM_CYCLE.md` | A brain's own dream cycle never sees the toolkit's templates | Drift found only when the owner runs `check`; whether the dream cycle should prompt for one is open |
| `MBT_DREAM_CYCLE.md` | This brain's own maintenance docs differ from their templates by design, since its subject is the pattern | Running the drift check on the toolkit reports its own docs as drift |
| Release notes | No longer carry upgrade steps | A change `check` can't detect (a renamed file, a moved convention) would have no channel at all |

## Testing approach

Each test also runs `MBT_TEMPLATE_DRIFT_EXPERIMENT.py` against the same brain and base. The agent's recommendations and conflicts must match the script's, file by file.

1. **0.72 fixture.** Seed a brain in a scratch directory from the 0.72 templates with the PR #19 retest's `seed.sh`, pointed at tag 0.72 and extended with work setup (scaffolds inlined) and work closeout. Run `check` from `main`.
   - Check 8 moves the hook into the project repo's `AGENTS.md`, adds the brain-side `AGENTS.md` and its exemptions, and keeps the hook's work-item block.
   - The drift check reports the rest of 0.73's procedure changes once each, with no conflicts: the session-ID variables and harness-neutral wording in session closeout and the README prompts, work setup's audit and alignment changes, the retire-move rule in `CLAUDE.md` and work closeout, and the dream cycle's naming exemptions read from `CLAUDE.md` and its read-only subagent wording. It reports nothing check 8 handled.
   - A second `check` reports no drift.

   Every existing brain needs this upgrade for 0.73, so it is the test that matters most.
2. **0.70 fixture.** The same, seeded at tag 0.70. It reports each change to a procedure template between 0.70 and `main` once, with the template's text, and no knowledge file. The walk-through, approving every update, leaves the filled-in placeholders and work-item block intact.
3. **lamarr-brain**, unstamped and seeded from 0.71. `check` proposes 0.71 as the base. It reports the upstream changes to session closeout, work setup's procedure, work closeout, `CLAUDE.md` and the README with no conflicts, nothing for the scaffolds, and none of the brain's adaptations. The hook is split across sections of the project's `CLAUDE.md`, and has no drift.
4. **mini-subtitle-wizard-brain** (https://codeberg.org/kolin-newby/mini-subtitle-wizard-brain), unstamped and seeded from 0.71 by an outside author. `check` reports the same upstream changes, and one conflict in work setup step 3. The deviations its first log entry records survive, as does its Codeberg burndown rule. The brain lives in `~/mini-brains/`, so the user names its project repo (https://codeberg.org/kolin-newby/subtitle-wizard) for check 8 and the hook.
5. **virtual-view-brain**, unstamped and predating 0.70. Session closeout fits 0.70 and takes its upstream changes cleanly. Work setup, work closeout, `CLAUDE.md` and the README raise the conflicts the script finds, each put to the owner with both texts. The brain has no dream cycle.

After each walk-through, a second `check` reports nothing for any change the owner declined.

## Implementation sequence

1. Fix the two `templates/DREAM_CYCLE.md` defects and its Phase 4 and Phase 5 wording, check 3's commented content, and the LOG-archiving rule.
2. Add the stamp to `create` and the procedure templates.
3. Write the drift check, report entry and walk-through step in `MBT_CHECK_BRAIN.md`, and align check 8's conventions fix with the current template's wording.
4. Run the fixture tests, then the three existing brains.

## Scope boundary — what this does NOT include

- Knowledge files written to an older standard, which `check`'s substance checks already cover.
- Updating anything without the owner's approval.
- The toolkit's own maintenance docs, which differ from the templates by design.

## Open issues

1. Whether a brain's dream cycle should flag that a `check` is due after a toolkit release, since it never reads the templates itself.
2. Whether a change that renames or moves a procedure file needs its own detection, so release notes stay free of upgrade steps.
3. Whether the rules preamble of `templates/ENFORCED_TERMS.md` is compared. It is procedure text, though the entries below it are knowledge.
4. Whether a multi-lobe brain's dream cycle is compared before MULTI_LOBE_DREAM lands. The template assumes a single lobe, so a copy adapted for a multi-lobe brain differs throughout, by design.
5. Overlaps with open work items. WORK_PLACEMENT and REHOMING both change `templates/WORK_SETUP.md`. MULTI_LOBE_DREAM redesigns `templates/DREAM_CYCLE.md` and requires `MBT_CHECK_BRAIN.md` and the dream cycle to flag the same things. Whichever lands after this item changes what its tests expect.
6. Whether this item also fixes `create` putting a `.gitkeep` only in `working/`, leaving a seeded brain's empty `archive/` untracked. The PR #19 retest found it, and subwiz's owner worked around it when seeding; the drift check can't find it, because no template carries it.
7. Check 8's move of a hook split across sections, as lamarr's is. The template's opening comment assumes one section to move.
