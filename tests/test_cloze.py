import json

from src import cloze


def test_dose_mask_extracted():
    cards = cloze.generate_clozes(
        "Calcium gluconate 1 g IV stabilizes the cardiac membrane in hyperkalemia.",
        "fact-1",
        max_per_fact=4,
    )
    assert any(c.mask_type == "dose" for c in cards)
    dose_card = next(c for c in cards if c.mask_type == "dose")
    assert "[DOSE]" in dose_card.masked_text
    assert "1 g" in dose_card.answer or "1g" in dose_card.answer


def test_placeholders_clearly_labeled():
    cards = cloze.generate_clozes(
        "Confirm hyperkalemia with an ECG before treating.",
        "fact-x",
        max_per_fact=4,
    )
    for c in cards:
        if c.mask_type == "condition":
            assert "[CONDITION]" in c.masked_text
        elif c.mask_type == "label":
            assert "[ABBREVIATION]" in c.masked_text
        elif c.mask_type == "drug":
            assert "[DRUG NAME]" in c.masked_text


def test_drug_pattern_does_not_match_adjectives():
    """'hepatic' is not a drug; must not be picked up as drug mask."""
    cards = cloze.generate_clozes(
        "Lactulose is given to reduce ammonia in patients with hepatic encephalopathy.",
        "fact-y",
        max_per_fact=4,
    )
    drug_answers = [c.answer.lower() for c in cards if c.mask_type == "drug"]
    assert "hepatic" not in drug_answers


def test_drug_mask_extracted():
    cards = cloze.generate_clozes(
        "Propofol 2 mg/kg IV is the standard induction dose in healthy adults.",
        "fact-2",
        max_per_fact=4,
    )
    types = {c.mask_type for c in cards}
    assert "drug" in types or "dose" in types


def test_condition_mask_extracted():
    cards = cloze.generate_clozes(
        "Lactulose is given to reduce ammonia in patients with hepatic encephalopathy.",
        "fact-3",
        max_per_fact=4,
    )
    assert any(c.mask_type == "condition" for c in cards)
    cond = next(c for c in cards if c.mask_type == "condition")
    assert "encephalopathy" in cond.answer.lower()


def test_label_mask_extracted():
    cards = cloze.generate_clozes(
        "Confirm hyperkalemia with an ECG before treating.",
        "fact-4",
        max_per_fact=4,
    )
    types = {c.mask_type for c in cards}
    assert "label" in types or "condition" in types


def test_short_skipped():
    # too short
    cards = cloze.generate_clozes("Dantrolene", "fact-x", max_per_fact=4)
    assert cards == []
    # not enough words even though long enough chars
    cards = cloze.generate_clozes("X" * 100, "fact-y", max_per_fact=4)
    assert cards == []


def test_unpunctuated_facts_still_generate_clozes():
    # Fact extractor strips trailing punctuation; cloze must still work.
    cards = cloze.generate_clozes(
        "Calcium gluconate 1 g IV stabilizes the cardiac membrane in hyperkalemia",
        "fact-z",
        max_per_fact=4,
    )
    assert any(c.mask_type == "dose" for c in cards)


def test_max_per_fact_respected():
    long_text = (
        "Propofol 2 mg/kg IV produces hypnosis. Etomidate 0.3 mg/kg IV preserves hemodynamics. "
        "Ketamine 1 mg/kg IV provides analgesia. Succinylcholine 1 mg/kg IV gives rapid paralysis."
    )
    cards = cloze.generate_clozes(long_text, "fact-z", max_per_fact=2)
    assert len(cards) == 2


def test_card_id_is_stable():
    a = cloze.generate_clozes(
        "Calcium gluconate 1 g IV stabilizes the cardiac membrane in hyperkalemia.",
        "fact-1",
        max_per_fact=4,
    )
    b = cloze.generate_clozes(
        "Calcium gluconate 1 g IV stabilizes the cardiac membrane in hyperkalemia.",
        "fact-1",
        max_per_fact=4,
    )
    assert {c.card_id for c in a} == {c.card_id for c in b}


def test_build_deck_writes_jsonl(tmp_path, monkeypatch):
    chroma_dir = tmp_path / "chroma"
    chroma_dir.mkdir()
    monkeypatch.setattr(cloze.settings, "chroma_dir", chroma_dir)
    chunks = [
        {
            "id": "f1",
            "text": "Calcium gluconate 1 g IV stabilizes the cardiac membrane in hyperkalemia.",
            "metadata": {
                "chunk_id": "f1",
                "chunk_type": "fact",
                "book": "Intern Notes / Survival Guide",
                "source_name": "Intern Notes / Survival Guide",
                "library": "intern_year_medicine",
                "page": 5,
                "section": "Hyperkalemia",
                "topic_tags": "Hyperkalemia",
            },
        },
        {
            "id": "p1",
            "text": "Some passage chunk content.",
            "metadata": {"chunk_id": "p1", "chunk_type": "passage", "book": "Intern Notes / Survival Guide"},
        },
    ]
    (chroma_dir / "chunks.jsonl").write_text("\n".join(json.dumps(c) for c in chunks), encoding="utf-8")
    summary = cloze.build_deck(max_per_fact=4)
    assert summary["facts_seen"] == 1
    assert summary["cards_emitted"] >= 1
    out = tmp_path / "curriculum" / "cloze_cards.jsonl"
    assert out.exists()
    cards = [json.loads(line) for line in out.read_text(encoding="utf-8").splitlines()]
    assert all(c["source_fact_id"] == "f1" for c in cards)
    assert all(c["book"] == "Intern Notes / Survival Guide" for c in cards)
    # Index by topic tag
    deck_idx = cloze.deck_by_unit_topic_tag()
    assert "Hyperkalemia" in deck_idx
