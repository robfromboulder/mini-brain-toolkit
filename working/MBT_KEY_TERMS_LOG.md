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

---

# Correct the placeholder collapse left by the rename (2026-09-21)

**Session ID**: `239392ec-f1f6-4f8a-93cf-f10bf1077c16`

Rob's session, with Claude (Opus 5, 1M context) as co-author. A code review of PR #5 found that the rename's placeholder unification had merged two placeholders with different binding times, breaking every template reference to a hub-only maintenance document. The session introduced `<HUB>` to restore the distinction, finished the vocabulary sweep the rename had left incomplete, and pushed the corrections to the branch with a review comment on the PR.

## What the review found

Rob ran a code review over the branch. Its central finding was that unifying the two template placeholders discarded a binding-time distinction the templates depend on: one was substituted once when a brain is created, the other stayed a runtime variable resolved per owning lobe and per work item. With a single name for both, the work-setup and work-closeout templates assert that the placeholder is *throughout* the owning lobe's lobespace — false for the references they carry to session closeout and to each other, which the multi-lobe layer says live only at the hub and are never namespaced to a child. Scaffolding a work item owned by a child lobe therefore pointed the implementer at maintenance files that cannot exist, and the check procedure's new migration walkthrough prescribed the same merge, reproducing the defect inside every brain it migrated. The positional substitution rule that replaced the name-based one was undecidable besides: its creation-time list named file-set tables, and the multi-lobe entrypoint's doctype grammar is a file-set table that has to stay runtime. Claude verified each claim against the branch before relaying any of it, rather than taking the review's report at face value.

## Naming the restored placeholder

Rob proposed "home lobe" in place of "hub" or "prefix". Claude checked the term against the repo and advised against it: "home" is already load-bearing twice over — the say-it-once writing rule states that each fact has exactly one home, and "re-homing" is the established name for moving a lobe or document to a new parent, carried in session closeout's content rules and holding an open work item of its own. Under "home lobe", re-homing a lobe would read as making it the home lobe, inverting the operation. "Hub" had no competing sense anywhere in the repo, including the comparables and biology registries, so Claude recommended keeping it and naming the placeholder `<HUB>`, with `<BRAIN>` as runner-up if binding-time legibility mattered more than the tie to the hub-only placement rule. Rob chose `<HUB>`.

## Implementation

Before editing, Claude corrected its own framing of the defect. The retired creation-time placeholder had never meant "the hub's lobespace" — the create procedure defined it as whichever lobe's copy was being seeded, so its real content was *substitute now*. A blanket rename of every former instance to `<HUB>` would have been wrong for a child lobe's own document set. `<HUB>` went only where the reference is to a document that lives at the hub alone; seeded doctype documents kept the per-lobe placeholder. That let the create procedure's rule return to being name-based, which is what made it decidable again.

One edit was made and reverted. Claude first added a sentence to both work templates defining `<HUB>` alongside the runtime placeholder, then removed it on noticing that `<HUB>` is substituted at seed time and the gloss would survive into the seeded brain as dead text — the reason the pre-rename templates never explained their creation-time placeholder either. The two "throughout" sentences were then left exactly as the branch had written them, since every placeholder still standing in those files genuinely is the owning lobe's.

A mechanical sweep after the fix caught a stale pattern-specific use in the create procedure that the review had missed, its file list having covered only the pattern, approach and findings docs. Worth noting for the next pass: the review's enumeration was a sample, not a census, and the sweep is what closed it.

## Decisions

- **`<HUB>` stays out of the single-lobe templates and the base pattern definition** (Claude's proposal, Rob agreed) — a brain with one lobe has one lobespace and no hub/child split, so the per-lobe placeholder is already unambiguous there, and introducing `<HUB>` would import multi-lobe vocabulary into the base pattern. The lone exception was the create procedure's seed-table row for session closeout, which had to change or it would contradict the same file's later instructions for the mature lifecycle.
- **No version bumps on files the branch had already bumped** (Claude's proposal, Rob agreed) — the branch is one unmerged substantive change per file and had already set the current date. Only the implementation-findings doc took a bump, being the file the branch never touched.
- **Swept the implementation-findings doc, reversing this work item's earlier decision to leave it alone** (Claude's finding, Rob directed the fix). The earlier session logged that exclusion as the plan's scope boundary, but the plan's scope boundary names only the enforced-terms work item and `archive/` content, and its testing approach affirmatively requires that no stale pattern-specific uses survive. The exclusion was that session's own call, attributed to a constraint the plan does not contain, and it conflicted with the plan's stated test. Four lines were renamed. The imperative quoted inside one of them was updated to track the live template text clause for clause rather than reworded freely, because that finding exists to warn that the sentence's position is load-bearing and was once silently regressed. Leaving the canonical session log untouched was not revisited and remains correct — the append-only rule genuinely forbids revising entries, which the vocabulary-of-their-time reasoning does fit.
- **Two ambiguous uses surfaced rather than replaced** (the check procedure's own rule, left with Rob) — two remaining uses of the old term in the implementation-findings doc mean a filename slot and a name, neither of which is the namespace sense the rename covers, so renaming them to "lobespace" would be wrong. Left as they stand pending Rob's judgment.

## Lessons

- **A placeholder's name can carry a binding time, and collapsing names collapses that too.** The unification looked like pure vocabulary work because both placeholders denoted a lobespace. What distinguished them was *when* they resolve, which no amount of care about the noun would have surfaced — the defect only became visible by asking what each site would resolve to in a multi-lobe brain.
- **A replacement rule that decides by position needs to be tested against the file set it governs.** The positional rule read plausibly and was wrong on its second example; the name-based rule it replaced had been decidable for free.
- **Check a proposed term against the repo before adopting it.** "Home lobe" was appealing in the abstract and collided with two established senses, one of them a named operation with live design work attached.
