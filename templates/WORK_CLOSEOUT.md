# <Project>: Work Closeout

> V1, <date>.

Procedure for folding a concluded work item's working docs into the canonical mini-brain. The bookend to `<PREFIX>_WORK_SETUP.md`. Read `CLAUDE.md` first for file conventions — those govern every edit made during closeout.

When a work item developed in `working/` concludes, its `<TOKEN>_<WORK>_*` docs hold knowledge that must move into the canonical mini-brain before the working files are retired. `<TOKEN>` throughout is the owning unit's namespace token — in a brain with one unit, the brain's own token. Enumerate whatever `working/<TOKEN>_<WORK>_*` actually exists rather than assuming a fixed set — a work item may carry fewer if a doc was implemented and retired mid-development (often the PLAN), or never created (e.g. a manual-only effort with no `<TOKEN>_<WORK>_CLAUDE.md` automated runbook) — and confirm each match's slug is exactly this item's: slugs are prefix-distinct by the setup rule, but an item that predates the rule can have a sibling whose compound extends this one's, and retiring its docs here would close it by accident. This procedure integrates that knowledge without losing it and without letting the canonical docs accumulate contradictions. Run it once per work item, when the work concludes — usually when its branch merges, occasionally without a merge — with one mid-item exception, defined next.

**Early plan archival — the one part of this procedure that runs mid-item.** When the developer requests it — typically once the plan has been converted to code — the PLAN retires to `archive/` mid-item. Before the plan moves, walk the developer through every unaddressed item from the plan; each is dropped or carried to the BURNDOWN by the developer's call, so nothing leaves the plan silently. The move touches the PLAN alone — §§1–5 still run once, when the item concludes. The agent does not offer early archival unprompted.

In a brain whose knowledge is divided into components, a work item lives in its owning unit's `working/` and carries that unit's token. Most of what it holds folds into that same unit's canonical docs — but not all of it, so place each piece of knowledge on its own merits rather than sweeping the lot into the owner. §1 says how.

Closeout is the additive-and-reconciling integration of one work item's known body of new knowledge, triggered by the work concluding (usually a merge). It is distinct from the brain's time-triggered, mini-brain-wide drift review — the dream cycle — which detects staleness across all docs on its own schedule. The two share machinery (the version-header bump, the reconcile step) but run at different times for different reasons. Done well, closeout is the front line and leaves little for the later periodic review to extract for that work item.

---

## 1. Enumerate the targets

Do not work from a hand-written task list alone — it is easy to name the obvious targets (LOG, FINDINGS) and miss the ones a work item quietly changes. Walk the full canonical set and decide, for each, whether this work item touches it:

| Candidate target | Touches it when the work item… |
|---|---|
| `<TOKEN>_LOG.md` | did any implementation work worth a session log (almost always) |
| `<TOKEN>_FINDINGS.md` | made a non-obvious decision worth preserving |
| `<TOKEN>_SCOPE.md` | changed a factual or absence claim about the codebase (verify even if you think not) |
| `<TOKEN>_APPROACH.md` | changed a design assumption or external dependency |
| any canonical testing/runbook doc | added a manual or automated check worth keeping — the work item's `<TOKEN>_<WORK>_TESTING.md` / `<TOKEN>_<WORK>_CLAUDE.md` fold in here |

One working file commonly fans out to several targets; do not assume one source maps to one target. Decide each finding's home by the **durability and reach of the decision, not the location of the code that implemented it**.

In a component-structured brain, walk that table against the **owning unit's** canonical docs, then place each piece of knowledge by its reach rather than by the work item's ownership. A finding about only the owning unit stays there. A finding that describes how two units relate belongs to their nearest common ancestor — the owner may not hold knowledge about a sibling, so an item owned by a child can and does push content up to its parent, and an item owned by a parent pushes a child-only finding down into that child. The work item's log entries are the exception: they are lineage, not knowledge to place by reach — every merged entry goes to the owning unit's canonical log, one destination for the whole item, matching where the item retires.

The mirror of this: whoever writes a work item's own closeout notes (in its `<TOKEN>_<WORK>_BURNDOWN.md`) should *not* pre-enumerate this table — which files a work item touches is derived here, at closeout time. A work item's closeout notes record only what this walk won't surface: deviations from the standard flow, and non-derivable callouts — most importantly the specific existing claim a work item **reverses**.

