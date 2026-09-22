# Enforced Terms: Decision Record

## Problem

A mini-brain's documents are authored one at a time, across many sessions, by writers who deliberately do not have the siblings in view — orthogonality requires exactly that. Under those conditions a word that carries a precise, load-bearing meaning in one document gets picked up as an ordinary generic in another. Each use is defensible read alone, and the collision surfaces only when both documents land in one context window — which is the reader the pattern is built for.

Nothing in the pattern reserves a word. A brain can state a convention in the term's own home document and still have that term quietly re-purposed three documents away, because the re-purposing writer never had a reason to check. The check procedure looks for a term carrying two jobs, but that check is purely detective: there is no declared vocabulary to check against, so it finds only what a reader notices by eye while holding the whole canonical set at once. Asserting a candidate list against this brain's current content found several words already carrying two senses — in a brain that runs that check — so the detective form is demonstrably not sufficient on its own.

The cost is paid twice. A reader spends attention resolving which sense is meant, on every encounter, forever. A writer extending the brain picks the wrong sense and writes a rule that is subtly false, which is far more expensive than a reader's momentary confusion because it propagates.

## Preferred approach: a small set of enforced terms, harvested rather than authored

The brain declares a deliberately small set of words whose meaning it **enforces**. Each entry is a prose paragraph that opens with the term in bold and states what the thing *is* in one to three sentences — never its benefits, motivation, history, use cases, or origin — then states what it must not be confused with, so a writer knows which sense to avoid. Each entry is defined without invoking any other entry, by name or by relation, so every entry stands alone and the file reads correctly in any order.

The disambiguation is the load-bearing part and the reason this is not a glossary. A glossary answers "what does this word mean?", which the term's home document already answers better; the un-derivable part is "this word is *taken*, and here is the sense it will be mistaken for." That is knowledge no document holds, because each document is written without its siblings in view — the exact negative-space test the pattern applies to everything else.

Three rules keep the set small, and each names the failure it prevents:

- **Harvest, never author.** An entry is added when a collision is *found* — by a check, by a maintenance pass, or by a session having to stop and ask which sense a word carries. Entries are never brainstormed from the domain's vocabulary. Authoring a vocabulary up front is how an enforced-terms list becomes an ontology, and an ontology is unbounded by construction.
- **An empty disambiguation is a delete.** A term nobody would plausibly misuse does not earn an entry, however important the concept is. This is the shrink discipline expressed as an entry-level test, and it is what lets the list get *smaller* as a brain's prose gets more careful.
- **Disambiguate, never define.** The entry says which sense is enforced and what it must not be confused with; it does not restate the full treatment that lives in the term's home document. An entry that grows into a paragraph of rationale has become a second copy of the concept and must be cut back.

The enforced terms are consumed at four points, which is what makes this enforcement rather than documentation:

- **Write time** — the writing rules gain one line: an enforced term is used in its enforced sense or a different word is used. This is the only point that *prevents* a collision.
- **Check time** — for listed terms, a per-term grep of the canonical docs replaces reading the whole set by eye, and every hit is judged against the entry's enforced meaning and its disambiguation. A collision on an unlisted term still needs the set read, and is reported as a candidate for the user to confirm.
- **Maintenance time** — a dedicated judgment pass in the dream cycle checks the file against its own rules, corrects a listed term's misuse in place, proposes drifting unlisted terms for the user to confirm, and flags entries whose disambiguation has gone empty. It never scans the logs, which are append-only and cannot be corrected.
- **Work closeout** — each doc the closeout edited is checked for a listed term used with the wrong meaning, or a loose synonym standing in for one, and corrected. Proposing new terms is left to maintenance time.

