# Key Terms: Decision Record

## Problem

Three of the pattern's core terms — "unit" (a brain's hub or any of its components at any depth), "token" (the SCREAMING_SNAKE_CASE namespace prefix a brain declares), and "component" (a non-hub unit whose problem is one of several its parent's problem divides into) — carry precise, load-bearing meanings in the pattern while sharing names with ubiquitous ordinary-English and software concepts. "Unit" collides with unit test, unit of work, organizational unit; "token" collides with auth token, LLM token, parsing token; "component" collides with software module, service, or UI component.

These collisions cannot be solved by enforcement. A grep for "unit," "token," or "component" in any brain documenting software returns overwhelmingly legitimate ordinary-English hits, burying the real collisions in noise. The enforced-terms mechanism requires a word whose ordinary form is rare enough that a grep can separate the senses — all three fail that test.

Every brain seeded from the toolkit inherits these terms. A downstream brain documenting LLM infrastructure uses "token" in both the namespace-prefix and context-window senses in the same documents. A downstream brain documenting a service architecture uses "unit" and "component" for both brain structure and software architecture. The collision is not a risk; it is a certainty for the domains the pattern most commonly serves.

## Preferred approach: rename to distinctive terms that don't collide

Replace the pattern's own vocabulary with words unlikely to appear in any downstream brain's domain:

- **unit → lobe** — extends the brain metaphor (a brain's lobes are distinct functional regions), is distinctive enough to be collision-free in software contexts, and works at any depth without strain.
- **component → lobe** — collapses into the same term. A component is a non-hub unit, which in the new vocabulary is simply a child lobe. "Component-structured brain" becomes "multi-lobe brain." This eliminates a collision-prone term entirely rather than replacing it with a second new word.
- **token → lobespace** — a compound of "lobe" and "namespace" that is self-describing (the namespace a lobe declares), maintains the brain metaphor, and has effectively zero collision risk in any domain.

All three terms collapse to two — lobe and lobespace — both specific to this pattern and unlikely to appear in a brain's product vocabulary. A brain documenting authentication tokens, LLM context tokens, or React components never needs to disambiguate against "lobe" or "lobespace."

## Alternatives considered

- **Enforce the current terms via the enforced-terms mechanism.** Rejected: their everyday forms are too ubiquitous for grep-based enforcement. An enforced-terms entry for "unit," "token," or "component" would generate more false positives than real hits, failing the mechanism it exists for.
- **prefix (for token).** Descriptive — says what the thing is. Rejected: "prefix" still collides with CSS vendor prefixes, CLI flag prefixes, and other software uses. Lobespace is more distinctive and maintains the brain metaphor.
- **cortex (for unit).** Extends the brain metaphor. Rejected: cortex specifically means the brain's outer layer, which maps poorly to nested structures — a sub-component is not a sub-cortex.
- **Invented opaque terms (e.g. "screamfix").** Maximally collision-resistant but opaque — a reader encountering the term has to stop and learn it with no etymological help. Lobespace is also a compound but self-describes (lobe + namespace), so the learning cost is lower.

## What this doesn't solve

- **Downstream brains that already use the old vocabulary.** A brain seeded before this rename uses "unit," "token," and "component" in its own docs. The migration path for existing brains is a separate concern.

## Reversals

Every document in the toolkit that uses "unit," "token," or "component" in the pattern-specific sense carries stale vocabulary after this rename. This is a wholesale vocabulary change, not a reconcile-in-place.