---

## 2. Classify each piece of knowledge before merging it

The canonical docs are not all the same shape, and merging the wrong way creates sedimentary layering — contradictory claims stacked because each merge only appended. Not every piece is merged:

- **Omit** — the target's stated coverage already excludes this, most often because the shipped code or runbook now states it outright. `<TOKEN>_FINDINGS.md` carries only what the code does not already show, so a finding the merged artifact spells out in full is dropped rather than folded. The test: *"does the target's stated coverage exclude this?"* Nothing is lost by dropping it — the working doc retires to the owning unit's `archive/` intact — while a redundant fold taxes every later reader with deciding whether it says something the artifact doesn't. Adding is cheap at merge time and winnowing never is, so make this call here.
- **Additive** — the target has no claim on this yet. Add it.
- **Reconcile (supersede)** — the new knowledge makes an existing statement *false* or reverses a committed direction. Do **not** add a second statement beside the old one. Rewrite the existing statement in place (bumping the version header), saying what changed and why the earlier direction was abandoned. The test: *"does this make an existing statement false?"* If yes, it is a rewrite, not an addition. Grepping the target for shared key terms catches duplicates; it will **not** catch a reversal whose wording differs — read the section and judge.
- **Snapshot-replace** — some sections are current-state snapshots, not logs. Replace these wholesale; never append a second "current" state beside the old one.
- **Append-log** — LOG files are append-only. Add a new entry per `<PREFIX>_SESSION_CLOSEOUT.md`; never revise content above the new separator. **Preserve the original session ID(s)** recorded in the work item's working log — each merged entry keeps the session ID under which that work was actually done, not the closeout session's ID (which often comes from a different project directory anyway). A work item whose log spans several sessions yields several merged entries, each with its own original ID. As you merge each entry, rewrite or drop the working log's internal references to sibling `<TOKEN>_<WORK>_*` docs (which are about to move to `archive/`) and strip any "pending closeout" block now that closeout is done — rather than carry a dangling `<TOKEN>_<WORK>_*` reference into a canonical doc (§5 check 4 will otherwise flag it).

At closeout the reversal is backed by a shipped decision, so reconcile **authoritatively**. (This is the opposite of a contradiction merely *discovered* later during a periodic review with no clear winner, which should be flagged for the user rather than auto-resolved.)

---

## 3. Make the edits

Follow `CLAUDE.md` for every edit: classify editorial vs. substantive, bump the version header for substantive changes, and cite canonical filenames (never retired `archive/` copies) in any cross-reference. Anchor each merged finding to the **PR/commit that changed the behavior**, so its lineage points at a diff you can actually read.

---

## 4. Retire the working files

Once the content is integrated, move each `working/<TOKEN>_<WORK>_*` file into the **owning unit's** `archive/` under its own name — no version suffix, since working files are not versioned; create that `archive/` if the unit does not have one yet. A work item retires where it lived, even when some of its knowledge folded upward. Move, don't delete: the content is preserved in the canonical docs, but the original is cheap to keep and occasionally worth consulting. Drop any now-dangling cross-references left behind by the merge.

---

## 5. Structural integrity check

Finish with these mechanical checks, to confirm the merge is clean:

1. **Read index ↔ disk** — every read-index file exists; no orphans. In a component-structured brain that covers the hub documents only, so also check the registry against disk and confirm each unit still carries its full doctype set.
2. **Version headers** — each substantively edited file's header version was bumped by one and carries today's date (compared numerically — `V10` beats `V9`).
3. **Cross-references** — every mini-brain filename reference resolves to a current canonical file, not an archive copy.
4. **No dangling work-item references** — grep the canonical docs for each of the item's just-retired filenames (the exact `<TOKEN>_<WORK>_*.md` names, not the bare compound, which can also match unrelated canonical names); there should be none left (they live in `archive/` now). The `<WORK>` token used in this doc is a deliberate placeholder, so grepping it returns zero — any hit is a genuine dangling reference to fix, most often one carried in from a merged LOG entry (see the append-log rule in §2).
5. **`working/` is clean** — the merged work item's working files are gone from the owning unit's `working/`.
6. **No sideways references** (component brains) — if a finding folded upward, confirm it landed in the ancestor and that neither sibling names the other.

Report what was merged (by target file and old → new version), what was reconciled (what reversed and why), and the result of the structural check.
