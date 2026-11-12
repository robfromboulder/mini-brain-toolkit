# Brain Split: Implementation Plan

## Objective

Move the toolkit's own mini-brain out of the product into a public `mini-mbt-brain` repo beside it, and make `mini-brain-toolkit` a project repo whose hook loads that brain. Installs then carry only the product, with the README's install line unchanged. No new tooling, no change to the install line, no second front door.

## Context

See `MBT_BRAIN_SPLIT_FINDINGS.md` in this directory for the decision record and alternatives considered.

Key references in the owning lobe:
- `MBT_SCOPE.md` — problem space this fits into
- `MBT_FINDINGS.md` — the install-line, drift-history and install-guard findings this item must keep true
- `MBT_APPROACH.md` — the dogfooding approach this item reverses

## What changes

**`mini-mbt-brain` (new, public)**
- Import commit: every existing file in FINDINGS' "Moves" column as of a named toolkit commit, with that commit in the message.
- `CLAUDE.md` — the entrypoint, in the exemplar brains' shape (decision 1): the read index without the Product block, the file conventions that govern brain files, the writing rules, the one-namespace rule (decision 5), and commit conventions per decision 4. Removed: the template binding for work items; `SKILL.md` from the naming and version-header exemptions; the `MBT_PATTERN.md` and `MBT_LOBES.md` rows of the declared reference exemptions; `SKILL.md` and the two procedures from the maintenance-doc boundaries.
- `AGENTS.md` — one line pointing at `CLAUDE.md`.
- `README.md` — from `templates/README.md`.
- `MBT_WORK_SETUP.md`, `MBT_WORK_CLOSEOUT.md` — instantiated from the templates. `check` scores a brain without them as not having adopted them.
- `MBT_APPROACH.md`, `MBT_DREAM_CYCLE.md`, `MBT_FINDINGS.md` — the reversals.
- `MBT_DREAM_CYCLE.md`, `MBT_TESTING.md` — the product is a sibling checkout, `../mini-brain-toolkit`, not this repo.
- `tests/` — the usage lines that assume the scripts sit inside the toolkit checkout; the scripts already take its path as an argument.

**`mini-brain-toolkit` (PR)**
- Delete every file that moved.
- `AGENTS.md` — the hook's "Working in the mini-brain" section from `templates/PROJECT_HOOK.md`, with the clone name adjusted to `mini-mbt-brain`.
- `CLAUDE.md` — an `@AGENTS.md` line, then the exemplar project repos' sections (decision 1): a one-line description, branching and rebase-only merges, the writing rules, no AI attribution, and the one-namespace rule (decision 5).
- `SKILL.md` — the path rule names the files the install holds (decision 2).
- `MBT_PATTERN.md`, `MBT_LOBES.md`, `MBT_CREATE_BRAIN.md`, `MBT_CHECK_BRAIN.md` — version headers removed (decision 3).
- `README.md` — links to RESEARCH and BIOLOGY point into `mini-mbt-brain`; any wording that calls the toolkit a brain.
- `CONTRIBUTING.md` — the brain repo, and where decisions and work items go.

**Off-PR**
- Create the GitHub repo; tag the first product release after the merge.

## Interaction with existing code

| Existing code | Interaction | Risk |
|---|---|---|
| `SKILL.md` path rule | Resolves every `MBT_*.md` against the install | `check` on `mini-mbt-brain` reads the install for the brain's own `MBT_SESSION_CLOSEOUT.md` and other procedures |
| `MBT_CHECK_BRAIN.md` drift check | Reads template history from the install | None while `templates/` stays put with its history |
| `README.md` install line | Checks out the newest tag | A full install updating to the first post-split tag must end with only product files |
| `templates/DREAM_CYCLE.md` release check | Reads the install's tags | None |
| Open items in `working/` | Move with the brain | MULTI_LOBE_DREAM edits `MBT_TESTING.md` and product files, so its change splits across both repos |
| Brain edits on `main` during the split | The import is a snapshot | An edit to a moving file after the import commit is lost |

