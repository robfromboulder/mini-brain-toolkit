# Mini-Brain Toolkit: Technical Approach

> V19, 2026-10-30.

This document describes the approach for addressing the problems defined in `MBT_SCOPE.md`. It covers the strategic approach and key design decisions — not delivery sequence.

---

## 1. Strategic Approach

### 1.1 Curate what can't be re-derived

The toolkit serves developers whose coding agent loads an instruction file at session start. That is narrower than whoever has the problem in `MBT_SCOPE.md`: a project worked through an agent that loads no instruction file is not served, and every goal goes unmet for it. It builds on SCOPE's premises rather than choosing them: git provides history, review and sharing on the project's own terms but holds no why beyond commit messages, and the coding agent provides the judgment to read, check and revise prose, reading its instruction file first.

On those foundations the toolkit's answer is the mini-brain pattern, an unusual bet: capture only what can't be re-derived, keep lineage separate from distilled truth, and shrink toward an irreducible core rather than accumulate. A few well-sized, indexed markdown files live in a repository of their own beside the project's code, curated by a person working with an agent. The bet is that a knowledge store kept small can be checked whole, so it stays true as it grows (*what is kept stays true as it grows*). Against the alternatives `MBT_SCOPE.md` assesses:

- **Wikis and second brains** are the second approach, the one that differs most: they make the opposite bet, capturing comprehensively and linking everything rather than keeping only what can't be re-derived. They could meet the context budget by loading pages selectively, but nothing forces a page to be revised, so their trustworthiness falls as they grow. The pattern keeps less, prunes what has become re-derivable, and re-checks all of it on a schedule (§2.3).
- **Automatic memory** captures as a side effect of work and retrieves on demand, with nobody curating. It removes the curation burden, but keeps whatever its extractor kept, accumulates, and leaves what was stored and who can read it hard to govern. The toolkit curates instead, and keeps what is kept in a repository under version control and review, so the owner sees and corrects it as they do code (*the owner governs what is kept*). That goal is only partly met: the brain's repository has its own access settings, so it is shared as the project is only where the owner sets it to match. Automatic capture is not ruled out; it is not what this toolkit provides.
- **Leaving it to the artifacts** keeps the code clean by keeping the why out. The pattern keeps the why beside the code rather than in it, so neither has to compromise (*the why survives sessions and people*).
- **Remembering it** leaves with the person and is re-explained every session. The pattern writes it where every session's agent loads it (*the why survives sessions and people*).
- **Agent instruction files** are the closest alternative, and the pattern builds on one: its entrypoint is the instruction file the agent loads first. It holds only a read index and conventions, and the why lives in separate files loaded on demand, so the file loaded every session stays within the context budget and rationale has a home the convention excludes (*an agent loads only what its question needs*).
- **Architecture decision records** hold lineage but leave the current state to be reconstructed. The pattern keeps lineage in an append-only log and revises the distilled truth in place.

The pattern belongs to the curated-store class `MBT_SCOPE.md` assesses, and within that class the toolkit settles how a store is set up and checked:

- **Copying a neighbor** inherits its drift. Establishment copies from templates instead (§1.5).
- **Generators and linters** (and IDE integrations) make setup and structural checks mechanical. The toolkit is instead agentic instructions plus templates, consumed by an agent reading markdown. The agent is already there to read and maintain the brain, so instructions add no dependency installed or versioned beside each project, and the checks that matter (is this true, is it still worth keeping, does it belong here) take the judgment a linter lacks. A distributable CLI or IDE integration is a separate concern, not built here.

### 1.2 Dogfood the pattern

The toolkit is itself a mini-brain, and its subject is the mini-brain pattern. Building and maintaining it runs the templates and procedures on a real brain, which is the strongest available test that someone can start a knowledge store without expertise and assess one (*starting needs no expertise and inherits no drift*, *any knowledge store can be assessed*). A toolkit that defined the pattern while not following it would be its own counterexample.

The one wrinkle dogfooding creates is that two kinds of top-level knowledge file coexist: the toolkit's *own* brain (its problem, design, and findings) and the *pattern it defines* as a consumable product (the reference documents and the two procedures). The read index resolves this by grouping the two in blocks rather than interleaving them.

