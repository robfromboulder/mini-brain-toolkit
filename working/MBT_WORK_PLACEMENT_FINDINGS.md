# Work-Item Placement: Decision Record

## Problem

A work item's owning lobe is the nearest common ancestor of the lobes the work *will* concern. Two things about that rule are unsettled.

**Nothing enacts it at intake.** Work setup states the rule, tells the reader to settle the owner first, and moves on without a method — no walk, no enumeration, no prompt to consider lobes the intake conversation has not already named. What the procedure actually produces is the lobe the conversation was sitting in: inception point, not reach.

**Nothing says what happens when it was wrong.** The owner is a prediction, and mid-flight scope growth can invalidate it: a child-owned item turns out to need a sibling's changes, so the owner should have been their parent. What happens then is undefined.

The two are one question. How much a first placement is worth depends on what a correction costs, and the correction chosen below is expensive enough that intake is the cheap moment and the only one.

## Preferred approach: derive the owner top-down, and supersede when it was wrong

### At intake: derive the owner from the registry

Placement starts at the root and works down: name the lobes the work will concern by matching it against the registry's routing terms, then walk up to their nearest common ancestor. It never starts from whichever lobe the conversation is already in.

Three constraints the derivation has to respect:

- **Read the registry, not the lobes.** The routing terms exist so a session can choose a lobe before reading anything. A walk that opens each lobe to judge relevance re-imports precisely the cost the multi-lobe layer was built to shed, and gets worse with depth.
- **Will, not could.** Almost any work *could* touch any lobe, so a top-down prompt phrased as "could this reach X?" drifts every item toward the hub. The rule already says *will concern*; the procedure has to hold that line explicitly or the walk inflates.
- **Over-placement has a specific cost.** An item sitting at a lobe whose lobespace is a prefix of its children's is next to the naming trap, where a slug that continues into a child's lobespace hands the item's files to that child. Placing too high is not merely untidy.

### When the placement was wrong: items don't move, they are superseded

A work item stays in the lobe where it was opened, for its whole life. When its reach outgrows that lobe, the item retires as **superseded** and a new item opens in the correct lobe, authored against what is now known — the fuller problem, the corrected owner, and the relationships to its new parent and siblings.

This extends a principle already on the books rather than introducing one: work closeout holds that an item retires where it lived, even when its knowledge folds upward.

Three reasons to prefer it over moving the item:

- **It matches the grain.** The pattern is append-only records plus canonical documents rewritten freely. A `git mv` with a lobespace rename across every document is neither — it mutates a record in place so that it reads as though the work had always lived somewhere else.
- **It reuses procedures that already exist.** Retirement and setup both work today. A move would need a bespoke procedure, and a half-moved item that closeout and session routing each have to tolerate.
- **The logs stay put, which is correct.** A superseded item's log entries merge into the *original* owner's canonical log under their original session IDs, because those sessions genuinely concerned that lobe. Splitting an item's lineage across two lobes' logs is an accurate record of work that happened in two places; a move would have to fabricate one continuous history for it.

The policy needs one piece of new machinery and one convention:

- **A supersede retirement** — archive the working documents *without* folding what they hold into canonical documents, since a relocated item is not concluded and its decisions are not yet settled. Merge the log entries as normal and record the successor's slug.
- **A predecessor line** in the successor's FINDINGS, written from the intake conversation, so the lineage is legible from the documents and not only from the log. Setup cannot discover the predecessor on its own once it has retired: setup reads `working/` and never `archive/`.

## Alternatives considered

- **Leave placement to the intake conversation and correct afterward.** Rejected: the correction is a retirement and a re-authoring, so the cost lands on a path that has to write two documents twice.
- **Move the item** — `git mv` to the new owner's `working/`, rename the lobespace on every document, update the runbook's branch declaration, re-run setup at the new home. Rejected: the frame drag is the entire cost. The plan and decision record fall out of sync with the new parent and siblings whichever way the files travel, so the rewrite the move was meant to avoid is required anyway — the move only adds a mutation on top of it, plus a window in which routing signals resolve to a home the item has half left.
- **Defer ownership past intake** until the work's reach is known. Rejected: the owner decides where the documents live and which lobespace they carry, so deferring it leaves the scaffold homeless from day one.
- **Have setup's audit find the predecessor** — widen the audit to search every lobe by slug and report a match as a probable predecessor. Rejected: a retired predecessor sits in `archive/`, which the audit excludes because its names match new slugs without belonging to them, and a predecessor still open is already read by setup's alignment against other open items whenever its lobe is one the work concerns. The successor's author knows the predecessor; the line records what they know.

## What this doesn't solve

- **Mis-predicted reach.** A better-informed decision at intake is still a prediction. Supersession is the path for the ones that miss, not a reason to place carelessly.
- **Knowledge placement**, which closeout settles by reach when an item concludes, independent of where the item lived or whether it was ever superseded.
