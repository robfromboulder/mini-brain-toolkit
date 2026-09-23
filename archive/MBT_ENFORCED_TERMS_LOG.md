# Enforced Terms: Working Log

---

# Implement enforced terms mechanism (2026-09-22)

**Session ID**: `9ca58e07-510b-4f01-b2ad-c3011d671966`

Rob and Claude implemented the enforced terms mechanism from the settled plan and decision record, landing as PR #7 on the `enforced-terms` branch. The session was straight execution — the plan was fully settled, so no design decisions were made; every change followed the plan's implementation sequence.

## What landed

Created the template (`templates/ENFORCED_TERMS.md`) and this brain's own enforced terms file (`MBT_ENFORCED_TERMS.md`) with two entries: "finding" and "work item." Wired four enforcement hooks: two-mode one-term-one-meaning check in `MBT_CHECK_BRAIN.md`, per-entry re-grep (Phase 1 check 7) and candidate harvesting (Phase 4) in both dream cycle files, and the coined-or-repurposed-term callout in the closeout template and work FINDINGS template. Added read-index rows and the write-time rule to all three entrypoint files (`CLAUDE.md`, `templates/CLAUDE.md`, `templates/LOBES_CLAUDE.md`), a declared-exemption row in `CLAUDE.md`, a stage-3 file-set row in `MBT_PATTERN.md`, and the enforced terms file to `MBT_CREATE_BRAIN.md`'s stage-3 growth step. Fixed seven generic uses of "finding" across four files and renamed the check procedure's report headings from "Structural/Substance findings" to "Structural/Substance issues."

## Decisions

Rob confirmed (post-commit) that "lobe" and "lobespace" from PR #5 should not be enforced terms — both fail the empty-disambiguation rule since they were specifically chosen to avoid the collisions the old terms had.

The plan's implementation sequence step 5 said "three entries" but the plan body specified two ("finding" and "work item"). Treated the step-5 count as a stale draft artifact and went with two.

## What didn't work

Nothing — clean execution against a settled plan.

---

# Align enforced-term hooks with the first adopting brain after PR #7 review (2026-09-22)

**Session ID**: `b8c5688f-8d1f-4731-ba54-62fa02f39b85`

Rob and Claude ran a medium-effort code review of PR #7, compared the branch's enforcement hooks against the first product brain to use enforced terms, and cut the hooks back to what that brain actually runs. Everything landed on the `enforced-terms` branch.

## Review

The review found seven issues. Three came from hooks the adopting brain doesn't have. First, the coined-term callout in the closeout and work FINDINGS templates was recorded but nothing ever acted on it, and the templates disagreed about where it went. Second, the dream cycle's term check sat in the mechanical Phase 1 but needed judgment, said to fix things "in Phase 2", and grepped the append-only logs, whose hits can never be fixed. Third, the check procedure only recommended declaring a term once a collision "recurs across checks", which conflicted with the Harvest rule. The other two issues didn't depend on that brain: the dream cycle still used "findings" in its generic sense in several places, and the Work item entry used "issue" in the tracker sense while the Finding entry reserves it as the generic word.

## Comparison with the adopting brain

Rob recalled that the adopting brain has no instruction for coining terms in a work item and no closeout step that acts on them, and asked for nothing beyond what it does. Reading that brain confirmed it. It enforces terms in three places: a terms rule at session closeout, a terminology conformance check in work closeout's structural checks, and a dedicated dream-cycle phase. That phase checks the terms file against its own rules, reads the canonical knowledge docs for drift, and proposes unlisted terms for the user to confirm. It never scans the log.

## What changed

- Reverted the coined-term callout in `templates/WORK_CLOSEOUT.md` and `templates/work/FINDINGS.md`. Added the adopting brain's terminology check to the closeout's structural checks in its place.
- In both dream cycle files, removed the Phase 1 term check and the Phase 4 candidates paragraph, and added an "Enforced terms" phase before the report, modeled on the adopting brain's. The report moves to Phase 6. In the toolkit's own cycle, the drift pass reads every top-level doc, since its product docs and procedures are its knowledge. The template reads only SCOPE, APPROACH and FINDINGS, as the adopting brain does.
- Changed the check procedure's term bullet to grep listed terms outside the logs and to report every unlisted collision as a candidate for the user.
- Fixed the remaining generic uses of "findings" in `MBT_DREAM_CYCLE.md`, and reworded the Work item entry to "not a tracker ticket or a task".
- Updated the decision record's enforcement points and added the two rejected designs as alternatives.

The adopting brain's session-closeout terms rule was not copied. The entrypoint's write-time rule already covers log entries.

---

