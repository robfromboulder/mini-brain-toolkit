# Mini-Brain Toolkit: Cognitive-Science Grounding Registry

> V2, 2026-07-16.

This file grounds the mini-brain pattern's biological metaphors for memory and cognition in the actual science — organized **by target field of cognitive science** — and interrogates whether each grounding is load-bearing or merely flattering. The conclusions this grounding supports live in `MBT_RESEARCH.md`.

A field's foundational science is effectively **static** — CLS (1995), SHY (2003/2014), and Richards & Frankland (2017) do not change month to month — so refreshing this file is *not* re-deriving the mapping from scratch. Per field: (a) confirm the mapping and verdict still hold, and (b) hunt for *new* research since a field's `reviewed` date that would strengthen, weaken, or add a mechanism.

**Adversarial by mandate.** Each field's verdict is a hypothesis to attack, not a label to defend. A broken metaphor is a finding, not an embarrassment. The disconfirmation anchor is §4.

**Overall verdict (2026-07-15): 2 load-bearing, 3 decorative, 2 mixed.** The grounding is load-bearing for the *conceptual architecture* (the episodic/semantic split and the consolidation+pruning combination) and as a *generative source* of mechanism candidates — but decorative for *implementation details* (`working/`, rituals, the re-derivability criterion). The honest framing: a useful design heuristic, not a deep structural parallel. Alternative frameworks (ADR practice, document management, knowledge graphs) produce similar designs for most mechanisms.

---

## 1. Mechanism mapping

The pattern's mechanisms mapped to their biological analogs, with the load-bearing verdict and the key divergence. This is the "what the pattern borrows" view; §3 is the "which field it borrows from" view.

| Pattern mechanism | Biological analog | Verdict | Key divergence |
|---|---|---|---|
| `MBT_LOG` (append-only) | Episodic memory | Mixed | LOG is immutable; real episodes are reconstructive and labile via reconsolidation |
| Canonical docs (SCOPE, APPROACH, FINDINGS) | Semantic / declarative memory | **Load-bearing** | Biology: gradual automatic extraction; pattern: deliberate editorial rewriting |
| `working/` directory | Working memory | Decorative | A staging area by any name; biology's capacity limits and attention mechanisms are absent |
| Dream cycle | Sleep-dependent consolidation + synaptic pruning | **Load-bearing** | Uniquely predicts the consolidation+pruning combination in a periodic offline pass |
| Work rituals (setup / closeout) | Procedural memory | Decorative | Rituals are explicit and declarative — the opposite of implicit procedural memory |
| "Store only what can't be re-derived" | Memory selectivity / encoding specificity | Decorative | Biology selects by salience / emotion / attention, not by re-derivability |
| "Shrink toward irreducible core" | Synaptic pruning / forgetting curves | Mixed | Motivational (justifies the stance via Richards & Frankland 2017), not mechanical |

---

## 2. Candidate-mechanism status

At-a-glance status of mechanisms present in cognitive science but absent from or underdeveloped in the pattern. Each is detailed under its field in §3; each is a *proposal* for the user, never auto-folded into the pattern.

| Mechanism | Field (§3) | Application | Status |
|---|---|---|---|
| **Salience / surprise-gated capture** | §3.5 | Tag LOG entries "surprising" at capture; dream preferentially promotes them | On roadmap, not operationalized |
| **Replay as creative recombination** | §3.6 | Dream cross-references findings *across* work items, not just promotes individual entries | Linear replay exists; recombinative missing |
| **Spaced retrieval / testing effect** | §3.7 | Verify claims at increasing intervals; "try to re-derive" test — if re-derivable from code, shed it | Maps to freshness ledger; "try to re-derive" is new |
| **Metacognitive confidence calibration** | §3.8 | Discount ease-of-verification as a confidence signal; the adversarial stance *is* calibration | Partially adopted (confidence scores) |

Lower-priority candidates tracked in §3.9.

