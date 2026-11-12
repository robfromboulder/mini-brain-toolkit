# Brain Split: Decision Record

## Problem

The toolkit repo holds two things: the product, which is the skill, its procedures and the templates they seed, and the toolkit's own mini-brain, which is its scope, approach, findings, logs, dream cycle, examples, testing, research, `tests/`, `working/` and `archive/`. Every install is a clone of the whole repo, so every install carries the brain. `SKILL.md` and the procedures read about 30 of the 102 files tracked at 0.73.

The brain in an install is more than clutter. `MBT_LOG.md` is 369 KiB and append-only, over the 256 KiB per-file limit of Anthropic's plugin directory and growing. `MBT_DREAM_CYCLE.md`, `MBT_SESSION_CLOSEOUT.md` and the entrypoint are instructions written to drive an agent, sitting beside `SKILL.md`, whose path rule resolves every `MBT_*.md` against the install. The repo also breaks the pattern's own second principle: a brain "must not be embedded in, versioned with, or shipped as part of the product."

Housing the brain in its product made sense while the brain was the toolkit's runtime surface: the way to use the pattern was to read the toolkit's files, so the toolkit being a brain was the demonstration. The skill is now the only way to use the toolkit, and this brain doesn't use it. It follows the work-item templates in place, where a brain made by `create` gets its procedures instantiated and kept current by `check`.

## Preferred approach: the brain moves to `mbt-brain`

The brain moves to the public repo `mbt-brain`, beside the toolkit repo. The toolkit repo becomes a project repo like any other: the product, plus a project hook that loads the brain. The README stays the toolkit's only front door; the brain repo is linked from it for readers who want the design.

| Stays in `mini-brain-toolkit` | Moves to `mbt-brain` |
|---|---|
| `SKILL.md`, `agents/openai.yaml` | `MBT_SCOPE.md`, `MBT_APPROACH.md`, `MBT_FINDINGS.md`, `MBT_ENFORCED_TERMS.md` |
| `MBT_PATTERN.md`, `MBT_LOBES.md` | `MBT_LOG.md`, `MBT_DREAM_LOG.md` |
| `MBT_CREATE_BRAIN.md`, `MBT_CHECK_BRAIN.md` | `MBT_SESSION_CLOSEOUT.md`, `MBT_DREAM_CYCLE.md` |
| `templates/` | `MBT_EXAMPLES.md`, `MBT_TESTING.md`, `tests/` |
| `README.md`, `LICENSE`, `CONTRIBUTING.md`, `.github/images/`, `.gitignore` | `MBT_RESEARCH.md`, `MBT_COMPARABLES.md`, `MBT_BIOLOGY.md` |
| `CLAUDE.md`, `AGENTS.md`, rewritten as a project repo's, with the hook in `AGENTS.md` | `working/`, `archive/` |
| | `CLAUDE.md` (the entrypoint, rewritten for the brain alone), `AGENTS.md` |
| | New: `README.md` from the template, merged into the repo's existing one; `MBT_WORK_SETUP.md` and `MBT_WORK_CLOSEOUT.md` instantiated from the templates |

- **No new tooling.** No manifest, release script, branch or ruleset; the separation is the pattern's own.
- **Installs migrate unaided.** The README's install line is unchanged, and the first tag after the split drops the brain from an unedited install when it updates.
- **`check` keeps its history.** `templates/` stays in the product repo with its full history, which the drift check reads from the install.
- **The toolkit dogfoods the product as users do.** The brain is loaded through the hook, kept by instantiated procedures, and checked by `check`; whatever is awkward about that is felt here first.
- **One front door.** Stars, issues, releases and install lines stay on `mini-brain-toolkit`.
- **The best example, not the self-example.** The toolkit stops being a brain and becomes the best-kept example of a project with one: its instruction files mirror the exemplar brains' project and brain repos, and its product files are skill material, carrying no version headers.

### Evidence

Tested on 2026-11-11 against scratch copies, not the real repos.

