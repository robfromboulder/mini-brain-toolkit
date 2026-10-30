# Mini-Brain Toolkit: Scoping Statement

> V15, 2026-10-30.

This document defines the problem that the mini-brain toolkit addresses, separately from design decisions and implementation details, as an objective and unbiased resource.

---

## 1. Problem Statement

Every non-trivial project accumulates knowledge that its own artifacts cannot express: why a decision went the way it did, what was tried and abandoned, which constraints are load-bearing, what a document *doesn't* cover. The code shows the *what*; the git history shows the *sequence*; tickets show the *tasks*. None of them reliably preserve the *why*, and it is lost when a session ends or a person moves on. Wherever a project's why is kept, whether in a person's memory, the artifacts, documents or a memory service, is its knowledge store.

This is not a lapse in discipline. A well-kept codebase leaves the why out on purpose. A bug with three candidate fixes ships one, and comments describing the two not taken would distract from what comments are for, explaining what the code does. The same holds at every scale: alternatives weighed, experiments that failed or succeeded, and decisions that shaped the codebase as a whole. The cleaner the artifacts, the less of the why they carry.

This problem is that of developers who keep their projects in git repositories and work on them through coding agents. Both are commitments they made outside any knowledge store, so every approach must fit projects kept in git and serve an agent reader. An agent starts each session knowing only what it loads, into a limited context window. Whatever holds the why must be readable within that budget.

Whatever form the knowledge store takes, it has to be set up and kept true by people and agents who didn't design it. A convention passed on by copying an existing example carries whatever drift that example has, and works only if the copier already understands its intent. Knowing how to keep such a store is itself knowledge of this kind: unless it is written down, it lives only with whoever built the first one.

---

## 2. State of the Problem

This assessment is as of October 2026.

**Leaving it to the artifacts.** Code, comments, commit messages, pull request descriptions and tickets. Nothing new to set up or maintain. The why survives only in fragments scattered across history, which an agent finds only by knowing to search for them, and a clean codebase keeps most of it out.

**Remembering it.** The developer holds the why and re-explains it as needed, to colleagues and to every new agent session. It costs nothing to set up. It scales with one person's memory and time, repeats the same explanation each session, and leaves with the person.

**Architecture decision records.** One short document per decision, kept in the repository and superseded rather than revised. They hold the why of individual decisions well. The current state must be reconstructed by reading the chain, the set grows with every decision, and experiments, discoveries and the problem itself have no place in it.

**Wikis and second-brain systems.** Comprehensive, linked and searchable. They grow without bound, drift because nothing forces a page to be revised, and lose trust as they grow. Most live outside the repository and its review.

**Agent instruction files (AGENTS.md, CLAUDE.md and kin).** One file at the repository root that tells an agent how to act, loaded every session. They are cheap and widely supported, but by convention hold instructions and exclude rationale and lineage, and a single file that tries to hold more outgrows the context budget.

**Automatic memory (agent-memory frameworks, harness memory features).** Capture happens as a side effect of work: memories are extracted from sessions, often into a vector store, and retrieved on demand. Nobody has to curate. What is kept is whatever the extractor kept, it accumulates, and retrieval returns fragments rather than a coherent account. Capturing what sessions see raises privacy and governance questions that aren't trivial to answer: what was stored, who can read it, and how to remove it. Many keep memory outside the repository, per user or per machine.

**A small curated knowledge store beside the code.** A handful of documents kept deliberately, holding only what the artifacts can't express, indexed so an agent loads the one a question needs, and revised in place as the project changes. It stays small enough to check whole and to fit the context budget. It asks someone to curate it and to check it against the project; left alone, it drifts like any document. It also has to be set up to a convention, in one of three ways. Set up by hand, it works only if the person setting it up already understands the convention. Copied from a neighboring project, it looks right at once but inherits the source's drift and project-specific detail, and depends on the copier understanding which parts carry the intent. Generated from templates and checked by a linter, its setup and structure are repeatable and mechanical, but the linter checks form, not whether the content is true or still worth keeping, and both tools are installed and versioned beside each project.

### Conditions every option faces

**Context is limited.** Whatever an agent loads competes with the work for its context window, so what is kept must be sized and indexed for selective loading.

**Knowledge drifts.** Code changes under any written account of it, and nothing marks the account stale unless something checks it.

**Upkeep has no natural moment.** Nobody maintains documentation unprompted, and nothing in the work stops to ask whether what is kept is still true.

### Evidence the problem is real

Each alternative above is in use. Architecture decision records have been practiced since Michael Nygard proposed them in 2011 as a record of each architectural decision's context and consequences. Agent instruction files are a convention shared across coding agents. Agent-memory frameworks are published, and coding agents ship memory features of their own. Each keeps some part of what a project's artifacts leave out.

---

## 3. Goals

### 3.1 The why survives sessions and people

What the artifacts can't express (decisions and the alternatives they beat, experiments and their results, the problem as understood) outlasts the session and the person that produced it, and is there for whoever works on the project next.

### 3.2 What is kept stays true as it grows

As the project changes, what is kept stays current, and its trustworthiness doesn't fall as it grows.

### 3.3 An agent loads only what its question needs

An agent with a limited context window finds and loads the knowledge a question needs, without loading the rest.

### 3.4 Starting needs no expertise and inherits no drift

Someone who has never seen an example can set up a knowledge store correctly, and a new one carries none of another project's drift. Setting one up never destroys what a project's repository already holds, so it is safe to repeat.

### 3.5 Any knowledge store can be assessed

Anyone can learn whether a project's knowledge store has drifted and what to do about it, whether it was set up deliberately or grew on its own.

### 3.6 Upkeep asks little of the owner

What is kept stays true without the owner having to remember to maintain it, and their attention is asked only for the calls only they can make.

### 3.7 The owner governs what is kept

Everything kept is visible to the project's owner, can be corrected or removed, and is shared only as the project is.

---

## 4. What Is Not In Scope

- **Prescribing project-specific content.** What a project's knowledge says is that project's own; the problem is how it is kept.
- **Migrating a knowledge store automatically.** Bringing a knowledge store up to a new convention changes how the owner's knowledge is organized and stated, so the owner directs it change by change.

---

## 5. Open Questions

### 5.1 Knowledge across several projects

Sessions increasingly span several projects at once, each with its own kept knowledge. What a session working across them needs to know of each, and when, is not settled.

### 5.2 How small a project can be and still lose its why

Below some size, the people involved may hold the whole why themselves. Where that line falls is not settled.