**Placement: a standalone file with a read-index row.** The enforced terms live in their own document (`<PREFIX>_ENFORCED_TERMS.md`), listed in the read index like any other canonical document. A standalone file gives clearer modularity and more efficient context use — enforced terms need not be loaded in every session, which matters as the list grows. The write-time rule in the entrypoint's writing conventions directs a writer to consult the file before authoring. In a brain whose knowledge divides into lobes the file lives at the hub, since terms govern writing across the whole brain — the same placement rule as session closeout and the other brain-wide documents.

**Maturity: added when the work justifies it, like the other lifecycle machinery.** A new brain declares nothing — it has not yet used any word enough to have a collision, and seeding a vocabulary is the authoring failure above wearing a procedure's clothes. An enforced terms file with zero entries is the normal state for most of a brain's life and is never a gap a check should flag.

## Alternatives considered

- **A glossary.** Rejected on the pattern's core bet. It defines the project's vocabulary, which grows without bound, duplicates the documents that already explain each concept, and is re-derivable from them. It also answers the wrong question: a reader confused by a word can already read its home document, whereas a *writer* about to re-purpose a word has no signal at all.
- **Rely on the existing one-term-one-meaning check.** Rejected as sufficient, kept as the fallback for brains that declare nothing. It requires holding the whole canonical set at once, scales badly as a brain grows, is detective rather than preventive, and has no declared vocabulary to test against — so it catches collisions in proportion to how carefully a particular reader happened to be looking. Live collisions surviving in this brain are the evidence.
- **Fix each collision with a disambiguating qualifier and move on** (e.g. write "namespace lobespace", never bare "lobespace"). Rejected as the mechanism, adopted as the usual *fix*. Nothing records which words need the qualifier, so every writer re-derives the need from scratch and most will not — the same divergence-by-imitation problem the toolkit exists to solve, one word at a time.
- **Let each document declare the terms it owns, with no central list.** Rejected: it puts the declaration where the term is already used correctly and leaves the writer who is about to misuse it — reading some other document — with nothing to consult. The declaration has to sit where the collision happens, not where the concept lives.
- **Make the maintenance check a mechanical grep in the structural-integrity phase.** Rejected: every hit needs a judgment about which sense is meant, which a mechanical phase cannot make, and an unscoped grep reaches the append-only logs, whose hits can never be fixed.
- **Have a work item declare any term it coins, for closeout to act on.** Rejected: nothing downstream reliably consumed the callout, and the brain that first used enforced terms runs on conformance checks alone, surfacing new terms only in its maintenance pass.
- **Place the enforced terms in the entrypoint's conventions section rather than a standalone file.** Rejected: a standalone file gives clearer modularity and more efficient context use. The entrypoint carries a write-time rule directing writers to consult the file, achieving the same enforcement without loading the terms into every session.

## What this doesn't solve

- **Terms whose everyday form is ubiquitous.** A word in constant innocent use cannot be enforced by grep, because the hits are dominated by legitimate ordinary English. Such a term fails the enforcement it exists for, so it does not earn an entry.
- **Collisions between two brains co-loaded in one session.** An enforced term binds inside one brain. Coordination across co-loaded brains is an open question the pattern already carries, and nothing here advances it.
- **Which sense should win.** The enforced terms file records that a word is taken and by whom; deciding which of two live senses is the enforced one is an editorial judgment for the user, exactly as the pattern treats every other contradiction discovered rather than shipped.
- **Two words for one concept.** An entry enforces a word against a rival *meaning*; it has no way to enforce against a rival *word*. A brain that drifts into calling one thing by two names costs a reader what one word for two things costs, and no disambiguation can express it.
- **Terms in the code the brain describes.** The enforced terms govern the brain's own prose. A project's domain vocabulary belongs to the project, and enforcing it here would pull the brain toward being a wiki for the product.

## Reversals

The check procedure states, of the one-term-one-meaning check, that the collision shows only side by side so no single-file check finds it. For a brain that declares enforced terms, a per-term grep does find it. The sentence becomes false for those brains and must be reconciled in place rather than joined by a second claim beside it.
