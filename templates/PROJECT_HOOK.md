<!-- Mini-brain hook: merge the section below into each project repo's CLAUDE.md (create the file if the repo has none — never overwrite an existing one). Substitute <project> and <PREFIX>, and adjust the relative path if the brain's clone sits elsewhere or under another name. If the brain is component-structured, also uncomment the component paragraph and fill `<Component>`, `<dir>`, and `<TOKEN>` for the component this repo maps to. -->

## Working in the mini-brain

**When the user mentions the mini-brain, work items, or <project> knowledge/history — or asks to start, work on, or close out a work item or session** — pull `../mini-<project>-brain/` to latest (it's a shared repo), then read its `CLAUDE.md` and follow it (sibling clone; if absent, tell the user to clone it beside this repo). Drive the whole workflow from *this* session — never make the user switch repos — and resolve its instructions' relative paths against `../mini-<project>-brain/`.

<!-- Component-structured brains only — name the component this repo maps to:

**This repo is the brain's `<Component>` component** (directory `<dir>/`, token `<TOKEN>`). Start there and read another component's documents only when the question crosses into it; the brain's registry says which terms route where.
-->

Mini-brain edits accumulate uncommitted during a session; **closeout is the sync point that lands them** — don't commit/push on every file write. The user can't see that tree, so a closeout must actually commit and push, not just write files, and it follows the mini-brain's own commit conventions. A session closeout commits the session's changes (edits, the new log entry) and pushes to the mini-brain's `main`, reporting both; if the push fails, resolve or surface it rather than leaving the change unpushed.

**Proactively offer a session closeout at natural stopping points** (PR opened, branch merged, work paused, user signals wrapping up). Offer once and briefly; run the procedure only after the user agrees; skip trivial sessions (a lone question, a typo).

**Never cite mini-brain docs (`<PREFIX>_*`, or any component's token) from code.** Information flows one way — down from the mini-brain into code — so a back-reference is circular. Roadmap, history, and rationale that isn't about operating *this* code belong in the mini-brain, not in code comments.

<!-- As the brain matures and gains work items (stage 3), add:

**Work-item closeout** is not a direct push — branch, commit, push, and open a PR against the mini-brain's `main`; report the link and leave it unmerged for review.

**Active work item** = the one whose `working/<PREFIX>_<WORK>_*` docs name your current git branch; none on `main` or an unclaimed branch. It resolves any "my work item" reference; ask if ambiguous. In a component-structured brain each unit has its own `working/` and its work items carry that unit's token, so search this repo's component first, then its ancestors.
-->
