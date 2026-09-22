<!-- Mini-brain hook: merge the section below into each project repo's CLAUDE.md (create the file if the repo has none — never overwrite an existing one). Substitute <project> and <LOBESPACE>, and adjust the relative path if the brain's clone sits elsewhere or under another name. If the brain is multi-lobe, also uncomment the lobe paragraph and fill `<Lobe>`, `<dir>`, and `<LOBESPACE>` for the lobe this repo maps to. -->

## Working in the mini-brain

**When the user says "mini brain", "mini-brain", or "work item"** — pull `../mini-<project>-brain/` to latest (it's a shared repo), then read its `CLAUDE.md` and follow it (sibling clone; if absent, tell the user to clone it beside this repo). Drive the whole workflow from *this* session — never make the user switch repos — and resolve its instructions' relative paths against `../mini-<project>-brain/`. Nothing else loads the brain.

<!-- Multi-lobe brains only — name the lobe this repo maps to:

**This repo is the brain's `<Lobe>` lobe** (directory `<dir>/`, lobespace `<LOBESPACE>`). Start there and read another lobe's documents only when the question crosses into it; the brain's registry says which terms route where.
-->

Mini-brain edits accumulate uncommitted during a session; **closeout is the sync point that lands them** — don't commit/push on every file write. The user can't see that tree, so a closeout must actually commit and push, not just write files. A session closeout commits the session's changes (edits, the new log entry) and pushes to the mini-brain's `main`, reporting both; if the push fails, resolve or surface it rather than leaving the change unpushed.

**Proactively offer a session closeout at natural stopping points** (PR opened, branch merged, work paused, user signals wrapping up) — only in a session that loaded the brain. Offer once and briefly; run the procedure only after the user agrees; skip trivial sessions (a lone question, a typo).

**Never cite mini-brain docs (`<LOBESPACE>_*`, or any lobe's lobespace) from code.** Information flows one way — down from the mini-brain into code — so a back-reference is circular. Roadmap, history, and rationale that isn't about operating *this* code belong in the mini-brain, not in code comments.

<!-- As the brain matures and gains work items (stage 3), add:

**Work-item closeout** is not a direct push — branch, commit, push, and open a PR against the mini-brain's `main`; report the link and leave it unmerged for review.

**Active work item** = the one whose `working/<LOBESPACE>_<WORK>_*` docs name your current git branch, where `<LOBESPACE>` is the owning lobe's lobespace and `working/` that lobe's own directory — both the brain's own in a single-lobe brain; none on `main` or an unclaimed branch. It resolves any "my work item" reference; ask if ambiguous. In a multi-lobe brain, search this repo's lobe first, then its ancestors.
-->
