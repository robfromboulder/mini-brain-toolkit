# Component Layer — Session Log

Running log of sessions on the component-layer work item. Each session appends after a `---` separator.

The first entry, and every one after it, follows the entry format and content rules in `MBT_SESSION_CLOSEOUT.md` — that spec is the authority, not the prior entry, since a fresh LOG file has none to copy.

---

# Component layer deep review and hardening (2026-07-31)

**Session ID**: `403e9e4a-0a60-4555-ae23-6df3f4f24ac1`

Rob's session, with Claude (Fable 5, max effort) as co-author. It began as a review of the component-brains branch — whether the component layer can serve larger knowledge bases without breaking the two exemplar brains or complicating simple ones — using the virtual-view bootstrap plan as the reference structure. The review found no contraindication and three weak clusters; Rob redirected from assessment to repair, and the session became a fix-then-verify cycle over every document a component brain would instantiate. Landed as one commit (8bdd4a5): the two-tier placeholder contract, pinned routing and naming rules, template fidelity repairs, and a standing agenda in `working/MBT_COMPOUND_RESEARCH.md` carrying the open items with per-area confidence.

## Turn-by-turn

- The review scored ten areas and clustered the weaknesses in three places: a placeholder meaning two things at once in the maintenance templates, an entirely single-unit dream-cycle template, and holes in three of the five restructuring migrations. Everything scoring below 70 was stage-3 machinery the virtual-view seed would not touch, which set the session's scope — fix the seeding path now, leave the stage-3 design for a living brain.
- Fixing the placeholder began with evidence rather than design: nebula's instantiated work-setup showed the de facto contract — brain-token references made concrete at creation, per-item variables surviving to runtime. `<TOKEN>` joined `<WORK>` as a surviving runtime variable on that precedent, with single-unit brains resolving it through one definition sentence.
- While pinning the review's log-merge ambiguity, Claude deviated from the review's own suggestion (collective nearest-common-ancestor) and pinned merged entries to the owner's canonical log, because session closeout already sends the closeout session there — one destination, matching where the item retires. Sprawl beyond the owner was reclassified as the re-homing problem and deferred.
- Rob then asked for read-backs of each changed file in turn, and every pass caught real defects — two of them in this session's own fresh edits. The naming constraint as first written forbade every legitimate child document, since a child's name necessarily begins with its parent's token; it was restated in longest-prefix form. The substitution clause said component brains substitute the hub's token everywhere, contradicting the seeding step that puts each component's doctype set under its own token; it became a per-copy rule.
- The component entrypoint pass found fidelity drops rather than logic errors — load-bearing sentences present in the spec or the base template but missing from the component variant (the never-bare-CLAUDE warning, logs never archived, move-not-delete retirement, the maturity comment blocks) — plus a missing routing fallback for questions no component claims, added to spec and template in the same words.
- The bookend pass renamed the work item's "prefix" to slug (it collided with the hub-token variable in the same document), surfaced the runbook's undocumented load-bearing branch declaration, and formalized nebula's organic self-containment: a brain's copy of work setup inlines the six scaffolds so the brain stands alone without the toolkit.
- The same pass found the declared maintenance-doc boundary contradicted by the family's own practice — the dream cycle and work closeout both cite the session-closeout doc as the log-entry format authority, which the boundary forbade. The boundary now sanctions exactly that citation and holds the rest strict.
- The open items were distilled into a standalone agenda with rescored confidence — no delta narration and no reference to the review, which Rob renamed and archived as `archive/MBT_COMPOUND_FABLE_REVIEW.md` to preserve the point-in-time record. A last look before commit caught the renamed agenda's stale title and a `.gitkeep` resurrected by the file moves; Rob questioned its removal, and it stood after weighing the written convention against a permanent placeholder — the procedures recreate `working/` on demand, so an empty directory may vanish harmlessly.

## Decisions

- **Fix the seeding path now, design stage-3 machinery against a living brain** — every low-confidence area sat in machinery the virtual-view seed won't exercise (Rob's sequencing, adopting the review's recommendation).
- **`<TOKEN>` survives as a runtime variable rather than substituting conditionally by brain shape** — uniformity and the `<WORK>` precedent: one meaning per symbol (Claude's proposal under Rob's direction to apply the fix).
- **A work item's merged log entries land in its owner's canonical log, always** — simpler than collective ancestry, and it agrees with where the closeout session logs and where the item retires (Claude's deviation from the review text, reported to Rob and kept).
- **Naming is constrained by longest prefix** — no document may bear a name of which another unit's token is a longer prefix than its owner's (correction of this session's own first formulation, caught in read-back).
- **Instantiated brains stand alone** — work setup's six scaffolds are inlined at instantiation, never referenced from the toolkit (formalizing what nebula already did).
- **The review stays frozen; the agenda stands alone** — no updates to the archived review, no change-tracking between the two documents (Rob's requirement, for traceability).

## What didn't work

- The session's own first-pass edits shipped two defects that only the read-backs caught — the overbroad naming rule and the contradictory substitution clause. The branch's previous session had already recorded this exact failure shape (each round of inspection finding another defect); it repeated anyway.
- The declared maintenance-doc boundary had never been checked against the documents it governs, and practice had drifted through it in two places.

## Lessons

- Simulating a template post-instantiation, once per brain shape, is the test that finds template defects; every template pass found real ones that way, and none were visible from the template text alone.
- Prefer the precedent a living brain already set: both structural decisions this session — two-tier substitution and inlined scaffolds — were read off nebula rather than invented.
- Declared reference boundaries need the same mechanical verification as filenames: a rule about who may cite whom is testable by grep and had simply never been run.