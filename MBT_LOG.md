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

Rob's session, with Claude as co-author. It set out to score three candidate differentiators for the pattern against the second-brain landscape and retool the README around the strongest ones, and grew into three deliverables: a fully rewritten README, the exemplar-derived "working in the mini-brain" hook absorbed into the toolkit (`templates/PROJECT_HOOK.md` plus wiring in the pattern, the create procedure, and the approach), and a repo-wide terminology change from "product repo" to "project repo." Nothing committed — Rob asked for closeout without commit.

## Turn by turn

- Rob proposed three differentiators: software-project-shaped with multi-author/GitHub affinity; fully agentic (no need to understand the pattern to use it); and chats-as-the-raw-content, citing the exemplar brain's proactive session-closeout prompt as the development that most increased brain use. Claude scored chats-as-raw-content strongest (it answers the "I don't have time to maintain it" objection and had observed adoption evidence), software-shaped next (with the connected observation that a codebase ground truth is what makes shrink-by-design operational — a personal second brain has nothing to diff against), and fully-agentic strong only if worded to avoid reading as *automatic* capture, the pattern's anti-position.
- Tracing the closeout-prompt instruction found it in the exemplar *product repo's* `CLAUDE.md`, not the brain's own files — meaning the README couldn't honestly claim just-chat behavior until the toolkit shipped the hook. Absorbing it became a prerequisite of the rewrite.
- Rob supplied the hook's origin story: the exemplar project used its brain before any product repos existed, early work items were thought through in the brain and rolled out as code, and once developers shifted to iterating in the main repo, switching directories to use the brain was instantly awkward; the bidirectional structure fixed that. This became the pattern's "the workflow follows the developer in both directions" framing and the approach's new merged-not-copied design decision.
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
- The adoption evidence behind the hook (the closeout prompt's effect on that exemplar) had to stay anonymous in public-facing text; the approach doc cites "the exemplar where it emerged."

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

---

# Three checks upstreamed from the exemplar brain — exemption enforcement, open-question scrub, needs-human contract (2026-07-27)

**Session ID**: `84035be9-f5ac-47bd-ace8-bc1ee98150e4`

Rob's session, with Claude as co-author, run from the exemplar brain's repo — which is why the session ID lives under that repo's project dir rather than this one's. A rebuild of that brain's dream cycle ended with a litmus comparison against this toolkit's cycle; five toolkit mechanisms flowed into the exemplar (recorded in its own log), and the comparison surfaced six places its cycle was ahead. Rob had the three that stand alone upstreamed into `MBT_DREAM_CYCLE.md` and then into the generic template, and aligned one piece of vocabulary. `MBT_DREAM_CYCLE.md` V9 → V10; `templates/DREAM_CYCLE.md` updated in place (its version header is the new-brain placeholder and stays untouched). Nothing committed or pushed; left for Rob.

## Turn-by-turn

- Claude ruled individually on the six candidates where the exemplar was ahead, judging standalone helpfulness against what this brain already has. Three stood alone: **exemption-direction enforcement** — the declared-exemptions table in `CLAUDE.md` was a declared invariant with no check behind it, since the structural phase verified only that cross-references resolve, never their direction or citation form; the **open-question scrub** — the Open Questions section of `MBT_SCOPE.md` was never revisited by any phase, even as the consistency check's own machinery erodes its templates-and-reference-sync question; and the **needs-human-decision format contract** — the cycle log asked only for a "Questions for humans" section "mirroring the report," with no self-containment requirement and under a name the orientation step doesn't even search for.
- Three did not stand alone, and Rob agreed to drop them: boundary-bleed scanning (already covered by the dogfooding phase's orthogonality confirmation), work accounting (no substrate — no project repo, no runbook branch keys, and this brain runs no work-item closeouts on itself; only an own-repo orphan-commit sweep would port, left unadopted), and shared-section drift (nothing here is intentionally duplicated across repos unchecked).
- Upstreamed the three into `MBT_DREAM_CYCLE.md`: the cross-reference item now grades each reference against the exemptions table and the citation form — a stray section number is a mechanical fix, a forbidden-direction reference is probable content bleed and gets flagged; the dogfooding phase gained a third check scrubbing the Open Questions section against the artifacts the phase just read, flag-never-resolve; and the report now requires a standalone, self-contained `## Needs human decision` section (numbered items: context, what changed, the decision), with the weaker cycle-log sentence removed so the rule has one home, and the report's flag bullet widened beyond the thesis phases since extraction/reflow substance flags belong there too.
- Folded the same three into `templates/DREAM_CYCLE.md` in `<PREFIX>` idiom. The scrub was inlined into the claim-verification paragraph so open questions enter the agent briefs at spawn — the after-spawn-briefing ordering bug had been caught in the exemplar's fresh draft the same day — and made conditional on SCOPE carrying an Open Questions section, since a generated brain may prune it.
- Vocabulary alignment to close: the exemplar renamed its external-technology phase "External drift" (Rob's nit — "freshness" reads like a shampoo, the same class of complaint that retired "currency" here a session earlier), and the template's matching flavor bullet under follow-on research was renamed to match. This brain's adversarial follow-on-research phase title was untouched.

## Decisions

- **Upstream three, drop three** — Rob's call on Claude's per-item rulings; each candidate was judged on its own, against this brain's existing coverage, not as a bundle.
- **The template gets them too** — Rob's call, "while this is fresh in mind." All three are generic-brain checks operating on substrate the templates already ship (the exemptions table in the template `CLAUDE.md`, the Open Questions section in the template SCOPE), and the template is where future brains inherit them.
- **Section naming unified on "Needs human decision"** — the orientation step already searched for that phrase; "Questions for humans" was a latent mismatch the contract fixes.
- **Exemptions table referenced generically, not enumerated** — the new check cites the table as the authority rather than listing the covered docs, so it stays correct as rows are added.

## Lessons

- A declared invariant with no enforcement check behind it is drift waiting to happen — the exemptions table carried direction rules the structural phase never graded, even though that phase was already grepping every cross-reference it would have needed.
- Instructions that add to an agent's brief after its spawn point are un-executable in the order written; when porting any check near an agent spawn, put the duty into the brief's composition. Caught once in the exemplar's draft, avoided pre-emptively in the template port.
- Cross-brain comparison pays in both directions in a single pass — cost mechanisms flowed out of this brain, integrity checks flowed back in — and each brain's log carrying only its own side keeps both accounts readable.

---

# Session-log routing upstreamed from one exemplar brain and mapped onto a second (2026-07-29)

**Session ID**: `a90be50c-ecb5-478b-ba5f-4b10b802ecc5`

Rob's session, with Claude as co-author. Rob had watched sessions in the first exemplar brain write their entries to the permanent log instead of the active work item's log — an effective early closeout that leaks unstable work-item detail into permanent memory — and had already tightened that exemplar's session-closeout doc to fix it. This session folded that tightening into this brain and the template, mapped it onto a second exemplar brain with a differently split structure, and corrected a drift the mapping surfaced. Landed: `MBT_SESSION_CLOSEOUT.md` V3, `CLAUDE.md` V13, `templates/SESSION_CLOSEOUT.md` and `templates/WORK_SETUP.md` in place, and in the second exemplar's repo its session-closeout doc (V4) and work-setup doc (V15). Nothing committed in either repo; Rob staged the first round mid-session and the commit is pending.

## Turn-by-turn

- The first exemplar's change: one entry format across the permanent and work-item logs, a priority-ordered routing rule — explicit direction, then session content, then current branch, with the permanent log demoted to last resort — ask-don't-guess when signals conflict, and a carve-out sending the session that runs a work item's closeout to the permanent log, since the work-item log is merged and retired in that same pass.
- The template took the rule nearly whole, since template brains share the branch/PR work-item machinery; "product repo" became the template's existing "project repo" term. This brain took a reduced form: its work items are in-flight `working/` docs with no branch machinery and no separate project repo, so the branch signal dropped, the content signal carries the weight, and — with no work-setup procedure to scaffold a working log — first append creates it. `CLAUDE.md`'s maintenance-doc boundary line was the one sentence the change falsified ("governs `MBT_LOG.md`") and was widened to cover both logs.
- Second change in the first exemplar reviewed on Rob's pointer: a work item's declared branch may be a glob when the item lands across several PRs. The bulk of that change serves that brain's open-work-items status listing, which neither this brain nor the template has — not ported. The kernel that does translate: the routing rule's branch signal accepts "exact name or glob."
- Mapping to the second exemplar — one brain spanning two sibling products: it keeps two platform logs and no shared log, joins to two product repos, and holds one open work item with no runbook (hence no branch declaration). The routing rule landed with the platform log as last resort, picked by which platform the session's work concerns; a platform-agnostic session has no clear home, which was folded into ask-don't-guess rather than inventing a default from that brain's lands-on-one-platform-first convention. Its `CLAUDE.md` needed nothing — no boundary sentence to falsify, no listing machinery to receive the glob-status rules.
- The mapping surfaced drift: the second exemplar's work-setup doc said work-item prefixes carry no platform token, while every open item on disk is platform-prefixed — practice had converged on that brain's own file-naming rule. Rob had the doc corrected to match practice, with examples pointing at real current items.
- Read-back review before commit caught one defect: the glob allowance had been hung on the work-item runbook scaffold's branch line, and scaffolds are copied verbatim — the explanation would leak into every generated runbook as permanent noise (real runbooks in the exemplars carry no such clause). Moved to the `<work-branch>` substitution in `templates/WORK_SETUP.md`, the author-facing definition site; the scaffold reverted to pristine.

## Decisions

- **Content signal outranks branch signal** — carried over from the first exemplar and load-bearing beyond it: in the second exemplar an open work item can lack a runbook entirely, leaving content as its only signal (Claude's observation, Rob's ordering).
- **No invented defaults for unroutable sessions** — a platform-agnostic session in the second exemplar asks rather than defaulting to its lands-on-one-platform-first convention; extending "ask, don't guess" beats creating log policy the brain's owner never set (Claude's call within the mapping).
- **Ignore the first exemplar's status-listing machinery everywhere** — it has no home outside that brain; only the field-shape kernel travels (Rob's framing: skip what's too specific to translate).
- **Guidance lives where its reader is** — the glob grammar sits with the setup procedure that writes the field, its legality with the routing rule that reads it, and nothing rides the generated scaffold (Claude, at the read-back review Rob asked for before committing).

## Lessons

- One rule, three reductions: the routing rule's portable core is the priority order, the last-resort default, and the closeout carve-out — which signals exist is a property of each brain's structure (branch/PR machinery, platform split), not of the rule.
- Scaffold templates are a distribution channel, not documentation: prose added to a template ships verbatim into every file generated from it, so author-facing guidance belongs in the procedure that does the generating.
- Mapping a rule onto a differently-shaped brain is an audit of that brain for free — the second exemplar's prefix drift only surfaced because routing forced a close read of how its work items are actually named.

---

# Component layer added as an opt-in convention set, from a three-project brain that broke the namespace (2026-07-31)

**Session ID**: `93f4946d-f171-4054-86d4-8c833f90bb86`

Rob's session, with Claude as co-author. It began as a review of a bootstrap plan for a brain spanning three sibling projects, which proposed six peer namespace families in one flat directory. The review found the scheme unparseable, and Rob redirected from "is this plan right" to "what does a brain look like at ten or thirty components" — which turned a brain-seeding session into a toolkit change. Landed: `MBT_COMPONENTS.md` V1 and `templates/COMPONENTS_CLAUDE.md` new, `MBT_PATTERN.md` V12, `MBT_CREATE_BRAIN.md` V11, `MBT_CHECK_BRAIN.md` V9, `CLAUDE.md` V14, and edits to the session-closeout, work-setup, work-closeout, project-hook, entrypoint and work-item templates. The brain that prompted it is planned but not seeded. Nothing committed in either repo.

## Turn-by-turn

- The proposed scheme varied the namespace token per project and appended module names to it. Reading both exemplar brains showed why that fails: each keeps one constant token acting as a pivot, so everything left of it is a platform and everything right of it is a work item, and every filename decomposes even at five underscores. Remove the anchor and a module log is indistinguishable from a work-item log — not hypothetical, since one exemplar already holds a work item whose name begins with the same word a module would have used.
- The scaling answer came from the second exemplar rather than from design: it carries ninety-six files behind an eleven-row index by refusing to enumerate its in-flight directory, stating a grammar and a discovery procedure instead. The pattern had already solved N-scaling once and only ever applied it to work items; the whole proposal is that mechanism moved up to the canonical layer.
- Four options were put to Rob. He rejected making the new layout canonical and framed the alternative: layer the conventions so simple brains never pay for them, let both styles live in one repo, and start simple with the option to grow. That framing held for the rest of the session. One correction to his reasoning: the flat fixed-pivot scheme bends the pattern *least*, not most — it is already-sanctioned text — so the case for the layer is scaling headroom alone, never pattern fit.
- Rob challenged whether the two modules of the middle project were really one component. Comparing the submodules settled it — different stacks, roadmaps, test suites and issue sets, and issues that touch one and never the other. Two problems, so two components, and components had to nest. The log-routing rule needed no rewording to absorb a third level, which was the first sign the recursion was real rather than bolted on.
- With modules as components, the layer's platform-qualifier slot had no user left. Rob asked whether that collapsed the need for it. It did — and then he supplied the fact that changed the reasoning underneath: the exemplar whose platform split looked like the argument for keeping the slot actually has two problem statements, one multi-model and one multi-tenant, carried under a single scope because everything was authored for the first platform and the second was ported against it. Opportunistic, not designed. That converted the only apparent instance of the category into an undeclared component split.
- Writing `MBT_COMPONENTS.md` surfaced six gaps in the specification it was written from, and reviewing it surfaced five more, three of them introduced during the drafting. All eleven were statement problems; none touched the structure.
- Rob's "stupid question" about session closeout was the last real gap: the closeout template's fallback assumed a single canonical log, and the one existing multi-log brain had hand-patched that rule rather than the template being fixed. A sweep for the same class of error then found the namespace token missing from work-item paths in roughly ten places, including the work-item scaffolds that generate cross-references into every real work item.

## Decisions

- **Layer the conventions, don't move the definition** — the pattern gains one sentence and a brain that never opts in reads it unchanged; neither exemplar changes a byte (Rob's framing, after rejecting the canonical-rewrite option).
- **Directories carve components, the trailing slot carves work items, and the token is declared per unit** — one mechanism per job, which is what restores the pivot the flat scheme destroyed (Claude's proposal, Rob's choice of the readable compound tokens over short opaque ones).
- **Placement by nearest common ancestor, siblings never named** — a fact about two units lives in the unit above them, which makes placement decidable rather than a judgment call. Rob's reason for taking it was enforceability in a structure where it is otherwise hard to tell where a fact belongs.
- **Drop the platform qualifier from the layer** — nothing would use it, and the base pattern still serves brains that split flat (Claude's recommendation on Rob's prompt; the evidence that the one candidate instance is really a component split arrived afterward and strengthened it).
- **A work item retires where it lived, but its knowledge is placed by reach** — an item owned by a child can push a finding up to its parent, because the child may not hold knowledge about a sibling (Claude, while making the two bookend procedures component-aware).

## What didn't work

- The delegating sentence, as specified, had the pattern doc name the new layer doc. That is a downstream reference, the one kind the toolkit's own rule says is never exemptable — it would have shipped as a live orthogonality violation in the most-read file. Rewritten to describe the convention inline and let the read index carry the pointer, which is exactly what the existing platform-split sentence does.
- An extra restructuring signal was invented while drafting the layer and cut on review: it did not discriminate between a unit that should split and a scope that was merely under-written, so it would have sent someone restructuring a brain when they should have finished a document.
- The checks were specified four times before any of them ran. Each round of inspection found another defect, ending with a prefix-matching rule that silently accepted a child's document sitting in its parent's directory — a false negative, the worst kind. Running them against both exemplars afterward confirmed one fix mattered: sweeping the retired-files directory into the token check would have raised four false failures in one brain and sixteen in the other.

## Lessons

- Look for the mechanism the pattern already has before designing one. Discovery-by-grammar was running over eighty-one files in a live brain; the contribution was noticing it had never been applied to the canonical layer.
- Writing the document *is* the test of the specification. Eleven defects surfaced between drafting and reviewing one file, none of which had been visible across five careful reviews of the proposal describing it.
- A section that restates another section's contents drifts every time that section changes — the proposal's list of what the new doc should contain went stale on four separate edits. Duplication that a rule would forbid inside a brain is just as costly in the document proposing the rule.
- Ask where a rule's reader actually looks. Log routing was specified in the conventions layer and was still missing from the closeout procedure, which is the only document a session opens when it needs to know.

---

# Scope authoring hardened after a full seed produced six status reports (2026-08-02)

**Session ID**: `e054f1be-03ab-4b37-a0dd-74f68fd3df60`

Rob's session, with Claude as co-author. A component-structured brain was seeded end to end against the current instructions, and every scope it produced described the project's own maturity instead of the problem's world. The instructions already said "solution-neutral" and "goals as outcomes, not deliverables", and they had been followed, so the fix was never more emphasis. Landed: `MBT_CREATE_BRAIN.md` V15, `MBT_CHECK_BRAIN.md` V12, `MBT_COMPONENTS.md` V3, `MBT_PATTERN.md` V13, `CLAUDE.md` V15, and edits to the scope, approach, entrypoint and component-entrypoint templates. Nine files, nothing committed.

## Turn-by-turn

- The failure was uniform across every unit, which ruled out carelessness in any one document and pointed at the instructions. Two things were diagnosed as causes. The section had a name and no definition, and the name it had invites exactly the wrong reading — a heading asking for the current state gets the current state of the thing being built. And the source material, being project documentation, was organized around the project, so distilling it preserved that organization unless the problem was deliberately re-derived. The second cause is the more general one: distillation carries the shape of what it distills.
- Two existing brains were read to calibrate what the section should hold. Both describe the world their problem lives in — what the environment already provides, what alternatives exist and where they stop — and neither reports on its own progress. That confirmed the convention existed in practice and had simply never been written down.
- Four rules went into the scope guidance, each stated with the test that catches its violation: the shipped-a-release test for status content, the could-a-different-design-satisfy-it test for goals, the shape-of-source-material warning, and a rule to report evidence at the strength the source gave it. The last came from an actual error in the seeded brain, where a source recorded what someone had done and the distillation invented why.
- Rob had independently reached the same conclusion about the heading and approved renaming it. He also scoped the change correctly: a heading that invites drift is worth renaming when touched, but a section under the old name whose content is right is not a finding. That distinction went into the check procedure so the rename never generates busywork against brains that predate it.
- Guidance was also moved to the point of use, as per-section comments inside the scope and approach templates that the author deletes while filling them. The procedure document is read once at seed time; the template is open at the moment the mistake gets made.
- The forward trace from design choices to goals found nothing wrong. Running it in reverse — for every goal, name the decision that answers it — found three goals with no answering decision in a single sitting, including one where the prose implied a mechanism handled a goal it did not. That pass was added to the approach guidance.
- Rob then directed two review cycles that the procedure did not describe: read every scope back as a group, and pair each approach with its own scope while explicitly *not* comparing approaches to each other. Both were added, with his reasoning for the asymmetry attached.
- Reviewing the additions found three defects at the joins, two of them introduced by the additions themselves. The check procedure's preamble tells a reviewer to delegate read-heavy passes to subagents, which is correct for per-document checks and fatal to set-level ones — a term collision is invisible to a reader holding one document. And the report structure predated four of the seven checks, leaving a reviewer nowhere to file the new findings.

## Decisions

- **Define the section rather than add emphasis** — the guidance that failed was being followed, so the gap was a missing definition, not weak wording (Claude's diagnosis, Rob's agreement).
- **Rename the heading, and treat the old name as cosmetic** — the new name carries the correction, while existing brains stay conforming and get flagged only when the section is next touched (Rob's call on both halves).
- **Put the rules where the work happens** — the template comments duplicate the procedure deliberately, because the two are read at different moments and only one is open when the error occurs (Claude's proposal, Rob's approval).
- **Scopes are reviewed as a set; approaches never are** — comparing sibling approaches invites the coupling the pattern forbids and pressures designs that legitimately differ into cosmetic agreement (Rob's instruction, and his reasoning).
- **A stale source is a finding about that source** — fact-checking turns up drift in the documents being distilled as often as in the brain, and reporting it back is part of the job rather than an obstacle to it (Claude).

## What didn't work

- The first rewrite of the scope guidance silently dropped an instruction it was replacing: strip strategy, tactics and vendor choices out of anything headed for the goals, and the pointer to where source material sits. The new goal rule covered the principle and lost the operative sentence. Caught only by reading the full diff rather than confirming the new text had arrived — reviewing one's own edits by checking that the intended change landed misses everything the change displaced.
- A rule against vocabulary collisions across documents was proposed and rejected as proofreading, then earned a place later when the same collision turned up in the seeded brain. The initial judgment was wrong about the category: a term meaning two things in two units is a structural defect, because each reading is defensible alone and only the set reveals it.
- A pre-existing miscount in the check procedure ("the two things that decay silently" above three bullets) was made worse by adding a fourth before being noticed. Additions to a list are a reason to re-read its introduction.

---

# Component layer deep review and hardening (2026-07-31)

**Session ID**: `403e9e4a-0a60-4555-ae23-6df3f4f24ac1`

Rob's session, with Claude (Fable 5, max effort) as co-author. It began as a review of the component-brains branch — whether the component layer can serve larger knowledge bases without breaking the two exemplar brains or complicating simple ones — using the multi-component prototype brain's bootstrap plan as the reference structure. The review found no contraindication and three weak clusters; Rob redirected from assessment to repair, and the session became a fix-then-verify cycle over every document a component brain would instantiate. Landed as one commit (8bdd4a5): the two-tier placeholder contract, pinned routing and naming rules, template fidelity repairs, and a standing agenda of the open items with per-area confidence.

## Turn-by-turn

- The review scored ten areas and clustered the weaknesses in three places: a placeholder meaning two things at once in the maintenance templates, an entirely single-unit dream-cycle template, and holes in three of the five restructuring migrations. Everything scoring below 70 was stage-3 machinery the prototype seed would not touch, which set the session's scope — fix the seeding path now, leave the stage-3 design for a living brain.
- Fixing the placeholder began with evidence rather than design: the simplest exemplar's instantiated work-setup showed the de facto contract — brain-token references made concrete at creation, per-item variables surviving to runtime. `<TOKEN>` joined `<WORK>` as a surviving runtime variable on that precedent, with single-unit brains resolving it through one definition sentence.
- While pinning the review's log-merge ambiguity, Claude deviated from the review's own suggestion (collective nearest-common-ancestor) and pinned merged entries to the owner's canonical log, because session closeout already sends the closeout session there — one destination, matching where the item retires. Sprawl beyond the owner was reclassified as the re-homing problem and deferred.
- Rob then asked for read-backs of each changed file in turn, and every pass caught real defects — two of them in this session's own fresh edits. The naming constraint as first written forbade every legitimate child document, since a child's name necessarily begins with its parent's token; it was restated in longest-prefix form. The substitution clause said component brains substitute the hub's token everywhere, contradicting the seeding step that puts each component's doctype set under its own token; it became a per-copy rule.
- The component entrypoint pass found fidelity drops rather than logic errors — load-bearing sentences present in the spec or the base template but missing from the component variant (the never-bare-CLAUDE warning, logs never archived, move-not-delete retirement, the maturity comment blocks) — plus a missing routing fallback for questions no component claims, added to spec and template in the same words.
- The bookend pass renamed the work item's "prefix" to slug (it collided with the hub-token variable in the same document), surfaced the runbook's undocumented load-bearing branch declaration, and formalized the simplest exemplar's organic self-containment: a brain's copy of work setup inlines the six scaffolds so the brain stands alone without the toolkit.
- The same pass found the declared maintenance-doc boundary contradicted by the family's own practice — the dream cycle and work closeout both cite the session-closeout doc as the log-entry format authority, which the boundary forbade. The boundary now sanctions exactly that citation and holds the rest strict.
- The open items were distilled into a standalone agenda with rescored confidence — no delta narration and no reference to the review, which Rob renamed and archived to preserve the point-in-time record. A last look before commit caught the renamed agenda's stale title and a `.gitkeep` resurrected by the file moves; Rob questioned its removal, and it stood after weighing the written convention against a permanent placeholder — the procedures recreate `working/` on demand, so an empty directory may vanish harmlessly.

## Decisions

- **Fix the seeding path now, design stage-3 machinery against a living brain** — every low-confidence area sat in machinery the prototype seed won't exercise (Rob's sequencing, adopting the review's recommendation).
- **`<TOKEN>` survives as a runtime variable rather than substituting conditionally by brain shape** — uniformity and the `<WORK>` precedent: one meaning per symbol (Claude's proposal under Rob's direction to apply the fix).
- **A work item's merged log entries land in its owner's canonical log, always** — simpler than collective ancestry, and it agrees with where the closeout session logs and where the item retires (Claude's deviation from the review text, reported to Rob and kept).
- **Naming is constrained by longest prefix** — no document may bear a name of which another unit's token is a longer prefix than its owner's (correction of this session's own first formulation, caught in read-back).
- **Instantiated brains stand alone** — work setup's six scaffolds are inlined at instantiation, never referenced from the toolkit (formalizing what the simplest exemplar already did).
- **The review stays frozen; the agenda stands alone** — no updates to the archived review, no change-tracking between the two documents (Rob's requirement, for traceability).

## What didn't work

- The session's own first-pass edits shipped two defects that only the read-backs caught — the overbroad naming rule and the contradictory substitution clause. The branch's previous session had already recorded this exact failure shape (each round of inspection finding another defect); it repeated anyway.
- The declared maintenance-doc boundary had never been checked against the documents it governs, and practice had drifted through it in two places.

## Lessons

- Simulating a template post-instantiation, once per brain shape, is the test that finds template defects; every template pass found real ones that way, and none were visible from the template text alone.
- Prefer the precedent a living brain already set: both structural decisions this session — two-tier substitution and inlined scaffolds — were read off the simplest exemplar rather than invented.
- Declared reference boundaries need the same mechanical verification as filenames: a rule about who may cite whom is testable by grep and had simply never been run.

---

# Pre-merge review closes twenty-one findings, dry-runs both brain shapes, and syncs the exemplar (2026-08-08)

**Session ID**: `7bec749a-e026-4e78-ba41-c53b4232419c`

Rob's session, with Claude (Fable 5) as co-author. It began as a deep final review of the component-brains PR before merge, using the multi-component prototype brain as the live example, and became the branch's hardening pass: a multi-agent verification review plus an independent validation converged on twenty-one confirmed findings, Rob directed that all be fixed one commit each for atomic review, and the session then ran the PR's own until-then-unchecked test plan and synced the prototype brain to the result. Landed: twenty-three commits on component-brains (4ef0af3 through 77e04fe) touching every canonical doc but the logs and the two registries, plus the prototype's sync commit in its own repo. Versions after: `CLAUDE.md` V17, `MBT_CHECK_BRAIN.md` V18, `MBT_CREATE_BRAIN.md` V19, `MBT_DREAM_CYCLE.md` V14, `MBT_COMPONENTS.md` V6, `MBT_APPROACH.md` V8, `MBT_FINDINGS.md` V10, `MBT_SESSION_CLOSEOUT.md` V4, `MBT_SCOPE.md` V7.

## Turn-by-turn

- The findings clustered four ways. Runnable commands that fail on healthy brains: the namespace check aborts under zsh whenever `working/` is empty or missing, its token grep matched anywhere in a filename, and the work-setup audit shipped an undefined unit-path placeholder with its errors suppressed — a silent-overwrite path through the very audit that promises idempotency. The toolkit not applying its own changes to itself: its session-closeout still routed by the pre-branch grammar while the branch itself opened three work items that grammar cannot tell apart, the entrypoint stated a weaker working-doc grammar than the one it ships, and the approach and findings docs made claims the branch had made false. Contract contradictions on the seeding path: the leave-runtime-variables-intact rule against the registry rows and hook paragraph that must be filled at creation, a seeded README claiming one brain-wide token, the component entrypoint carrying only two of the four placement rules, and the hook stating two grammars for one lookup. And the COMPOUND retirement had deleted its documents rather than archiving them.
- Every command fix was executed against fixture brains before shipping, including the failure cases — the old commands demonstrably fail open under zsh; the replacements tolerate a missing `working/`, anchor the token to the filename start, and were confirmed to catch a planted stray that the originals pass.
- Rob asked for a before/after quality rating and then for what would raise it: the answer was the PR's own test plan, still unchecked in its description. The dry run seeded a single-unit brain and a three-level component brain from the templates literally — nested tokens, a non-nested token, and a sub-component — and both came through with no improvisation required: the two-tier placeholder contract, per-unit substitution, registry fill and README reword all executed as written, and the check procedure passed on both. A planted misplacement (a child-token document at the hub root) was flagged by the new anchored command. The dry run's one finding was pre-existing: the README template's usage prompts cited filenames without their extensions.
- Two wording calls were walked through with Rob one at a time and both applied: the no-match log-routing rule, and the scope goal that had prescribed a document count.
- The prototype sync ported four lagging deltas into its entrypoint and closeout, kept five divergences as deliberate, and ran the check procedure as acceptance. Every mechanical check passed across its six units, and the new substance checks earned their place on first contact with real content: the hub scope elaborates its children's problems near-verbatim in three places, one open question arguably belongs a level down, and the hub approach carries a version range that will date within weeks. All reported to that brain rather than edited — checking observes.
- The sync surfaced a harvest candidate: both living brains independently grew a commit-conventions section and the project hook already depends on one existing, yet no template carries even a stub. Flagged for Rob; not acted on.

## Decisions

- **One fix, one commit** — the branch is reviewed as atomic diffs rather than start/end state (Rob's requirement, before any fix landed).
- **Restore the retired COMPOUND docs to `archive/`** — the written move-not-delete convention and the frozen-review-for-traceability decision already on record outweigh treating git history as the archive; the restoring commit is deliberately separable if the deletion turns out to have been intended (Claude's finding, Rob's direction to address all findings; the sessions of 2026-08-05 and 2026-08-07 that deleted and that added the omit rule left no log entries, and this entry is the record of that gap).
- **The no-match routing rule states the nearest-common-ancestor rule first**, with the single-unit case as a closing conditional — the template ships into both brain shapes, and wrong-then-corrected text in one shape is worse than inert-but-conditional text in either (Rob's choice between presented alternatives).
- **The definition goal names the outcome, not a document count** — "a single current document" failed the branch's own could-a-different-design-satisfy-it test and the goals section's own no-file-structure preamble; it now asks for one canonical current definition with each concern defined in exactly one place (Rob's call, as scoping judgment).
- **Check commands are enumerated fail-safe, not globbed** — an unmatched glob aborts the pipeline under zsh and an empty result reads as a pass, so the checks now enumerate with find and anchor their filters (Claude, verified empirically before shipping).

## What didn't work

- Every check command on the branch had been specified and reviewed repeatedly and executed never; the first real run falsified three of them in minutes. The log already records this failure shape twice — each round of inspection finding what only inspection can, while the defects that survive are the ones only execution finds — and it repeated anyway, this time as shell behavior rather than prose.
- The toolkit's own instantiated docs were the blind spot: the dream cycle's consistency pass compares the five teaching artifacts to each other but never to this brain's own entrypoint or closeout, which is exactly where the stale grammar sat unnoticed.

## Lessons

- A reviewed-but-never-run command is prose, not a check. Executing each one against a fixture — including its failure cases — is cheaper than one false pass from a check that fails open.
- The dry run per brain shape keeps earning its keep: after twenty-one fixes both seeds executed clean, and the one remaining defect it found sat in the oldest template nobody had touched.
- Reading a document set together finds what per-file review structurally cannot: the exemplar's parent-child duplication was invisible in every earlier single-file pass over those same documents, and became obvious the moment the scopes were read as a set.

---

# Remove commit-conventions dependency from the project hook template (2026-08-08)

**Session ID**: `a417fef1-dd6a-4a31-af07-71734d9d506c`

Rob's session, with Claude (Sonnet 4.6) as co-author. Addressed the harvest candidate flagged in the previous session: the project hook template told the agent to follow "the mini-brain's own commit conventions" at closeout, implying every downstream brain should have commit conventions. Rob's direction was that MBT has nothing to say about commit conventions for downstream brains — enforcing a policy there hurts adoption — and the only commit-convention text that belongs in the toolkit is what governs MBT's own development (the no-AI-attribution rule in `CLAUDE.md`). The fix was one sentence in `templates/PROJECT_HOOK.md`: drop the phrase "and it follows the mini-brain's own commit conventions." No work item was opened; the fix was immediate and required no design.

## Decisions

- **Drop the commit-conventions reference from the hook template entirely** — MBT should not prescribe commit conventions to downstream brains; doing so would alienate developers and hurt adoption. The MBT-specific convention (no AI attribution trailer) stays in `CLAUDE.md` and applies only to this repo's own development (Rob's call).

---

# Append-only redefined to let two logs merge, and work-item re-homing ruled out entirely (2026-08-08)

**Session ID**: `91e26ed2-da03-4ae7-bb07-2127a3764e95`

Rob's session, with Claude (Opus 5) as co-author. It opened as a sequencing question — whether two open work items should land together — and became a session that fixed a live contradiction in merged instructions, reversed a design direction that had been carried for weeks, opened a new work item, and left caveats on two moves nobody should run yet. Three commits landed on main (unpushed); everything after them — the working-doc rewrites, the two migration caveats, a findings promotion, and this entry — is uncommitted at session end.

## Turn-by-turn

- The sequencing question resolved by reading both plans: the two items were different in kind, not just in priority. Rob sharpened the distinction and it drove everything after — the collapse's log problem is a genuine hole in instructions already merged, while re-homing was far-out work that might need deeper hierarchy before its decisions could even be vetted.
- The re-homing plan's activation trigger was retargeted from "the prototype's first live work item" to hierarchy depth, on Rob's reasoning that at two levels every re-home has exactly one possible destination, so a live example would confirm a procedure while being incapable of falsifying it. Fixture shapes were written into the plan for the cases only depth exposes.
- The log-fold question went to Rob as a choice between leaving the retired hub log in place and folding it in summarized, with a recommendation to append it verbatim under a dated wrapper. Rob rejected the framing: append-only should protect each entry's *content*, not its position, which makes merging by date legal. Checking every place the rule is actually written confirmed he was reading it as already stated — the pattern doc says "never edited after the fact," work closeout says "never revise content above the new separator," and both are content claims. This repo's own log was already out of date order, since work closeout preserves each merged entry's original date.
- That falsified the recommendation rather than refining it. Appending verbatim leaves an old entry at the file's tail, breaking the read-from-the-last-separator ritual the check procedure names; a date merge preserves it. The fix therefore reached five files rather than the single table row originally promised, and Rob approved the wider surface before it was written.
- With the bug fixed, Rob directed that the migrations item be rewritten against the corrected files, explicitly without a "part 1" the same session would immediately close. Rewriting it surfaced something the item had never recorded: the extraction move has no inverse. Absorbing an existing standalone brain as a component is not in the table, and is not extraction reversed — extraction mints an entrypoint and maintenance set for a subtree that lacks them, absorption sheds the ones an arriving brain already has.
- Rob then questioned re-homing itself and proposed the simplifying policy: a work item never moves. One that outgrows its unit retires as superseded and re-opens in the corrected unit, authored against what is now known. Both re-homing documents were rewritten to that policy, which removed the depth gate, the fixture apparatus and the audit guard in a single stroke — all three existed to serve a move that no longer happens.
- A verification read-back, which Rob asked for before accepting the rewrite, found three defects in the pair and then a fourth class outside it: the same cross-item staleness that had just been repaired in one work item was still sitting in two siblings.
- The intake-placement question, left owned by nobody once relocation became deliberate and costly, was opened as its own work item.
- A closing audit asked whether any of the four open items held urgent work. Two did not. Two were loaded guns rather than absent features, and both got a caveat at the point of danger instead of a fix.
- Rob asked whether the findings document needed updating. Nothing in it had been falsified, and the two design reversals belong to open items whose own closeouts will fold them — but the append-only result qualified on its own, because the files now carry the corrected rule while showing nothing of the reasoning that no exception was required. Writing that entry surfaced a collision the relocation item had missed: work closeout already uses *supersede* for a knowledge-edit classification, so adding a superseded retirement reason would give one word two meanings in one document.

## Decisions

- **The collapse merges logs by date, and append-only means section integrity rather than fixed position** — Rob's reframe, against Claude having ruled date-merging out as a violation before checking what the rule said. The definition was not relaxed; it was found to be what two of the five statements of it already said.
- **The definition lands in all three entrypoints, not only the toolkit's** — the templates ship the same sentence, so a definition corrected in one place would leave every seeded brain with the old one (Claude).
- **Work items never re-home; they are superseded** — Rob's call, on frame drag. The plan and findings fall out of sync with the new parent and siblings whichever way the files travel, so the rewrite the move was meant to avoid is required anyway, and the move only adds a mutation plus a window where routing resolves to a half-left home.
- **The setup-audit guard is rejected as the answer to duplicate scaffolds** — under the supersede policy a same-slug item in another unit is the *expected* state, so the audit's job is to find and link a predecessor, not to prevent one (Claude, following from Rob's policy).
- **Placement earns its own work item rather than a note** — it fires on every work item in every component brain, where the other three items serve rare or dormant paths (Rob's direction).
- **Caveats rather than fixes for the two loaded moves** — Rob stated he would not revisit the open items soon, which made the point-of-danger warning worth more than the deferred repair.
- **The append-only result is promoted to findings now rather than left for a dream cycle to extract** — the corrected rule is visible in the files and the reasoning is not, and the durable half is that no exception was carved (Claude's recommendation, Rob's direction to write it).

## What didn't work

- The log-fold question was put to Rob twice before the framing was right. The first attempt bundled a question he had already reframed; the second ruled out the option he wanted, on an assumption about append-only that a single grep falsified. Reading what a rule says before reasoning from what it is called would have collapsed both rounds into one.
- The re-homing plan was given a depth gate and a five-case fixture table that were obsolete within the hour, because the plan edit was directed before the policy question was asked. Nothing recovers that work; the ordering was simply wrong.
- Cross-item staleness was repaired in one work item and not propagated to its two siblings until a read-back was requested. The same defect class had been repaired earlier in the same session, which is what makes it a miss rather than an oversight.

## Lessons

- A rule's name is not its content. "Append-only" was reasoned about positionally for most of the session, and two of the five places it is written already defined it as content integrity. The check costs one grep and precedes any argument built on the rule.
- The repo's own artifacts are admissible evidence. The claim that chronological order was load-bearing died on the observation that this log has been out of date order by design for weeks.
- Unloading a trap is cheaper than fixing it and survives indefinite delay. A caveat at the point of danger converts a silently-broken outcome into a stop sign without waiting for the work item that owns the repair.

---

# Hook trigger narrowed to three phrases, with the closeout offer gated behind them (2026-08-08)

**Session ID**: `03f40aec-073e-4ae2-988a-c41d9b4f36e4`

Rob's session, with Claude (Opus 5) as co-author. It set out to true the project hook template up against narrower trigger language being proposed in the exemplar brain, and ended with the hook's entry conditions rewritten twice under Rob's successive narrowing: the three canonical phrases became the only way to load the brain, and then the only way to reach a closeout offer. Two changed lines in one template, committed with this entry.

## Turn-by-turn

- The narrower language was not where it was expected. Rob pointed at the exemplar brain's entrypoint; that file was unmodified, and the proposal turned out to be staged in the exemplar's in-flight work-item docs and already implemented in its project repo's entrypoint on an unmerged branch. Reading the project repo's version gave the sentence to port: three phrases, named as the only passive trigger, with everything else about the brain reached by typing a skill command.
- The first pass narrowed the trigger and kept an example list naming the retired ones, then added a clause letting a closeout pull and read the brain if the session had not already — a hole the narrowing opened, since the old wording made "close out a session" a trigger in its own right.
- Rob asked for a read-back review. It found two words that had travelled with the sentence rather than being chosen for it: "passive trigger" only means something against the typed commands being deliberately excluded, and the new clause's tail restated what the trigger sentence already said. Both were cut. The review also flagged that the exemplar offsets its narrowing with typed commands and a session-start greeting, while the template ships no other door — a discoverability loss with nothing compensating for it.
- Rob resolved that with the simplest version: the phrases are the only way in, no escape hatch, and the create procedure must not introduce skills either. A check confirmed the toolkit mentions skills nowhere outside a competitor description in the comparables registry, so the create procedure complies by silence and no prohibition was added — a rule against a thing the document never raises is a spare token.
- Rob then extended the rule to the closeout offer, on the reasoning that the exemplar ties eligibility to a team roster, which is a far more advanced case and would confuse a single-user adopter. The offer became conditional on the brain having loaded, and the pull-and-read rescue clause was deleted: it existed for exactly the case the rule now forbids.
- A final review, requested before committing, found two defects in Claude's own wording. The gate had been given a justification — that a session which never loaded the brain has nothing to close out — which is false: a code-only session can produce plenty worth logging, it simply never opened the brain. And the trigger's enforcement sentence stated one fact twice. The false reason was dropped rather than repaired, leaving the condition attached to the sentence that authorizes the offer.
- Rob closed by questioning the one caveat left standing — whether the work-item phrase firing in a brain too young to have work-item machinery was a real defect. It is not, and the templates say so: the seeded entrypoint carries the term, the working directory, the doc-naming convention and the fold-on-conclude rule, and the closeout instructions carry log routing with an explicit hedge for brains that lack the machinery. Setup is additive and idempotent and names the partial-item case; work closeout enumerates whatever docs exist rather than assuming a fixed set. An improvised early work item is a supported input to both, resting entirely on the naming convention the seed states.

## Decisions

- **The three phrases are the only way in** — no escape hatch for an outright request, no adjacent-subject triggers (Rob).
- **They are also the only route to a closeout offer** — a session that never loaded the brain is never offered one (Rob).
- **No skills in the hook or the create procedure** — an advanced configuration, better left to project-specific setup (Rob).
- **No roster-based closeout gating** — the exemplar's eligibility list answers a question a single-user adopter does not have (Rob).
- **The example list of retired triggers was dropped** — it retires wording that exists only in the old template, and echoed the roadmap/history triple in the never-cite-from-code rule, where the same words mean something different (Claude).
- **The omission of skills and roster gating is promoted to findings now rather than left for a dream cycle to extract** — the narrowed trigger is visible in the hook and the reasoning is not, and the durable half is what the exemplar's machinery had been compensating for (Claude's recommendation, Rob's direction to write it).
- **Append-only binds an entry once its commit is pushed, not the moment it is written** — Rob's call when the findings promotion arrived after this entry was already committed. A session amending its own unpushed closeout is still writing; the rule protects finished history from later sessions, not a session from itself.

## What didn't work

- Porting the exemplar's sentence wholesale imported vocabulary that depends on the half being excluded. "Passive" is only meaningful against a typed command.
- The pull-and-read rescue clause was written to close a hole, then deleted two turns later when the hole became the rule. It was authored before the offer gate existed and could not have been right in both worlds.
- Attaching a reason to the gate produced a false claim while the rule itself was sound.
- An edit that replaced a trailing clause with nothing also consumed the paragraph break, silently merging two paragraphs; the diff caught it.
- Closeout ran before the findings candidate was raised, so this entry had to be reopened to record it. Raising the promotion question during closeout rather than after would have written the entry once.

## Lessons

- Porting a rule out of a richer system imports that system's vocabulary. The words that only parse against the machinery being left behind are the ones to strip.
- A gate needs no reason attached, and a false one is worse than none — it is the handle a model uses to argue its way around the gate.
- Whether something is a gap is usually answerable from the templates themselves. The early-stage work-item worry dissolved on reading what the seed carries and how the later procedures enumerate.

---

# Open issues resolved and implementation landed (2026-08-10)

**Session ID**: `c867407e-917d-4591-b124-f85a037f75a3`

Rob's session, with Claude (Opus 4.6) as co-author. It resolved all six open issues in the burndown work item's plan, folded those decisions into the plan and findings docs, then implemented the rename across all sixteen sites in ten files — the scaffold rewrite, the new-content additions to work setup and work closeout, and the mechanical glob renames. A voice-consistency pass on the three new-content files caught a pre-existing tension between "resolves without a code change" in the setup and closeout templates and the findings' "no-merge means unfinished," and tightened it.

## Turn-by-turn

- Rob opened by giving decisions on all six open issues in a single message. The decisions were internally consistent: positive scope framing (not exclusion), user-requested archival only, routine items as inheritable defaults, guided per-item review instead of automatic merge, burndown presupposes a merge, and the scaffold describes its own purpose without naming the plan.
- Claude identified implications — the early-archival mechanic changes from automatic to guided, no-merge items simplify the scope, positive framing resolves the back-test, and the adoption discussion drops out entirely — and confirmed no tensions between decisions. Rob approved the update.
- The plan and findings were updated: open issues section removed entirely, decisions folded into the body where they belong. Three decisions became findings (positive scope, guided review, burndown presupposes merge); three became plan details (migration scoped out, routine as defaults, archival user-requested only).
- Rob asked for a final check of both docs. The read-back confirmed internal consistency — the standalone paragraph about no-merge items reads as a corollary to the four commitments, not a miscounted fifth, and the three burndown descriptions across the findings are aligned.
- Rob asked what files needed changing and estimated LoC. Claude enumerated ten files and estimated 42–47 lines. Rob asked for a confidence rating; Claude gave 85, noting the three new-content files hadn't been read yet. Rob said to read them and implement.
- Reading the scaffold, setup, and closeout established the voice: terse, imperative, checklist-style for the scaffold; dense procedural prose for setup and closeout. Implementation proceeded in batches — scaffold write and delete, nine parallel first-round edits, then sequential edits for multi-edit files, then version bumps.
- A grep sweep confirmed all sixteen sites landed and no stray TASKS references remained outside the working docs and archive.
- Rob requested a voice read-back of the scaffold and two new-content files. Claude flagged that "resolves without a code change" in setup and closeout pre-dated the "no-merge means unfinished" decision and carried a success connotation the findings contradicted. Rob said to tighten it; two edits changed "resolves" to "concludes" in setup and "occasionally without one" in closeout.

## Decisions

- **All six open issues resolved by Rob in one pass** — no iteration needed. Each decision's rationale was clear enough to fold directly into the docs.
- **Open issues removed from the plan, not marked closed** — decisions important enough to preserve became findings; the rest became plan details (Rob's direction).
- **Positive scope statement for the burndown: "everything between working code and a merged PR"** — this is the sentence that has to pass the back-test (Rob).
- **The "resolves" → "concludes" tightening was applied even though the tension predated this work item** — it was surfaced by the rename and would have read as an inconsistency in the shipped text (Claude flagged, Rob directed).

## What didn't work

- Nothing blocked. The implementation was mechanical enough that the plan's site inventory guided it directly. The only judgment call was the "resolves" language, which was a pre-existing issue surfaced by reading the files in context rather than an implementation error.

## Lessons

- Giving all open-issue decisions at once, with rationale, eliminates the back-and-forth that typically stretches resolution across multiple turns. Six issues resolved in one message.
- Reading the target files before writing new content into them is the difference between matching voice and approximating it — Claude's self-assessed confidence jumped from 85 to 92 on that read alone.
- A rename that touches ten files is mostly mechanical, but the three files that gain new content are where the voice and consistency risks concentrate. Separating the read-back into "scaffold + new-content files" from "glob renames" focused the review where it mattered.

---

# Migration dropped entirely; TASKS forgotten as a concept (2026-08-13)

**Session ID**: `57b543b7-ee8d-4ac9-b67c-2f8a228b4d91`

Rob's session, with Claude (Opus 4.8) as co-author. A code review of the rename branch surfaced two edge-case gaps in setup's legacy-adoption rule; rather than patch them, Rob decided to remove migration from the toolkit altogether so TASKS survives nowhere as a token or concept. The setup rule was deleted, the canonical templates were swept clean, and these working docs were corrected to record the reversal and its reason.

## Turn-by-turn

- A background code review (high effort, against the branch's PR, briefed with this work item for context) returned two findings, both landing on setup's legacy-rename bullet: its "overwriting nothing" claim is false for a half-migrated item that already holds a burndown, and its instruction to repoint the old name in the item's other docs can force an edit to the append-only working LOG, which setup grants no carve-out for. Both were real but narrow.
- Rob rejected patching them and asked the simpler question: take migration out entirely. His reasoning — the pattern is too young to accumulate migration rules, only a handful of brains carry the old name, and any live TASKS concept is an attractor that re-invites the master-list drift the rename exists to kill.
- A grep sweep located every TASKS reference. The only canonical migration site was setup's legacy bullet; everything else was in-flight working docs, the archive, or legitimate ordinary-English use ("tickets show the tasks" in SCOPE, left untouched).
- Removed the legacy-classification bullet from setup and the matching "renamed from a legacy name" clause in its handoff step. Setup now knows only three doc states: missing, exists in `working/`, exists in `archive/`. A confirming grep showed TASKS gone from all canonical and template files.
- Closeout corrected these working docs: the plan's scope boundary dropped the delivered "setup audit rule for the legacy name" and reframed the out-of-scope bulk-migration bullet to state the toolkit carries no legacy-adoption at all; the findings gained a rejected-alternative entry recording why migration was dropped.

## Decisions

- **Remove migration wholesale rather than fix the two findings** (Rob) — the findings dissolve by construction once the rule is gone: no rename left to clobber a burndown slot or to touch an append-only LOG.
- **TASKS is forgotten as a concept, not deprecated** (Rob) — BURNDOWN is treated as the only name that ever existed, because a concept setup still knows how to retire is a concept a writer can still be tempted to fill.
- **Existing brains are fixed by hand, not by the toolkit** (Rob) — the few carrying the old name get a one-time manual rename each; the toolkit gains no mechanism for it.

## Lessons

- A young pattern is better served by forgetting a bad concept than by carrying a rule to migrate away from it — the migration rule is itself a place the bad concept keeps living. The two review findings were the symptom; the standing TASKS token was the cause.
- When a review surfaces edge cases in a mechanism, "delete the mechanism" is a candidate fix worth weighing before patching it — here it was cheaper and removed the underlying attractor rather than guarding it.

---

# Rename branch merged to main (2026-08-13)

**Session ID**: `ca400db6-6efb-45e2-996d-0fa605d396bb`

Rob's session, with Claude (Opus 4.8) as co-author. A short session to land the rename branch: Rob asked whether the PR needed a rebase before merging, and once confirmed clean, had it merged. The branch carrying the TASKS→BURNDOWN rename is now on main.

## Turn-by-turn

- Rob asked whether the rename PR needed rebasing first. Its merge status reported mergeable and clean — up to date with main, no conflicts — so no rebase was needed.
- On Rob's go-ahead the PR was merged with a merge commit (not squash or rebase), and the merged state was confirmed.

## Decisions

- **Plain merge, no rebase** (Rob) — the branch was already current with main and conflict-free, so there was nothing for a rebase to resolve.

## Lessons

- Check the PR's mergeability before assuming a rebase is required; a clean branch needs none, and rebasing it anyway only rewrites history for no gain.

---

# BURNDOWN work item closed out and folded into the canonical docs (2026-08-13)

**Session ID**: `ca400db6-6efb-45e2-996d-0fa605d396bb`

Rob's session, with Claude (Opus 4.8) as co-author. With the rename branch merged to main earlier this session, Rob declared the BURNDOWN work item done and directed a work-item closeout, held short of any commit so the result can be reviewed later — possibly across several models — before it lands. Its durable, file-invisible design lessons were folded into the toolkit findings, its consumed plan and read log archived, and the three working docs moved to `archive/`.

## Turn-by-turn

- Two lessons were lifted from the burndown decision record into the toolkit findings, as the halves of the rename that the templates cannot show now that they carry only the renamed result: that a document admitting a wrong reading is fixed by renaming it rather than rewording it, and that a young pattern forgets a discarded concept rather than carrying a rule to migrate away from it — the migration rule having been shipped, then deleted on the reasoning that a live TASKS concept is itself where the drift keeps living.
- The burndown working log's three sessions were merged whole into this log in date order. They are all newer than everything already here, so they land after the last 2026-08-08 entry, and the most recently written of them keeps the tail.
- The PLAN — consumed into the template and pattern edits that shipped in the merged branch — the FINDINGS, and the LOG were moved to `archive/` under their working basenames.
- The plan's remaining testing approach was walked before archiving. The site-landing grep ran during implementation, but the end-to-end scaffold dry run, the adoption check, and the master-list back-test are not recorded as executed, and the manual TESTING-doc lifetime was scoped out from the start as a separate call. Surfaced to Rob rather than treated as blocking, since he declared the item done and is reviewing before anything commits.

## Decisions

- **BURNDOWN declared done and closed out now** (Rob) — the fold and the archive moves are performed, but nothing is committed; a review across models comes first.
- **The two rename lessons are promoted to findings rather than left in the work item's log** (Claude's recommendation, Rob's direction) — the canonical docs show the new name everywhere but not why a rename beat a rewording, nor that a migration rule was shipped and then deliberately removed.
