# <Project>: Feature Closeout

> V1, <date>.

Procedure for folding a merged feature's working docs into the canonical mini-brain. The bookend to `<PREFIX>_FEATURE_SETUP.md`. Read `CLAUDE.md` first for file conventions — those govern every edit made during closeout.

When a feature developed in `working/` merges, its `<FEATURE>_*` docs hold knowledge that must move into the canonical mini-brain before the working files are retired. Enumerate whatever `working/<FEATURE>_*` actually exists rather than assuming a fixed set — a feature may carry fewer if a doc was implemented and retired mid-development, or never created. This procedure integrates that knowledge without losing it and without letting the canonical docs accumulate contradictions. Run it once per feature, after the branch merges.

Closeout is the additive-and-reconciling integration of one feature's known body of new knowledge, triggered by a merge. It is distinct from the time-triggered, mini-brain-wide drift review in `<PREFIX>_DREAM_CYCLE.md`, which detects staleness across all docs on its own schedule. The two share machinery (the version-header bump, the reconcile step) but run at different times for different reasons. Done well, closeout is the front line and leaves little for the later periodic review to extract for that feature.

---

## 1. Enumerate the targets

Do not work from a hand-written task list alone — it is easy to name the obvious targets (LOG, FINDINGS) and miss the ones a feature quietly changes. Walk the full canonical set and decide, for each, whether this feature touches it:

| Candidate target | Touches it when the feature… |
|---|---|
| `<PREFIX>_LOG.md` | did any implementation work worth a session log (almost always) |
| `<PREFIX>_FINDINGS.md` | made a non-obvious decision worth preserving |
| `<PREFIX>_SCOPE.md` | changed a factual or absence claim about the codebase (verify even if you think not) |
| `<PREFIX>_APPROACH.md` | changed a design assumption or external dependency |
| any canonical testing/runbook doc | added a manual or automated check worth keeping — the feature's `<FEATURE>_TESTING.md` / `<FEATURE>_CLAUDE.md` fold in here |

One working file commonly fans out to several targets; do not assume one source maps to one target. Decide each finding's home by the **durability and reach of the decision, not the location of the code that implemented it**.

The mirror of this: whoever writes a feature's own closeout notes (in its `<FEATURE>_TASKS.md`) should *not* pre-enumerate this table — which files a feature touches is derived here, at merge time. A feature's closeout notes record only what this walk won't surface: deviations from the standard flow, and non-derivable callouts — most importantly the specific existing claim a feature **reverses**.

---

## 2. Classify each edit before making it

The canonical docs are not all the same shape, and merging the wrong way creates sedimentary layering — contradictory claims stacked because each merge only appended. Classify every edit:

- **Additive** — the target has no claim on this yet. Add it.
- **Reconcile (supersede)** — the new knowledge makes an existing statement *false* or reverses a committed direction. Do **not** add a second statement beside the old one. Rewrite the existing statement in place (bumping the version header), saying what changed and why the earlier direction was abandoned. The test: *"does this make an existing statement false?"* If yes, it is a rewrite, not an addition. Grepping the target for shared key terms catches duplicates; it will **not** catch a reversal whose wording differs — read the section and judge.
- **Snapshot-replace** — some sections are current-state snapshots, not logs. Replace these wholesale; never append a second "current" state beside the old one.
- **Append-log** — LOG files are append-only. Add a new entry per `<PREFIX>_SESSION_CLOSEOUT.md`; never revise content above the new separator. **Preserve the original session ID(s)** recorded in the feature's working log — each merged entry keeps the session ID under which that work was actually done, not the closeout session's ID. As you merge each entry, rewrite or drop the working log's internal references to sibling `<FEATURE>_*` docs, which are about to move to `archive/`.

At closeout the reversal is backed by a shipped decision, so reconcile **authoritatively**. (This is the opposite of a contradiction merely *discovered* later during a periodic review with no clear winner, which should be flagged for the user rather than auto-resolved.)

---

## 3. Make the edits

Follow `CLAUDE.md` for every edit: classify editorial vs. substantive, bump the version header for substantive changes, and cite top-level filenames (never retired `archive/` copies) in any cross-reference. Anchor each merged finding to the **PR/commit that changed the behavior**, so its lineage points at a diff you can actually read.

---

## 4. Retire the working files

Once the content is integrated, move each `working/<FEATURE>_*` file into `archive/` under its own name — no version suffix, since working files are not versioned. Move, don't delete: the content is preserved in the canonical docs, but the original is cheap to keep and occasionally worth consulting. Drop any now-dangling cross-references left behind by the merge.

---

## 5. Structural integrity check

Finish with these mechanical checks, to confirm the merge is clean:

1. **Read index ↔ disk** — every read-index file exists; no top-level orphans.
2. **Version headers** — each substantively edited file's header version was bumped by one and carries today's date (compared numerically — `V10` beats `V9`).
3. **Cross-references** — every mini-brain filename reference resolves to a current top-level file, not an archive copy.
4. **No dangling feature references** — grep the top-level docs for the feature's `<FEATURE>_*` names; there should be none left (they live in `archive/` now).
5. **`working/` is clean** — the merged feature's working files are gone from `working/`.

Report what was merged (by target file and old → new version), what was reconciled (what reversed and why), and the result of the structural check.
