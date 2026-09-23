# Mini-Brain Toolkit: Check an Existing Mini-Brain

> V25, 2026-09-22.

This document is the procedure for evaluating an existing mini-brain against the pattern and surfacing where it could improve — whether the brain was built from this toolkit or grew on its own.

**Stance.** This is a diagnostic that produces *opportunities*, not a grade. Most repos match some principles and not others; partial adherence is normal and fine. A repo can be a healthy mini-brain without doing everything here, and doing everything mechanically without the underlying value misses the point. Lead with what's working, then what would help most. Never edit the target brain during a check unless the user explicitly asks — checking observes; creation and the dream cycle change.

**Inputs.** The path to the target repo. If the user hasn't named it, ask. If a known healthy mini-brain is available to consult, use it to calibrate what "good" looks like for a convention before judging the target against it — but the pattern reference (`MBT_PATTERN.md`) is the authority, not any single exemplar.

---

## 1. Orient

Read the target's entrypoint first (`CLAUDE.md` or equivalent), then list the repo top-level and its `archive/`/`working/` dirs. Identify: the lobespace in use, which canonical docs exist, whether there's a session log, and what stage the brain is at (per `MBT_PATTERN.md`: seed / content / mature). Read the canonical docs' first lines (not their full bodies yet) to see version headers and purpose. This is a bounded, low-context pass — save heavy full-file reads for §3.

**If the entrypoint carries a lobe registry**, the brain uses the multi-lobe layer described in `MBT_LOBES.md`. Note the hub lobespace and every lobe's directory and lobespace, and list each lobe's directory rather than the top level alone. Several checks below then run per lobe instead of once. A brain with no registry is single-lobe and everything runs as written.

If the repo has no entrypoint and no namespaced docs, it may not be a mini-brain — or the path may be wrong. Say so and stop: report that the target doesn't look like a mini-brain, ask the user to confirm the location, and do nothing else — don't score it, and don't scaffold what's missing.

---

## 2. Score against the principles

Walk the ten principles from `MBT_PATTERN.md` one at a time, in order. For each, give a verdict — **present / partial / absent / not applicable** — with a one-line note on what you actually saw, and (when not present) the concrete opportunity. The table below is a checking aid, not the authority.

| # | Principle | What to look for |
|---|---|---|
| 1 | Keep only what can't be re-derived | Docs hold *why*, not a restated copy of the code/README. Is there a stated bias toward small? Contrast: a store that mirrors the architecture and only grows. |
| 2 | Its own repository, outside the code | The brain is a standalone repo beside the project repos, not a folder committed inside one. Contrast: docs forked and versioned with the code they describe. |
| 3 | Orthogonal documents | Each doc covers one non-overlapping dimension (problem, approach, findings, log); a question maps to one file. Contrast: overlapping docs, or one doc covering everything. |
| 4 | Log separate from distilled docs | An append-only, dated, attributed session log *and* a distinct set of living current-state docs. Contrast: one mutable blob, or an ever-growing log never distilled. |
| 5 | Entrypoint with read index | One file a reader opens first, carrying a table of what to read for a given question and what's current vs. retired. Contrast: finding files by guesswork. |
| 6 | SCREAMING_SNAKE_CASE namespace | A shared uppercase lobespace on every knowledge file; wouldn't clash if two brains loaded together. Contrast: generic names lost among repo files. |
| 7 | Versioned and dated | A lightweight `> V<N>, date` stamp on canonical docs; history left to version control. Contrast: undated docs, or in-tree "old version" copies. |
| 8 | WIP apart from settled | A `working/` (or equivalent) holding area for drafts/experiments, distinct from the trusted core. Contrast: provisional and canonical content mixed. |
| 9 | Standard open/close of a work item | A setup ritual and a matching closeout that harvests durable lessons into canonical docs and retires (moves, not deletes) scratch files. Contrast: every effort reinventing structure and stranding its insights. |
| 10 | Scheduled reflection pass | A defined, recurring review of the *memory itself* that both prunes re-derivable content and looks for gaps. Contrast: a store only ever added to. |

Principles 9 and 10 are stage-3 machinery — mark them **not applicable** (not **absent**) for a seed or content-stage brain that legitimately doesn't need them yet. The signal is need, not a checkbox: a brain tracking many work items with no closeout ritual is a real gap; a small single-purpose brain without one is fine.

Score a multi-lobe brain's principles 5 and 6 against the multi-lobe layer, not against enumeration. Principle 5 is satisfied when a hub index, a doctype grammar and a registry together resolve every document — not when every document is listed. Principle 6 is satisfied by a lobespace declared per lobe, not by one lobespace across the brain.