## Testing approach

Automated: `tests/MBT_SHELL_CHECKS.sh`'s install-line scenario, run from the brain against a scratch remote of the product, adds an upgrade from 0.73 to a post-split tag and asserts the install holds only product files. The existing scripts stay green from their new home. Manual steps live in `MBT_BRAIN_SPLIT_TESTING.md`.

## Implementation sequence

1. Compare the drafted instruction files with lamarr, lamarr-brain, nebula and mini-nebula-brain section by section.
2. Freeze brain edits on `main`; commit the open working docs.
3. Create `mini-mbt-brain`; import at a named commit; write its entrypoint, README and pointer.
4. Open the product PR: deletions, hook, path rule, version headers, README, CONTRIBUTING.
5. Run `check` on `mini-mbt-brain` from an install of the PR branch, not 0.73, whose path rule would send the brain's own `MBT_*.md` reads to the install; apply what it recommends.
6. Run the acceptance tests from the brain against the PR branch; merge; tag.
7. Update a real 0.73 install with the unchanged README line.

## Scope boundary — what this does NOT include

- Listings, plugin manifests and other channels, which belong to DISTRIBUTION.
- Log rotation or any other change to how logs grow.
- Renaming the `MBT` lobespace or any `MBT_` file (decision 5).
- Rewriting the brain's history into the new repo.

## Decisions

Settled by Rob on 2026-11-11. Consequences Claude drew from them are marked *(Claude)*.

1. **Instruction files mirror the exemplar brains.** The project repos lamarr, nebula, viewzoo and viewmapper share a `CLAUDE.md` shape: a one-line description, the hook, the project's own operating sections, then Writing Docs and Instructions and Commit Conventions. The brain repos lamarr-brain, mini-nebula-brain and virtual-view-brain share Read Index, File Conventions and Writing Docs and Instructions, and the latter two add Commit Conventions. The toolkit and `mini-mbt-brain` take these shapes. The exemplars hold the hook in `CLAUDE.md`, but the current hook template puts it in `AGENTS.md` imported by `CLAUDE.md`; the toolkit follows the template, since it is the example `create` produces today. Rules both repos follow, like the writing rules and no AI attribution, are repeated in each because these projects happen to share them, not added to the templates, which require no such convention of downstream brains.
2. **`SKILL.md`'s path rule names the files the install holds.** It resolves `MBT_PATTERN.md`, `MBT_LOBES.md`, `MBT_CREATE_BRAIN.md`, `MBT_CHECK_BRAIN.md` and `templates/` against the install, and every other path against the target, so `mini-mbt-brain`'s own `MBT_*.md` files resolve in the brain. The lobespace is not renamed.
3. **Product files drop their version headers.** The toolkit repo's files are skill material, not brain material, so they carry no `> V<N>` line and rely on git history and release tags. *(Claude)* Templates keep their `> V1, <date>.` lines, because those are what a seeded brain starts from.
4. **The brain commits to `main`; work-item closeouts go through PRs.** Session closeouts push straight to `mini-mbt-brain`'s `main`, as in lamarr's hook. *(Claude)* "No working files in a PR" retires: the product repo has no `working/`, and the brain's closeout PRs move working files by design.
5. **`MBT_` is one namespace across both repos.** Product files keep their `MBT_` names, for continuity and because the prefix marks a single namespace however the files are split. Each `MBT_` name lives in exactly one repo and is never duplicated in the other. *(Claude)* Both repos' `CLAUDE.md` state the rule, and it is what keeps decision 2's path rule unambiguous: no brain file can share a product file's name.

## Open issues

1. **Alignment.** DISTRIBUTION depends on this item: its open issue on `MBT_LOG.md` and the plugin's per-file limit resolves here. MULTI_LOBE_DREAM's change spans both repos after the split. WORK_PLACEMENT edits `templates/WORK_SETUP.md` and `templates/WORK_CLOSEOUT.md`, which the brain will instantiate rather than follow in place, so it lands in the brain through `check`. MIGRATIONS touches only product files.
