# Enforce the Work-Item Token Prefix: Session Log

Running log of implementation sessions. Each session appends after a `---` separator.

The first entry, and every one after it, follows the entry format and content rules in `MBT_SESSION_CLOSEOUT.md` — that spec is the authority, not the prior entry, since a fresh LOG file has none to copy.

---

# Draft the prefix-enforce edit (2026-08-13)

**Session ID**: `a347c9b8-a0fa-41e3-b521-807aaeb8fc35`

Rob's session, with Claude as co-author: turn the settled SETUP_PREFIX plan into a first draft of the actual `WORK_SETUP` edit. It landed — the branch exists and the Slug paragraph now carries the name → slug → filename transform, dry-run against the three manual test cases and passing.

## Lineage

Opened by reading the full work-item set (PLAN, FINDINGS, CLAUDE runbook, LOG, TESTING) plus the real target, `templates/WORK_SETUP.md`. Rob first asked for a code-generation confidence rating; Claude gave 85/100 — the transform and acceptance cases are fully pinned, so the only residual risk was landing the wording under the repo's writing law without spawning a second copy of the prepend rule that the Slug paragraph's prefix-distinctness prose already implies.

Rob then had Claude cut the feature branch and start drafting. Branch `setup-prefix-enforce` was created to match the name the runbook already declared, rather than inventing one.

The edit rewrote the opening of the Slug paragraph: it now states up front that every produced filename is the token-led compound, derives the slug from the work-item name, and resolves the handed-name ambiguity by stripping a leading owning-unit token before use so it can never double. A short placeholder example (`<TOKEN>_FOO` → files `<TOKEN>_FOO_*`, not the doubled form) carries the never-double point. The distinctness/longest-match prose was left verbatim.

## Decisions

- **Transform lives in the slug step only, not the doc-generation step** — Claude's call, within the plan's open issue on placement. The slug step is where the handed name becomes the slug, so it's the decision point; the doc-generation step already composes the token-led filename through the template names, so repeating the rule there is exactly the duplicated prepend statement the plan warned against.
- **Intake step left untouched** — the other open issue. Its existing forward-pointer to the slug step already captures the name cleanly; no transform detail belongs there.
- **Removed the paragraph's old closing sentence** ("every doc carries the owning unit's token ahead of it…") — the new opener states that outcome once, so keeping the tail would have duplicated it. The dropped ownership rationale is background, not load-bearing here.
- **Template version line held at V1** — Claude's call. The `> V1, <date>.` line is the seed baseline every freshly seeded brain starts its `WORK_SETUP` from, not a changelog of the template file; bumping it would push new brains to V2 wrongly.

## Lessons

The whole risk of this item was prose discipline, not logic: the fix is one sentence of behavior, but the failure mode is stating it twice. Placing it strictly at the name → slug decision point, and deleting the now-redundant tail in the same edit, is what keeps it single-homed. Left uncommitted at Rob's direction.

---

# Review and repair the slug rewrite (2026-08-14)

**Session ID**: `a4b4e607-cc9b-4cc3-90ea-85efd9e06c99`

Rob's session, with Claude as co-author: run a deep code review over this branch, then fix what it found. The review returned nine verified findings — four confirmed defects in the rewritten Slug paragraph, three confirmed compliance breaks in this log, two plausible wording problems — and the fixes landed: the Slug paragraph was rewritten with its leading imperative restored, the test plan gained the cases the fixes introduce, and this log was brought back into spec.

## What the review established

The drafting session's work was committed after its entry closed — the branch's first commit landed the drafted edit together with this log, and a second commit reworded the Slug paragraph twenty-seven minutes later in a session this log never recorded; that rework's diff survives in git but its reasoning is lost, which is itself one of the findings. The rework, while fixing real wording problems, had undone the fix's load-bearing structure: it deleted the leading imperative commanding the token-led filename and moved "not a mechanical transform of the name" — the exact phrase this item's FINDINGS names as root cause — back to the paragraph lead. That left the bare-name path with no commanding instruction at the decision point, and the paragraph contradicting itself about whether the slug is mechanical, when the manual test cases hold only under the verbatim reading. Two further confirmed gaps: the strip rule keyed only on the owning unit's token, so a handed name carrying another unit's token (a hub-token habit in a component brain) would silently embed that token mid-slug; and a mechanical strip could manufacture exactly the parent-continues-into-child compound the same paragraph's longest-match guard forbids, with nothing saying which rule wins.

## The repaired paragraph

Rob directed the fixes wholesale; the wording is Claude's, within what the review prescribed. The paragraph now opens with the imperative — every produced filename is `<TOKEN>_<WORK>_*`, derive the slug from the name, lead with the owning unit's token, always — and resolves the mechanical question by input shape: a handed SCREAMING_SNAKE identifier is the slug verbatim, any other name gets a short specific slug written for it, so identical handed names can no longer yield different files run to run. The strip now removes any unit's token at the head of a handed identifier, longest match, not only the owning unit's. The distinctness and longest-match guards became an explicit gate the derived compound must pass, with rewording the slug as the commanded escape — the guards outrank the verbatim rule, closing the precedence hole. The "not a mechanical transform" phrase is gone entirely, as are the extra restatements of the never-double rule: the mid-slug token ban is now stated once, as a stipulation rather than an inference. Dry-run against the manual test plan with the final text: the bare name, the already-prefixed name, and the component-brain case all produce the expected token-led filenames, and two cases were appended to the plan for the new behavior — a handed name carrying a foreign unit's token, and a handed name whose mechanical slug fails the gate and must be reworded.

## Repairs to this log

The review confirmed the prior entry referenced the target's sections by number throughout, against the session-closeout rules; those references were rewritten to substance names before merge — a knowing revision of a prior entry, done as the review prescribed, because after merge the append-only law would fix the breakage in place forever. The prior entry's claims otherwise stand: they were true of their session, and this entry supplies what changed after — the commits ended the left-uncommitted state, and the opener that entry describes was deleted by the unlogged rework and is restored by this session's fix.

## Decisions

- **The imperative lead is deliberate — pinned in FINDINGS** — Rob's call, made after walking the paragraph's git history, which showed its form flipping on three consecutive edits: imperative-led, then demoted back to definition-led by the unlogged rework, then restored by this session's fix. Rob doesn't recall directing that demotion and judges it a mistake, though it's unknowable now — sessions have run on different models to manage cost, and only a log entry could have said which this was. FINDINGS now records the settled form so a future wording pass can't re-fight it silently.

## Lessons

A fix whose substance is structure — an imperative at a decision point — can be reworded to death while every individual sentence still looks right; the regression was caught only by re-checking the final text against the item's own FINDINGS and test cases. And an unlogged rework session costs double: its rationale is unrecoverable, and every later session pays to reconstruct what it did from the diff. When sessions run on different models, the log is also the only thing that separates a decision from a cheaper model's drift — unlogged, the two are indistinguishable in the diff.