---

## 3. Verify substance, not just structure

Structure can be present while the content rots. Spot-check the things that decay silently — delegate the read-heavy parts to Explore agents so the active context stays free for judgment. The three set-level checks are the exception: an unlisted term collision, a duplicated question and a parent's overreach are each invisible to a reader holding one document, so those have to be read together by whoever is judging, not split across agents.

- **SCOPE factual drift.** Pull a handful of falsifiable claims from the scope doc (class/tool/config names, counts, and especially *absence* claims like "no control does X") and check them against the actual codebase. Absence claims break silently when capabilities are added — prioritize them. Report claims that no longer hold.
- **SCOPE drifted into status.** Find the section describing where things stand — headed "State of the Problem", "Current State" or similar — and ask what it actually describes: the world the problem exists in, or the project's own progress through it. Version numbers, test counts, release status, maturity labels, benchmarks and issue counts are the tell; they belong to the project, not to a problem that exists whether or not anything addresses it. A scope written this way looks well-researched and dates within weeks, so flag it as a rewrite rather than a trim — the content that should be there was never gathered. The heading itself is cosmetic: "Current State" invites the drift and is worth renaming when the section is next touched, but a section under that name whose content is right is not a defect.
- **Re-derivable content.** Skim the canonical docs for passages that merely restate what the current code plainly shows. These are pruning candidates (principle 1) — the brain would be *more* trustworthy smaller.
- **One term, one meaning.** Read the brain's top-level documents, never its logs or `archive/`. *Listed terms:* for each term the brain's enforced terms file lists, grep its stem so every inflection matches ("authenticat", not "Authentication"), and judge each hit against the entry's enforced sense and its disambiguation. Look hardest at the senses the entry rules out and at the word's meaning in adjacent vocabularies (a protocol's, a cloud provider's), where misuse concentrates. Report a misuse as a wording fix. Report a use showing the entry itself is wrong or too narrow as an entry concern, with the evidence. *Unlisted terms:* read the top-level documents as a set and watch for a word carrying two jobs (a domain term in one document borrowed as a generic in another); each reading is defensible alone and the collision shows only side by side. Report a collision as a candidate enforced term for the user to confirm only when it meets the enforced terms file's own rule for adding an entry. *The file itself:* check the enforced terms file against its own stated rules and entry format, and report an entry whose disambiguation is empty as a retirement candidate.
- **Question ownership** (multi-lobe brains). An open question belongs to exactly one lobe: the one whose work would resolve it. The same question standing in a parent and a child means neither owns it, and the copies drift as the answer develops.
- **Parent overreach** (multi-lobe brains). A parent names what a child elaborates and stops. Where a parent explains *why* a child's problem is hard, or how it is solved, in its own words, that explanation belongs to the child — the tell is a passage equally at home in either document.
- **Shape.** Ask of each lobe whether its SCOPE still states one problem, or whether writing it honestly today would force two onto the page. A brain that should have split is internally consistent either way, so no structural check can see it; the tell is a lobe that authored one target's documents first and ported a second against them.

Also run the structural checks below; they're mechanical and catch the cheap, common failures.

### Structural checks

