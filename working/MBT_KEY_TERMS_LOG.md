# Implement the KEY_TERMS vocabulary rename (2026-09-21)

**Session ID**: `953bc885-70e0-4783-be46-997852def708`

Rob's session, with Claude (Opus 4.6) as co-author. Implemented the full vocabulary rename planned in the KEY_TERMS work item: "unit" → "lobe", "component" → "lobe" (collapsed), "token" → "lobespace" across the toolkit's canonical docs and templates, then opened PR #5 and early-archived the consumed plan.

## Implementation

Rob directed the rename to proceed per the plan. The seven implementation steps ran in order — pattern definition first (`MBT_PATTERN.md`), then the multi-lobe layer (renaming `MBT_COMPONENTS.md` → `MBT_LOBES.md`), then procedures and dream cycle, templates, and this brain's own `CLAUDE.md`. At each site the edit classified the use as pattern-specific or ordinary English: "unit test," "auth token," "software component" and similar were left untouched; "the brain's token," "component-structured brain," "owning unit" and similar were renamed. Files with pervasive changes (`MBT_LOBES.md`, `templates/LOBES_CLAUDE.md`) were full rewrites; the rest used targeted edits.

Two files not in the plan's explicit file list — `MBT_SCOPE.md` and `MBT_APPROACH.md` — turned up during the verification grep with pattern-specific "token" references ("namespace-token convention," "Namespace token `MBT`") and were fixed with version bumps.

The placeholder unification (`<TOKEN>` and `<PREFIX>` both becoming `<LOBESPACE>`) required rewriting `MBT_CREATE_BRAIN.md`'s placeholder-substitution rules: the old procedure distinguished creation-time vs. runtime substitution by placeholder *name*; the new procedure distinguishes them by *position* (hub docs vs. doctype grammar).

A vocabulary-alignment walkthrough was added as structural check 7 in `MBT_CHECK_BRAIN.md` — when the check finds a brain using old terms, it classifies each hit (unambiguous pattern-specific → replace silently, unambiguous ordinary English → skip, ambiguous → surface to user) and performs the walkthrough only when the user opts in.

## Verification

A final grep for remaining pattern-specific uses of "unit," "token," and "component" across all top-level and template files caught three stragglers: a leftover "namespace token" and "include the token" in `templates/CLAUDE.md`, and a leftover `<PREFIX>_*` in `MBT_DREAM_CYCLE.md`. All three were fixed before commit.

## Decisions

- **Full rewrite for heavily-changed files, targeted edits for the rest** (Claude's approach, Rob didn't object) — `MBT_LOBES.md` and `templates/LOBES_CLAUDE.md` changed so pervasively that line-level edits would have been harder to get right than a clean rewrite.
- **Distinguish creation-time vs. runtime `<LOBESPACE>` by position, not name** (plan's design, carried through) — the plan anticipated this and the implementation followed: hub-level docs get their lobespace substituted at creation time, the doctype grammar's `<LOBESPACE>` stays as a runtime variable.
- **Leave `MBT_FINDINGS.md` untouched** (plan's scope boundary) — historical decisions are recorded in the vocabulary of their time.
- **Leave `MBT_LOG.md` untouched** (plan's scope boundary, append-only rule) — log entries are never revised after the fact.
- **Early-archive the plan** (Rob's direction) — the plan was fully consumed (all seven steps complete, both scope-boundary items explicitly out of scope); moved to `archive/` with no unaddressed items.
