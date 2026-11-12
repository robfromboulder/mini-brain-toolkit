# Distribution: Decision Record

## Problem

A user finds the toolkit only by finding its GitHub repo, and installs it only by copying a `git clone` line from the README. The skill-install work named this gap and left it open: the skill appears in a harness's command list only after it is installed. Promotion through LinkedIn reaches people once per post. A listing in a directory or registry that agent users already browse keeps reaching new users without further effort.

The toolkit is free and Apache-2.0, and stays that way. A listing must reach users commercial and personal alike, and must not put a price, a revenue share or a sign-up between a user and the toolkit.

## Channel facts

Read from each channel's own pages on 2026-11-11.

| Channel | Reach | How to get listed | Gate | Fit |
|---|---|---|---|---|
| Anthropic plugin directory (`anthropics/claude-plugins-community`) | Claude Code and Cowork users; `claude plugin install <name>@claude-community` | "Plugin bundle" from a public GitHub repo at the portal claude.ai/directory/manage; the repo is a read-only mirror that auto-closes PRs | `.claude-plugin/plugin.json`; a `LICENSE` and a README of 40+ words; automated scan, then a person reviews; a paid claude.ai plan to submit; 512 files at most and every non-image file under 256 KiB, else held for a reviewer | Needs plugin packaging; `MBT_LOG.md` (369 KiB) exceeds the per-file limit |
| Anthropic official marketplace (`anthropics/claude-plugins-official`) | Same, curated; auto-updates on by default | The repo README invites third-party submissions through the same form; the Claude Code docs say it takes none through the portal | Anthropic's discretion | Not something to plan around |
| OpenAI plugin directory | ChatGPT and Codex users, one directory | Submission portal on developers.openai.com | `.codex-plugin/plugin.json`; review before publication; skill-only plugins accepted per a third-party guide, unconfirmed | Codex is a supported harness; second manifest |
| skills.sh (`vercel-labs/skills` CLI) | About 20 harnesses, Claude Code, Codex, Cursor, Copilot and Gemini among them; install leaderboard | Automatic: the leaderboard ranks skills by the CLI's anonymous install telemetry; no submission | None | Discovers a root `SKILL.md`; pins a tag with `owner/repo@tag`; symlinks agent dirs to one canonical copy; skips only `.git` and a few cache folders, so it installs the whole repo |
| hesreallyhim/awesome-claude-code | Largest Claude Code list | Web UI issue form only, submitted by a human; no PRs, no `gh` | 14 days old with active development, or 100 stars; one resource at a time; one-line description | Qualifies now |
| travisvn/awesome-claude-skills | Claude Code skills list | PR | 10 stars; PRs written or submitted with AI assistance are closed; non-promotional | After 10 stars, written by Rob |
| ComposioHQ/awesome-claude-skills | Largest skills list by stars | PR that adds the skill's folder to their repo | Tested skill, `name` and `description` frontmatter | Vendors a copy |
| Agensi (agensi.io) | Marketplace across SKILL.md harnesses; contacted Rob | Zip upload through the creator dashboard; each new version re-uploaded and re-reviewed | Listing free is allowed; non-exclusive license to Agensi; skills load only through Agensi's connector, behind a free Agensi account; buyer terms forbid copying or redistributing a skill | Fails the free-and-open constraint |
| Gemini CLI extension gallery | Gemini CLI users | Automatic: indexes public repos with the `gemini-cli-extension` topic and a root `gemini-extension.json`, on a tagged release | Validation | Gemini CLI is not a harness the toolkit supports |
| Cursor marketplace, cursor.directory | Cursor users | Publish form at cursor.com/marketplace/publish; cursor.directory reviewed separately | `.cursor-plugin/plugin.json`; manual review, reported slow | Cursor is not a harness the toolkit supports |
| Crawled registries (skills.re, skillsmd.dev, askill.sh and others) | Small, overlapping | URL submission, or crawling GitHub | None | GitHub topics reach them |

## Preferred approach: list where listings persist, install from the repo

List the toolkit in the channels that keep surfacing it to agent users, ordered by reach over effort: Anthropic's plugin directory, then skills.sh, then the awesome lists as their gates open. Every listing installs from or points at this repo's tagged releases, so the repo stays the single source and a listing never serves a copy that drifts behind a release.