---

## 3. Target fields

One subsection per organizing principle. Each carries: the key research (with `reviewed` date), the pattern's relationship to it, the verdict where one applies, and the new research a currency pass should hunt for.

### 3.1 Systems consolidation (complementary learning systems)

- **Key research:** CLS — McClelland, McNaughton & O'Reilly (1995). *reviewed 2026-07-15.*
- **Maps to:** `MBT_LOG` (fast hippocampal episodic store) → canonical docs (slow neocortical semantic store), with the dream cycle as the offline transfer. Underwrites the episodic/semantic split.
- **Verdict:** **Load-bearing** (for canonical docs as semantic memory). Divergence: biology extracts gradually and automatically; the pattern rewrites deliberately and editorially.
- **Watch for:** updated CLS / hippocampal-neocortical interaction models; challenges to the two-store account.

### 3.2 Sleep-dependent consolidation & synaptic homeostasis

- **Key research:** SHY (synaptic homeostasis hypothesis) — Tononi & Cirelli (2003, 2014). *reviewed 2026-07-15.*
- **Maps to:** the dream cycle as periodic offline consolidation **combined with** synaptic downscaling / pruning.
- **Verdict:** **Load-bearing** — this analogy uniquely predicts the *consolidation + pruning together in one offline pass* that distinguishes the dream cycle from every monotonic accumulation pattern.
- **Watch for:** SWS-vs-REM division-of-labor findings; mechanistic work on sleep-dependent pruning; anything that separates consolidation from pruning (would weaken the "combination" claim).

### 3.3 Adaptive forgetting

- **Key research:** Richards & Frankland (2017), "The Persistence and Transience of Memory." *reviewed 2026-07-15.*
- **Maps to:** "shrink toward irreducible core" — forgetting as a feature that improves generalization, not a failure.
- **Verdict:** **Mixed** — motivational, not mechanical: it *justifies* the shrink stance but the pattern does not implement a forgetting mechanism the way decay models do.
- **Watch for:** active-forgetting mechanisms; benefits-of-forgetting results tying transience to better decision-making.

### 3.4 Episodic vs. semantic memory (declarative taxonomy)

- **Key research:** Tulving (1972), episodic/semantic distinction; declarative memory literature. On the CS side, LangMem names the episodic/semantic/procedural taxonomy explicitly. *reviewed 2026-07-15.*
- **Maps to:** the LOG-vs-canonical-docs architecture; the vocabulary for NOTES vs. findings vs. instructions.
- **Verdict:** **Load-bearing** as conceptual architecture (this is the same split §3.1 delivers, viewed as a taxonomy rather than a transfer mechanism).
- **Watch for:** challenges to the episodic/semantic boundary; procedural-memory framing for the work rituals.

### 3.5 Salience & surprise-gated encoding

- **Key research:** prediction error enhances hippocampal encoding (Schultz et al. 1997; Axmacher et al. 2010); emotional arousal enhances consolidation (McGaugh 2004). *reviewed 2026-07-15.*
- **Maps to:** **candidate** — surprise-gated capture: tag prediction-error moments in the LOG at capture time; the dream preferentially promotes tagged entries.
- **Status:** on the roadmap, not operationalized.
- **Watch for:** dopamine / prediction-error encoding results; work operationalizing "surprise" as a capture trigger in agent memory.

### 3.6 Memory replay & recombination

- **Key research:** hippocampal replay generates novel sequences (Gupta et al. 2010); preplay represents future paths (Pfeiffer & Foster 2013). *reviewed 2026-07-15.*
- **Maps to:** **candidate** — the dream cycle's cross-reference step should look for *connections between findings across work items*, i.e. recombinative replay, not only linear promotion of individual entries.
- **Status:** linear replay exists in the dream cycle; recombinative replay is missing.
- **Watch for:** offline-recombination / preplay results; any agent-memory system doing cross-episode synthesis.

### 3.7 Spacing & testing effects

