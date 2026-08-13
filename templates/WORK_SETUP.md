# <Project>: Work Setup

> V1, <date>.

Procedure for scaffolding a new work item's working docs from an intake conversation. The bookend to `<PREFIX>_WORK_CLOSEOUT.md`: setup creates the `working/` docs at branch start, closeout folds them into the canonical mini-brain when the work concludes. Read `CLAUDE.md` first for file conventions — they govern every file this procedure touches.

Run this when starting a new work item — **code-changing work that gets its own branch and PR**: a feature, a bug fix, or a hardening effort — or when formalizing a partial one that already lives in `working/` (e.g. a PLAN+FINDINGS pair that needs the rest of its scaffolding). The output is the `working/<TOKEN>_<WORK>_*.md` documents that track a work item until it concludes. `<TOKEN>` throughout is the owning unit's namespace token — in a brain with one unit, the brain's own token. Setup is **additive and idempotent**: it creates only the docs that are missing and never overwrites existing work, so it is safe to re-run as a work item grows.

The scope is deliberately narrow and practical: **assume a work item has a branch and a PR until proven otherwise.** It is often not knowable at inception whether an idea is a shallow doc/config tweak or something deeper, so default to the full scaffold rather than guessing small — an oversized scaffold is cheap, and under-scaffolding something that turns out deep is not. If the work later concludes without a code change, closeout still folds in whatever knowledge the docs hold (see `<PREFIX>_WORK_CLOSEOUT.md`); the burndown does not apply. A pure question that produces no artifact worth keeping needs no work item at all: answer it, and if the answer is worth recording, add a session-log entry.

The working docs and their roles:

| Doc | Role | Seeded at setup from the chat? |
|---|---|---|
| `<TOKEN>_<WORK>_PLAN.md` | The spec: objective, what changes, testing approach, scope boundary, open issues | Yes — written from the intake conversation |
| `<TOKEN>_<WORK>_FINDINGS.md` | The decision record: problem, preferred approach, tradeoffs, alternatives | Yes — written from the intake conversation |
| `<TOKEN>_<WORK>_LOG.md` | Append-only session log; one entry per implementation session | No — header only; the first session appends the first entry |
| `<TOKEN>_<WORK>_BURNDOWN.md` | Finishing checklist: what remains to land the change | No — template checklist |
| `<TOKEN>_<WORK>_CLAUDE.md` | Runbook for automated tests — declares the item's branch (the session-routing join key), defers to the platform runbook, then adds work-specific steps | No — template with a placeholder step |
| `<TOKEN>_<WORK>_TESTING.md` | Manual test plan: steps to verify the work item by hand; folds into the canonical testing doc at closeout | No — template scaffold |

PLAN and BURNDOWN are two halves of the same work: the plan gets the code written, the burndown gets it merged. The burndown's Routine rows are inherited defaults: a brain adopting this procedure refines them once, outside any setup run, to match its PR conventions — the closeout-notes row is not a PR convention and stays. Custom rows are always per-item.

These are **working files**, so per `CLAUDE.md` they are *not* versioned (no `> V<N>` header), are *not* added to the read index, and are not read in future sessions unless explicitly asked.

---

## 1. The intake conversation

Before scaffolding anything, have the conversation. Setup turns a settled discussion into documents; it does not invent the design. Pin down, at minimum:

- **Owning unit** — in a brain whose knowledge is divided into components, which unit the work belongs to: the nearest common ancestor of the units the work will concern. That unit's `working/` holds the docs and its token becomes their `<TOKEN>`. Settle this first, since it decides both. A brain with one unit skips this and uses the brain's own token.
- **Work-item name** → derive the `<WORK>` slug (§2).
- **One-line definition** — what the work item is, in a sentence.
- **Problem** — what's broken or missing, and who feels it. This anchors FINDINGS.
- **Preferred approach + tradeoffs** — the chosen direction and *why*, plus the alternatives weighed and rejected. This is the heart of FINDINGS; capture the reasoning, not just the verdict.
- **Scope boundary** — what the work item explicitly does *not* touch. Goes into PLAN's "what this does NOT include"; it is the cheapest way to prevent scope creep.
- **Testing approach** — what's covered by automated tests and what can only be checked by hand. Seeds PLAN's testing section, the BURNDOWN checklist, and the runbook/testing docs.

