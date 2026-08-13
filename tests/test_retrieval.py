import json

from src.retrieval import expand_query, hybrid_search, retrieval_confidence
from src.reranking import rerank


def test_retrieval_returns_metadata(tmp_path, monkeypatch):
    from src import retrieval

    store = tmp_path / "chunks.jsonl"
    store.write_text(json.dumps({"id": "1", "text": "Shunt physiology causes hypoxemia that responds poorly to oxygen.", "metadata": {"book": "Miller/Baby Miller", "filename": "miller.pdf", "page": 12, "section": "Shunt", "topic_tags": "Respiratory physiology", "chunk_id": "1"}}) + "\n", encoding="utf-8")
    monkeypatch.setattr(retrieval.settings, "chroma_dir", tmp_path)
    results, insufficient = hybrid_search("shunt physiology hypoxemia", max_results=3)
    assert results
    assert results[0].page == 12
    assert not insufficient


def test_retrieval_filters_library_and_returns_confidence(tmp_path, monkeypatch):
    from src import retrieval

    store = tmp_path / "chunks.jsonl"
    rows = [
        {
            "id": "intern-hyperk",
            "text": "Hyperkalemia treatment includes ECG assessment, calcium gluconate, insulin and dextrose.",
            "search_text": "Hyperkalemia treatment ECG calcium gluconate insulin dextrose intern medicine",
            "metadata": {
                "book": "Intern Notes / Survival Guide",
                "source_name": "Intern Notes / Survival Guide",
                "library": "intern_year_medicine",
                "training_phase": "intern_year",
                "clinical_context": "wards",
                "filename": "intern.pdf",
                "page": 4,
                "section": "Hyperkalemia",
                "topic_tags": "Hyperkalemia",
                "retrieval_tags": "Hyperkalemia,calcium gluconate,insulin dextrose",
                "chunk_id": "intern-hyperk",
            },
        },
        {
            "id": "anes-last",
            "text": "LAST treatment includes lipid emulsion.",
            "search_text": "LAST lipid emulsion anesthesia",
            "metadata": {"book": "Stanford CA-1", "source_name": "Stanford CA-1", "library": "anesthesiology_boards", "page": 82, "topic_tags": "LAST", "chunk_id": "anes-last"},
        },
    ]
    store.write_text("\n".join(json.dumps(row) for row in rows), encoding="utf-8")
    monkeypatch.setattr(retrieval.settings, "chroma_dir", tmp_path)
    results, insufficient = hybrid_search("hyperkalemia treatment", mode="intern_teach", library_filter="intern_year_medicine")
    assert results[0].library == "intern_year_medicine"
    assert retrieval_confidence(results) in {"medium", "high"}
    assert not insufficient


def test_weak_retrieval_flags_insufficient(tmp_path, monkeypatch):
    from src import retrieval

    monkeypatch.setattr(retrieval.settings, "chroma_dir", tmp_path)
    results, insufficient = hybrid_search("nonexistent topic", max_results=3)
    assert results == []
    assert insufficient


def test_query_expansion_handles_medical_acronyms_without_substring_noise():
    expanded = expand_query("LAST treatment")
    assert "local anesthetic systemic toxicity" in expanded
    assert "malignant hyperthermia" not in expand_query("rhythm control")
    assert "local anesthetic systemic toxicity" not in expand_query("last case of the day")


def test_retrieval_uses_normalized_search_text(tmp_path, monkeypatch):
    from src import retrieval

    store = tmp_path / "chunks.jsonl"
    row = {
        "id": "mh-1",
        "text": "Malignant hyperther-\nmia treatment includes dantrolene.",
        "search_text": "Malignant hyperthermia treatment includes dantrolene.",
        "metadata": {
            "book": "Stanford CA-1",
            "filename": "ca1.pdf",
            "page": 85,
            "section": "Treatment",
            "topic_tags": "Malignant hyperthermia",
            "chunk_id": "mh-1",
        },
    }
    store.write_text(json.dumps(row) + "\n", encoding="utf-8")
    monkeypatch.setattr(retrieval.settings, "chroma_dir", tmp_path)
    results, insufficient = hybrid_search("malignant hyperthermia", max_results=3)
    assert results[0].page == 85
    assert not insufficient


def test_retrieval_eval_case_shape(monkeypatch):
    from src import retrieval_eval

    monkeypatch.setattr(
        retrieval_eval,
        "EVAL_CASES",
        [retrieval_eval.EvalCase("shunt physiology", "Respiratory physiology", ("shunt",))],
    )
    rows = retrieval_eval.run_eval()
    assert rows[0]["query"] == "shunt physiology"
    assert "hit" in rows[0]


def test_basics_exam_mode_prioritizes_stanford_ca1():
    candidates = [
        {"id": "miller", "text": "local anesthetic toxicity treatment", "metadata": {"book": "Miller/Baby Miller"}},
        {"id": "stanford", "text": "local anesthetic toxicity treatment", "metadata": {"book": "Stanford CA-1"}},
        {"id": "morgan", "text": "local anesthetic toxicity treatment", "metadata": {"book": "Morgan & Mikhail"}},
    ]
    ranked = rerank("BASICS exam local anesthetic toxicity treatment", candidates, mode="basics_exam")
    assert ranked[0]["metadata"]["book"] == "Stanford CA-1"
