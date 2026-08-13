from src.chunking import chunk_page_text
from src.fact_extraction import is_testable_chunk
from src.ingest import normalize_search_text
from src.source_classifier import ICU_LIBRARY, INTERN_LIBRARY, infer_source_metadata
from src.topic_taxonomy import build_retrieval_tags, tag_topics


def test_chunking_runs_on_sample_text():
    text = "Airway management and oxygenation. " * 120
    chunks = chunk_page_text(text, target_tokens=100, overlap_tokens=20)
    assert chunks


def test_topic_tagging():
    assert "Malignant hyperthermia" in tag_topics("Treat malignant hyperthermia with dantrolene.")
    tags = build_retrieval_tags("Hyperkalemia with ECG changes should be treated with calcium gluconate.", "Intern Notes")
    assert "Hyperkalemia" in tags["topic_tags"]
    assert "calcium gluconate" in tags["retrieval_tags"]


def test_source_classification_for_added_medicine_sources():
    assert infer_source_metadata("UHInternNFSurvivalGuideV4.pdf").library == INTERN_LIBRARY
    assert infer_source_metadata("Intern-Survival-Guide-2022-2023.pdf").source_name == "Intern Notes / Survival Guide"
    assert infer_source_metadata("MGH Housestaff Manual 2024-2025.pdf").library == INTERN_LIBRARY
    assert infer_source_metadata("The Little ICU Book - Paul Marino.pdf").library == ICU_LIBRARY


def test_normalize_search_text_dehyphenates_pdf_line_breaks():
    assert normalize_search_text("malignant hyperther-\n mia") == "malignant hyperthermia"


def test_morgan_narrative_kept_for_max_recall():
    meta = {"source_name": "Morgan & Mikhail", "page": 200}
    text = "The history of inhalational anesthesia is long and storied; many practitioners contributed observations across decades of practice."
    assert is_testable_chunk(meta, text) is True


def test_morgan_dosing_kept():
    meta = {"source_name": "Morgan & Mikhail", "page": 200}
    text = "Propofol induction dose is 1.5 to 2.5 mg/kg IV in healthy adults."
    assert is_testable_chunk(meta, text) is True


def test_morgan_pearl_kept():
    meta = {"source_name": "Morgan & Mikhail", "page": 300}
    text = "Pearl: succinylcholine is contraindicated in patients with hyperkalemia or recent burns."
    assert is_testable_chunk(meta, text) is True


def test_high_yield_score_signals():
    from src.fact_extraction import high_yield_score
    assert high_yield_score({"has_bold": True}, "anything") >= 0.30
    assert high_yield_score({}, "Propofol 2 mg/kg IV") > 0.0
    assert high_yield_score({}, "Pearl: never give succinylcholine in burns.") > 0.0
    assert high_yield_score({}, "narrative without signals") == 0.0


def test_intern_passage_kept_without_high_yield_signal():
    meta = {"source_name": "Intern Notes / Survival Guide", "page": 22}
    text = "Always confirm the patient's identity before any procedure on the wards."
    assert is_testable_chunk(meta, text) is True


def test_reference_pages_dropped():
    meta = {"source_name": "Morgan & Mikhail", "page": 100}
    text = "Smith J et al. doi:10.1234 PMID 999. Jones K et al. doi:10.5678 PMID 888. Brown L et al."
    assert is_testable_chunk(meta, text) is False


def test_appendix_section_dropped():
    meta = {"source_name": "Morgan & Mikhail", "page": 1500, "chapter_title": "APPENDIX"}
    text = "Propofol 2 mg/kg IV induction dose."
    assert is_testable_chunk(meta, text) is False
