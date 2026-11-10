# Work-Item Placement: Session Log

Running log of implementation sessions. Each session appends after a `---` separator.

The first entry, and every one after it, follows the entry format and content rules in `MBT_SESSION_CLOSEOUT.md` — that spec is the authority, not the prior entry, since a fresh LOG file has none to copy.

---

# REHOMING folded in, and the plan brought up to the current procedures (2026-11-10)

**Session ID**: `7c2b9d32-fb57-405b-a124-62f1f716a7f1`

Rob's session, with Claude as co-author, reviewing every parked work item; the full account is in `MBT_LOG.md`. For this item the result is a rewritten PLAN and FINDINGS that hold both halves of the ownership question: deriving the owning lobe at intake, and superseding an item whose placement proved wrong. No template was changed.

## What changed for this item

- Rob chose to fold REHOMING into this item under this slug. Its two files are in `archive/` under their own names.
- The audit rework left the plan. Setup's audit reads only `working/`, so it cannot find a retired predecessor, and Claude's rewrite has the successor name its predecessor from the intake conversation.
- The plan now lists three edits: work setup's intake step, work closeout's retire step, and a predecessor line in the FINDINGS scaffold.
- The supersession test moved to the seeder's multi-lobe fixture. The three intake cases stay on a copy of the six-lobe prototype, since two subtrees need three levels.
- The open issue on whether a single-lobe brain skips the step was removed: work setup already says it does.

## Open

- Whether the successor opens before the predecessor retires. Claude's view is successor first, so setup's alignment step reads the predecessor while it is still in `working/`. Rob has not ruled.
- The derivation's only input is the registry's routing terms, which nothing maintains until MULTI_LOBE_DREAM lands.
