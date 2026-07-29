# Mini-Brain Toolkit: Cognitive-Science Grounding Registry

> V5, 2026-07-28.

This file grounds the mini-brain pattern's biological metaphors for memory and cognition in the actual science — organized **by target field of cognitive science** — and interrogates whether each grounding is load-bearing or merely flattering. The conclusions this grounding supports live in `MBT_RESEARCH.md`.

---

## 1. Mechanism mapping

The pattern's mechanisms mapped to their biological analogs, with each mapping's verdict and key divergence; §2 tracks the research behind each field.

| Pattern mechanism | Biological analog | Verdict | Key divergence |
|---|---|---|---|
| LOG (append-only) | Episodic memory | Mixed | LOG is immutable; real episodes are reconstructive and labile via reconsolidation |
| Canonical docs (SCOPE, APPROACH, FINDINGS) | Semantic / declarative memory | **Load-bearing** (neural basis now contested) | Biology: gradual automatic extraction; pattern: deliberate editorial rewriting. 2026: Tibon et al. found no neural episodic/semantic dissociation — the functional record→distillate mapping holds; "separate brain systems" no longer does |
| `working/` directory | Working memory | Decorative | A staging area by any name; biology's capacity limits and attention mechanisms are absent |
| Dream cycle | Sleep-dependent consolidation + synaptic pruning | **Load-bearing** | Predicts the consolidation+pruning combination in an offline pass. 2026 caveat: SWS/REM specialization and Fountas et al. argue the pass is staged/iterative, not single — the pairing holds, the "single pass" detail weakens |
| Work rituals (setup / closeout) | Procedural memory | Decorative | Rituals are explicit and declarative — the opposite of implicit procedural memory |
| "Store only what can't be re-derived" | Memory selectivity / encoding specificity | Decorative | Biology selects by salience / emotion / attention, not by re-derivability |
| "Shrink toward irreducible core" | Synaptic pruning / forgetting curves | Mixed | Motivational (justifies the stance via Richards & Frankland 2017), not mechanical |

---

## 2. Target fields

One subsection per field. Each carries: the key research (with `reviewed` date), the pattern's relationship to it, a candidate mechanism's status where one exists, and the new research the next follow-on pass should hunt for.

### 2.1 Systems consolidation (complementary learning systems)

- **Key research:** CLS — McClelland, McNaughton & O'Reilly (1995); Singh & Schapiro (2026, *Phil. Trans. R. Soc. B*) propose C-HORSE, a division of labor *within* the hippocampus (pattern-separation vs. structure-learning subfields). *reviewed 2026-07-28.*
- **Maps to:** the LOG (fast hippocampal episodic store) → canonical docs (slow neocortical semantic store), with the dream cycle as the offline transfer. Underwrites the episodic/semantic split.
- **Watch for:** updated CLS / hippocampal-neocortical interaction models; challenges to the two-store account. (C-HORSE extends it, does not overturn it.)

### 2.2 Sleep-dependent consolidation & synaptic homeostasis

- **Key research:** SHY (synaptic homeostasis hypothesis) — Tononi & Cirelli (2003, 2014). 2026: Iatropoulos et al. (PNAS) treat pruning + homeostatic scaling as one unified optimization (*supports* the combination); Fountas et al. (arXiv 2603.04688) unify consolidation+forgetting but argue it needs *iterative multi-step* refinement, not one offline pass; SWS-vs-REM division-of-labor findings show real stage specialization; Xie (arXiv 2603.14517) builds sleep-inspired consolidate+forget in one ML mechanism. *reviewed 2026-07-28.*
- **Maps to:** the dream cycle as periodic offline consolidation **combined with** synaptic downscaling / pruning.
- **Candidate mechanism:** a **two-phase dream cycle** — a consolidation/distill phase, then a distinct prune/extract phase — mirroring SWS/REM specialization and Anthropic's own "Dreaming," which splits its pass in two. *Status: candidate (flagged).*
- **Watch for:** SWS-vs-REM division-of-labor findings; mechanistic work on sleep-dependent pruning; anything that separates consolidation from pruning (would weaken the "combination" claim).

