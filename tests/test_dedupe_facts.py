import json

from src import dedupe_facts


def _row(id_, text, book, page, chunk_type="fact"):
    return {
        "id": id_,
        "text": text,
        "metadata": {
            "chunk_id": id_,
            "chunk_type": chunk_type,
            "book": book,
            "source_name": book,
            "page": page,
        },
    }


def test_normalize_strips_lead_noise_and_refs():
    a = dedupe_facts.normalize_for_hash("Pearl: hyperkalemia treatment is calcium gluconate.")
    b = dedupe_facts.normalize_for_hash("1. Hyperkalemia treatment is calcium gluconate.")
    c = dedupe_facts.normalize_for_hash("• Hyperkalemia treatment is calcium gluconate (see chapter 5).")
    assert a == b == c


def test_is_medical_fact_keeps_dose_and_drug_lines():
    assert dedupe_facts.is_medical_fact("Propofol 2 mg/kg IV induction dose.")
    assert dedupe_facts.is_medical_fact("Patient with sepsis should get lactate measurement.")
    assert dedupe_facts.is_medical_fact("Hyperkalemia: confirm with ECG and treat with calcium.")


def test_is_medical_fact_drops_boilerplate():
    assert not dedupe_facts.is_medical_fact("In this chapter we will discuss the basics.")
    assert not dedupe_facts.is_medical_fact("See Table 12.3 for details.")
    assert not dedupe_facts.is_medical_fact("Reproduced with permission.")
    assert not dedupe_facts.is_medical_fact("www.example.com")
    assert not dedupe_facts.is_medical_fact("Acknowledgments")


def test_canonical_priority_prefers_spine():
    assert dedupe_facts.canonical_priority("Intern Notes / Survival Guide") > dedupe_facts.canonical_priority("Morgan & Mikhail")
    assert dedupe_facts.canonical_priority("Marino ICU Book") > dedupe_facts.canonical_priority("Miller/Baby Miller")


def test_run_dry_run_dedupes_exact_duplicates(tmp_path, monkeypatch):
    monkeypatch.setattr(dedupe_facts.settings, "chroma_dir", tmp_path)
    rows = [
        _row("a1", "Hyperkalemia: confirm ECG, give calcium gluconate IV.", "Intern Notes / Survival Guide", 5),
        _row("b1", "Hyperkalemia: confirm ECG, give calcium gluconate IV.", "Morgan & Mikhail", 200),
        _row("c1", "Pearl: hyperkalemia: confirm ECG, give calcium gluconate IV.", "Miller/Baby Miller", 300),
        _row("d1", "Propofol 2 mg/kg IV induction.", "Stanford CA-1", 50),
    ]
    path = tmp_path / "chunks.jsonl"
    path.write_text("\n".join(json.dumps(r) for r in rows), encoding="utf-8")
    summary = dedupe_facts.run(dry_run=True)
    assert summary["input_facts"] == 4
    assert summary["dropped_exact_dupe"] == 2
    assert summary["canonical_facts"] == 2


def test_run_drops_boilerplate_via_medical_gate(tmp_path, monkeypatch):
    monkeypatch.setattr(dedupe_facts.settings, "chroma_dir", tmp_path)
    rows = [
        _row("a1", "Sepsis: lactate >2 mmol/L, give 30 mL/kg crystalloid and antibiotics within 1 hour.", "MGH Housestaff Manual", 50),
        _row("a2", "In this chapter we will discuss sepsis.", "MGH Housestaff Manual", 50),
        _row("a3", "See Table 4.1 for details.", "MGH Housestaff Manual", 50),
    ]
    path = tmp_path / "chunks.jsonl"
    path.write_text("\n".join(json.dumps(r) for r in rows), encoding="utf-8")
    summary = dedupe_facts.run(dry_run=True)
    assert summary["dropped_non_medical"] == 2
    assert summary["canonical_facts"] == 1


def test_run_writes_backup_and_keeps_canonical(tmp_path, monkeypatch):
    monkeypatch.setattr(dedupe_facts.settings, "chroma_dir", tmp_path)
    rows = [
        _row("p1", "Some passage chunk content here.", "Intern Notes / Survival Guide", 5, chunk_type="passage"),
        _row("a1", "Hyperkalemia: confirm with ECG and treat with calcium gluconate IV.", "Intern Notes / Survival Guide", 5),
        _row("b1", "Hyperkalemia: confirm with ECG and treat with calcium gluconate IV.", "Morgan & Mikhail", 200),
    ]
    path = tmp_path / "chunks.jsonl"
    path.write_text("\n".join(json.dumps(r) for r in rows), encoding="utf-8")
    summary = dedupe_facts.run(dry_run=False)
    assert summary["canonical_facts"] == 1
    assert summary["passages"] == 1
    backup = tmp_path / "chunks.jsonl.predupe.bak"
    assert backup.exists()
    new_rows = [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines()]
    survivors = [r for r in new_rows if r.get("metadata", {}).get("chunk_type") == "fact"]
    assert len(survivors) == 1
    assert survivors[0]["metadata"]["source_name"] == "Intern Notes / Survival Guide"
    assert survivors[0]["metadata"]["is_canonical_fact"] is True


def test_within_book_near_dedupe(tmp_path, monkeypatch):
    monkeypatch.setattr(dedupe_facts.settings, "chroma_dir", tmp_path)
    long_text = (
        "Hyperkalemia treatment includes ECG monitoring, calcium gluconate one gram intravenous, "
        "insulin ten units intravenous with dextrose, albuterol nebulized, and dialysis if refractory."
    )
    near_dupe = (
        "Hyperkalemia treatment includes ECG monitoring, calcium gluconate one gram intravenous, "
        "insulin ten units intravenous with dextrose, albuterol nebulized, and consider dialysis."
    )
    unrelated = "Aspirin 325 mg PO is given for acute coronary syndrome."
    rows = [
        _row("a1", long_text, "MGH Housestaff Manual", 5),
        _row("a2", near_dupe, "MGH Housestaff Manual", 87),
        _row("a3", unrelated, "MGH Housestaff Manual", 102),
    ]
    path = tmp_path / "chunks.jsonl"
    path.write_text("\n".join(json.dumps(r) for r in rows), encoding="utf-8")
    summary = dedupe_facts.run(dry_run=True, near_threshold=0.70)
    assert summary["dropped_near_dupe"] == 1
    assert summary["canonical_facts"] == 2
