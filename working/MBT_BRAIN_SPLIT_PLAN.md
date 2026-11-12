# Brain Split: Implementation Plan

## Objective

Move the toolkit's own mini-brain out of the product into the public `mbt-brain` repo beside it, and make `mini-brain-toolkit` a project repo whose hook loads that brain. Installs then carry only the product, with the README's install line unchanged. No new tooling, no change to the install line, no second front door.

## Context

See `MBT_BRAIN_SPLIT_FINDINGS.md` in this directory for the decision record and alternatives considered.

Key references in the owning lobe:
- `MBT_SCOPE.md` — problem space this fits into
- `MBT_FINDINGS.md` — the install-line, drift-history and install-guard findings this item must keep true
- `MBT_APPROACH.md` — the dogfooding approach this item reverses

## What changes

**`mbt-brain` (exists, public; holds only GitHub's README)**
- Moved unchanged, in one import commit naming the toolkit commit it was cut from: `MBT_SCOPE.md`, `MBT_ENFORCED_TERMS.md`, `MBT_RESEARCH.md`, `MBT_COMPARABLES.md`, `MBT_BIOLOGY.md`, `MBT_EXAMPLES.md`, `MBT_LOG.md`, `MBT_DREAM_LOG.md`, `AGENTS.md` (already the one-line pointer at `CLAUDE.md`), `archive/`, `working/`.
- Minor edits after the move:
  - `MBT_FINDINGS.md` — the install-guard finding's reversal.
  - `MBT_APPROACH.md` — "Dogfood the pattern" rewritten.
  - `MBT_TESTING.md` — the commit under test is `../mini-brain-toolkit`'s `HEAD`; scenario 11 plants a defect other than a missing version header; scenario 10's toolkit-target case; the change-detection list.
  - `tests/` — the usage comments that assume the scripts sit inside the toolkit checkout; the scripts already take its path as an argument.
  - `MBT_SESSION_CLOSEOUT.md` — only if open issue 3 takes back the branch signal.
- Rewritten:
  - `CLAUDE.md` — the entrypoint, in the exemplar brains' shape (decision 1): the read index without the Product block, the file conventions that govern brain files, the writing rules, the one-namespace rule (decision 5), commit conventions per decision 4, and how product names (`MBT_PATTERN.md`, `templates/`) resolve in the sibling checkout. Removed: the template binding for work items; `SKILL.md` from the naming and version-header exemptions; the `MBT_PATTERN.md` and `MBT_LOBES.md` rows of the declared reference exemptions; `SKILL.md` and the two procedures from the maintenance-doc boundaries.
  - `MBT_DREAM_CYCLE.md` — per open issue 2.
- New:
  - `README.md` — `templates/README.md` merged into the existing README.
  - `MBT_WORK_SETUP.md`, `MBT_WORK_CLOSEOUT.md` — instantiated from the templates.

**`mini-brain-toolkit` (PR)**
- Unchanged: `agents/openai.yaml`, `templates/` (unless open issue 1 fixes the hook template), `LICENSE`, `.github/images/`, `.gitignore`.
- Deleted: every file that moved.
- Minor:
  - `SKILL.md` — the path rule names the files the install holds (decision 2).
  - `MBT_PATTERN.md`, `MBT_LOBES.md`, `MBT_CREATE_BRAIN.md`, `MBT_CHECK_BRAIN.md` — the version line only (decision 3).
  - `README.md` — the RESEARCH and BIOLOGY links point into `mbt-brain`.
  - `CONTRIBUTING.md` — two of its four paragraphs, which describe the read index and the session log, now in the brain.
- Rewritten:
  - `AGENTS.md` — the hook's "Working in the mini-brain" section from `templates/PROJECT_HOOK.md`, with the clone name `mbt-brain` and the back-reference rule per open issue 1.
  - `CLAUDE.md` — an `@AGENTS.md` line, then the exemplar project repos' sections (decision 1): a one-line description, branching and rebase-only merges, the writing rules, no AI attribution, and the one-namespace rule (decision 5).

**Off-PR**
- Tag the first product release after the merge.

## Interaction with existing code

| Existing code | Interaction | Risk |
|---|---|---|
| `SKILL.md` path rule, at 0.73 | Resolves every `MBT_*.md` against the install | `check` on `mbt-brain` from a 0.73 install reads the brain's own procedures from the install; run it from an install of the PR branch |
| `templates/PROJECT_HOOK.md` back-reference rule | "Never cite mini-brain docs (`<HUB>_*`…) from code" | Under decision 5, product files citing product `MBT_` files match the rule's wording (open issue 1) |
| `MBT_CHECK_BRAIN.md` check 10 | Skips only a target holding `SKILL.md` and `MBT_CHECK_BRAIN.md` | Runs on `mbt-brain`, comparing its `CLAUDE.md`, session closeout and dream cycle with the templates and reporting each departure as an own edit or a missing part |
| `MBT_CHECK_BRAIN.md` drift history | Reads template history from the install | None: confirmed reachable from a post-split tag |
| `README.md` install line | Checks out the newest tag | An install with a local edit to a deleted file stops on 0.73 with git's error, as for any edited install |
| `MBT_DREAM_CYCLE.md` Phases 1, 2 and 5 | Fix product files directly | The product repo takes changes only by PR (open issue 2) |
| Open items in `working/` | Move with the brain | MULTI_LOBE_DREAM edits `MBT_TESTING.md` and product files, so its change splits across both repos |
| Brain edits on `main` during the split | The import is a snapshot | An edit to a moving file after the import commit is lost |

## Testing approach

Automated: `tests/MBT_SHELL_CHECKS.sh`'s install-line scenario, run from the brain against a scratch remote of the product, adds an upgrade from 0.73 to a post-split tag and asserts the install holds only product files. The existing scripts stay green from their new home.

Rehearsal: before the product PR, a scratch split built from the drafted files, and a report-only `check` on the scratch brain from the scratch product, run with `MBT_TESTING.md`'s full Claude Code allow-list. The first rehearsal ran with a narrower one, which denied the temporary copies check 10 makes, so its drift labels fell back to searching template history.

Manual steps live in `MBT_BRAIN_SPLIT_TESTING.md`.

## Implementation sequence

1. Compare the drafted instruction files with lamarr, lamarr-brain, nebula and mini-nebula-brain section by section.
2. Settle open issues 1–4.
3. Rehearse the split, and gate on its report.
4. Freeze brain edits on `main`; commit the open working docs.
5. Import into `mbt-brain` at a named commit; write its entrypoint and pointer; merge its README; make the minor edits.
6. Open the product PR.
7. Run `check` on `mbt-brain` from an install of the PR branch; apply what it recommends.
8. Run the acceptance tests from the brain against the PR branch; merge; tag.
9. Rewrite the dream cycle in `mbt-brain`; it needs no product change, so it can follow the merge.
10. Update a real 0.73 install with the unchanged README line.

## Scope boundary — what this does NOT include

- Listings, plugin manifests and other channels, which belong to DISTRIBUTION.
- Log rotation or any other change to how logs grow.
- Renaming the `MBT` lobespace or any `MBT_` file (decision 5).
- Rewriting the brain's history into the new repo.
- What a routine `check` of the brain raises beyond the split: SCOPE's evidence, the design check's questions, pruning.

## Decisions

Settled by Rob on 2026-11-11. Consequences Claude drew from them are marked *(Claude)*.

1. **Instruction files mirror the exemplar brains.** The project repos lamarr, nebula, viewzoo and viewmapper share a `CLAUDE.md` shape: a one-line description, the hook, the project's own operating sections, then Writing Docs and Instructions and Commit Conventions. The brain repos lamarr-brain, mini-nebula-brain and virtual-view-brain share Read Index, File Conventions and Writing Docs and Instructions, and the latter two add Commit Conventions. The toolkit and `mbt-brain` take these shapes. The exemplars hold the hook in `CLAUDE.md`, but the current hook template puts it in `AGENTS.md` imported by `CLAUDE.md`; the toolkit follows the template, since it is the example `create` produces today. Rules both repos follow, like the writing rules and no AI attribution, are repeated in each because these projects happen to share them, not added to the templates, which require no such convention of downstream brains.
2. **`SKILL.md`'s path rule names the files the install holds.** It resolves `MBT_PATTERN.md`, `MBT_LOBES.md`, `MBT_CREATE_BRAIN.md`, `MBT_CHECK_BRAIN.md` and `templates/` against the install, and every other path against the target, so `mbt-brain`'s own `MBT_*.md` files resolve in the brain. The lobespace is not renamed.
3. **Product files drop their version headers.** The toolkit repo's files are skill material, not brain material, so they carry no `> V<N>` line and rely on git history and release tags. *(Claude)* Templates keep their `> V1, <date>.` lines, because those are what a seeded brain starts from.
4. **The brain commits to `main`; work-item closeouts go through PRs.** Session closeouts push straight to `mbt-brain`'s `main`, as in lamarr's hook. *(Claude)* "No working files in a PR" retires: the product repo has no `working/`, and the brain's closeout PRs move working files by design.
5. **`MBT_` is one namespace across both repos.** Product files keep their `MBT_` names, for continuity and because the prefix marks a single namespace however the files are split. Each `MBT_` name lives in exactly one repo and is never duplicated in the other. *(Claude)* Both repos' `CLAUDE.md` state the rule, and it is what keeps decision 2's path rule unambiguous: no brain file can share a product file's name.
6. **The brain repo is `mbt-brain`.** Not `create`'s `mini-<project>-brain`; the hook template allows a clone under another name.

## Open issues

1. **The hook's back-reference rule.** Under decision 5, `SKILL.md` citing `MBT_CHECK_BRAIN.md` matches the rule's wording, though it is product citing product. Adjust it as an own edit in the toolkit's `AGENTS.md`, or fix the template for any brain whose code shares the brain's prefix.
2. **The dream cycle.** Rebuild it from `templates/DREAM_CYCLE.md`, which gains the Toolkit release check and the Scope accuracy phase that now apply, and keep the research phases 3a and 3b; or repoint it, about 16 places plus Phase 2's framing. Either way Phases 1, 2 and 5 can no longer fix product files directly: they flag, or leave a branch and PR for review.
3. **Session closeout's branch signal.** The brain's copy lacks the template's current-branch signal. After the split, sessions run on the toolkit's feature branches, which the signal matches to work items.
4. **Reference rules for product files.** Orthogonal content, the declared exemptions (`MBT_LOBES.md` may cite `MBT_PATTERN.md`) and the maintenance-doc boundaries govern the product files today from the brain's `CLAUDE.md`. They move to the toolkit's `CLAUDE.md`, or lapse.
5. **Alignment.** DISTRIBUTION depends on this item: its open issue on `MBT_LOG.md` and the plugin's per-file limit resolves here. MULTI_LOBE_DREAM's change spans both repos after the split. WORK_PLACEMENT edits `templates/WORK_SETUP.md` and `templates/WORK_CLOSEOUT.md`, which the brain will instantiate rather than follow in place, so it lands in the brain through `check`. MIGRATIONS touches only product files.
