from __future__ import annotations

from dataclasses import dataclass

from .retrieval import hybrid_search, retrieval_confidence


@dataclass(frozen=True)
class GoldenQuery:
    query: str
    mode: str
    expected_families: tuple[str, ...]


GOLDEN_QUERIES = [
    GoldenQuery("hyperkalemia treatment", "intern_teach", ("intern_year_medicine", "MGH Housestaff Manual", "Intern Notes / Survival Guide")),
    GoldenQuery("ARDS ventilator strategy", "ICU_teach", ("ICU_critical_care", "Marino ICU Book")),
    GoldenQuery("shunt physiology", "anesthesia_boards", ("anesthesiology_boards", "Morgan & Mikhail", "Miller/Baby Miller", "Stanford CA-1")),
    GoldenQuery("LAST treatment", "crisis", ("anesthesiology_boards", "Stanford CA-1", "Morgan & Mikhail", "Miller/Baby Miller")),
]


BENCHMARK_QUERIES = [
    GoldenQuery("afib with RVR intern management", "intern_teach", ("intern_year_medicine",)),
    GoldenQuery("hyponatremia workup", "intern_teach", ("intern_year_medicine",)),
    GoldenQuery("hypoxemia on night float", "cross_cover", ("intern_year_medicine", "ICU_critical_care")),
    GoldenQuery("sepsis initial management", "intern_teach", ("intern_year_medicine", "ICU_critical_care")),
    GoldenQuery("GI bleed admission plan", "intern_teach", ("intern_year_medicine",)),
    GoldenQuery("AKI differential", "intern_teach", ("intern_year_medicine",)),
    GoldenQuery("altered mental status workup", "intern_teach", ("intern_year_medicine",)),
    GoldenQuery("shock differential", "ICU_teach", ("ICU_critical_care", "intern_year_medicine")),
    GoldenQuery("vasopressor choice septic shock", "ICU_teach", ("ICU_critical_care", "Marino ICU Book")),
    GoldenQuery("ventilator high pressure alarm", "ICU_teach", ("ICU_critical_care",)),
    GoldenQuery("sedation ICU delirium", "ICU_teach", ("ICU_critical_care",)),
    GoldenQuery("MAC increases decreases", "anesthesia_boards", ("anesthesiology_boards",)),
    GoldenQuery("succinylcholine contraindications", "drug", ("anesthesiology_boards",)),
    GoldenQuery("malignant hyperthermia management", "crisis", ("anesthesiology_boards",)),
    GoldenQuery("hypotension after induction", "anesthesia_boards", ("anesthesiology_boards",)),
    GoldenQuery("bronchospasm after intubation", "crisis", ("anesthesiology_boards",)),
]


def _matches_expected(result: dict, expected: tuple[str, ...]) -> bool:
    values = {
        result.get("library", ""),
        result.get("source", ""),
        result.get("source_name", ""),
        result.get("book", ""),
    }
    return any(expected_value in values for expected_value in expected)


def audit_case(case: GoldenQuery) -> dict:
    results, insufficient = hybrid_search(case.query, mode=case.mode, max_results=5)
    dumped = [r.model_dump() for r in results]
    top3_hit = any(_matches_expected(result, case.expected_families) for result in dumped[:3])
    return {
        "query": case.query,
        "mode": case.mode,
        "confidence": retrieval_confidence(results),
        "insufficient_context": insufficient,
        "expected_source_hit_top3": top3_hit,
        "top_sources": [f"{r.book} ({r.library}) p.{r.page} score={r.score}" for r in results[:5]],
    }


def run_audit() -> list[dict]:
    return [audit_case(case) for case in GOLDEN_QUERIES + BENCHMARK_QUERIES]


def main() -> None:
    rows = run_audit()
    failures = [row for row in rows if not row["expected_source_hit_top3"] or row["confidence"] == "low"]
    print(f"retrieval_audit: {len(rows) - len(failures)}/{len(rows)} acceptable")
    for row in rows:
        status = "PASS" if row["expected_source_hit_top3"] and row["confidence"] != "low" else "WARN"
        print(f"\n{status} | {row['query']} | mode={row['mode']} | confidence={row['confidence']} | insufficient={row['insufficient_context']}")
        for source in row["top_sources"]:
            print(f"  - {source}")


if __name__ == "__main__":
    main()