### 2.3 Adaptive forgetting

- **Key research:** Richards & Frankland (2017), "The Persistence and Transience of Memory." 2026: Fountas et al. frame "predictive forgetting for optimal generalisation" — keep what predicts future outcomes, discard the rest. *reviewed 2026-07-28.*
- **Maps to:** "shrink toward irreducible core" — forgetting as a feature that improves generalization, not a failure.
- **Candidate mechanism:** adopt *predictive forgetting* as a sharper formal statement of "store only what can't be re-derived" — shed what current knowledge already predicts. *Status: candidate (flagged).*
- **Watch for:** active-forgetting mechanisms; benefits-of-forgetting results tying transience to better decision-making.

### 2.4 Episodic vs. semantic memory (declarative taxonomy)

- **Key research:** Tulving (1972), episodic/semantic distinction; declarative memory literature; LangMem names the taxonomy on the CS side. **2026 challenge:** Tibon, Greve, Humphreys et al. (*Nature Human Behaviour*, Registered Report) found *no significant neural difference* between episodic and semantic retrieval — a surprising null against decades of dissociation work; corroborated by a 2026 "shared brain state" preprint and by GENESIS (episodic/semantic as two *interacting* generative systems). *reviewed 2026-07-28.*
- **Maps to:** the LOG-vs-canonical-docs architecture — the same split §2.1 delivers, viewed as a taxonomy rather than a transfer mechanism; the vocabulary for NOTES vs. findings vs. instructions. The *functional* split (raw record vs. curated distillate) survives the 2026 null; the claim that these map onto *separate brain systems* does not.
- **Watch for:** challenges to the episodic/semantic boundary; procedural-memory framing for the work rituals.

### 2.5 Salience & surprise-gated encoding

- **Key research:** prediction error enhances hippocampal encoding (Schultz et al. 1997; Axmacher et al. 2010); emotional arousal enhances consolidation (McGaugh 2004). **2026 cluster operationalizing prediction-error as the memory-write gate:** D-MEM (2603.14597), AURA (2606.02775), "Worth Remembering" (2606.03787), "Surprise as a Signal" (2606.31495), Nemori / "What Deserves Memory" (2508.03341, ACL 2026) — rule: if existing knowledge already predicts an event, don't store it; only the prediction-error residual is distilled. *reviewed 2026-07-28.*
- **Maps to:** **candidate** — surprise-gated capture: tag prediction-error moments in the LOG at capture time; the dream preferentially promotes tagged entries.
- **Status:** on the roadmap, not operationalized — but now with strong external validation, and the strongest candidate to graduate.
- **Watch for:** dopamine / prediction-error encoding results; work operationalizing "surprise" as a capture trigger in agent memory.

### 2.6 Memory replay & recombination

- **Key research:** hippocampal replay generates novel sequences (Gupta et al. 2010); preplay represents future paths (Pfeiffer & Foster 2013). 2026: Anthropic's shipped "Dreaming" performs cross-session recombination; GENESIS computationally models episodic recombination. *reviewed 2026-07-28.*
- **Maps to:** **candidate** — the dream cycle's cross-reference step should look for *connections between findings across work items*, i.e. recombinative replay, not only linear promotion of individual entries.
- **Status:** linear replay exists in the dream cycle; recombinative replay is missing.
- **Watch for:** offline-recombination / preplay results; any agent-memory system doing cross-episode synthesis.

### 2.7 Spacing & testing effects

