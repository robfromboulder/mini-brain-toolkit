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

---

# README repositioning, the project-repo hook, and the product→project sweep (2026-07-27)

**Session ID**: `f9e592d2-1f41-451c-b00f-67f0ac704b1a`

Rob's session, with Claude as co-author. It set out to score three candidate differentiators for the pattern against the second-brain landscape and retool the README around the strongest ones, and grew into three deliverables: a fully rewritten README, the Nebula-derived "working in the mini-brain" hook absorbed into the toolkit (`templates/PROJECT_HOOK.md` plus wiring in the pattern, the create procedure, and the approach), and a repo-wide terminology change from "product repo" to "project repo." Nothing committed — Rob asked for closeout without commit.

## Turn by turn

- Rob proposed three differentiators: software-project-shaped with multi-author/GitHub affinity; fully agentic (no need to understand the pattern to use it); and chats-as-the-raw-content, citing the Nebula brain's proactive session-closeout prompt as the development that most increased brain use. Claude scored chats-as-raw-content strongest (it answers the "I don't have time to maintain it" objection and had observed adoption evidence), software-shaped next (with the connected observation that a codebase ground truth is what makes shrink-by-design operational — a personal second brain has nothing to diff against), and fully-agentic strong only if worded to avoid reading as *automatic* capture, the pattern's anti-position.
- Tracing the closeout-prompt instruction found it in the Nebula *product repo's* `CLAUDE.md`, not the brain's own files — meaning the README couldn't honestly claim just-chat behavior until the toolkit shipped the hook. Absorbing it became a prerequisite of the rewrite.
- Rob supplied the hook's origin story: Nebula used its brain before any product repos existed, early work items were thought through in the brain and rolled out as code, and once developers shifted to iterating in the main repo, switching directories to use the brain was instantly awkward; the bidirectional structure fixed that. This became the pattern's "the workflow follows the developer in both directions" framing and the approach's new merged-not-copied design decision.
- Claude drafted the hook template (stage-3 pieces held in a maturity comment, matching the entrypoint template's convention) and wired it in: the own-repository principle gained the hook as its load-on-demand mechanism, the seed file set notes the one piece living outside the brain, the lifecycle gained the closeout offer at natural stopping points, and the create procedure gained a project-repos intake question, a merge-don't-overwrite seed-table row, and a stage-3 uncomment note. The check procedure needed no edit — it works off the principles.
- The README then went through many rounds of tightening driven by Rob against a "skeptical reader who knows second brains" standard: much shorter, no claim that invites challenge, no abstraction the reader must map themselves.

## Decisions

- **Drop the tagline entirely** — Rob's call, after asking for an honest opinion and Claude argued "self-improving software" claims the wrong subject (the *brain* is self-improving) and pattern-matches to AI hype. Replacement candidates all provoked questions they didn't answer ("why does small mean trustable?"), so the fix was removal; the opening sentence gained "about your software project" to absorb the tagline's anchoring job. For the GitHub repo description, Claude recommended "Capture the why behind your code, just by chatting with Claude."
- **Kill the unprovable growth claims** — Rob's call. "Most knowledge systems die of growth… until nobody trusts them" was rewritten as the active, demonstrable "Mini-brains are self-improving" paragraph and moved last, its dreaming list settled at verify / prune / follow-on research with "curious about what it doesn't know" as the earned closer. Rob trimmed the list to three items; Claude argued "identifying potential conflicts" would duplicate verification and orphan the curiosity line, and "surfacing open questions" went too, for scan weight.
- **The unification thesis leads** — Rob's course-correction: triage and estimates are aspects of the benefit, not the benefit; the benefit is code plus never-in-code knowledge as a single vehicle, versus details scattered across heads, tickets, wikis, and product docs.
- **Keep "just Markdown files"** — Rob questioned the diminutive; Claude argued it is load-bearing (it answers "what do I have to install?") and "organized using" would raise questions instead; Rob accepted.
- **"Project repo," not "product repo"** — Rob's call after the README settled on "project repos." Swept through the pattern, both procedures, the approach, and the templates; `templates/PRODUCT_HOOK.md` renamed to `PROJECT_HOOK.md`. Deliberately kept: "the product" as the shipped artifact in the own-repository principle, "product brain" as the dream cycle's term for a non-research brain, "production" systems, and the README's "product docs."
- Version calls: the hook work was substantive (`MBT_PATTERN.md` V11, `MBT_CREATE_BRAIN.md` V10, `MBT_APPROACH.md` V7); the terminology sweep was classified editorial, no bumps.

## What didn't work

- Claude's first README rewrite failed the skeptic test in review: too many words, "codebase keeps the brain honest" was an internals lecture where the reader needed an outcome, and the epistemology of re-derivability belongs in the docs, not the advert.
- The approach doc's new design decision initially wanted to cite the pattern and procedure docs by name — disallowed by its declared upstream-only exemption (scope only); reworded to speak of "the establishment procedure" generically.
- The adoption evidence behind the hook (the closeout prompt's effect on Nebula) had to stay anonymous in public-facing text; the approach doc cites "the exemplar where it emerged."

## Lessons

- The skeptic test is the strongest editing tool this repo has found for outward-facing prose: every sentence must be self-evident, demonstrable in the repo, or cut. It killed the tagline, the growth claims, and half the word count while making the claims stronger.
- Show mechanism, not category: "a periodic agent-run pass" lost the reader; "verifying all claims against the codebase" convinced them. The concrete list *is* the argument.
- Adoption-side differentiators (nothing-extra, team-shaped) are the wrapper that makes the content-side differentiator (shrink-by-design) land; stated alone, shrink reads as philosophy.
- A README claim is a toolkit obligation: "you'll be asked to save what the session decided" was true of one project's local practice until the hook template made it true of the toolkit. Positioning work surfaces shipping gaps.

---

# Repositioning fallout in the research docs, the follow-on-research rename, and dream-cycle cost containment (2026-07-27)

**Session ID**: `8f53a437-1774-4746-9d97-c4e259b182f5`

Rob's session, with Claude as co-author. It opened as a review of how the README repositioning lands on the comparison docs and grew into four deliverables: the research agenda absorbing the new positioning as comparison surfaces to defend, a repo-wide retirement of "currency check" in favor of "follow-on research" and "freshness," a rewrite of the research agenda as a standalone document free of run-history narration, and cost-containment controls folded into the dream cycle after a post-mortem of the expensive dry run. Committed at closeout.

## Turn by turn

- Rob asked how the repositioning commit impacts the comparison docs. Claude found no facts invalidated — the impact was one-sided: the outward positioning staked three claims (just-chat capture, team-owned via PR, self-improving) while the research agenda only defended shrink-by-design. Each new pillar already had a nearest threat sitting in the registry: Copilot Memory (frictionless but uncurated — a review/approve step there would attack a headline pillar), and Letta's git-backed Context Repositories (makes team-shared, PR-reviewed memory natural; the landscape had never been scored per-user vs. team-shared). Also surfaced: the hook makes the instruction-file family our delivery channel, not just our anti-pole; the README's speed/autonomy claims rest on evidence gaps the agenda itself admits; and a tension between the README's "every brain does follow-on research" and the agenda's "a product brain's research pass is a plain currency check."
- Rob said address it all, and resolved the tension: dream cycles are core to the pattern even though young brains defer them, and follow-on research with curiosity about what it doesn't know is what every brain's dream does — only the registries are toolkit-specific, because this brain's field happens to be the memory-systems landscape. Claude added the two-layer positioning and a fifth comparison thread (stress-test the adoption pillars), widened the Copilot/Letta/CLAUDE.md watch signals, and swept the terminology.
- Rob then flagged that the research agenda narrated its own history — a first deep pass, dated headlines, "done" markers — pointing at dream-cycle runs whose logs were deliberately not kept (the dry run). Claude confirmed the dream log holds only its header and rewrote the agenda as standing conclusions: run-status markers became "Standing result:" / "Open," provenance sentences and dated headlines went, external world-facts with dates stayed.
- Rob asked for a cost evaluation of the dream cycle with a dry run if needed. Claude traced the file history: the expensive run happened under the original instructions, whose research phase was a from-scratch field survey with agent fan-out per family; the registry refactor the following day was already the cost fix, converting the phase to a delta pass. A dry run of the structural phase (all checks pass, effectively free) plus sizing showed the residual risks: every registry date is identical (the fossil of the one big run), so "select the stalest" selects everything; no numeric agent budget anywhere; agent-mandatory delegation for reads of a few hundred lines; the research phase unconditional; the disconfirmation gate readable as extra searches; and the empty dream log disconnecting the instructions' own effort-calibration loop.
- Rob challenged the proposed cap: a full re-baseline shouldn't take multiple cycles of hoping for coverage. Claude's answer — the cap is a default, and the invocation is the override point — held, plus two softeners: a capped rotation self-converges in about three cycles via the verified dates, and a full re-baseline under the delta workflow is change-checking, not the synthesis that made the first run expensive.
- Rob approved folding everything in. Claude added to the dream cycle: a ~10 sub-agent budget per routine cycle (exceeding it is a report flag), the ~5-stalest triage cap with the full-re-baseline override, a nap gate (skip the research phase when all registry dates are fresher than ~30 days and nothing is flagged), fetch-before-agent for change-checks, size-conditional delegation at roughly 500 lines (also in the template), the disconfirmation-is-not-extra-fan-out clarification, and keep-the-log-even-for-dry-runs. The roadmap's sleep-pressure item was marked partly operationalized.
- Rob had Claude add a dream-cycle entry to the README's usage section, then reverted it: dreaming is for contributors, not end users of the toolkit.

## Decisions

- **"Follow-on research," not "currency check"** — Rob's call, on connotation ("currency" reads as foreign-exchange) and substance: the phrase pair "follow-on research" / "curious about what it doesn't know" is the pattern's real claim. "Freshness" took over where the meaning is genuinely re-checking dates. Swept through the research agenda, both registries, the dream cycle, and the template — the dream cycle's research phase is now named "Follow-on research."
- **Every brain dreams with curiosity; only the registries are toolkit-specific** — Rob's call, resolving the README-vs-agenda tension in the README's favor. A product brain's follow-on research targets whatever its project depends on; the adversarial attack-the-thesis mandate stays exclusive to this research brain.
- **The research agenda stands alone** — Rob's call: no references to its own revision history or to dream-cycle runs whose logs weren't kept. Conclusions are stated as standing results; the freshness trail lives in the registries' verified/reviewed dates.
- **Budget as default, invocation as override** — Rob probed, Claude recommended, Rob accepted: routine dreams check the ~5 stalest entries and stay under ~10 sub-agents; asking for a full re-baseline lifts the cap and the nap gate for that run.
- **Dream cycle stays out of the README** — Rob's call after seeing it added: contributor-facing machinery, wrong audience for the usage section.
- Version calls: one bump per uncommitted change-set even across multiple editing rounds (research agenda, comparables registry, and dream cycle each absorbed several rounds under a single bump); the biology registry's terminology rename was classified editorial, no bump.

## What didn't work

- The README dream-cycle usage entry — written, then reverted the same session for audience mismatch.
- "Select the stalest" as the sole triage rule — defeated by its own history: one big baseline run left every entry equally stale, so the rule selected everything. Uniform dates need a numeric cap, not a comparative.

## Lessons

- A positioning rewrite creates research obligations: every new outward claim is a comparison surface that needs its own stress test, and existing registry watch signals change stakes when positioning changes — a review/approve step in a competitor went from side-note to pillar threat without the competitor doing anything.
- Run-history framing in a conclusions doc rots the moment the runs' logs aren't kept. Conclusions docs should state standing results; provenance and freshness belong in the registries.
- The expensive dream was the one-time baseline build, not the steady state — but qualitative cost guardrails ("keep the fan-out small") don't survive contact with edge cases like uniform staleness; numeric defaults with explicit user overrides do.
- Discarding a dream log entry discards the mechanism that makes the next cycle cheaper: orientation and effort calibration read exactly that log.
