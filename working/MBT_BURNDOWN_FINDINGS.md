# Burndown: Decision Record

## Problem

A work item's checklist document is named TASKS and described as "Checklist: PR wrangling, testing, docs, closeout." Its mechanics are sound and are not in question: it is unversioned, out of the read index, scaffolded at setup, retired at closeout, and read at closeout for deviations and reversals. The name and the framing around it are the problem.

*Tasks* is the most general word available for outstanding work, so a reader holding a plan in one hand and a document called TASKS in the other has no principled basis for deciding what goes where. Brains seeded from these templates have resolved it in incompatible directions: one wrote TASKS as a complete master list of everything open for the work item, restating the plan's implementation sequence; another wrote it as a summary of the plan's high-level items. Both are consistent with what the document says about itself. That is the defect — the framing admits both readings, and the name actively invites the first.

The consequence is three-way drift. The codebase, the plan, and the checklist each claim to say what remains, and they diverge the moment code is written. It also leaves a standing question no rule answers: how much are the plan and the checklist supposed to overlap?

Underneath the naming problem sits a lifetime problem the name conceals. **A plan and a checklist have different lifespans by nature.** A plan is an input to writing code; once the code exists, the codebase is ground truth and the plan is stale by construction. What remains after that — PR wrangling, review response, docs, ports, closeout notes — outlives the plan and never depended on it. But there is no sanctioned way to retire a plan early, because the follow-on work a plan accumulates, at its end or discovered while writing code against it, would be orphaned with it. So stale plans are kept alive to protect the items buried in them, and go on competing with the codebase for authority for as long as the item stays open.

## Preferred approach: rename to BURNDOWN and define the pair by its handoff

**A plan gets the code written. A burndown gets the code pushed upstream.** Two sides of one coin: one document is consumed to produce the change, the other is consumed to land it. Four commitments follow.

- **The burndown is a finishing checklist: everything between working code and a merged PR.** Stated as a positive scope — a reader asking "must this happen before this ships?" — rather than as an exclusion from the plan or an instruction to summarize. The scope ends the overlap question by construction: implementation planning is work already done, so it cannot appear on a list of work remaining.
- **Its items come in two kinds.** *Routine* items are inherited defaults — branch, draft PR, review, full retest, review feedback, closeout notes — that each brain refines to match its PR conventions. *Custom* items are this item's own: a port, a doc screenshot, a follow-on the code revealed. Both kinds share one document because both answer the same question.
- **The burndown is standalone and never names the plan.** It is written to survive the plan's archival, so a reference to the plan would dangle at exactly the moment it mattered most.
- **Early plan archival becomes a sanctioned, user-requested move.** When the developer asks for it — typically once the plan has been converted to code — the plan retires to `archive/` mid-item. Before the plan moves, the agent walks the developer through any significant unaddressed items to decide per-item what belongs in the burndown. The agent does not offer early archival unprompted — retiring a plan someone is still working from is the wrong kind of helpful.

A work item that concludes without a merge is by definition unfinished. The burndown is the definition of done — a list that goes to zero when the item ships — so a canceled or reframed item retires its burndown part-full rather than driving it to zero.

**Why the rename carries the fix rather than a wording change.** A name is the only part of a document that appears in every reference to it, including its own filename, so when the name and the instructions pull in opposite directions the name wins. A *task list* means, in ordinary usage, everything you have to do — it asks for a master list, and a reader who produces one has read it correctly. A *burndown* names a quantity that goes to zero against a scope fixed when it opened. The question the writer asks changes with the word: "must this be done before this ships?" rather than "is this a thing to do?" The first question excludes the plan's contents automatically; the second includes all of them.

## Alternatives considered

- **Keep the name, tighten the prose.** Rejected. The mechanics are already stated clearly and the drift happened anyway, in more than one brain, in different directions. When prose has to work against the name on the file, the prose is read once and the name is read every time.
- **Delete the document and fold its contents into the plan.** Rejected — it makes the lifetime problem strictly worse. The remaining work would then live in the one document guaranteed to go stale, and early archival would become impossible rather than merely undefined.
- **Split it in two: a fixed routine checklist and a follow-on list.** Rejected. Routine versus custom is a property of individual rows, not of documents, and two files to consult before a PR is ready is exactly the did-I-miss-one failure a burndown exists to prevent.
- **Other names weighed.** CHECKLIST and TODO carry the same everything-you-have-to-do sense that TASKS does, so they reproduce the defect. REMAINING is accurate but silent on remaining-before-*what*, which is the part that does the excluding. SHIPPING and LANDING name the destination but not the shrinking quantity. BURNDOWN carries both the destination and the goes-to-zero property, and has no ordinary-English sense waiting to be mistaken for it.

## What this doesn't solve

- **Whether a burndown is complete.** Nothing verifies that a follow-on discovered while coding was actually written down. The rename makes the right home obvious; it does not make the writing automatic.
- **The manual test plan, which has the same lifetime property.** Manual checks outlive the plan exactly as the remaining work does, and are not addressed here.
- **Judging when a plan is stale enough to archive.** The move becomes available; deciding that the moment has arrived stays with the developer.

## Reversals

Two claims become false rather than merely renamed.

The checklist's stated role — "Checklist: PR wrangling, testing, docs, closeout" — is replaced by a positive scope statement, so a reader can no longer derive its contents from an enumeration of categories. Reconcile in place.

`MBT_PATTERN.md` states the version-header exemption as applying to "task checklists", which stops being what the document is. The filename glob that expresses the exemption in seven documents, this one among them, is a rename; the phrase describing what is exempt is a reversal.