- **Key research:** spacing effect (Cepeda et al. 2006 meta-analysis); testing effect (Roediger & Karpicke 2006) — retrieving beats re-studying. *reviewed 2026-07-15.*
- **Maps to:** **candidate** — verify claims at increasing intervals (the freshness ledger); and the **"try to re-derive" test**: if a finding can be re-derived from current code, shed it.
- **Status:** the spacing side maps to the freshness ledger (now partly realized via the `verified` / `reviewed` dates in these registries); the "try to re-derive" retrieval test is new.
- **Watch for:** spaced-retrieval results applicable to agents; retrieval-based forgetting.

### 2.8 Metacognition & confidence calibration

- **Key research:** fluent/vivid memories are systematically overconfident (Talarico & Rubin 2003); delayed judgments are more accurate (Nelson & Dunlosky 1991). **2026 risk signal:** LLMs show persistent, poorly-generalizing overconfidence — "No Signs of Individuated Metacognition" (2605.24299), MIRROR (2604.19809), validity-scaling (2604.17707) — directly relevant, since the dream cycle relies on the model self-judging "load-bearing vs. prunable." *reviewed 2026-07-28.*
- **Maps to:** the dream cycle's confidence discipline — discount ease-of-verification as a confidence signal; the adversarial stance *is* confidence calibration.
- **Status:** partially adopted (the cycle's 1–100 confidence scores and disconfirmation gate).
- **Watch for:** metamemory calibration results; work on overconfidence in LLM self-assessment.

### 2.9 Lower-priority fields

Tracked but not load-bearing and not currently generating high-value candidates:
- **Reconsolidation** — memories become labile on retrieval; handled by the pattern's existing update mechanisms. *reviewed 2026-07-15.*
- **Interference** (proactive / retroactive) — mitigated by the orthogonal-docs design (SCOPE vs. APPROACH). *reviewed 2026-07-15.*
- **Context-dependent retrieval** (encoding specificity) — relevant to cross-brain composition. *reviewed 2026-07-15.*
- **Schema theory** — reinforces surprise-gated capture (schema-incongruent items are better remembered). *reviewed 2026-07-15.*
- **Working memory** (Baddeley & Hitch 1974) — maps to `working/`. *reviewed 2026-07-15.*

---

## 3. Disconfirmation & critiques

The evidence that the biological framing is (partly) flattering, kept here so the adversarial stance is auditable and the biological-grounding pass can attack from a fresh angle each run.

- **The field's most successful systems ignore biology at the implementation level.** Letta, Mem0, Zep, and MemOS use computer-architecture, vector-store, and graph-database metaphors, not biological ones — and lead on adoption. If biology were load-bearing for *implementation*, we'd expect the winners to use it. (2026-07-15.)
- **Medium mismatch.** Biological memory is reconstructive and distributed; the pattern is verbatim and discrete-file. This limits how far the analogy can be pushed and is why the implementation-level mappings are decorative.
- **Published critiques of biological metaphor in CS:** McDermott (1976), Zador (2019), Huber (2022) — biological labels can inflate claims without adding explanatory value.
- **2026 — the episodic/semantic neural dissociation is contested.** Tibon et al. (*Nature Human Behaviour*) found no neural difference between episodic and semantic retrieval, weakening the *neural* basis (not the functional mapping) of the load-bearing "canonical docs ↔ semantic memory" verdict (§2.4). (2026-07-28.)
- **2026 — the "single offline pass" is contested.** SWS/REM stage-specialization and Fountas et al.'s iterative-refinement requirement argue real consolidation is staged/iterative; this weakens the "single pass" detail of the dream-cycle verdict, though the consolidation+pruning *pairing* holds (§2.2). (2026-07-28.)
- **Open disconfirmation question:** would the consolidation+pruning combination (§2.2) have been arrived at *without* the biological model? 2026 evidence leans *yes, independently discoverable*: Anthropic's "Dreaming" looks like a team reaching essentially this design from engineering pressure (context hygiene, task performance) and reaching for the hippocampal metaphor retrospectively — suggestive, not conclusive (inference from public framing). It further caps the "load-bearing" verdict's confidence.
