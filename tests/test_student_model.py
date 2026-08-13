from src.student_model import generate_session_plan, get_ca1_coverage, get_due_reviews, get_fact_catalog, get_or_create_topic, get_source_coverage, initialize_database, log_attempt


def test_student_model_initializes(tmp_path, monkeypatch):
    from src import student_model

    monkeypatch.setattr(student_model.settings, "sqlite_db_path", tmp_path / "student.db")
    initialize_database()
    tid = get_or_create_topic("Airway", "mask ventilation")
    assert tid > 0


def test_log_attempt_updates_mastery(tmp_path, monkeypatch):
    from src import student_model

    monkeypatch.setattr(student_model.settings, "sqlite_db_path", tmp_path / "student.db")
    initialize_database()
    log_attempt("s", "LAST", "", "q", "bad", "lipid rescue", "incorrect", "crisis_algorithm")
    due = get_due_reviews()
    assert any(r["topic"] == "LAST" for r in due)


def test_session_plan_includes_topics(tmp_path, monkeypatch):
    from src import student_model

    monkeypatch.setattr(student_model.settings, "sqlite_db_path", tmp_path / "student.db")
    plan = generate_session_plan()
    assert plan["session_id"]
    assert plan["plan"]
    assert plan["training_phase"] == "intern_year"


def test_basics_session_plan_uses_ca1_catalog(tmp_path, monkeypatch):
    from src import student_model

    monkeypatch.setattr(student_model.settings, "sqlite_db_path", tmp_path / "student.db")
    monkeypatch.setattr(
        student_model,
        "get_ca1_fact_catalog",
        lambda: [{"target_id": "ca1-last", "topic": "LAST", "subtopic": "CA-1 p. 82: lipid rescue", "fact": "lipid rescue", "page": 82, "source": "Stanford CA-1"}],
    )
    monkeypatch.setattr(student_model, "get_supporting_fact_catalog", lambda: [])
    plan = generate_session_plan(mode="BASICS")
    assert "BASICS mode" in plan["rationale"]
    assert any(item["topic"] == "LAST" for item in plan["plan"])
    assert plan["plan"][0]["subtopic"] == "CA-1 p. 82: lipid rescue"


def test_intern_session_plan_uses_granular_intern_catalog(tmp_path, monkeypatch):
    from src import student_model

    monkeypatch.setattr(student_model.settings, "sqlite_db_path", tmp_path / "student.db")
    monkeypatch.setattr(
        student_model,
        "get_intern_fact_catalog",
        lambda: [
            {
                "target_id": "intern-hyperk",
                "topic": "Hyperkalemia",
                "subtopic": "Intern Notes / Survival Guide p. 4: calcium stabilizes myocardium",
                "fact": "calcium stabilizes myocardium",
                "page": 4,
                "source": "Intern Notes / Survival Guide",
                "library": "intern_year_medicine",
                "training_phase": "intern_year",
            }
        ],
    )
    plan = generate_session_plan(mode="default")
    assert plan["training_phase"] == "intern_year"
    assert plan["plan"][0]["topic"] == "Hyperkalemia"
    assert plan["plan"][0]["library"] == "intern_year_medicine"


def test_ca1_coverage_reports_remaining_topics(tmp_path, monkeypatch):
    from src import student_model

    monkeypatch.setattr(student_model.settings, "sqlite_db_path", tmp_path / "student.db")
    monkeypatch.setattr(
        student_model,
        "get_ca1_fact_catalog",
        lambda: [{"target_id": "ca1-last", "topic": "LAST", "subtopic": "CA-1 p. 82: lipid rescue", "fact": "lipid rescue", "page": 82, "source": "Stanford CA-1"}],
    )
    coverage = get_ca1_coverage()
    assert coverage["source"] == "Stanford CA-1"
    assert coverage["total_topics"] == 1
    assert coverage["total_facts"] == 1
    assert coverage["remaining_facts"] == 1


def test_source_coverage_summarizes_all_books(tmp_path, monkeypatch):
    from src import student_model

    monkeypatch.setattr(student_model.settings, "sqlite_db_path", tmp_path / "student.db")
    monkeypatch.setattr(
        student_model,
        "get_fact_catalog",
        lambda source, max_facts_per_chunk=8: [{"target_id": source, "topic": "Airway", "subtopic": f"{source} fact", "fact": "fact", "page": 1, "source": source}],
    )
    coverage = get_source_coverage()
    assert len(coverage["source_summaries"]) >= 3
    assert any(row["source"] == "Stanford CA-1" for row in coverage["source_summaries"])


def test_fact_catalog_skips_ca1_front_matter(tmp_path, monkeypatch):
    from src import student_model

    store = tmp_path / "chunks.jsonl"
    rows = [
        {
            "id": "front",
            "text": "TABLE OF CONTENTS Airway Local Anesthetics",
            "search_text": "TABLE OF CONTENTS Airway Local Anesthetics",
            "metadata": {"book": "Stanford CA-1", "page": 2, "section": "TABLE OF CONTENTS", "topic_tags": "Airway"},
        },
        {
            "id": "real",
            "text": "Local anesthetic systemic toxicity requires stopping local anesthetic and giving intralipid early.",
            "search_text": "Local anesthetic systemic toxicity requires stopping local anesthetic and giving intralipid early.",
            "metadata": {"book": "Stanford CA-1", "page": 82, "section": "Local Anesthetics", "topic_tags": "LAST"},
        },
    ]
    store.write_text("\n".join(__import__("json").dumps(row) for row in rows), encoding="utf-8")
    monkeypatch.setattr(student_model.settings, "chroma_dir", tmp_path)
    facts = get_fact_catalog("Stanford CA-1")
    assert len(facts) == 1
    assert facts[0]["page"] == 82
