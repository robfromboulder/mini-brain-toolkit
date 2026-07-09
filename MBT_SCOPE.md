# Mini-Brain Toolkit: Scoping Statement

> V4, 2026-07-09.

This document defines the problem that the mini-brain toolkit addresses, separately from design decisions and implementation details, as an objective and unbiased resource.

The mini-brain pattern has emerged organically across several projects as a way to hold a project's un-derivable knowledge in a small, curated set of plain-text files. It works, but at the time this toolkit was conceived it existed only as tacit convention plus one philosophical write-up — portable to no one who hadn't already seen the exemplars. Section 1 makes that gap precise.

---

## 1. Problem Statement

Every non-trivial project accumulates knowledge that its own artifacts cannot express: why a decision went the way it did, what was tried and abandoned, which constraints are load-bearing, what a document *doesn't* cover. The code shows the *what*; the git history shows the *sequence*; tickets show the *tasks*. None of them reliably preserve the *why*, and that is exactly the knowledge that is most expensive to reconstruct and most easily lost when a session ends or a person moves on.

The dominant responses to this fail in opposite directions. Wikis, second-brain systems, and most agent-memory frameworks **accumulate without bound** — they grow, drift out of date, and lower trust the larger they get. Lightweight instruction conventions (AGENTS.md and its kin) capture *how to act* but by design exclude rationale and lineage. Neither is tuned for the reader that increasingly consumes this knowledge: an AI agent loading files into a limited context window, which needs a few well-sized, well-indexed, high-signal files rather than a swarm of fragments or one monolith.

The mini-brain pattern answers this with an unusual bet — capture only what can't be re-derived, keep lineage separate from distilled truth, and shrink toward an irreducible core rather than accumulate. The pattern is demonstrably effective in the projects that use it. But the pattern itself was not portable. It lived as convention in a handful of repositories and as a single philosophical description. To start a new mini-brain, someone copied files from an existing one and imitated its structure by eye — which propagated whatever drift the source carried and depended on the copier already understanding the pattern's intent. There was no canonical definition an agent could apply, no repeatable procedure to establish or assess a brain, and no maintained set of base templates. The knowledge of *how to build the knowledge store* was itself un-derivable and undocumented — the exact problem the pattern was invented to solve, unsolved for the pattern itself.

---

## 2. Goals

These goals define what the toolkit must accomplish, expressed as outcomes. They do not prescribe the toolkit's own file structure or content, which are approach decisions.

### 2.1 Provide one canonical, operational definition of the pattern

A single current document should define what a mini-brain is in operational terms — the principles, the concrete file set, and the lifecycle — precise enough that a human or an agent can apply it without having seen the exemplars. It supersedes copy-and-imitate as the source of the pattern's intent, and both the establish and assess procedures build on it rather than restating it.

### 2.2 Make establishing a new mini-brain repeatable

Standing up a new mini-brain should be a defined procedure that an agent can execute from an intake conversation: choose a namespace, produce the seed file set, and know how to grow it into a filled brain and, later, a mature one. The procedure should be safe to re-run (additive, never destructive) and should not require the operator to have internalized the pattern first.

### 2.3 Make assessing an existing mini-brain repeatable

Evaluating whether a repo follows the pattern should be a defined procedure that produces *opportunities, not a grade*: a per-principle read, structural checks, and a spot-check that the content hasn't rotted, ending in ranked, concrete recommendations. It should work on any repo — one built from this toolkit or one that grew on its own — and it should observe without modifying the target.

### 2.4 Supply base templates for the whole file set

Every file in the pattern's file set should have a maintained base template with clear placeholders — the seed set and the mature-lifecycle machinery — so establishment is a copy-and-substitute operation against a single source of truth rather than a copy from whichever neighbor was nearest.

### 2.5 Exemplify the pattern it defines

The toolkit should itself be a mini-brain, following its own conventions at the sophistication of a healthy content-stage brain. Dogfooding makes the repo a worked example a reader can inspect, and it is the strongest possible test that the pattern and templates are usable in practice.

---

## 3. What Is Not In Scope

- **A general knowledge-management or "second-brain" system.** The toolkit serves the mini-brain pattern specifically — small, curated, shrink-toward-irreducible. Comprehensive knowledge capture is the opposite bet and is out of scope.
- **Automated or machine-managed capture.** The pattern is deliberately human-curated. Auto-extracting memories, vector stores, and background ingestion belong to a different family of tools (surveyed in `MBT_RESEARCH.md`) and are explicitly not what this toolkit provides.
- **Executable tooling — CLI, plugins, packaged automation.** The toolkit is agentic instructions plus templates, consumed by an agent reading markdown. A distributable CLI or IDE integration is a separate concern; `MBT_RESEARCH.md` tracks it, this scope does not include it.
- **Automatic migration of existing brains.** Assessment recommends; it does not rewrite a target brain in place. Bringing an existing brain up to the current pattern is a human-directed activity, not an automated one.
- **Prescribing project-specific content.** The toolkit defines structure and procedure, not what any given project's scope, approach, or findings should say.

---

## 4. Open Questions

### 4.1 Universal vs. exemplar-specific machinery

The mature-lifecycle templates are generalized from one mature brain. How much of that machinery is intrinsic to the pattern versus incidental to that project's shape (multi-platform, heavy test suites, eval numbers)? Until more brains reach maturity from these templates, the line between "part of the pattern" and "one project's local practice" is an estimate.

### 4.2 Keeping templates and reference brains in sync

The templates are distilled from live brains that keep evolving. When a reference brain improves a convention, nothing yet propagates that improvement back into the templates — the same divergence-by-copy problem the toolkit exists to solve, now between the toolkit and its exemplars. What mechanism (a periodic reconciliation, a designated source-of-truth brain) should keep them aligned is unresolved.

### 4.3 Whether assessment should ever change the target

Assessment is defined as observe-only. But the boundary between assessment and the dream cycle's mechanical fixes (a broken cross-reference, a malformed version header) is thin. Should there be a sanctioned "assess-and-fix-mechanical-only" mode, or does any change belong strictly to establishment and the dream cycle? Left observe-only for now.

### 4.4 Composition across multiple brains

The namespace-token convention exists so multiple brains can load into one session without collision. As that becomes common — a session spanning several projects' brains — questions arise about cross-brain references, a shared index, and role-lensed recall. The pattern supports co-loading today; it does not yet address coordination between co-loaded brains.

### 4.5 The right maturity floor for a new brain

Establishment produces a seed and documents growth into content and mature stages, deferring machinery until "the work justifies it." That judgment is left to the operator. Whether some projects should start further along — or whether a lighter-than-seed brain is legitimate for very small projects — is not settled.