- **Key research:** spacing effect (Cepeda et al. 2006 meta-analysis); testing effect (Roediger & Karpicke 2006) — retrieving beats re-studying. *reviewed 2026-07-15.*
- **Maps to:** **candidate** — verify claims at increasing intervals (the freshness ledger); and the **"try to re-derive" test**: if a finding can be re-derived from current code, shed it.
- **Status:** the spacing side maps to the freshness ledger (now partly realized via the `verified` / `reviewed` dates in these registries); the "try to re-derive" retrieval test is new.
- **Watch for:** spaced-retrieval results applicable to agents; retrieval-based forgetting.

### 3.8 Metacognition & confidence calibration

- **Key research:** fluent/vivid memories are systematically overconfident (Talarico & Rubin 2003); delayed judgments are more accurate (Nelson & Dunlosky 1991). *reviewed 2026-07-15.*
- **Maps to:** the dream cycle's confidence discipline — discount ease-of-verification as a confidence signal; the adversarial stance *is* confidence calibration.
- **Status:** partially adopted (the cycle's 1–100 confidence scores and disconfirmation gate).
- **Watch for:** metamemory calibration results; work on overconfidence in LLM self-assessment.

### 3.9 Lower-priority fields

Tracked but not load-bearing and not currently generating high-value candidates:
- **Reconsolidation** — memories become labile on retrieval; handled by the pattern's existing update mechanisms. *reviewed 2026-07-15.*
- **Interference** (proactive / retroactive) — mitigated by the orthogonal-docs design (SCOPE vs. APPROACH). *reviewed 2026-07-15.*
- **Context-dependent retrieval** (encoding specificity) — relevant to cross-brain composition. *reviewed 2026-07-15.*
- **Schema theory** — reinforces surprise-gated capture (schema-incongruent items are better remembered). *reviewed 2026-07-15.*
- **Working memory** (Baddeley & Hitch 1974) — maps to `working/`; **decorative** (capacity limits and attention mechanisms are absent). *reviewed 2026-07-15.*

---

## 4. Disconfirmation & critiques

The evidence that the biological framing is (partly) flattering, kept here so the adversarial stance is auditable and the biological-grounding pass can attack from a fresh angle each run.

- **The field's most successful systems ignore biology at the implementation level.** Letta, Mem0, Zep, and MemOS use computer-architecture, vector-store, and graph-database metaphors, not biological ones — and lead on adoption. If biology were load-bearing for *implementation*, we'd expect the winners to use it. (2026-07-15.)
- **Medium mismatch.** Biological memory is reconstructive and distributed; the pattern is verbatim and discrete-file. This limits how far the analogy can be pushed and is why the implementation-level mappings are decorative.
- **Published critiques of biological metaphor in CS:** McDermott (1976), Zador (2019), Huber (2022) — biological labels can inflate claims without adding explanatory value.
- **Open disconfirmation question:** would the consolidation+pruning combination (§3.2) have been arrived at *without* the biological model? Plausible (ADR practice + document hygiene might reach it), but unproven — this is the main unknown capping the "load-bearing" verdict's confidence.

---

## 5. Sources

Biological grounding (author-year; classic neuroscience/psychology, content stable): CLS (McClelland, McNaughton & O'Reilly 1995); adaptive forgetting (Richards & Frankland 2017); SHY (Tononi & Cirelli 2003/2014); episodic/semantic (Tulving 1972); prediction-error encoding (Schultz et al. 1997; Axmacher et al. 2010); emotional consolidation (McGaugh 2004); replay/preplay (Gupta et al. 2010; Pfeiffer & Foster 2013); spacing (Cepeda et al. 2006); testing effect (Roediger & Karpicke 2006); metamemory (Talarico & Rubin 2003; Nelson & Dunlosky 1991); working memory (Baddeley & Hitch 1974). Critiques: McDermott (1976), Zador (2019), Huber (2022).