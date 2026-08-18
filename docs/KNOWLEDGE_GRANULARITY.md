# Knowing exactly what he knows

**Status:** design + implementation log. Opened 2026-08-18.

## The requirement, in the maintainer's words

> Achieving granularity on what exactly I know and what exactly I don't know is
> really important to the project. Not quizzing me on things that I already
> know cuts down on review time, and only quizzing me on things that I don't
> know is how I learn and keep reviews effective. If I don't feel like I'm
> getting good value out of the system, then I'm gonna abandon it.

That last sentence is the design constraint. This is not an accuracy problem to
be optimised asymptotically — it is a product that gets deleted if a session
feels like a waste of time. Two failures cost trust, and they are opposites:

- **Wasted question** — asking something he demonstrably knows. Feels like
  busywork, inflates review time, and is the failure he will notice first.
- **Missed gap** — never asking something he does not know. Invisible to him,
  the more dangerous of the two clinically, and the reason the system exists.

Everything below is in service of shrinking both at once. Any change that
trades one for the other straight across is not progress.

---

## What is actually broken (measured, 2026-08-18 session)

The session transcript was compared line by line against the database. Four
distinct mechanisms were destroying granularity, and they push in *both*
directions.

### 1. Partial answers credit nothing — the wasted-question engine

Grading happens per ANSWER, but knowledge lives per FACT. One question routinely
tests three or four facts, and a `partial` verdict collapses them into a single
outcome. In practice only the *corrected* material got carded:

| The tutor said | What the backend recorded |
|---|---|
| "Your transfusion threshold knowledge is solid" | nothing |
| "Dose range is right" | nothing |
| "Epinephrine as next step confirmed correct" | nothing |
| "Prerenal nailed" | credited (1 of 7 partials) |
| "Holding metformin, correct" | credited |

**5 of 7 partial answers wrote only failure facts.** Demonstrated knowledge
evaporated. Because it was never recorded as known, it stays in the queue and
comes back — this is precisely the "quizzing me on things I already know" the
maintainer is objecting to, and it is structural, not incidental.

### 2. Parroting counted as knowledge — the missed-gap engine

The ARDS teach-back, verbatim:

> **Tutor (20:05:01):** "...6 mL per kg of ideal body weight, not actual weight,
> **since lung size tracks height**."
> **User (20:05:48):** "You just told me since because **lung size tracks
> height**, not fat."

Graded `correct`. The fact advanced to 3-of-5 with a three-day interval. He
even flagged it himself — *"you just told me"* — and the grader took the
restatement at face value. The tutor did record `teach_back_quality = 0.5`,
which was the right instinct, but **that field has no effect on the FSRS
rating**, so it changed nothing.

Worse: the cleaned `user_answer` was rewritten as *"Because lung size tracks
height, not fat"* — deleting the four words that revealed it was regurgitation.
Only the verbatim field preserved the evidence. This is the argument for
verbatim capture in one example.

### 3. Facts written before they were taught

A BiPAP mechanism card was created at 15:53, one minute **before** the BiPAP
question was asked at 15:54. Same pattern for post-obstructive diuresis. The
tutor is batch-writing topic content rather than recording what was
demonstrated, which manufactures cards nobody has been tested on and then
schedules them as if they had been failed.

### 4. Ingestion is indistinguishable from failure

Bulk fact extraction wrote 253 facts as `times_seen=1, times_correct=0,
status='weak'` — byte-identical to "asked and got it wrong". Coverage read
6.6% when the honest figure was 2.4%, every accuracy number was dragged toward
zero by questions never asked, and all of it was queued for the next morning in
the highest-priority bucket.

**Common root cause across all four: the system records a VERDICT but not the
EVIDENCE for the verdict.** Nothing stored answers "how do you know he knows
this?", so nothing can be audited, and wrong states persist invisibly.

---

## The design principle

> A fact's state must be derived from evidence, and the evidence must be stored
> next to it.

Concretely: never write "he knows this" without also writing *the words he said
that prove it*. This single rule fixes the audit problem, the parroting
problem, and the partial-credit problem simultaneously, because a grader forced
to quote evidence per fact cannot collapse four facts into one impression.

---

## Proposals

Ordered by (value to the two failure modes) ÷ (cost + risk). Status noted.

### P1 — Per-fact verdicts carrying evidence · **IMPLEMENTING**

`knowledge_points` entries gain `evidence`: the span of the user's own answer
that demonstrates the fact.

```
{"point": "...", "correct": true,  "evidence": "transfusion threshold hemoglobin of 7"}
{"point": "...", "correct": false, "evidence": ""}
```

Rules: no evidence ⇒ cannot be marked correct. Evidence must appear in
`user_answer_verbatim` (checked server-side by token overlap, not exact match,
so paraphrase survives but invention does not).

This is the single highest-value change. It directly ends the wasted-question
engine, and it makes every future audit answerable.

### P2 — A provenance taxonomy for how a fact was touched · **IMPLEMENTING**

`correct: true|false` cannot express what actually happens in a tutoring turn.
Replace with an explicit outcome:

| outcome | meaning | scheduling consequence |
|---|---|---|
| `demonstrated` | produced unprompted, in his own words | full credit, normal interval |
| `partial` | substance present, component missing | FSRS Hard, shortened |
| `corrected` | got it wrong, was taught | lapse, short interval |
| `parroted` | restated right after being told | **no credit**, re-test next day |
| `exposed` | tutor said it, he never responded | not knowledge; `log_tangent`'s model |
| `untested` | ingested, never presented | new-material pool, not a review |

