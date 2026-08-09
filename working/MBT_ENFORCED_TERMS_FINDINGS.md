# Enforced Terms: Decision Record

## Problem

A mini-brain's documents are authored one at a time, across many sessions, by writers who deliberately do not have the siblings in view — orthogonality requires exactly that. Under those conditions a word that carries a precise, load-bearing meaning in one document gets picked up as an ordinary generic in another. Each use is defensible read alone, and the collision surfaces only when both documents land in one context window — which is the reader the pattern is built for.

Nothing in the pattern reserves a word. A brain can state a convention in the term's own home document and still have that term quietly re-purposed three documents away, because the re-purposing writer never had a reason to check. The check procedure looks for a term carrying two jobs, but that check is purely detective: there is no declared vocabulary to check against, so it finds only what a reader notices by eye while holding the whole canonical set at once. Asserting a candidate list against this brain's current content found several words already carrying two senses — in a brain that runs that check — so the detective form is demonstrably not sufficient on its own.

The cost is paid twice. A reader spends attention resolving which sense is meant, on every encounter, forever. A writer extending the brain picks the wrong sense and writes a rule that is subtly false, which is far more expensive than a reader's momentary confusion because it propagates.

## Preferred approach: a small registry of reserved terms, harvested rather than authored

The brain declares a deliberately tiny set of words it has **reserved**. Each row carries four cells:

| Cell | What it holds |
|---|---|
| **Term** | The reserved word. |
| **Reserved meaning** | One line of disambiguation — not a definition of the concept. |
| **Home** | The document whose subject the term is, where its full treatment already lives. |
| **Not** | The specific near-miss the term must not be used for. |

**Not** is the load-bearing cell and the reason this is not a glossary. A glossary answers "what does this word mean?", which the home document already answers better; the un-derivable part is "this word is *taken*, and here is the sense it will be mistaken for." That is knowledge no document holds, because each document is written without its siblings in view — the exact negative-space test the pattern applies to everything else.

Three rules keep the registry small, and each names the failure it prevents:

- **Harvest, never author.** A row is added when a collision is *found* — by a check, by a maintenance pass, or by a session having to stop and ask which sense a word carries. Rows are never brainstormed from the domain's vocabulary. Authoring a vocabulary up front is how a reserved-terms list becomes an ontology, and an ontology is unbounded by construction.
- **An empty Not cell is a delete.** A term nobody would plausibly misuse does not earn a row, however important the concept is. This is the shrink discipline expressed as a row-level test, and it is what lets the registry get *smaller* as a brain's prose gets more careful.
- **Disambiguate, never define.** The row says which sense is reserved and points at the home; it does not restate what the home says. A row that grows into a paragraph has become a second copy of the concept and must be cut back.

The registry is consumed at four points, which is what makes it enforcement rather than documentation:

- **Write time** — the writing rules gain one line: a reserved term is used in its reserved sense or a different word is used. This is the only point that *prevents* a collision, and it is why placement matters below.
- **Check time** — a per-term grep replaces reading the whole set by eye. Every hit is judged against the row's reserved meaning and its Not cell. This moves the one-term-one-meaning check from a substance check needing a full-set read to a structural check a grep can drive.
- **Maintenance time** — re-grep each row, harvest candidates the sessions since the last pass surfaced, and retire rows whose Not cell has gone empty.
- **Work closeout** — a work item that coins a term or gives an existing one a second job declares it, alongside the existing callout naming the canonical claim the item reverses. Both are things a wording-based grep cannot find at merge time and only the author knows.

**Placement: the entrypoint's conventions, graduating to its own document.** Enforcement at write time requires the list to be in context while prose is being written, and the entrypoint is the one document every session loads. A separate document in the read index is loaded only when a question needs it, and "am I about to misuse a word?" is never the question a session sets out to ask — so a reserved-terms document nobody loads enforces nothing. The registry is small by construction, so the always-loaded cost is bounded. When it outgrows a screen it earns its own document, and the entrypoint keeps a line instructing that it be read before authoring. In a brain whose knowledge divides into components the registry sits at the hub with the other conventions, since a term used by two units is by the placement rule the ancestor's to hold.

**Maturity: added when the work justifies it, like the other lifecycle machinery.** A new brain declares nothing — it has not yet used any word enough to have a collision, and seeding a vocabulary is the authoring failure above wearing a procedure's clothes. A registry with zero rows is the normal state for most of a brain's life and is never a gap a check should flag.

## Alternatives considered

- **A glossary.** Rejected on the pattern's core bet. It defines the project's vocabulary, which grows without bound, duplicates the documents that already explain each concept, and is re-derivable from them. It also answers the wrong question: a reader confused by a word can already read its home document, whereas a *writer* about to re-purpose a word has no signal at all.
- **Rely on the existing one-term-one-meaning check.** Rejected as sufficient, kept as the fallback for brains that declare nothing. It requires holding the whole canonical set at once, scales badly as a brain grows, is detective rather than preventive, and has no declared vocabulary to test against — so it catches collisions in proportion to how carefully a particular reader happened to be looking. Live collisions surviving in this brain are the evidence.
- **Fix each collision with a disambiguating qualifier and move on** (write "namespace token", never bare "token"). Rejected as the mechanism, adopted as the usual *fix*. Nothing records which words need the qualifier, so every writer re-derives the need from scratch and most will not — the same divergence-by-imitation problem the toolkit exists to solve, one word at a time.
- **Let each document declare the terms it owns, with no central list.** Rejected: it puts the declaration where the term is already used correctly and leaves the writer who is about to misuse it — reading some other document — with nothing to consult. The declaration has to sit where the collision happens, not where the concept lives.

## What this doesn't solve

- **Terms whose everyday form is ubiquitous.** A word in constant innocent use cannot be enforced by grep, because the hits are dominated by legitimate ordinary English. Such a term can still be listed, but its check stays a by-eye read, so the registry is only partly mechanical.
- **Collisions between two brains co-loaded in one session.** A reserved term binds inside one brain. Coordination across co-loaded brains is an open question the pattern already carries, and nothing here advances it.
- **Which sense should win.** The registry records that a word is taken and by whom; deciding which of two live senses is the reserved one is an editorial judgment for the user, exactly as the pattern treats every other contradiction discovered rather than shipped.
- **Two words for one concept.** A row reserves a word against a rival *meaning*; it has no cell for a rival *word*. A brain that drifts into calling one thing by two names costs a reader what one word for two things costs, and no Not cell can express it — the mirror defect, and the registry is structurally blind to it.
- **Terms in the code the brain describes.** The registry governs the brain's own prose. A project's domain vocabulary belongs to the project, and reserving it here would pull the brain toward being a wiki for the product.

## Reversals

The check procedure currently states, of the one-term-one-meaning check, that the collision shows only side by side so no single-file check finds it. For a brain that declares reserved terms, a per-term grep does find it. The sentence becomes false for those brains and must be reconciled in place rather than joined by a second claim beside it.
