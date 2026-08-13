from __future__ import annotations

from .retrieval import hybrid_search, retrieval_confidence


STANDARD_QUERIES = [
    "afib with RVR intern management",
    "hyperkalemia treatment",
    "hyponatremia workup",
    "hypoxemia on night float",
    "sepsis initial management",
    "GI bleed admission plan",
    "AKI differential",
    "altered mental status workup",
    "shock differential",
    "vasopressor choice septic shock",
    "ARDS ventilator strategy",
    "ventilator high pressure alarm",
    "sedation ICU delirium",
    "shunt physiology",
    "MAC increases decreases",
    "succinylcholine contraindications",
    "LAST treatment",
    "malignant hyperthermia management",
    "hypotension after induction",
    "bronchospasm after intubation",
]


def main() -> None:
    print("Clinical Attending OS retrieval debugger. Blank query exits. Type :bench for standard queries.")
    while True:
        query = input("query> ").strip()
        if not query:
            break
        queries = STANDARD_QUERIES if query == ":bench" else [query]
        mode = input("mode [intern_teach]> ").strip() or "intern_teach"
        library_filter = input("library filter [optional]> ").strip() or None
        source_filter = input("source filter [optional]> ").strip() or None
        for q in queries:
            results, insufficient = hybrid_search(q, mode=mode, library_filter=library_filter, source_filter=source_filter, max_results=10)
            print(f"\nQUERY: {q}")
            print(f"retrieval_confidence={retrieval_confidence(results)} insufficient_context={insufficient}")
            for i, r in enumerate(results, start=1):
                print(f"\n#{i} final={r.score} vector={r.vector_score} bm25={r.bm25_score} reranker={r.reranker_score} method={r.retrieval_method}")
                print(f"{r.book} | {r.library} | {r.filename} | page {r.page} | {r.section} | {', '.join(r.topic_tags)}")
                print("why selected: keyword/source/topic/vector hybrid score")
                print((r.excerpt or r.text)[:1000].replace("\n", " "))


if __name__ == "__main__":
    main()
