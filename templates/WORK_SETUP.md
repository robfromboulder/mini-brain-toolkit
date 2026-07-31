# <Project>: Work Setup

> V1, <date>.

Procedure for scaffolding a new work item's working docs from an intake conversation. The bookend to `<PREFIX>_WORK_CLOSEOUT.md`: setup creates the `working/` docs at branch start, closeout folds them into the canonical mini-brain when the work concludes. Read `CLAUDE.md` first for file conventions — they govern every file this procedure touches.

Run this when starting a new work item — **code-changing work that gets its own branch and PR**: a feature, a bug fix, or a hardening effort — or when formalizing a partial one that already lives in `working/` (e.g. a PLAN+FINDINGS pair that needs the rest of its scaffolding). The output is the `working/<PREFIX>_<WORK>_*.md` documents that track a work item until it concludes. Setup is **additive and idempotent**: it creates only the docs that are missing and never overwrites existing work, so it is safe to re-run as a work item grows.

The scope is deliberately narrow and practical: **assume a work item has a branch and a PR until proven otherwise.** It is often not knowable at inception whether an idea is a shallow doc/config tweak or something deeper, so default to the full scaffold rather than guessing small — an oversized scaffold is cheap, and under-scaffolding something that turns out deep is not. If the work later resolves without a code change, it simply concludes without a merge — closeout still folds in whatever knowledge the docs hold (see `<PREFIX>_WORK_CLOSEOUT.md`) — rather than being forced through the PR checklist. A pure question that produces no artifact worth keeping needs no work item at all: answer it, and if the answer is worth recording, add a session-log entry.

The working docs and their roles:

| Doc | Role | Seeded at setup from the chat? |
|---|---|---|
| `<PREFIX>_<WORK>_PLAN.md` | The spec: objective, what changes, testing approach, scope boundary, open issues | Yes — written from the intake conversation |
| `<PREFIX>_<WORK>_FINDINGS.md` | The decision record: problem, preferred approach, tradeoffs, alternatives | Yes — written from the intake conversation |
| `<PREFIX>_<WORK>_LOG.md` | Append-only session log; one entry per implementation session | No — header only; the first session appends the first entry |
| `<PREFIX>_<WORK>_TASKS.md` | Checklist: PR wrangling, testing, docs, closeout | No — template checklist |
| `<PREFIX>_<WORK>_CLAUDE.md` | Runbook for automated tests; defers to the platform runbook, then adds work-specific steps | No — template with a placeholder step |
| `<PREFIX>_<WORK>_TESTING.md` | Manual test plan: steps to verify the work item by hand; folds into the canonical testing doc at closeout | No — template scaffold |

These are **working files**, so per `CLAUDE.md` they are *not* versioned (no `> V<N>` header), are *not* added to the read index, and are not read in future sessions unless explicitly asked.

---

## 1. The intake conversation

Before scaffolding anything, have the conversation. Setup turns a settled discussion into documents; it does not invent the design. Pin down, at minimum:

- **Owning unit** — in a brain whose knowledge is divided into components, which unit the work belongs to: the nearest common ancestor of the units it will touch. That unit's `working/` holds the docs and its token becomes their `<PREFIX>`. Settle this first, since it decides both. A brain with one unit skips this and uses the brain's own token.
- **Work-item name** → derive the `<WORK>` prefix (§2).
- **One-line definition** — what the work item is, in a sentence.
- **Problem** — what's broken or missing, and who feels it. This anchors FINDINGS.
- **Preferred approach + tradeoffs** — the chosen direction and *why*, plus the alternatives weighed and rejected. This is the heart of FINDINGS; capture the reasoning, not just the verdict.
- **Scope boundary** — what the work item explicitly does *not* touch. Goes into PLAN's "what this does NOT include"; it is the cheapest way to prevent scope creep.
- **Testing approach** — what's covered by automated tests and what can only be checked by hand. Seeds PLAN's testing section, the TASKS checklist, and the runbook/testing docs.

If the chosen approach makes an existing canonical claim false (a reversal, not just an addition), note it now — record it in FINDINGS and flag it for closeout. A reversal is the one thing a wording-based grep won't catch at merge time, so the merge relies on it being called out explicitly here.

---

## 2. Derive the prefix and audit what exists

**Prefix.** SCREAMING_SNAKE_CASE. It is a short slug, *not* a mechanical transform of the work-item name — short, specific, and distinct enough that `<PREFIX>_<WORK>_*.md` won't collide with another work item's docs. The fuller name lives in the `# <Work-Item Name>` heading. Every doc carries the owning unit's token ahead of it, which is what keeps a work item's files parseable and tells a reader which unit owns the effort.

**Audit (this is what makes setup safe on partial/existing work items).** Before creating anything, list the owning unit's `working/` and `archive/` for the prefix — the repo root for a single-unit brain, the unit's directory otherwise:

```bash
ls -1 <unit>/working/<PREFIX>_<WORK>_*.md <unit>/archive/<PREFIX>_<WORK>_*.md 2>/dev/null
```

Classify each doc:
- **Missing** — create from the template (§3).
- **Exists in `working/`** — leave it. Do not overwrite. If the intake chat adds genuinely new material, append it; never rewrite existing working content from a setup run.
- **Exists in `archive/`** — already implemented and retired (as a `<WORK>_PLAN.md` often is once its plan has shipped). Do **not** recreate it in `working/`; note that it is done and move on.

A brand-new work item has nothing on disk, so the full set is created. A partial one (commonly PLAN+FINDINGS) gets only its missing docs created.

---

## 3. Generate the docs

Create each missing doc in the owning unit's `working/`, from the template below, substituting `<PREFIX>` (the owning unit's token), `<WORK>` (SCREAMING_SNAKE), `<Work-Item Name>` (Title Case), and `<work-branch>` — a single branch name, or a glob when the item will land across several branches/PRs. Create that `working/` if the unit does not have one yet. Fill PLAN and FINDINGS with real content from the intake chat; leave the others as scaffolds for the implementer.

Do not add a `> V<N>` version header to any of these — working files are unversioned. Do not copy them into `archive/` (that happens only at closeout). Do not touch the read index or any canonical doc.

Base templates for each doc live in `templates/work/` (`PLAN.md`, `FINDINGS.md`, `LOG.md`, `TASKS.md`, `CLAUDE.md`, `TESTING.md`).

---

## 4. Handoff

After creating the docs:

1. Report the owning unit, the prefix used, which docs were **created**, and which already **existed** (and where — `working/` or `archive/`).
2. Remind that these are working files: they stay out of the read index, and the canonical mini-brain is untouched until the work concludes.
3. Point at `<PREFIX>_WORK_CLOSEOUT.md` as the closeout bookend — it consumes exactly these docs.
