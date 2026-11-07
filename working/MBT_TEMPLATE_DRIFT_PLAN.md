# Template Drift: Implementation Plan

## Objective

Make upgrading a brain the same act every release: run `check` and follow its recommendations. Deliver a `check` step that merges each procedure template's change since a brain's copy was last brought up to date into that copy, reports each change as a recommendation carrying the template's text, and leaves every change to the owner in the walk-through. Release notes then never carry upgrade steps.

## Context

See `MBT_TEMPLATE_DRIFT_FINDINGS.md` in this directory for the decision record, the evidence and the alternatives considered. `MBT_TEMPLATE_DRIFT_EXPERIMENT.py` in this directory runs the comparison by script against a given base; `MBT_TEMPLATE_DRIFT_INFER.py` infers the base by check 10's rule, then merges.

The procedure files and their templates:

| Brain's file | Template |
|---|---|
| `<HUB>_SESSION_CLOSEOUT.md` | `templates/SESSION_CLOSEOUT.md` |
| `<HUB>_WORK_SETUP.md` | `templates/WORK_SETUP.md`, plus the six `templates/work/` scaffolds it inlines |
| `<HUB>_WORK_CLOSEOUT.md` | `templates/WORK_CLOSEOUT.md` |
| `<HUB>_DREAM_CYCLE.md` | `templates/DREAM_CYCLE.md` |
| `<HUB>_ENFORCED_TERMS.md`: its rules, above the entries | `templates/ENFORCED_TERMS.md` |
| The brain's `CLAUDE.md`: the template's text in its Read Index and conventions sections | `templates/CLAUDE.md`, or `templates/LOBES_CLAUDE.md` for a multi-lobe brain |
| The hook's paragraphs, wherever they sit in each project repo's `AGENTS.md` or `CLAUDE.md` | `templates/PROJECT_HOOK.md` |
| The template's text in the brain's `README.md`, wherever it sits | `templates/README.md` |

`templates/AGENTS.md` is not in the table. Check 8 (loading reach) in `MBT_CHECK_BRAIN.md` owns the brain's `AGENTS.md`, the `AGENTS.md` exemptions in the brain's `CLAUDE.md` and dream cycle, and the hook's move from a project repo's `CLAUDE.md` into its `AGENTS.md`. The drift check reports none of these.

Knowledge files are never compared, and neither are a work item's docs. The scaffolds inlined in `<HUB>_WORK_SETUP.md` are procedure text and are compared against `templates/work/`. The template's sentence locating them in `templates/work/` is not drift, since a brain's copy inlines them by design.

## What changes

- `MBT_CHECK_BRAIN.md`, structural checks — a procedure-drift check. For each file in the table the brain holds:
  - Infer its base on every run, matching paragraphs word for word. Bound it by the oldest release whose dropped text the file still holds. Below that bound, take the candidate holding the most of the file's paragraphs; on a tie, the one holding the fewest paragraphs the file has no version of, verbatim or rewritten; then the newest.
  - Take the base and current templates from the install's git history (`git -C <install> show <ref>:templates/<file>`).
  - Normalize all three texts: fold the brain's lobespace back to `<LOBESPACE>`, read `<HUB>` as `<LOBESPACE>`, fill the display and lowercase names, and drop version lines.
  - Merge paragraph by paragraph. A paragraph only the template changed is a recommendation; one both changed is a conflict; one only the brain changed is not reported.
  - Split work setup's inlined scaffolds out by content, whatever their heading or fence, and merge each against its `templates/work/` file.
  - Match the hook's paragraphs by content in the project repo's instruction files.
  - Skip the paragraphs check 8 rewrites.
  - Treat a paragraph the base and current template hold and the brain lacks as the brain's own, without consulting the brain's history.
  - Skip a multi-lobe brain's dream cycle, which adapts the single-lobe template whole, and say so in the report.
  - Follow a template that no longer exists under the name this check gives it through the install's history, and recommend the matching rename of the brain's file.
  - Work in a temporary directory outside the brain and the install, even when reporting only, since `git merge-file` misreads pipes.
  - Without git history in the install, compare two ways and put every difference to the user.