| Aspect | Detail |
|---|---|
| Source of truth | This repo's tags; no vendored copies |
| License | Apache-2.0, unchanged; it already permits every listing here |
| Price | Free in every channel |
| PR scope | Packaging and README install lines; submissions and repo topics happen off-PR |

- **Reach** — the plugin directory and skills.sh are where Claude Code and cross-harness users search for skills, so each adds an audience the README alone does not reach.
- **Durability** — directory search and list backlinks keep working after a post's attention fades, and LinkedIn posts can then carry a one-line install command.
- **No drift** — a listing that installs from the repo picks up each release; one that holds a copy needs a resubmission per release.

### Plugin packaging, reopened

`MBT_FINDINGS.md` records plugin packaging as rejected: Rob chose the unnamespaced `/mini-brain-toolkit create` and the git-based update path over a plugin's per-command menu entries. That decision weighed packaging by the experience of a user who already had the repo. Distribution was not on the table. Anthropic's directory takes only plugins, so reach through it is a cost of the rejection that the decision never counted. The namespacing claim it rested on was also never verified against Claude Code's docs. This item reopens the choice with reach as a third factor beside command syntax and update path.

Claude Code's plugin docs, read 2026-11-11, settle most of what the rejection left open:

- **Layout costs nothing.** A plugin whose root holds `SKILL.md`, with no `skills/` directory and no `skills` key, loads as a single skill. The install copies the whole plugin directory to a versioned cache, so `MBT_*.md` and `templates/` stay beside `SKILL.md` and its path rule holds unchanged. A `marketplace.json` in this repo can list the repo itself with `"source": "./"`.
- **The command is namespaced.** Every plugin component is named `/plugin-name:skill-name`, and a root `SKILL.md` takes its skill name from frontmatter `name`, so the command would read `/mini-brain-toolkit:mini-brain-toolkit create` unless the plugin or skill is renamed. The docs say the bare name also invokes a plugin skill "unless another command already uses that name," but state it only for a skill whose `name` is overridden, so whether `/mini-brain-toolkit create` survives is a test, not a fact.
- **Both installs coexist.** A plain skill in `~/.claude/skills` and a plugin skill of the same name both load, because the plugin's is namespaced. A user with both sees two entries, and the bare name goes to the plain skill.
- **Releases pin cleanly.** A `version` in `plugin.json` pins the plugin until it changes, and a marketplace entry can pin a tag with `ref`. Auto-update is off for every marketplace but Anthropic's official ones.

What remains of the rejection is command syntax alone, and the directory's reach is what weighs against it.

## Alternatives considered

- **ComposioHQ/awesome-claude-skills.** Rejected: contributing copies the skill's folder into their repo, and the skill depends on the whole toolkit at a tagged release, so the copy would drift.
- **Submitting to each crawled registry.** Rejected: their audiences are small and overlap skills.sh, and GitHub topics reach the crawlers without a submission each.
- **Planning around the official marketplace.** Rejected: it is curated at Anthropic's discretion; the community directory is the route a submitter controls.
- **A paid or revenue-sharing listing.** Rejected by Rob: the toolkit is not revenue-bearing.
- **Gemini CLI and Cursor listings.** Deferred: a listing for a harness promises that the brains create produces load there, and neither harness has been tested; supporting one is its own work item.

## What this doesn't solve

- **Listings carry no context.** A one-line directory entry cannot explain what a mini-brain is; the README still has to convert a visitor.
- **Gated lists wait on stars.** travisvn needs 10 and hesreallyhim's fallback needs 100, so their timing depends on promotion this item doesn't do.
- **A marketplace that hosts its own copy.** Any channel that takes an upload rather than installing from the repo, as Agensi does, serves whatever was last uploaded.

## Reversals

Conditional on plugin packaging landing: `MBT_FINDINGS.md`, the finding that the toolkit installs as a skill whose root is the repository, says a plugin lost to the root `SKILL.md`. If this item ships a plugin manifest, that finding is reversed in part and must be reconciled at closeout, including its unverified namespacing claim.
