# Mini-Brain Toolkit: Session Log

Running log of mini-brain-toolkit sessions. Each session appends after a `---` separator. Read only from the last `---` separator forward — this file grows large.

---

# Full-strict orthogonality pass and the CHECK fail-stop decision (2026-07-24)

**Session ID**: `6a7faae8-7adc-4850-abdc-e23af7a5375e`

Rob's session, with Claude as co-author. Rob asked for a file-by-file pass bringing the top-level knowledge docs into line with the just-added "Writing Docs and Instructions" conventions. The open question was how strictly to read the cross-reference and orthogonality rules; Rob chose full strict enforcement. The pass rewrote several docs to stand on their own, added two exemption-table rows, and — through a course-correction Rob drove — turned the check procedure's "not a mini-brain" branch into a hard stop.

## Turn by turn

- Read every top-level knowledge doc and split the findings into clear convention breaks (foreign section-number citations, sibling references outside the declared exemptions, sideways narration) and genuine judgment calls (whether a design or reference doc may name the product docs it discusses). Rather than pick a depth unilaterally, asked Rob how strict to be; he chose full strict.
- Applied the pass. Foreign section numbers became name-plus-description. `MBT_APPROACH.md`'s design decisions were reworded to stop naming the reference and the two procedures — describing them by what they are rather than by filename. `MBT_PATTERN.md` dropped its narration of what create and check do, so it stands alone. `MBT_SCOPE.md` dropped its pointers to the research agenda. `MBT_BIOLOGY.md`'s mechanism labels were de-tokenized to match its own bare labels. `MBT_DREAM_CYCLE.md` kept the docs it operates on (the maintenance carve-out) but lost its claim-support citations. Each touched file was bumped.
- On Rob's request, added `MBT_PATTERN.md` and `MBT_RESEARCH.md` to the exemption table, both *none* — the pattern reference is foundational like scope, and the research agenda's only reference candidates are the downstream registries that feed it. Put research above those registries in the table so it reads define-before-use.

## Decisions