# Keep other brains unnamed in mini-brain docs (2026-09-22)

**Session ID**: `b8c5688f-8d1f-4731-ba54-62fa02f39b85`

Rob and Claude finished the review follow-up from the previous entry: they removed another brain's name from this item's docs, then committed and pushed the enforced-term changes to PR #7.

## Decisions

Rob directed that mini-brain docs never name the product brain the hooks were compared against. The previous entry had named it before it was committed, so Claude rewrote it to say "the first product brain to use enforced terms" before the commit. The decision record already used that phrasing. An older `MBT_LOG.md` entry that names the same brain was left alone because the log is append-only. Mentions in `archive/` were left alone as well.

## Landed

The review follow-up was committed as one change and pushed to the `enforced-terms` branch, updating PR #7.

---

# Dry-run the check procedure's enforced-terms pass against the adopting brain (2026-09-22)

**Session ID**: `a64e0725-e1c6-4004-b30f-58c59b00378b`

Rob asked Claude to dry-run the PR #7 version of `MBT_CHECK_BRAIN.md` against the first product brain to use enforced terms, to see what the revised term check would surface. The run showed where the procedure's wording was ambiguous. Rob then had Claude tighten the term check and push the result to PR #7.

## The dry run

The path Rob gave was the product's code repo. Its entrypoint pointed to the mini-brain in a sibling repo, so Claude checked that one. Claude ran the structural checks mechanically. For the listed-term pass it counted hits per term across the top-level docs, excluding logs, and got about 500 hits for ten terms. Reading all of them wasn't practical, so Claude grepped for the senses each entry rules out: a protocol's sense of a term, a cloud provider's permission vocabulary, and generic verb forms. That's where every real misuse turned up. Some uses didn't break an entry but showed the entry was too narrow; a cost-allocation sense of an accountability term was the clearest. The unlisted-term pass relied on greps rather than a full read of the knowledge docs as a set, and Claude said so in the report.

## What the run showed about the instructions

- "Judge every hit" doesn't scale on a mature brain. The intro's rule that set-level checks can't be split across agents also seemed to cover the listed-term pass, which is per-hit judgment against one entry.
- The check read "canonical docs, not the logs" while the dream cycle's term phase reads every top-level doc. Nothing settled whether procedures and the entrypoint were in scope.
- The check reported every unlisted collision as a candidate, while the dream cycle proposes only terms that meet the brain's own admission rule. The adopting brain's rule excludes overloaded common words, so the check would have proposed a term that rule rejects.
- The check had no outcome for "the entry itself is too narrow". The dream cycle has one.
- Grepping a term literally missed its inflections, because entries are nouns and the misuses were verbs and participles.
- Nothing in the check examined the terms file itself. The adopting brain's file predates the template, and two of its entries have no disambiguation clause.

## Decisions

Rob asked Claude to tighten the instructions, and Claude made all six fixes in `MBT_CHECK_BRAIN.md`. Both term passes now read top-level docs and never logs or `archive/`. Listed terms are grepped by stem, starting with the senses the entry rules out. An entry concern is reported separately from a misuse. An unlisted candidate goes to the user only if it meets the terms file's own rule for adding an entry. The terms file is checked against its own rules, and an entry with an empty disambiguation is reported as a retirement candidate. The intro's no-delegation exception now covers only unlisted collisions, so listed-term hits can go to Explore agents. That one change covers delegation; no separate rule was added. Claude put the terms-file check in the check procedure rather than leaving it to the dream cycle alone, because the check only reports and doesn't edit. The file kept its version, because this PR had already bumped it once.

Rob then directed that PR #7 not name the adopting brain. The only mention was in the new commit's message, so Claude reworded that commit and force-pushed the branch with a lease. An older `MBT_LOG.md` entry that names the brain was left alone, because it's already on `main` and the log is append-only.

## Lessons

- Dry-running a procedure against a real brain surfaced ambiguities that reviewing the text had missed.
- For a listed term, misuse concentrates in the senses the entry rules out and in neighboring vocabularies. Grepping those first finds it faster than reading every consistent hit.

---

# Re-run the dry run, then dry-run a brain without enforced terms (2026-09-22)

**Session ID**: `a64e0725-e1c6-4004-b30f-58c59b00378b`

Rob and Claude, continuing the previous entry's session. Rob had Claude re-run the tightened check against the first product brain to use enforced terms, then run it against the virtual-view brain, which is multi-lobe and declares no enforced terms. Claude fixed five more gaps in the instructions and pushed each round to PR #7.

## Second run against the adopting brain

