# <Project>: Work Setup

> V1, <date>.

Procedure for scaffolding a new work item's working docs from an intake conversation. The bookend to `<HUB>_WORK_CLOSEOUT.md`: setup creates the `working/` docs when a work item opens, closeout folds them into the canonical mini-brain when the work concludes. Read `CLAUDE.md` first for file conventions — they govern every file this procedure touches.

Run this when starting a new work item — **code-changing work that gets its own branch and PR**: a feature, a bug fix, or a hardening effort — or when formalizing a partial one that already lives in `working/` (e.g. a PLAN+FINDINGS pair that needs the rest of its scaffolding). The output is the `working/<LOBESPACE>_<WORK>_*.md` documents that track a work item until it concludes. `<LOBESPACE>` throughout is the owning lobe's lobespace — in a brain with one lobe, the brain's own lobespace. Setup is **additive and idempotent**: it creates only the docs that are missing and never overwrites existing work, so it is safe to re-run as a work item grows.

The scope is deliberately narrow and practical: **assume a work item has a branch and a PR until proven otherwise.** It is often not knowable at inception whether an idea is a shallow doc/config tweak or something deeper, so default to the full scaffold rather than guessing small — an oversized scaffold is cheap, and under-scaffolding something that turns out deep is not. If the work later concludes without a code change, closeout still folds in whatever knowledge the docs hold (see `<HUB>_WORK_CLOSEOUT.md`); the burndown does not apply. A pure question that produces no artifact worth keeping needs no work item at all: answer it, and if the answer is worth recording, add a session-log entry.

The working docs and their roles:

| Doc | Role | Seeded at setup from the chat? |
|---|---|---|
| `<LOBESPACE>_<WORK>_PLAN.md` | The spec: objective, what changes, testing approach, scope boundary, open issues | Yes — written from the intake conversation |
| `<LOBESPACE>_<WORK>_FINDINGS.md` | The decision record: problem, preferred approach, tradeoffs, alternatives | Yes — written from the intake conversation |
| `<LOBESPACE>_<WORK>_LOG.md` | Append-only session log; one entry per implementation session | No — header only; the first session appends the first entry |
| `<LOBESPACE>_<WORK>_BURNDOWN.md` | Finishing checklist: what remains to land the change | No — template checklist |
| `<LOBESPACE>_<WORK>_CLAUDE.md` | Runbook for automated tests — declares the item's branch (the session-routing join key), defers to the brain's canonical runbook, then adds work-specific steps | No — template with a placeholder step |
| `<LOBESPACE>_<WORK>_TESTING.md` | Manual test plan: steps to verify the work item by hand; folds into the canonical testing doc at closeout | No — template scaffold |

PLAN and BURNDOWN are two halves of the same work: the plan gets the code written, the burndown gets it merged. The burndown's Routine rows are inherited defaults: a brain adopting this procedure refines them once, outside any setup run, to match its PR conventions — the closeout-notes row is not a PR convention and stays. Custom rows are always per-item; the scaffold's category placeholders there are prompts to fill or strike, not standing work.

These are **working files**, so per `CLAUDE.md` they are *not* versioned (no `> V<N>` header), are *not* added to the read index, and are not read in future sessions unless explicitly asked. This procedure's own alignment step (§2) is the one exception: it reads other open items' PLAN and FINDINGS.

---

## 1. The intake conversation

Before scaffolding anything, have the conversation. Setup turns a settled discussion into documents; it does not invent the design. Pin down, at minimum:

- **Owning lobe** — in a multi-lobe brain, which lobe the work belongs to: the nearest common ancestor of the lobes the work will concern. That lobe's `working/` holds the docs and its lobespace becomes their `<LOBESPACE>`. Settle this first, since it decides both. A brain with one lobe skips this and uses the brain's own lobespace.
- **Work-item name** → derive the `<WORK>` slug (§2).
- **One-line definition** — what the work item is, in a sentence.
- **Problem** — what's broken or missing, and who feels it. This anchors FINDINGS.
- **Preferred approach + tradeoffs** — the chosen direction and *why*, plus the alternatives weighed and rejected. This is the heart of FINDINGS; capture the reasoning, not just the verdict.
- **Scope boundary** — what the work item explicitly does *not* touch. Goes into PLAN's "what this does NOT include"; it is the cheapest way to prevent scope creep.
- **Testing approach** — what's covered by automated tests and what can only be checked by hand. Seeds PLAN's testing section, the BURNDOWN checklist, and the runbook/testing docs.

If the chosen approach makes an existing canonical claim false (a reversal, not just an addition), note it now — record it in FINDINGS and flag it for closeout. A reversal is the one thing a wording-based grep won't catch at merge time, so the merge relies on it being called out explicitly here.

---

## 2. Derive the slug, audit what exists, and align

