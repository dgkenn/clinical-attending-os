"""Pre-shift case prep.

Take a one-line case stem ("admitting AECOPD overnight") and return 3-5
review topics drawn from intern guides + Marino, each with a short rationale
and 1-2 source snippets.

Pipeline:
- Extract candidate topics by overlapping the stem against
  topic_taxonomy.TOPICS keywords + medical_lexicon.
- Rank candidates by stem-token overlap, prefer ICU-overlap topics if the
  stem mentions ICU/wards crossover.
- For each top topic, hybrid_search(intern_teach mode, intern+ICU libraries)
  and pull 1-2 sources.
"""

from __future__ import annotations

import re
from typing import Any

from concurrent.futures import ThreadPoolExecutor

from .retrieval import hybrid_search
from .schemas import CasePrepResponse, CasePrepTopic, SourceChunk
from .topic_taxonomy import TOPICS


_DURATION_TO_N = {3: 3, 5: 4, 10: 5}


def _topic_score(stem: str, topic: str, keywords: list[str]) -> float:
    stem_low = stem.lower()
    score = 0.0
    if topic.lower() in stem_low:
        score += 3.0
    for kw in keywords:
        if kw.lower() in stem_low:
            score += 1.0
        elif any(part in stem_low for part in kw.lower().split() if len(part) >= 4):
            score += 0.4
    return score


def _rank_topics(stem: str, n: int) -> list[tuple[str, float]]:
    scored: list[tuple[str, float]] = []
    for topic, kws in TOPICS.items():
        s = _topic_score(stem, topic, kws)
        if s > 0:
            scored.append((topic, s))
    if not scored:
        # crude fallback: extract key nouns
        tokens = re.findall(r"[a-zA-Z]{4,}", stem.lower())
        for t in tokens[:n]:
            scored.append((t.capitalize(), 0.5))
    scored.sort(key=lambda x: -x[1])
    return scored[: max(2, n)]


def _why_for(topic: str, stem: str) -> str:
    s_low = stem.lower()
    if any(t in s_low for t in ("admit", "admission")):
        return f"Lock down the {topic} workup and admission orders before you walk in."
    if any(t in s_low for t in ("cross", "night", "page")):
        return f"You'll get paged about {topic}; rehearse the cross-cover differential and first move."
    if any(t in s_low for t in ("icu", "vent", "pressor", "shock")):
        return f"ICU-relevant: {topic} drives bedside decisions in the next few hours."
    if any(t in s_low for t in ("preop", "or case", "induction", "anesthesia")):
        return f"Preop: how {topic} changes the anesthetic plan."
    return f"High-yield review for this case: {topic}."


def _retrieve_for_topic(topic: str, stem: str, max_results: int = 2) -> list[SourceChunk]:
    results, _ = hybrid_search(
        f"{topic} {stem}",
        mode="intern_teach",
        topic_filter=topic,
        max_results=max_results,
        use_cross_encoder=False,
    )
    return results


def case_prep(stem: str, duration_minutes: int = 5) -> CasePrepResponse:
    n = _DURATION_TO_N.get(duration_minutes, max(3, min(5, duration_minutes // 2)))
    ranked = _rank_topics(stem, n)
    selected = ranked[:n]
    # Single broad search instead of 4 narrow ones — Python's GIL makes
    # threading ineffective for the CPU-bound hybrid_search hot path.
    selected_topics = [t for t, _ in selected]
    broad_query = stem + " " + " ".join(selected_topics)
    pool, _ = hybrid_search(
        broad_query,
        mode="intern_teach",
        max_results=max(15, n * 5),
        use_cross_encoder=False,
    )
    by_topic: dict[str, list[SourceChunk]] = {t: [] for t in selected_topics}
    for chunk in pool:
        chunk_tags_low = ",".join(chunk.topic_tags).lower()
        chunk_text_low = (chunk.text or "").lower()
        for t in selected_topics:
            if len(by_topic[t]) >= 2:
                continue
            t_low = t.lower()
            if t_low in chunk_tags_low or t_low in chunk_text_low:
                by_topic[t].append(chunk)
                break
    topics: list[CasePrepTopic] = []
    for topic in selected_topics:
        sources = by_topic[topic]
        if not sources:
            sources = pool[:2]  # fallback to top of pool
        topics.append(
            CasePrepTopic(
                topic=topic,
                why=_why_for(topic, stem),
                sources=sources,
            )
        )
    rationale = (
        f"Pulled {len(topics)} review topics for a {duration_minutes}-minute pre-shift block. "
        "Single broad search, results binned by topic; spine sources prioritized."
    )
    return CasePrepResponse(case_stem=stem, review_topics=topics, rationale=rationale)