- **Full strict enforcement** (Rob's call) resolved the recurring judgment call: a design or reference doc does not name the sibling deliverables it discusses, even when that forces a generic description. This drove the approach and pattern rewrites.
- **The check procedure now fails stop when the target isn't a mini-brain** (Rob's call, reversing Claude's recommendation). Claude first argued to keep a check-to-create handoff, reading it as a control-flow pointer that is load-bearing when the check doc is loaded on its own. Rob rejected that on safety grounds: asking to check a directory presumes a brain already lives there, so pivoting to creation is a state-changing action that could overwrite or damage the target — the more so under auto-approval. The right behavior is to stop, report, and let the user confirm the path or intent, doing nothing else. This also dropped the cross-procedure reference outright, so no carve-out to the maintenance-doc boundary was needed after all.

## What didn't work / course corrections

- Claude's first instinct on the check-to-create question was the wrong frame — it treated "how do I make this handoff legal under the orthogonality rules" as the problem, when the real problem was that the handoff should not happen. A failed precondition in one procedure is a reason to stop, not to invoke another procedure that changes state.
- The final full-file verification (Rob asked for it explicitly) caught a contradiction the editing pass had walked straight past: `MBT_CREATE_BRAIN.md`'s authoring step still told new brains to "cite SCOPE goals by section" — the exact section-number anti-pattern the pass existed to remove, and one the templates' own conventions forbid. Fixed to cite by name. A comment in `templates/CLAUDE.md` also carried a toolkit filename as a numbered pointer into every seeded brain — a dangling reference the check procedure would later flag in the new repo — fixed to a name-plus-description.

## Lessons

- Strict orthogonality sometimes has no rewrite that keeps the sibling's name; the escape is to name the decision by what the sibling *is* ("the reference," "the assessment procedure"), not what it is called.
- A verification read-through earns its keep over a diff review: the "cite by section" contradiction was pre-existing, untouched by the pass, and invisible to anyone reading only the changed lines — only a full read against the convention surfaced it.

---

# Writing-conventions audit and dedup pass (2026-07-26)

**Session ID**: `afb3e0b3-2a50-46d2-868f-3855366b4bc8`

Rob's session, with Claude as co-author. Rob asked for a file-by-file verification that the ten locally changed files follow the "Writing Docs and Instructions" conventions — assessment first, no edits. The review found the already-staged cleanup mechanically clean but left a cluster of say-it-once violations plus one literal forward pointer; on Rob's "fix all of these," Claude applied the fixes across nine files (`MBT_FINDINGS.md` was the only fully clean file) and bumped each edited file's version.

## Turn by turn

- The review deliberately covered whole files, not just the staged hunks. Mechanical checks — hard wrapping, version headers, sibling naming against the declared exemptions, foreign section numbers — all passed; the staged changes had already stripped foreign section-number references and downstream sibling references. Everything that survived was prose duplication, plus the dream cycle's "(see there)" forward pointer.
- Claude reported findings without editing. Rob then said to fix everything, and the fixes went in as a second pass ending with a verification sweep: greps confirming each formerly duplicated phrase now appears in exactly one file, all internal section references resolve, and headers are well-formed.

## Decisions

Rob made the single call to fix all findings; the per-fix editorial choices were Claude's. The recurring choice was picking each duplicated fact's one home, decided by the upstream/downstream rule and by which doc owns the concern:

- Verdicts live in `MBT_BIOLOGY.md`'s mechanism-mapping table; the per-field entries keep only research, review dates, and candidate status. The registry's at-a-glance candidate table and its Sources section were deleted outright as complete second copies of the per-field entries, and its intro paragraphs restating the dream cycle's refresh procedure and adversarial stance were deleted — the procedure doc is their home.
- The headline biological-grounding verdict lives in `MBT_RESEARCH.md` (confirmed by reading it: the wording was already there near-verbatim), so `MBT_BIOLOGY.md`'s copy was deleted rather than kept as a "summary."
- The dogfooding rationale lives in `MBT_APPROACH.md`; the corresponding `MBT_SCOPE.md` goal now states the outcome only. Same pattern for the defer-mature-machinery rationale: `MBT_APPROACH.md` keeps the why, `MBT_CREATE_BRAIN.md` keeps only the instruction.
- Observe-only is stated once, in `MBT_CHECK_BRAIN.md`'s stance paragraph; the abort case and the report step now just act on it.
- `CLAUDE.md`'s "No sideways narration" writing bullet was narrowed to sibling sections, making the "Orthogonal content" convention the sole owner of the cross-file rule — the two had carried the same prohibition with identical examples. Mirrored in `templates/CLAUDE.md`.
- `MBT_APPROACH.md`'s standalone design decision on the three-document split was merged into the strategy section that already argued it, keeping the alternative weighed (one combined doc) and the cost (reader must pick a file); the decisions list renumbered.

## What didn't work / course corrections

- The review report omitted `MBT_PATTERN.md` from its per-file verdicts entirely — an outright miss, caught during the fix pass, disclosed to Rob, and fixed alongside the rest (its "In short" principles recap and the lifecycle section's restatement of the stage-table file roles).
- Trimming `MBT_CHECK_BRAIN.md`'s authority sentence silently broke `MBT_DREAM_CYCLE.md`, which quoted that sentence's exact wording; the quote had to be reconciled after the fact. Paraphrase a sibling's rule, never quote it — a quotation is cross-file duplication with extra fragility.
- `templates/CLAUDE.md`'s maturity comment carried a toolkit filename into every seeded brain — a dangling reference the check procedure itself would then flag in the new repo. Found only by asking "what happens when this file is copied"; template files need that question asked of every reference they carry.

## Lessons

- A cleanup pass can *create* duplication: the staged rewrite of `MBT_SCOPE.md`'s intro had tightened it into a near-verbatim collision with the problem statement two paragraphs later. Whole-file review catches what diff review misses.
- Summary tables and "at-a-glance" sections are where say-it-once dies quietly: `MBT_BIOLOGY.md` had grown three-to-four homes per fact (mapping table, tally, per-field entries, sources list), each individually defensible as a "view." The fix that held up was declaring one structure the data's home and making every other mention a pointer or deleting it.