If the chosen approach makes an existing canonical claim false (a reversal, not just an addition), note it now — record it in FINDINGS and flag it for closeout. A reversal is the one thing a wording-based grep won't catch at merge time, so the merge relies on it being called out explicitly here.

---

## 2. Derive the slug and audit what exists

**Slug.** SCREAMING_SNAKE_CASE. Not a mechanical transform of the work-item name — short and specific, and distinct in the **prefix** sense: the procedures find an item's docs by the glob `<TOKEN>_<WORK>_*`, so `<TOKEN>_<WORK>_` must not begin any canonical document's name or another open item's compound, and no other item's compound may begin this one's — a slug `PLUM` beside an item slugged `PLUM_JAM` would sweep that item's docs into its own closeout. In a component brain, also pick the slug so that no other unit's token is a longer prefix of `<TOKEN>_<WORK>` than `<TOKEN>` itself: ownership goes to the longest match, so a parent's slug that continues into a child's token hands the item's files to that child. The fuller name lives in the `# <Work-Item Name>` heading. Every doc carries the owning unit's token ahead of it, which is what keeps a work item's files parseable and tells a reader which unit owns the effort.

**Audit (this is what makes setup safe on partial/existing work items).** Before creating anything, list the owning unit's `working/` and `archive/` for the slug. From the owning unit's directory — the repo root for a single-unit brain:

```bash
find working archive -maxdepth 1 -name '<TOKEN>_<WORK>_*.md' 2>/dev/null
```

A unit missing one of the two directories is normal and doesn't hide the other's matches. Empty output means a brand-new item **only if the command ran in the owning unit's directory** — confirm the location before trusting an empty audit, because everything below builds on it.

Classify each doc — first match wins:
- **A legacy `<TOKEN>_<WORK>_TASKS.md` in `working/`** — the item's burndown under its pre-rename name, so the BURNDOWN slot is not missing. Rename the file to `<TOKEN>_<WORK>_BURNDOWN.md` — a rename keeps its content and its `<TOKEN>_<WORK>_` routing prefix, overwriting nothing — update references to the old name among the item's other docs, and do not scaffold a second checklist.
- **Missing** — create from the template (§3).
- **Exists in `working/`** — leave it. Do not overwrite. If the intake chat adds genuinely new material, append it; never rewrite existing working content from a setup run.
- **Exists in `archive/`** — already implemented and retired (as a `<TOKEN>_<WORK>_PLAN.md` often is once its plan has shipped). Do **not** recreate it in `working/`; note that it is done and move on.

A brand-new work item has nothing on disk, so the full set is created. A partial one (commonly PLAN+FINDINGS) gets only its missing docs created.

---

## 3. Generate the docs

Create each missing doc in the owning unit's `working/`, from its base template, substituting `<TOKEN>` (the owning unit's token), `<WORK>` (SCREAMING_SNAKE), `<Work-Item Name>` (Title Case), and `<work-branch>` — a single branch name, or a glob when the item will land across several branches/PRs. Create that `working/` if the unit does not have one yet. Fill PLAN and FINDINGS with real content from the intake chat; leave the others as scaffolds for the implementer.

Do not add a `> V<N>` version header to any of these — working files are unversioned. Do not copy them into `archive/` (docs land there only when they retire). Do not touch the read index or any canonical doc.

Base templates for each doc live in the toolkit's `templates/work/` (`PLAN.md`, `FINDINGS.md`, `LOG.md`, `BURNDOWN.md`, `CLAUDE.md`, `TESTING.md`); a brain's copy of this procedure inlines all six here, so the brain stands alone without the toolkit.

---

## 4. Handoff

After creating the docs:

1. Report the owning unit, the slug used, which docs were **created**, which were **renamed** from a legacy name, and which already **existed** (and where — `working/` or `archive/`).
2. Remind that these are working files: they stay out of the read index, and the canonical mini-brain is untouched until the work concludes.
3. Point at `<PREFIX>_WORK_CLOSEOUT.md` as the closeout bookend — it consumes exactly these docs.
