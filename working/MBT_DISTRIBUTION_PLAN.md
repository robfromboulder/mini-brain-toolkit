# Distribution: Implementation Plan

## Objective

Get the toolkit listed in the channels that keep reaching agent users after one-time promotion: Anthropic's plugin directory, the skills.sh registry and the curated awesome lists, plus a reply to Agensi. Every listing installs from or points at this repo's tagged releases. Research comes first, because whether a plugin manifest lands decides what the PRs contain. No price, no revenue share, no vendored copies, no license change.

## Context

See `MBT_DISTRIBUTION_FINDINGS.md` in this directory for the decision record and alternatives considered.

Key references in the owning lobe:
- `MBT_SCOPE.md` — problem space this fits into
- `MBT_FINDINGS.md` — the skill-packaging finding this item reopens
- `MBT_APPROACH.md` — design constraints, including that a distributable CLI or IDE integration is not built here

## What changes

Stub until the plugin decision settles.

- `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` listing the repo as `"./"` — only if plugin packaging is chosen.
- `.codex-plugin/plugin.json` — only if the OpenAI directory takes a skill-only plugin.
- `CLAUDE.md` — the file-naming and version-header exemptions for any manifest file, as `SKILL.md` got.
- `MBT_DREAM_CYCLE.md` — its namespace check excludes any manifest file, as it does `SKILL.md`.
- `MBT_FINDINGS.md` — the skill-packaging finding, reconciled if a plugin lands.
- `README.md` — an install block for each new channel that installs cleanly.
- `MBT_TESTING.md` — at closeout, the install scenarios worth repeating at each release.

Off-PR actions, tracked in the burndown: GitHub repo topics, the plugin-directory submission, the awesome-list submissions and the Agensi reply.

## Interaction with existing code

| Existing code | Interaction | Risk |
|---|---|---|
| `SKILL.md` path rule | Resolves `MBT_*.md` and `templates/` against the directory holding `SKILL.md` | A plugin layout that moves `SKILL.md` into `skills/<name>/` breaks every procedure path |
| `README.md` install lines | Pin the latest tag | A plugin or skills.sh install that tracks `main` serves unreleased work |
| Root `SKILL.md` frontmatter | `disable-model-invocation: true`; Codex gets `agents/openai.yaml` | A channel that rewrites or ignores frontmatter auto-invokes the skill |
| `MBT_FINDINGS.md` skill-packaging finding | States a plugin lost | A plugin lands without that finding being reconciled |

## Testing approach

Automated: `claude plugin validate . --strict` if a manifest lands; the scripts in `tests/` stay green. Manual steps live in `MBT_DISTRIBUTION_TESTING.md`.

## Implementation sequence

1. Hands-on tests for open issues 1, 3 and 5: a local plugin marketplace from this repo, and a skills.sh install, each in Claude Code and Codex.
2. Decide plugin packaging and Agensi with Rob.
3. Add GitHub repo topics.
4. Land the packaging and README PR(s), then tag a release.
5. Submit to the plugin directory and hesreallyhim/awesome-claude-code from that release; reply to Agensi.
6. Submit to travisvn/awesome-claude-skills once the repo has 10 stars, written by Rob.

## Scope boundary — what this does NOT include

- Paid or revenue-sharing listings.
- Copies of the toolkit vendored into another repo.
- LinkedIn or other promotional content.
- A CLI or IDE integration.
- Changes to the create and check procedures.
- Submissions to registries that GitHub topics already reach.
- Listings for harnesses the toolkit doesn't support, Gemini CLI and Cursor among them.

## Open issues

1. **Plugin decision (Rob).** Docs settle layout, coexistence and pinning in the plugin's favor; command syntax is the remaining cost. Test what a root-`SKILL.md` plugin's command reads, bare and namespaced, before deciding.
2. **`MBT_LOG.md` over the directory's 256 KiB limit.** Resolved by BRAIN_SPLIT, which moves the brain to `mbt-brain` so installs carry only the product. This item depends on it: submissions follow the first release after the split.
3. **Skill directory at runtime.** `SKILL.md` resolves paths against "the directory that holds this file"; confirm the agent knows that directory in the plugin cache and in a skills.sh install, or switch to `${CLAUDE_SKILL_DIR}` where the harness supports it.
4. **Plugin version source.** A `version` in `plugin.json` must be bumped each release, beside the tag; a marketplace `ref` pins only `github`, `url` and `git-subdir` sources, not `"./"`.
5. **skills.sh contents and updates.** Confirm a `@<tag>` install copies the whole repo, keeps `agents/openai.yaml` for Codex, and what `skills update` does to a tag-pinned install. Then decide whether the README offers it as an install line.
6. **Agensi (Rob).** Its connector puts an Agensi account between a user and the toolkit, its buyer terms forbid the redistribution Apache-2.0 grants, and each release is a fresh upload and review. Recommend declining, or a reply pointing to the repo.
7. **OpenAI plugin directory.** Codex is a supported harness, so its directory is in reach; confirm from OpenAI's own submission page that skill-only plugins qualify and what `.codex-plugin/plugin.json` needs.
8. **Alignment.** No overlap with the open items MIGRATIONS, MULTI_LOBE_DREAM and WORK_PLACEMENT, which concern multi-lobe brains and the dream cycle and touch neither the install path nor the toolkit's `README.md`. MIGRATIONS edits `templates/README.md`, a brain's README, not this one.
