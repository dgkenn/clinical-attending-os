# Clinical Attending OS — Mastery Strategy

**North star:** master *all* of internal medicine + anesthesiology at maximum
granularity and breadth, in the least time, with maximum long-term retention,
building **functional** (bedside-usable, transferable) knowledge — using
evidence-based pedagogy. This is a multi-year program and the user's primary
learning method.

Synthesized 2026-06-21 from five parallel research/audit agents (spaced-repetition
science, encoding pedagogy, clinical-reasoning/mastery-learning, curriculum
decomposition, codebase audit). Sources cited in those briefs.

---

## The model: five layers

1. **Content — an atomic, grounded knowledge graph.** The learnable unit is the
   *conditionalized knowledge point*: "when X → do/expect Y because Z." All of IM +
   anesthesia is ~25k–43k such points (manageable active deck ~15–20k). Today's
   1,214-topic blueprint is a *skeleton*, not the content. Each point carries
   `source_chunk_ids` (anti-hallucination) and a `blueprint_code` (ABIM/ABA) for
   coverage verification. Edges: `PREREQUISITE_OF` (ordering), `CONFUSABLE_WITH`
   (contrastive cases), `MECHANISM_OF` (integration). Diagnoses get a 5-field
   **illness script** (enabling conditions · fault/pathophys · time course · key
   discriminating features · consequence-if-missed).

2. **Scheduling — per-item FSRS under a daily load budget.** Route knowledge points
   through the existing FSRS-4 engine (retire the fixed ladder). Target retention
   **90%** globally, **95%** for flagged critical items. Daily economics: cap new
   points at **~20/day**, review budget **~150–200/day**, ≥24 h before first
   retrieval, **interleave** the queue across systems, partial-stability reset on
   lapse. ~20 new/day × ~3 yr = full coverage without review collapse.

3. **Pedagogy — how each rep builds functional knowledge.** Retrieval-first,
   **free-recall default** (not multiple-choice) for mature points. **Force the
   "why"** (elaborative interrogation) after every correct answer. **Force error
   self-diagnosis + a one-line "failure postmortem"** after every miss. **Problem
   representation one-liner** before the answer is revealed. **Contrastive cases**
   for confusable pairs (tension PTX vs tamponade). **Far-transfer wrap** by the 3rd
   correct recall (novel presentation) — the test of functional vs inert knowledge.
   **Productive failure** (attempt before explanation) for hard mechanisms. **Dual
   coding** (generate a schematic) for cascades/circuits.

4. **Mastery gating — Bloom/Miller ladder.** Per point: introduced → recognized →
   recalled (2× free recall) → **applied** (correct in a vignette *with
   justification*) → **mastered** (correct across 2 contrastive cases + can generate
   the discriminating feature). Do not present analyze-level items before apply is
   met; gate a topic cluster at ≥85% of its points "applied+".

5. **Two cognition tracks.** IM ward cognition = deliberative System 2 (build
   differentials, justify). Anesthesia crisis = **recognition-primed**: drill
   if-then production rules, score on **latency**, run **rapid-cycle deliberate
   practice** (tight loop, not spaced days apart). Keep crisis algorithms on a weekly
   drill cycle; reserve SR for anesthesia pharmacology/physiology.

---

## Baseline (what already exists — build on it)

- **FSRS-4 at topic level** — fully implemented (`src/fsrs.py`), confidence-weighted.
- **knowledge_points** table + record/get/due tools — right grain; only the scheduler
  (fixed `_KP_LADDER`) needs replacing with FSRS.
- **Hybrid retrieval** over a 1.5 GB Chroma corpus (vector + keyword + rerank) — solid.
- **mastery_vector** (accuracy, transfer, mechanism, calibration) — right shape for gates.
- **curriculum** (1,214 topics) + MCP tool pattern + test suite — extensible.
- Unused but present: `topic_hierarchy` table (prereq edges) — wire it up, don't create it.

---

## Roadmap (prioritized by impact/effort)

### Phase 0 — Pedagogy contract (instructions only; live on re-paste, no deploy)
Cheapest, highest-impact. Encode in `CLAUDE_PROJECT_INSTRUCTIONS.md`: free-recall
default; mandatory "why" on correct; error self-diagnosis + postmortem on miss;
problem-representation one-liner before reveal; illness-script reconstruction;
contrastive cases; far-transfer wrap at 3rd recall; productive failure for hard
mechanisms; Bloom gating; metacognitive error-type naming; anesthesia crisis track.

### Phase 1 — Scheduling + load economics + gates (backend; one push)
- Route `knowledge_points` through `fsrs_review` (add `fsrs_state`); retire `_KP_LADDER`.
- Target retention 90% / 95% critical.
- Daily **new-item cap** + **review budget** + **interleave** in `get_next_topic`;
  surface counts in `get_session_state`.
- `bloom_level` on `question_attempts` + Bloom-rung mastery gate in `get_mastery_gates`.
- Fix `get_progress` domain metrics (real per-discipline, like `get_mastery_map`).
- New: `illness_scripts` + `confusable_pairs` tables + `get_contrastive_case` tool;
  populate `topic_hierarchy` prereqs.

### Phase 2 — The atomic knowledge graph (content; parallel, delegated, ~$25)
Generate ~15–25k grounded knowledge points from the corpus, coverage-checked against
ABIM + ABA blueprints. Pipeline (delegate to Haiku/Sonnet, parallel batches):
blueprint seeding → corpus-grounded KP extraction (attach `source_chunk_ids`) →
embed+dedup → edge annotation (PREREQUISITE_OF, CONFUSABLE_WITH) → coverage
verification (flag any blueprint domain <70% of expected). Spot-check 2% for grounding.

### Phase 3 — Graph-aware tutoring
Prereq gating + contrastive generation from edges in `get_next_topic`; coverage/gap
dashboard; periodic cross-system integration cases.

---

## Decisive recommendation
Do **Phase 0 now** (free, immediate). Build **Phase 1** as the next backend push
(scheduling correctness + gates are the foundation everything else assumes). Kick off
**Phase 2** in parallel as a delegated background build (it's mostly automated and
cheap, and it's the only thing that delivers true breadth+granularity). Phase 3 once
the graph exists.

Coverage metrics to track throughout: breadth (% blueprint leaf nodes with ≥1 point,
target 100%), depth (median points/topic ≥15 high-yield), grounding rate (% points
with ≥2 source chunks, >95%), daily review load vs retention.