The brain was unchanged since the first run, so only the term pass was repeated. This time Claude read SCOPE, APPROACH and FINDINGS in full, together, rather than working from greps. Grepping stems and looking at the senses each entry rules out found five more misuses of "grant" in its IAM and OAuth senses. One of them, "a grant's type", collides with the phrase the entry reserves for OAuth. The new entry-concern outcome gave the ambiguous results somewhere to go: attribution used for cost, "grant" as a verb, OAuth's "authorization server", and the Delegation entry not separating delegation from internal identity propagation. The admission-rule filter dropped "token", because the brain's own rule excludes overloaded common words and "User token" is already the precise term. It kept "permissions boundary" and "gateway target". The full read also found a FINDINGS claim that every credential is issued through the identity provider, which three other statements in the brain contradict.

The run exposed three more gaps. The check didn't cover a loose synonym standing in for a listed term, which the dream cycle and the brain's own terms file both treat as misuse. The retirement rule would have retired Delegation, which has no disambiguation clause yet is one of the brain's most misused terms. And the template's rule that an entry stands alone conflicted with its requirement to say what the entry must not be confused with. Four of the brain's entries break its own standalone rule, in exactly their disambiguation clauses, because authentication and authorization can't be told apart without naming each other.

## Fixes to the three gaps

Rob asked for all three to be fixed. The check's unlisted pass now reports a loose synonym as a wording fix. An entry with no disambiguation is flagged as needing one when its term was misused, and as a retirement candidate only when it was not. That applies in the check and in both dream cycle files, where the rule moved from the integrity step into the drift pass because it depends on the drift pass's results. An entry's definition still invokes no other entry, but its disambiguation may name the one listed term it is confused with. That change is in `MBT_ENFORCED_TERMS.md`, `templates/ENFORCED_TERMS.md` and the decision record. Whether procedure documents should be in scope for the term pass stays open for Rob.

## Run against the virtual-view brain

This brain exercised the multi-lobe checks and the path for a brain with no terms file. The structural checks were clean apart from twelve staged but uncommitted work-item docs, stale commented-out index blocks, and heavy use of the old vocabulary. The substance checks found parents explaining what their children elaborate at two levels, and an open question that belongs to the ViewMapper agent lobe. Two counts checked against the code were slightly off. The unlisted term pass proposed "catalog", where the manifesto's naming convention contradicts Trino's usage in the other lobes, and "finding", the collision the toolkit had already harvested for itself.

The run exposed two more gaps. The check's candidate filter deferred to the target's own admission rule, which a brain without a terms file doesn't have, so strictly nothing could be proposed. And old pattern words collided with their ordinary senses inside the brain: "component" names a lobe in the entrypoint and a software part in ViewZoo's design. The one-term pass would propose that as a candidate while vocabulary alignment already recommends the rename that resolves it.

## Fixes to the two gaps

Rob asked for both to be fixed. A brain with no terms file is now judged against the rules in `templates/ENFORCED_TERMS.md`. A collision on an old pattern word is reported under the vocabulary-alignment check, whose rename resolves it, and not as a candidate. Claude put that sentence in the vocabulary check rather than the term check, so the instruction never points ahead to a later section.

## Lessons

- Each dry run against a different kind of brain found gaps the previous one could not. The adopting brain tested the listed-term path, and the virtual-view brain tested the multi-lobe layout and the path with no terms file.
- Reading the knowledge documents together is where the most valuable results came from: the permissions-boundary collision, the contradicted credential claim, and the parents restating their children. Greps did not surface any of them.
- How much the unlisted pass costs depends on the brain's size. It was heavy at about 220KB and cheap at about 74KB.

---

# Keep procedure documents in the term check's scope (2026-09-22)

**Session ID**: `a64e0725-e1c6-4004-b30f-58c59b00378b`

Rob and Claude closed the one question the dry runs left open: whether a brain's enforced terms should govern its procedure documents as well as its knowledge documents. Rob decided they should, for consistency. No file changed, because the check already reads every top-level document.

## Decisions

- **Procedure documents stay in scope.** This was Rob's call. Claude agreed for two reasons. First, the dream cycle's drift pass and the work-closeout terminology check both already cover procedures, so exempting them in the check alone would give three different verdicts on one brain. Second, this toolkit's own Finding entry exists mostly to keep procedures from using the word in its generic sense.
- **Procedure noise is an entry concern, not a reason to exempt procedures.** An everyday verb in a procedure that collides with a listed term, such as delegating a read to an agent, shows that the entry's disambiguation doesn't rule that sense out. The check now reports that as an entry concern, and the brain decides whether to reword the procedure or widen the entry.

## State at close

PR #7 carries every fix from the three dry runs. The two test brains were not edited. Once PR #7 merges, the work item is ready for closeout.
