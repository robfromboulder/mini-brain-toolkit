# Work-Item Relocation: Decision Record

## Problem

A work item's owning unit is settled at intake as the nearest common ancestor of the units the work *will* concern — a prediction. Mid-flight scope growth can invalidate it: a child-owned item turns out to need a sibling's changes, so the owner should have been their parent. What happens then is undefined.

## Preferred approach: items don't move, they are superseded

A work item stays in the unit where it was opened, for its whole life. When its reach outgrows that unit, the item retires as **superseded** and a new item opens in the correct unit, authored against what is now known — the fuller problem, the corrected owner, and the relationships to its new parent and siblings.

This extends a principle already on the books rather than introducing one: work closeout holds that an item retires where it lived, even when its knowledge folds upward.

Three reasons to prefer it over moving the item:

- **It matches the grain.** The pattern is append-only records plus canonical documents rewritten freely. A `git mv` with a token rename across every document is neither — it mutates a record in place so that it reads as though the work had always lived somewhere else.
- **It reuses procedures that already exist.** Retirement and setup both work today. A move would need a bespoke procedure, and a half-moved item that closeout and session routing each have to tolerate.
- **The logs stay put, which is correct.** A superseded item's log entries merge into the *original* owner's canonical log under their original session IDs, because those sessions genuinely concerned that unit. Splitting an item's lineage across two units' logs is an accurate record of work that happened in two places; a move would have to fabricate one continuous history for it.

The policy needs one piece of new machinery and one convention:

- **A supersede retirement** — archive the working documents *without* folding their findings into canonical documents, since a relocated item is not concluded and its findings are not yet settled. Merge the log entries as normal and record the successor's slug.
- **A predecessor line** in the successor's FINDINGS, so the lineage is legible from the documents and not only from the log.

## Alternatives considered

- **Move the item** — `git mv` to the new owner's `working/`, rename the token on every document, update the runbook's branch declaration, re-run setup at the new home. Rejected: the frame drag is the entire cost. The plan and findings fall out of sync with the new parent and siblings whichever way the files travel, so the rewrite the move was meant to avoid is required anyway — the move only adds a mutation on top of it, plus a window in which routing signals resolve to a home the item has half left.
- **Defer ownership past intake** until the work's reach is known. Rejected: the owner decides where the documents live and which token they carry, so deferring it leaves the scaffold homeless from day one.
- **A setup-audit guard as the answer** — widen the audit so re-running setup under a corrected owner cannot silently scaffold a duplicate. Rejected as the primary fix: it treats the duplicate as the failure, when under this policy a same-slug item in another unit is the *expected* state during a supersession. The audit should surface it so the two get linked, not prevent it.

## What this doesn't solve

- **Final knowledge placement**, which is untouched: closeout places each finding by reach, so knowledge reaches the right units whether or not an item was ever superseded.
- **How intake settles the owning unit.** Making relocation deliberate raises what a good first placement is worth, but the method for deriving it is a separate question.