**Slug.** Every filename this procedure produces is `<LOBESPACE>_<WORK>_*` — derive `<WORK>` from the work-item name and lead with the owning lobe's lobespace, always. `<WORK>` is a SCREAMING_SNAKE_CASE slug and never carries a lobe's lobespace, its own or another's. A handed SCREAMING_SNAKE identifier is the slug verbatim, minus any lobe's lobespace it opens with, taking the longest match (a handed `<LOBESPACE>_FOO` gives `<WORK>` = `FOO` and files `<LOBESPACE>_FOO_*`); any other handed name gets a short, specific slug written for it. Check the compound `<LOBESPACE>_<WORK>` before use, rewording the slug — handed or written — until both checks pass. Distinctness in the **prefix** sense: the procedures find an item's docs by the glob `<LOBESPACE>_<WORK>_*`, so `<LOBESPACE>_<WORK>_` must not begin any canonical document's name or the compound of another open item in `working/`, and no other item's compound may begin this one's — a slug `PLUM` beside an item slugged `PLUM_JAM` would sweep that item's docs into its own closeout. And in a multi-lobe brain: no other lobe's lobespace may be a longer prefix of `<LOBESPACE>_<WORK>` than `<LOBESPACE>` itself — ownership goes to the longest match, so a parent's slug that continues into a child's lobespace hands the item's files to that child. Names in `archive/` don't count. The fuller name lives in the `# <Work-Item Name>` heading.

**Audit (this is what makes setup safe on partial/existing work items).** Before creating anything, list the owning lobe's `working/` for the slug. From the owning lobe's directory — the repo root for a single-lobe brain:

```bash
find working -maxdepth 1 -name '<LOBESPACE>_<WORK>_*.md' 2>/dev/null
```

The audit does not search `archive/`. Its stale, abandoned and older-convention material can carry names that match a new slug without belonging to it. Empty output means a brand-new item **only if the command ran in the owning lobe's directory** — confirm the location before trusting an empty audit, because everything below builds on it.

Classify each doc — first match wins:
- **Exists in `working/`** — leave it. Do not overwrite. If the intake chat adds genuinely new material, append it; never rewrite existing working content from a setup run.
- **Missing PLAN on an item with other docs in `working/`** — ask the developer whether the PLAN was retired early before creating one; if it was, don't recreate it.
- **Missing** — create from the template (§3).

A brand-new work item has nothing on disk, so the full set is created. A partial one (commonly PLAN+FINDINGS) gets only its missing docs created.

**Align against other open items.** Read the PLAN and FINDINGS of every other open work item in the `working/` of each lobe the work concerns, the owning lobe, and each of the owning lobe's ancestors — in a brain with one lobe, the owning lobe alone. From each such lobe's directory, with `<L>` that lobe's lobespace:

```bash
find working -maxdepth 1 \( -name '<L>_*_PLAN.md' -o -name '<L>_*_FINDINGS.md' \) 2>/dev/null
```

Group the matches by compound, the name before `_PLAN.md` or `_FINDINGS.md`, and skip this item's own. Record each overlap or conflict in this item's PLAN under open issues — written into the PLAN §3 creates, or appended to the PLAN that already exists. When the PLAN was retired early, record it in FINDINGS under an `## Open issues` heading instead, adding the heading if FINDINGS lacks one.

---

## 3. Generate the docs

Create each missing doc in the owning lobe's `working/`, from its base template, substituting `<LOBESPACE>` (the owning lobe's lobespace), `<WORK>` (SCREAMING_SNAKE), `<Work-Item Name>` (Title Case), and `<work-branch>` — a single branch name, or a glob when the item will land across several branches/PRs; setup declares the name — creating the branch belongs to the project's workflow, when coding starts. Create that `working/` if the lobe does not have one yet. Fill PLAN and FINDINGS with real content from the intake chat; leave the others as scaffolds for the implementer.

Do not add a `> V<N>` version header to any of these — working files are unversioned. Do not copy them into `archive/` (docs land there only when they retire). Do not touch the read index or any canonical doc.

Base templates for each doc live in the toolkit's `templates/work/` (`PLAN.md`, `FINDINGS.md`, `LOG.md`, `BURNDOWN.md`, `CLAUDE.md`, `TESTING.md`); a brain's copy of this procedure inlines all six here, so the brain stands alone without the toolkit.

---

## 4. Handoff

After creating the docs:

1. Report the owning lobe, the slug used, which docs were **created**, which already **existed** in `working/`, and any doc not recreated because it was retired early.
2. Remind that these are working files: they stay out of the read index, and the canonical mini-brain is untouched until the work concludes.
3. Point at `<HUB>_WORK_CLOSEOUT.md` as the closeout bookend — it consumes exactly these docs.
