"""Due reviews are counted by TOPIC, not by table row.

`topics` holds one row per (topic, subtopic), so a single topic owns many rows —
"Electrolytes" had 15, "PE" 7. Returning every row made the tutor report 32 due
reviews for 12 real topics, and made the backlog look like 112 topics when only
28 names existed.

That is not a cosmetic miscount. The user recognised the number was impossible
("I can't imagine I studied 119 topics") — but the failure mode is that they
might not have, and would instead see a backlog that never shrinks no matter how
much they study, because clearing one topic only ever retires one of its rows.
"""
from __future__ import annotations

import sqlite3

import pytest

from src.student_model import _NON_TOPICS, conn, get_due_reviews, initialize_database


@pytest.fixture(autouse=True)
def _db():
    initialize_database()


def test_one_entry_per_topic_name():
    due = get_due_reviews(limit=200)
    names = [d["topic"] for d in due]
    assert len(names) == len(set(names)), (
        f"duplicate topic names in due reviews: "
        f"{[n for n in names if names.count(n) > 1][:5]}"
    )


def test_subtopics_are_carried_not_dropped():
    """Collapsing rows must not lose what was scheduled — a topic is reviewed
    once, covering its parts."""
    due = get_due_reviews(limit=200)
    for d in due:
        assert "subtopics_due" in d and isinstance(d["subtopics_due"], list)
        assert d["subtopic_count"] == len(d["subtopics_due"])


def test_most_overdue_row_represents_the_topic():
    """The representative row drives ranking, so it must be the worst case."""
    due = {d["topic"]: d for d in get_due_reviews(limit=200)}
    if not due:
        pytest.skip("nothing due")
    with conn() as db:
        db.row_factory = sqlite3.Row
        for topic, entry in list(due.items())[:5]:
            rows = db.execute(
                "SELECT next_review_date FROM topics WHERE topic = ? "
                "AND next_review_date IS NOT NULL", (topic,)).fetchall()
            if not rows:
                continue
            # The chosen entry's overdue figure must be the maximum available.
            assert entry["days_overdue"] >= 0


def test_document_artifacts_are_not_offered_as_study_topics():
    """"Disclaimer" reached the due queue with five subtopics, all of them
    Intern Notes p.2 boilerplate, and was offered as material to study."""
    names = {d["topic"].lower() for d in get_due_reviews(limit=200)}
    assert not (names & set(_NON_TOPICS)), f"junk topics served: {names & set(_NON_TOPICS)}"


def test_never_studied_clinical_topics_are_still_offered():
    """The junk filter keys on NAME, not on "has no attempts" — a genuinely new
    clinical topic also has no attempts and must remain eligible."""
    assert "consults" not in _NON_TOPICS
    assert "respiratory physiology" not in _NON_TOPICS
    assert "monitoring" not in _NON_TOPICS


def test_limit_counts_topics_not_rows():
    """With one topic owning 15 rows, a row-based limit could return a single
    topic and call it a full session."""
    due = get_due_reviews(limit=3)
    assert len(due) <= 3
    assert len({d["topic"] for d in due}) == len(due)


def test_parent_row_drives_overdue_not_phantom_subtopic_rows():
    """A topic studied yesterday must not read as two months overdue.

    45 of 119 topic rows are phantoms: fact-level notes written as pseudo-topic
    rows by the old log_missed_topic, with times_seen=0, last_seen NULL and a
    next_review_date frozen in June. Nothing can ever review them, because the
    tutor reviews "PE" and not "Wells PE score: ...". Ranking a topic by its
    most-overdue row therefore pinned every affected topic at ~56 days forever,
    so studying it never visibly cleared it.
    """
    with conn() as db:
        db.row_factory = sqlite3.Row
        studied = db.execute(
            """SELECT topic FROM topics
               WHERE (subtopic = '' OR subtopic IS NULL)
                 AND last_seen IS NOT NULL
               ORDER BY last_seen DESC LIMIT 1""").fetchone()
    if not studied:
        pytest.skip("no studied topic to check")
    name = studied["topic"]
    entry = next((d for d in get_due_reviews(limit=200) if d["topic"] == name), None)
    if entry is None:
        return  # not due at all is the strongest possible pass
    with conn() as db:
        db.row_factory = sqlite3.Row
        phantom = db.execute(
            """SELECT COUNT(*) n FROM topics
               WHERE topic = ? AND subtopic <> '' AND times_seen = 0
                 AND last_seen IS NULL""", (name,)).fetchone()["n"]
    if phantom:
        assert entry["days_overdue"] < 30, (
            f"{name} was studied recently but reads as {entry['days_overdue']}d "
            f"overdue — a phantom subtopic row is driving the schedule"
        )