1. **Read index ↔ disk** — every file in the read index exists; no top-level knowledge file is missing from the index (orphans). Ignore HTML-commented entries (`<!-- ... -->`) — a brain commonly stages its read index with commented-out rows for docs it will add later. *Multi-lobe brain:* run that against the hub index and the hub's documents, then check the registry against disk both ways — every registered lobe has a directory, every lobe directory is registered, at every depth — and check grammar conformance: every lobe carries the full doctype set, and any document beyond it appears in that lobe's **Also holds** cell or its local index.
2. **Version headers** — every canonical doc (except the version-exempt ones the target's `CLAUDE.md` declares; absent a declaration, those the version-and-date principle in `MBT_PATTERN.md` exempts) opens with a well-formed `> V<N>, YYYY-MM-DD.` and no smuggled change-note.
3. **Cross-references** — every mini-brain filename mentioned resolves to a current canonical file, not an `archive/` copy or a deleted file. *Multi-lobe brain:* resolve against the lobe that owns the lobespace, not the repo root.
4. **Namespace prefix** — every top-level knowledge file and every `working/` doc carries the lobespace (`find . working -maxdepth 1 -name '*.md' 2>/dev/null | grep -vE '/(CLAUDE|README)\.md$' | grep -v '/<LOBESPACE>_'` should print nothing — it tolerates a missing or empty `working/` and anchors the lobespace to the start of the filename). *Multi-lobe brain:* run it per lobe against that lobe's declared lobespace, over the lobe's own documents and its `working/` — never its `archive/`, where retired files legitimately keep the basename they were retired under and need not be markdown. Match the lobespace exactly: a document belongs to the lobe whose lobespace its name begins with in full, longest match winning. Lobespaces nest as prefixes (`ORCHARD` inside `ORCHARD_PRESS`), so the prefix test above silently accepts a child's document sitting in its parent's directory. A brain seeded before working docs carried the brain's lobespace names its in-flight docs `working/<WORK>_*` by the then-current convention — treat that as adopt-when-touched guidance, not a violation, since renaming a live item's docs breaks the routing signals that match on those names.
5. **Log discipline** — the session log is append-only and readable from its last separator (not required to be read whole); entries carry a date and session identifier. Append-only governs each entry's content, not its position, so dates out of sequence are not a violation: work-item closeout preserves each merged entry's original date, and folding one log into another places entries by date among the existing ones. Check that no entry was revised after the fact, not that the file runs chronologically.
6. **Cross-lobe references** (multi-lobe brains) — cross-lobe references stay within the entrypoint's declared exemptions: a child's SCOPE may cite its parent's SCOPE, its APPROACH its parent's APPROACH, and any document may name its own child lobes — never their files. Any other reference to another lobe or its files is a violation, sibling references above all. Logs and maintenance documents are exempt — a log records what a session touched, and a procedure names the files it operates on.
7. **Vocabulary alignment** — grep the target's canonical docs, `CLAUDE.md` and `README.md` for the old pattern vocabulary: "unit" (pattern-specific sense: a brain's hub or any of its children), "token" (pattern-specific sense: the SCREAMING_SNAKE_CASE namespace), "component" (pattern-specific sense: a non-hub node), "component-structured" and `<TOKEN>` / `<SUBTOKEN>` / `<PREFIX>` placeholders. A brain seeded before the rename to "lobe" / "lobespace" uses the old terms in its own docs and `CLAUDE.md`. The rename doesn't break it — its internal vocabulary is self-consistent — but it creates a vocabulary split: the toolkit says "lobe" while the brain says "unit," and a session loading both sees two terms for one concept. Report the split as an opportunity. Perform the walkthrough below only when the user opts in — never edit the target brain during a check unless the user explicitly asks. **Walkthrough:** for each hit, classify it by surrounding context. *Unambiguous pattern-specific* (e.g. "the brain's token is `ORCHARD`") — replace silently: "unit" → "lobe", "component" → "lobe", "component-structured" → "multi-lobe", "token" (namespace sense) → "lobespace", `<TOKEN>` → `<LOBESPACE>`, `<SUBTOKEN>` → `<SUBLOBESPACE>`, and `<PREFIX>` → `<LOBESPACE>` except where it names a document that lives only at the hub (session closeout, work setup, work closeout, dream cycle), which takes `<HUB>`. A brain that defined `<PREFIX>` as a compound (e.g. `LOBESPACE_<WORK>`) rather than the bare lobespace needs the compound expanded to its concrete form — the `<WORK>` slot must survive the conversion, so the replacement is the expanded compound, not a simple rename to `<LOBESPACE>`. *Unambiguous ordinary-English* (e.g. "unit test", "auth token", "software component") — skip silently. *Genuinely ambiguous* — surface to the user to judge. Bump version headers on each file touched.

---

## 4. Report

Produce a written assessment. Structure it:

- **Summary** — the brain's stage, its lobespace (or its lobe tree and per-lobe lobespaces, if multi-lobe), and a one-line overall read (what kind of shape it's in).
- **What's working** — the principles it embodies well. Lead here.
- **Principle scorecard** — the table from §2 with each verdict and note.
- **Structural issues** — anything the §3 checks flagged, most-actionable first.
- **Substance issues** — drifted SCOPE claims, a scope that has become a status report, cross-document inconsistencies, a lobe whose scope no longer states one problem, enforced-term misuses, entry concerns and candidates, and pruning candidates, if any.
- **Recommended next steps** — ranked, concrete opportunities. Frame each as "this brain does X well but Y would help because …", tied to a principle. If a step is "adopt lifecycle machinery," name the specific machinery and point at the relevant `templates/` file.

Keep it proportionate: a healthy brain gets a short report that says so. Reserve length for real, actionable gaps.