- **The install line moves an install unaided.** A scratch remote held 0.73 and a 0.74 cut from it without the brain. The README's line, unchanged, took a clean 0.73 install to 0.74: 102 tracked files became 39, nothing of the brain remained, and 17 commits changing `templates/SESSION_CLOSEOUT.md` stayed reachable for check 10. An install with a local edit to a deleted file stopped on 0.73 with git's "would be overwritten" error and exit 1, as `MBT_FINDINGS.md` records for any edited install. An untracked file in `working/` survived the update, harmlessly.
- **The narrowed path rule works in an agent run.** A headless, report-only `check` in Claude Code ran on a scratch copy of the brain from a scratch product carrying decision 2's path rule. Every read of a brain `MBT_*.md` went to the brain and every product read to the install, and neither repo changed.
- **Check 10 compares the brain's procedures once it lacks `SKILL.md`.** The same run labelled `MBT_SESSION_CLOSEOUT.md`'s seven departures from its template as own edits, among them the missing current-branch signal. It found `MBT_DREAM_CYCLE.md` missing two template parts that apply once the brain consumes the product: the Toolkit release check and the Scope accuracy phase. Its labels are approximate, because the run's tool list denied the temporary copies check 10 makes.
- **The hook template's back-reference rule collides with decision 5.** The same run flagged "Never cite mini-brain docs (`<HUB>_*`…) from code" against product files citing product `MBT_` files.

### One repo per lifecycle

The product is tagged, released, installed and reviewed by PR; the brain is committed to `main`, never released, and opens PRs only for work-item closeouts. Git and the tools around it treat a repo as one thing with one lifecycle: a clone, a plugin marketplace, skills.sh and GitHub's landing page each take a single default branch or tag stream, and stars, issues and license detection attach to the repo. Two lifecycles in one repo surfaced as rules special to this repo: the version-header and naming exemptions, "no working files in a PR", and the path-rule collision. Every branch-based separation weighed here then needed tooling to teach each consumer which part to take, and eventually to pull the two histories apart again. Separate repos cost a one-time setup, which `create` already performs; separating within one repo costs tooling and conventions for as long as the repo lives. Separate repos won without being presupposed: the release branch was the first recommendation, and lost on what it took to build.

## Alternatives considered

- **A generated release branch from an opt-in manifest, as the default branch.** A release script would build product-only commits onto `release`, with two parents each to keep template history reachable for `check`. Rejected by Rob: a manifest, a script, two-parent commits, a ruleset and a default-branch switch, all specific to this repo, weaken the toolkit as an example of its own pattern.
- **A product-only `mini-brain-skills` repo generated at release.** Keeps the toolkit repo unchanged. Rejected: keeping `check`'s template history needs a filtered mirror of `main`, and `git filter-repo` can't be assumed installed; existing installs would need their origin repointed and tags force-fetched; and stars, issues and README would split across two front doors, which Rob ruled out.
- **The product in a subdirectory.** A clone puts the repo root in the skills directory, so the install line would need a sparse checkout and a symlink; the skill-install work rejected a `skill/` root for this reason.
- **A release zip installed by `curl`, or GitHub Packages.** Plugin marketplaces and skills.sh install from git refs, not archives or packages; GitHub's npm registry needs a token even for public installs, and its container registry needs `docker` or `oras`.
- **`export-ignore` in `.gitattributes`.** Filters only `git archive`, which no install uses.
- **Log rotation alone.** Fixes `MBT_LOG.md`'s size, and may be worth having for every brain, but leaves the brain's procedures in every install and the toolkit outside its own pattern.

## What this doesn't solve

- **A change and its reasons land in two repos.** Product edits are PRs to the toolkit; decisions, logs and work items are commits and closeout PRs to the brain. That is every user's workflow, not a cost the toolkit can avoid.
- **The brain's logs still grow without bound.** They no longer ship, but the brain still loads them.
- **History before the split stays in the toolkit repo.** The brain repo starts from an import commit.

## Reversals

- `MBT_APPROACH.md`, "Dogfood the pattern": "The toolkit is itself a mini-brain," and the paragraph on two kinds of top-level knowledge file coexisting. Dogfooding becomes the toolkit project having a brain, not the toolkit being one.
- `MBT_DREAM_CYCLE.md`: "This brain has no product code — its "code" is its own teaching artifacts, and its `APPROACH` commits it to *being* the pattern it defines." The product becomes a sibling repo whose code the cycle verifies.
- `CLAUDE.md`: the binding that has this brain follow the work-item templates in place rather than keep instantiated procedures; the Product block of the read index; `SKILL.md`'s naming and version-header exemptions; the `MBT_PATTERN.md` and `MBT_LOBES.md` rows of the declared reference exemptions; the maintenance-doc boundaries for `SKILL.md` and the two procedures; the version-header rule, for the four product files that leave its reach; and the "no working files in a PR" convention.
- `MBT_FINDINGS.md`, on `SKILL.md` forbidding writes under the install: it calls a copy of the toolkit "the one target that shares the `MBT` lobespace." `mbt-brain` becomes a second, and a routine one.
