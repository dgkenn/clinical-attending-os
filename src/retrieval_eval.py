from __future__ import annotations

from dataclasses import dataclass

from .retrieval import hybrid_search


@dataclass(frozen=True)
class EvalCase:
    query: str
    expected_topic: str
    expected_terms: tuple[str, ...]
    max_rank: int = 3


EVAL_CASES = [
    EvalCase("shunt physiology", "Respiratory physiology", ("shunt", "hypoxemia")),
    EvalCase("MAC increases and decreases", "Inhaled anesthetics", ("mac",)),
    EvalCase("succinylcholine contraindications", "Neuromuscular blockers", ("succinylcholine", "contraindications")),
    EvalCase("LAST treatment", "LAST", ("local anesthetic", "lipid")),
    EvalCase("malignant hyperthermia management", "Malignant hyperthermia", ("malignant hyperthermia", "dantrolene")),
    EvalCase("high spinal treatment", "High spinal", ("high spinal",)),
    EvalCase("bronchospasm after induction", "Bronchospasm", ("bronchospasm",)),
    EvalCase("difficult airway algorithm", "Difficult airway", ("difficult airway",)),
]


def score_case(case: EvalCase) -> dict:
    results, insufficient = hybrid_search(case.query, max_results=5)
    hit_rank = None
    for idx, result in enumerate(results, start=1):
        text = result.text.lower()
        tags = {tag.lower() for tag in result.topic_tags}
        topic_hit = case.expected_topic.lower() in tags
        term_hit = any(term.lower() in text for term in case.expected_terms)
        if topic_hit or term_hit:
            hit_rank = idx
            break
    return {
        "query": case.query,
        "hit": hit_rank is not None and hit_rank <= case.max_rank,
        "hit_rank": hit_rank,
        "insufficient_context": insufficient,
        "top_source": None if not results else f"{results[0].book} p. {results[0].page}",
    }


def run_eval() -> list[dict]:
    return [score_case(case) for case in EVAL_CASES]


def main() -> None:
    rows = run_eval()
    hits = sum(1 for row in rows if row["hit"])
    print(f"retrieval_eval: {hits}/{len(rows)} top-3 hits")
    for row in rows:
        status = "PASS" if row["hit"] else "FAIL"
        print(f"{status} | rank={row['hit_rank']} | {row['query']} | top={row['top_source']} | insufficient={row['insufficient_context']}")


if __name__ == "__main__":
    main()