- `MBT_CHECK_BRAIN.md`, report — procedure drift gets its own entry among the structural issues: each recommendation with a one-line reading of what the template's text changes, then each conflict with both texts. The report names the release the install has checked out, the newest its remote publishes, each file's base and any comparison skipped.
- `MBT_CHECK_BRAIN.md`, walk-through — check 8's fix runs before drift updates. An approved recommendation or a resolved conflict replaces that paragraph, filling placeholders as the brain's copy fills them around it. A declined one stays as it is, and nothing records the decision. A declined added paragraph goes quiet once the file takes a change from that release or a later one; a declined change to an existing paragraph comes back on every check.
- `MBT_CHECK_BRAIN.md`, check 8 — in a brain copied from the templates, the conventions fix takes the current template's wording for the paragraphs it changes, so the drift check finds them current rather than in conflict.
- `MBT_CREATE_BRAIN.md` — a staged `.gitkeep` in `archive/` as well as `working/` when either would be empty. `MBT_CHECK_BRAIN.md`'s structural checks flag an empty `archive/` or `working/` that git doesn't track, with the same fix, and tell the user the directory survives a clone once committed.
- `templates/DREAM_CYCLE.md` — fix a defect that the drift check would otherwise carry into every brain. Codex and OpenCode 2 each found it independently during the PR #19 retest. Check 6 exempts names carrying `<LOBESPACE>` as placeholder notation, but `create` substitutes the lobespace, so a seeded brain exempts its own real `working/` filenames and lets leaked references through. The exemption becomes "a name carrying an angle-bracketed variable such as `<WORK>`", which survives `create`'s substitution and still exempts `working/ORCHARD_<WORK>_PLAN.md` while flagging `working/ORCHARD_FOO_PLAN.md`. Its checks 1 and 4 also flag the rows the entrypoint template stages in comments; Rob kept that, on 2026-11-06, rather than add rules for docs a brain may add later.
- `templates/DREAM_CYCLE.md`, Phase 5 — with no enforced terms file, the drift pass still proposes a term by "the enforced terms file's rule for adding an entry", which doesn't exist. `MBT_CHECK_BRAIN.md` falls back to `templates/ENFORCED_TERMS.md`, but a brain's dream cycle never sees the toolkit, so the rule must be stated in the dream cycle itself.
- `templates/DREAM_CYCLE.md`, Phase 4 — extraction promotes "discoveries that reframed the problem" to FINDINGS, which the template's exemption table defines as implementation decisions that did not shape the approach. Extraction must route by that definition.
- `MBT_DREAM_CYCLE.md` — the same Phase 4 routing in this brain's own dream cycle.
- `templates/CLAUDE.md`, `templates/LOBES_CLAUDE.md`, `CLAUDE.md` — "LOG files are never archived" contradicts work closeout's retire step, which moves a work item's working log to `archive/`. Scope the rule to canonical logs.
- `MBT_PATTERN.md` — the distinction between knowledge files and procedure files, which the pattern does not yet draw.
- `README.md`, `MBT_FINDINGS.md` — the install lines check out the newest release tag instead of tracking `main`, so users run only released code, and only after a successful fetch or clone. Rob's call.
- `templates/DREAM_CYCLE.md`, Phase 1 — a toolkit-release check: when a clone at a standard install path has checked out an older release than its remote publishes, the cycle adds a needs-human-decision item to update the toolkit and run `check`. It reads nothing about the brain's own files. Rob's call, over a prompt at session start or none.

## Interaction with existing docs

| Existing doc | Interaction | Risk |
|---|---|---|
| `MBT_CHECK_BRAIN.md` check 8 | Owns the loading path through `AGENTS.md`, including paragraphs of the brain's `CLAUDE.md`, its dream cycle and the project hook that the drift check also compares | If check 8's fix words a paragraph differently from the current template, the next drift check reports it as a conflict |
| `MBT_CREATE_BRAIN.md` placeholder rules | The walk-through fills placeholders in the template text it applies | Filling by the brain's own surrounding text can't follow a rule the copy never exercised; a new placeholder needs the user |
| `SKILL.md` path rule | Templates and their history resolve against the install | A stale install compares against stale templates; the report states the install's release and the remote's newest, and says when the remote's answer is missing |
| `templates/DREAM_CYCLE.md` | A brain's own dream cycle compares a standard-path clone's release with its remote's newest | A toolkit installed elsewhere, or a machine offline, never prompts a `check` |
| `MBT_DREAM_CYCLE.md` | This brain's own maintenance docs differ from their templates by design, since its subject is the pattern | Running the drift check on the toolkit reports its own docs as drift |
| Release notes | No longer carry upgrade steps | A change `check` can't detect would have no channel at all; history covers a renamed or moved template, but not a convention moved into a file with no template |

## Testing approach

Each test also runs `MBT_TEMPLATE_DRIFT_EXPERIMENT.py` against the same brain and base. The agent's recommendations and conflicts must match the script's, file by file.

1. **0.72 fixture.** Seed a brain in a scratch directory from the 0.72 templates with the PR #19 retest's `seed.sh`, pointed at tag 0.72 and extended with work setup (scaffolds inlined) and work closeout. Run `check` from `main`.
   - Check 8 moves the hook into the project repo's `AGENTS.md`, adds the brain-side `AGENTS.md` and its exemptions, and keeps the hook's work-item block.
   - The drift check reports the rest of 0.73's procedure changes once each, with no conflicts: the session-ID variables and harness-neutral wording in session closeout and the README, work setup's audit and alignment changes, the retire-move rule in `CLAUDE.md` and work closeout, and the dream cycle's naming exemptions read from `CLAUDE.md` and its read-only subagent wording. It reports nothing check 8 handled.
   - A second `check` reports no drift.

   Every existing brain needs this upgrade for 0.73, so it is the test that matters most.
