import pytest


@pytest.fixture(autouse=True)
def disable_heavy_local_models(monkeypatch):
    from src import reranking

    monkeypatch.setattr(reranking.settings, "enable_local_reranker", False)
    reranking._cross_encoder.cache_clear()


@pytest.fixture(scope="session", autouse=True)
def isolate_student_db(tmp_path_factory):
    """Point the whole test session at a THROWAWAY copy of the student model DB.

    Without this, every test run writes straight into the real
    storage/sqlite/student_model.db — the user's actual spaced-repetition
    progress. Test topics (`test_topic_correct`, `mastery_track_test`,
    `topic-with-special_chars!@#$`, ...) end up interleaved with genuine study
    history, polluting mastery_matrix, coverage percentages and the FSRS queue,
    and they get carried into every backup.

    We copy rather than start empty because tests may rely on seeded curriculum
    /topic rows; the copy is made with sqlite's backup API so it is consistent
    even with WAL enabled. `settings` is a module-level singleton shared by all
    importers, so reassigning the attribute redirects every caller of
    student_model.conn().
    """
    import shutil
    import sqlite3
    from pathlib import Path
    from src.config import settings

    real_path = Path(settings.sqlite_db_path)
    tmp_db = tmp_path_factory.mktemp("student_db") / "student_model.db"

    if real_path.exists():
        src = sqlite3.connect(str(real_path))
        dst = sqlite3.connect(str(tmp_db))
        with dst:
            src.backup(dst)  # consistent snapshot including WAL contents
        dst.close()
        src.close()

    original = settings.sqlite_db_path
    settings.sqlite_db_path = tmp_db
    try:
        yield tmp_db
    finally:
        settings.sqlite_db_path = original
        for suffix in ("", "-wal", "-shm"):
            p = Path(str(tmp_db) + suffix)
            if p.exists():
                try:
                    p.unlink()
                except OSError:
                    pass
        shutil.rmtree(tmp_db.parent, ignore_errors=True)
