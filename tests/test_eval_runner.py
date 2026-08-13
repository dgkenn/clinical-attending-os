import json

from src import eval_runner


def test_eval_runner_smoke(tmp_path, monkeypatch):
    from src import retrieval

    store = tmp_path / "chunks.jsonl"
    rows = [
        {
            "id": "intern-hyperk",
            "text": "Hyperkalemia treatment includes ECG, calcium gluconate, insulin and dextrose.",
            "search_text": "Hyperkalemia treatment ECG calcium gluconate insulin dextrose intern medicine",
            "metadata": {
                "book": "MGH Housestaff Manual",
                "source_name": "MGH Housestaff Manual",
                "library": "intern_year_medicine",
                "page": 4,
                "section": "Hyperkalemia",
                "topic_tags": "Hyperkalemia",
                "chunk_id": "intern-hyperk",
            },
        },
        {
            "id": "icu-shock",
            "text": "Septic shock treated with norepinephrine and vasopressin per Marino.",
            "search_text": "septic shock norepinephrine vasopressin Marino",
            "metadata": {
                "book": "Marino ICU Book",
                "source_name": "Marino ICU Book",
                "library": "ICU_critical_care",
                "page": 220,
                "topic_tags": "Vasopressors",
                "chunk_id": "icu-shock",
            },
        },
    ]
    store.write_text("\n".join(json.dumps(row) for row in rows), encoding="utf-8")
    monkeypatch.setattr(retrieval.settings, "chroma_dir", tmp_path)

    gold_path = tmp_path / "gold_set.json"
    gold_path.write_text(
        json.dumps(
            {
                "queries": [
                    {
                        "query": "hyperkalemia treatment",
                        "mode": "intern_teach",
                        "expected_libraries": ["intern_year_medicine"],
                        "must_appear_top_5": ["calcium", "insulin"],
                    },
                    {
                        "query": "vasopressor septic shock",
                        "mode": "ICU_teach",
                        "expected_libraries": ["ICU_critical_care"],
                        "must_appear_top_5": ["norepinephrine"],
                    },
                ]
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(eval_runner, "GOLD_PATH", gold_path)

    summary = eval_runner.run(use_cross_encoder=False)
    assert summary["n_queries"] == 2
    assert 0.0 <= summary["mrr5"] <= 1.0
    assert summary["recall10"] == 1.0
    assert summary["latency_p50"] > 0
