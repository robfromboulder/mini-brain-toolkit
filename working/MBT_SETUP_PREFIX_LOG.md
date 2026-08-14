# Enforce the Work-Item Token Prefix: Session Log

Running log of implementation sessions. Each session appends after a `---` separator.

The first entry, and every one after it, follows the entry format and content rules in `MBT_SESSION_CLOSEOUT.md` — that spec is the authority, not the prior entry, since a fresh LOG file has none to copy.

---

# Draft the §2 prefix-enforce edit (2026-08-13)

**Session ID**: `a347c9b8-a0fa-41e3-b521-807aaeb8fc35`

Rob's session, with Claude as co-author: turn the settled SETUP_PREFIX plan into a first draft of the actual `WORK_SETUP` edit. It landed — the branch exists and the §2 Slug paragraph now carries the name → slug → filename transform, dry-run against the three manual test cases and passing.

## Lineage

Opened by reading the full work-item set (PLAN, FINDINGS, CLAUDE runbook, LOG, TESTING) plus the real target, `templates/WORK_SETUP.md`. Rob first asked for a code-generation confidence rating; Claude gave 85/100 — the transform and acceptance cases are fully pinned, so the only residual risk was landing the wording under the repo's writing law without spawning a second copy of the prepend rule that §2's prefix-distinctness prose already implies.

Rob then had Claude cut the feature branch and start drafting. Branch `setup-prefix-enforce` was created to match the name the runbook already declared, rather than inventing one.

The edit rewrote the opening of the §2 Slug paragraph: it now states up front that every produced filename is the token-led compound, derives the slug from the work-item name, and resolves the handed-name ambiguity by stripping a leading owning-unit token before use so it can never double. A short placeholder example (`<TOKEN>_FOO` → files `<TOKEN>_FOO_*`, not the doubled form) carries the never-double point. The distinctness/longest-match prose was left verbatim.

## Decisions

- **Transform lives in §2 only, not §3** — Claude's call, within the plan's open issue on placement. §2 is where the handed name becomes the slug, so it's the decision point; §3 already composes the token-led filename through the template names, so repeating the rule there is exactly the duplicated prepend statement the plan warned against.
- **§1 intake left untouched** — the other open issue. Its existing forward-pointer to the slug step already captures the name cleanly; no transform detail belongs there.
- **Removed the paragraph's old closing sentence** ("every doc carries the owning unit's token ahead of it…") — the new opener states that outcome once, so keeping the tail would have duplicated it. The dropped ownership rationale is background, not load-bearing here.
- **Template version line held at V1** — Claude's call. The `> V1, <date>.` line is the seed baseline every freshly seeded brain starts its `WORK_SETUP` from, not a changelog of the template file; bumping it would push new brains to V2 wrongly.

## Lessons

The whole risk of this item was prose discipline, not logic: the fix is one sentence of behavior, but the failure mode is stating it twice. Placing it strictly at the name → slug decision point, and deleting the now-redundant tail in the same edit, is what keeps it single-homed. Left uncommitted at Rob's direction.