`parroted` and `untested` are the two states the system could not previously
express, and they are exactly the two that were corrupting the ledger.

### P3 — Mechanical parroting detection · **IMPLEMENTING**

Do not rely on the tutor to self-report — it already graded the ARDS answer
`correct` while recording `teach_back_quality=0.5`. Detect it server-side:
compare the answer against the immediately preceding `tutor_response` in the
same session. High content-word overlap plus a short gap ⇒ downgrade to
`parroted` regardless of the declared verdict.

Deterministic, needs no model call, and catches the exact case observed. Also
wire `teach_back_quality` into the rating so a low score actually costs
something.

### P4 — The confident-wrong queue · **PROPOSED**

Confidence × correctness is the highest-value signal already being collected
and it is not being used to prioritise:

|  | correct | wrong |
|---|---|---|
| **confident** | known — push interval out hard | **dangerous misconception — top priority** |
| **unsure** | fragile — shorten interval | ordinary gap — teach |

Confident-and-wrong is the clinically dangerous quadrant: he will act on it.
`_confident_wrong` exists in the code but only nudges an interval; it should be
its own surfaced queue. Conversely **confident-and-right deserves aggressive
interval extension** — the cheapest available cut to review time.

### P5 — User override: `mark_known` / `mark_unknown` · **IMPLEMENTING**

The ledger needs a correction path the user controls. Precedent: he declined
the "consults" card *out loud during a session* — reasoning that it was a
checklist, not clinical knowledge — and that judgement reached the backend
nowhere, because conversational prose never becomes state unless a tool carries
it. Same class of loss as the parroting case.

Also serves the trust requirement directly: when the system asks something he
knows, he needs a one-sentence way to say so that permanently stops it.

### P6 — Discrimination testing between confusable facts · **PROPOSED**

The catalog already carries `confusable_with`. Knowing a fact in isolation is
not the same as being able to tell it from its neighbour, and confusion is what
actually fails on the wards — FeNa vs FeUrea, the ARDS severity bands, DKA
potassium thresholds. A discrimination question tests the boundary and is worth
more per minute than either fact alone. Also a review-time *saving*: one
boundary question retires two cards.

### P7 — Latency as a fluency signal · **PROPOSED**

A correct answer that took 40 seconds is not the same as one that took 5. For
ward and OR use, retrieval speed *is* the competence. Timestamps are already
stored per attempt; the gap between question delivery and answer is derivable
today with no new capture. Use it to modulate interval, not to grade.

### P8 — Prerequisite dampening, NOT inference · **PROPOSED, deliberately limited**

Tempting: explaining a mechanism correctly implies the facts that depend on it,
so credit them and skip the questions. Rejected as *credit* — it manufactures
knowledge that was never demonstrated, which is the exact sin P2 exists to stop.
Accepted as a *dampener*: deprioritise dependent facts so they surface later,
without ever marking them known. Suppressing a question is reversible; a false
`mastered` is not.

### P9 — Evidence-backed "why am I seeing this?" · **PROPOSED**

Every served card should be able to answer the question the maintainer will
inevitably ask. With P1 in place the answer is already stored: *"On 8/18 you
said 'FeNa under 1 percent' but missed the postrenal branch."* Cheap once P1
lands, and it converts the most trust-destroying moment — a repeat that feels
unearned — into a demonstration that the system is paying attention.

### P10 — Retire the topic layer's authority over fact scheduling · **PROPOSED**

Two schedulers exist (topic-level and fact-level) and the topic layer has
repeatedly produced phantom rows and resurrections. Facts are the unit the
maintainer actually cares about. The topic layer should become a *view* over
facts, not an independent scheduler. Larger change; flagged, not started.

---

## Explicitly rejected

- **Blanket similarity-based auto-merge of facts.** Already tried at the
  catalog level; it destroyed real distinctions (the FeNa-on-diuretics caveat
  vs the FeNa thresholds are different knowledge). Merging stays per-pair with
  clinical judgement.
- **Inferring mastery from topic-level accuracy.** That is how the phantom-row
  problem started.
- **Trusting a self-reported `teach_back_quality` alone.** Observed producing
  `correct` + `0.5` on the same parroted answer. Keep the field, but gate on
  mechanical detection.
- **Asking the user to grade himself per fact.** Correct in principle, but it
  is friction on every single answer and he is doing this between shifts.
  Evidence extraction has to be the tutor's job.

---

## How this gets measured

Granularity claims must not become another unaudited number. Per session:

- **Wasted-question rate** — served facts answered correctly with high
  confidence and no prior failure. Target: falling.
- **Evidence coverage** — share of `correct` verdicts carrying evidence that
  actually appears in the verbatim answer. Target: ~100%; anything lower means
  the grader is guessing.
- **Parrot rate** — share of corrects flagged `parroted` by detection. Expect
  non-zero and honest; zero means detection is broken, not that it never
  happens.
- **Ghost rate** — facts with `times_seen > 0` and no evidence of presentation.
  Target: zero, permanently.

`scripts/doctor.py` is the place for these.

---

## Log

- **2026-08-18** — Session transcript compared against DB; the four mechanisms
  above identified. ICU retrieval routing fixed the same day (`_attach_sources`
  hardcoded `mode="intern_teach"`, so `ICU_teach` — which ranks Marino first —
  never fired; Marino sat fifth of eight and ICU questions were built from
  ward-intern references while a 7,134-chunk ICU textbook went unused).
  Ghost-fact migration written and dry-run verified; awaiting maintainer
  approval to run.