2. **0.70 fixture.** The same, seeded at tag 0.70. It reports each change to a procedure template between 0.70 and `main` once, with the template's text, and no knowledge file. The walk-through, approving every update, leaves the filled-in placeholders and work-item block intact.
3. **lamarr-brain**, seeded from 0.71. `check` proposes 0.71 as the base. It reports the upstream changes to session closeout, work setup's procedure, work closeout, `CLAUDE.md` and the README with no conflicts, nothing for the scaffolds, and none of the brain's adaptations. The hook is split across sections of the project's `CLAUDE.md`, and has no drift.
4. **mini-subtitle-wizard-brain** (https://codeberg.org/kolin-newby/mini-subtitle-wizard-brain), seeded from 0.71 by an outside author. `check` reports the same upstream changes, and one conflict in work setup step 3. The deviations its first log entry records survive, as does its Codeberg burndown rule. The brain lives in `~/mini-brains/`, so the user names its project repo (https://codeberg.org/kolin-newby/subtitle-wizard) for check 8 and the hook.
5. **virtual-view-brain**, predating 0.70. Session closeout fits 0.70 and takes its upstream changes cleanly. Work setup, work closeout, `CLAUDE.md` and the README raise the conflicts the script finds, each put to the owner with both texts. The brain has no dream cycle.

6. **Added paragraph.** A multi-lobe `CLAUDE.md` seeded from the 0.71 `LOBES_CLAUDE.md`. `check` infers 0.71 and recommends 0.72's "A child works within its ancestors' choices" paragraph.
7. **Partly applied update.** A dream cycle seeded from 0.72 with every other 0.72-to-`main` change applied by hand. `check` infers 0.72, recommends the missed changes, and reports none of the applied ones.
8. **Declines and check 9.** The fixture from test 6 with an empty, untracked `archive/`. The walk-through approves check 9's fix, declines the added `CLAUDE.md` paragraph and the session-closeout session-ID rewrite, and takes the rest. A second `check` reports no check 9 entry, does not report or mention the declined paragraph, and recommends the declined rewrite again.

After each walk-through, a second `check` reports nothing for a declined added paragraph once the file took a later change, and reports a declined rewrite again.

## Implementation sequence

1. Fix the `templates/DREAM_CYCLE.md` leakage defect and its Phase 4 and Phase 5 wording, and the LOG-archiving rule. Done on branch `template-drift`, with the matching Phase 4 fix in `MBT_DREAM_CYCLE.md`. Skips for HTML-commented rows were added to check, the dream cycle and work closeout, then reverted at Rob's direction.
2. Add the `archive/` `.gitkeep` to `create`, and check 9, tracked directories. Done on branch `template-drift`. Per-file stamps were built here too, then removed at Rob's direction in favor of inferring each file's base.
3. Write the drift check, report entry and walk-through step in `MBT_CHECK_BRAIN.md`, and align check 8's conventions fix with the current template's wording. Done on branch `template-drift` as check 10, with check 8's split-hook move, the release pin, the dream cycle's release check and the pattern's file kinds; reworked to infer bases once the stamps went.
4. Run the fixture tests, then the three existing brains. Done on 2026-11-06 in Claude Code 2.1.319, headless, against `3c8f54a` on scratch copies, each graded on disk against `MBT_TEMPLATE_DRIFT_EXPERIMENT.py`. The 0.72 and 0.70 fixtures, lamarr, subwiz and virtual-view-brain all ended with every procedure file current apart from the brain's own changes. Subwiz raised its one expected conflict, lamarr's declined README paragraph stayed declined, and second checks on the 0.72 fixture and lamarr reported nothing and changed nothing. Earlier rounds found that counting differing lines inferred the wrong base for adapted hooks, which led to the switch to matching paragraphs, and that a report-only run needs a temporary directory. The 0.70 fixture and virtual-view-brain ran before that switch; their brain-side results do not depend on it.
5. Open the PR. Done: PR #22, one squashed commit (`dfea6c0`) holding only the toolkit's files.
6. Address the PR #22 review. Done on 2026-11-07 as `bb2f6b9` on branch `template-drift`: the bounded base rule, the release in the report, the multi-lobe dream-cycle skip, check 9's staged `.gitkeep`, the install lines' `&&`, and the findings and forward-reference wording. Tests 6–8 passed headless in Claude Code 2.1.319 against a scratch install of the branch, each graded on disk against `MBT_TEMPLATE_DRIFT_INFER.py`. The new rule leaves lamarr's bases unchanged and infers 0.70 for virtual-view-brain's three hooks.

## Scope boundary — what this does NOT include

- Knowledge files written to an older standard, which `check`'s substance checks already cover.
- Updating anything without the owner's approval.
- The toolkit's own maintenance docs, which differ from the templates by design.

## Open issues

1. Overlaps with open work items. WORK_PLACEMENT and REHOMING both change `templates/WORK_SETUP.md`. MULTI_LOBE_DREAM redesigns `templates/DREAM_CYCLE.md` and requires `MBT_CHECK_BRAIN.md` and the dream cycle to flag the same things. Whichever lands after this item changes what its tests expect.