### 1.3 Distill from live exemplars, do not invent

The pattern already works in production brains. The toolkit's job is to *capture* what those brains do, not to design a pattern from first principles. Every template and every procedure step is derived from the ground-truth exemplars — a content-stage brain and a mature brain — so the toolkit inherits conventions that survived real use rather than conventions that sounded good on paper, and someone adopting them needs no expertise to trust them (*starting needs no expertise and inherits no drift*). Where the exemplars carry project-specific detail (test suites, eval numbers, platform splits), the toolkit generalizes it to placeholders while preserving the mechanics that give the convention its value.

### 1.4 Separate the reference from the procedures

The definition and the two procedures are split into separate documents rather than one, serving *starting needs no expertise and inherits no drift*, *any knowledge store can be assessed* and *an agent loads only what its question needs* in `MBT_SCOPE.md`: a standalone reference that says *what a mini-brain is and why* — a base definition plus an opt-in layout layer for brains whose knowledge divides into several lobes, so a simple brain never loads conventions it doesn't use — and two procedure documents that say *how to build one* and *how to judge one*. A single combined document would be simpler to find, but it would fuse the neutral reference with two opposed procedures. The split mirrors how the live brains separate a standalone reference from action-oriented runbooks, and it pays off in two ways: each document stays small and loads only when its question is being asked, and establishment and assessment — genuinely different activities — don't get tangled in one document. The cost is more files where the reader must know which one they want, mitigated by the grouped read index. Each part of the definition lives in exactly one reference document, cited rather than restated, so it has exactly one home.

### 1.5 Templates as the single source of truth

Establishment is a copy-and-substitute operation against `templates/` (answering *starting needs no expertise and inherits no drift* in `MBT_SCOPE.md`), never a copy from whichever neighbor was nearest. Centralizing the base files in one directory is what turns "propagate the pattern" from imitation-with-drift into a mechanical, repeatable step — and it gives the template/reference sync problem (§2.9) a single place to be solved when it's solved.

---

## 2. Key Design Decisions

### 2.1 Lobespace `MBT`

The toolkit carries a lobespace like any other brain. `MBT` was chosen over mirroring the repo name (`TOOLKIT`) or the subject (`BRAIN`): it is short, unambiguous, and — because the toolkit is frequently loaded *alongside* the very brains it assesses — must not collide with a target brain's files. `BRAIN` risked conceptual collision in exactly that scenario; `MBT` cannot.

### 2.2 Keep the archived docs as source material, distill a canonical reference

The philosophical description stays in `archive/` and is treated as source, exactly as a content-stage brain keeps its originating design docs in `archive/` and distills them into SCOPE/APPROACH. The distilled, current, operational reference is what the read index carries; the archived philosophical doc remains the fuller "why" for anyone who wants it. This avoids two live copies of the definition drifting apart — the philosophy doc is deliberately kept out of the read index. The improvement roadmap gets the same treatment: the archived source stays in `archive/`, distilled into a living current-state document.

### 2.3 Checking is a conversation; the dream cycle runs unattended

The two procedures that examine an existing brain answer *any knowledge store can be assessed* and *upkeep asks little of the owner* in `MBT_SCOPE.md`, and they sit at opposite ends. A check is a specific ask from a user who wants to know whether their brain needs modernizing, so it is conversational. It leads with what's working and ranks the gaps as opportunities rather than a grade, matching the pattern's stance that adherence is a target, not a gate. It puts judgment calls to the user as they arise — an ambiguous vocabulary hit, a candidate enforced term — and changes the target only where the user directs, item by item. The dream cycle runs on a cadence with nobody present, so it never waits on an answer: it corrects mechanical drift, and every judgment call goes to its log for the user to act on later. Keeping the two apart lets the check ask freely and the dream cycle finish every time.

### 2.4 Templates are un-namespaced

Template files use bare names and placeholders so the copy-and-substitute step is obvious. `README.md` in a new repo is merged into rather than overwritten, since it is a repo artifact that may already exist.

### 2.5 Defer mature machinery when establishing

A new brain gets the seed only. The mature-lifecycle docs are real read-index entries a reader must skip on every load, so scaffolding them empty is a cost paid every session for machinery not yet in use. Establishment therefore defers them until the work justifies them — the same shrink-toward-what's-needed discipline the pattern applies to content, applied to structure.

### 2.6 The project-repo hook is merged, not copied

Where a developer works migrates over a project's life: before project code exists, work items are thought through in the brain itself; once the project is established, iteration happens in a project repo, and switching directories to use the brain is friction that kills the habit. The hook template answers this — a section merged into each project repo's `CLAUDE.md` that loads the brain into that repo's sessions on demand and has the agent proactively offer a session closeout at natural stopping points — so the brain's workflows run wherever the developer already is, in both directions and at every stage. It was distilled from the exemplar where it emerged, where the closeout prompt measurably increased brain use. Because the target `CLAUDE.md` belongs to the project repo and may already exist, the hook is merged in as a section, never copied over — the same rule as `README.md`.

### 2.7 An entrypoint routes each question to one file

The agent loads the entrypoint every session, and it carries a read index mapping each kind of question to the one file that answers it, which the orthogonal file set makes possible. Logs are read from their last separator, not whole, and a brain whose knowledge divides into lobes routes a question to its lobe before its file. An agent therefore loads the index and the files its question names and nothing else (*an agent loads only what its question needs*). Retrieval by search over a larger knowledge store was the alternative; it returns fragments ranked by similarity rather than the one account the question needs, and it requires an index or service installed beside each project, a dependency the toolkit chooses not to add.

### 2.8 Open: universal vs. exemplar-specific machinery

The mature-lifecycle templates are generalized from one mature brain. How much of that machinery is intrinsic to the pattern versus incidental to that project's shape (multi-platform, heavy test suites, eval numbers)? Until more brains reach maturity from these templates, the line between "part of the pattern" and "one project's local practice" is an estimate.

### 2.9 Open: keeping templates and reference brains in sync

The templates are distilled from live brains that keep evolving, and an improvement a reference brain makes to a convention reaches the templates only if someone carries it back — the same divergence-by-copy problem the toolkit exists to solve, now between the toolkit and its exemplars. What mechanism (a periodic reconciliation, a designated source-of-truth brain) should keep them aligned is unresolved.

### 2.10 Open: the maturity floor for a new brain

Establishment produces a seed and defers machinery until the work justifies it (§2.5), leaving that judgment to the operator. Whether some projects should start further along, or whether a lighter-than-seed brain is legitimate for very small projects, is not settled.

### 2.11 Open: coordination between co-loaded brains

The lobespace convention lets several brains load into one session without collision, but the pattern does not coordinate them. Whether co-loaded brains need references between them, a shared index, or recall that reads each through the role it plays is not settled.

### 2.12 Open: a check's proportion on a large scope

The check reports a section once as a rewrite when issues cover most of it, and a scope once as one to re-gather when most sections need that. Whether this keeps a report proportionate on a large scope is unsettled: a blind check of a mid-sized scope still reported its 33 issues item by item.

### 2.13 Open: ordering goals by impact

The create procedure orders goals by their impact on whoever has the problem, as far as the evidence ranks them. Whether that ordering earns its place when the evidence cannot rank them is undecided.

### 2.14 Open: the create procedure on a multi-lobe intake

One single-lobe test intake, answered by a simulated owner, produced a neutral SCOPE on the first pass. Whether the first pass holds for a multi-lobe intake and a real owner is untested.

### 2.15 Open: one home for the definitions

Premise, choice, alternative and second approach are defined in the create and check procedures, the dream cycle and three templates, and the copies differ: create decides whether something the problem holder has is a premise by whether every approach must use it, while check lets the owner's answer decide. Whether each definition should live once, in the pattern's reference document, for the procedures to cite, is undecided.

### 2.16 Open: testing the instructions by running them

A review checks the instructions against their own rules. A dry run, in which an agent holding only a procedure runs it on a real brain, checks whether it reaches the owner's verdict, and it found what review did not. Whether to keep a fixed set of synthetic brains with planted defects and expected results, run blind after each change to the instructions, is undecided.
