from datetime import datetime, timedelta, timezone

import pytest

from src.fsrs import (
    deserialize,
    due_now,
    fsrs_init,
    fsrs_review,
    mastery_proxy,
    retrievability_now,
    serialize,
)


def _t(days: float) -> datetime:
    return datetime(2026, 1, 1, tzinfo=timezone.utc) + timedelta(days=days)


def test_init_state_is_new():
    s = fsrs_init()
    assert s["state"] == "new"
    assert s["stability"] == 0.0
    assert s["reps"] == 0
    assert s["next_due"] is None


def test_first_good_review_sets_due_in_future():
    s, due = fsrs_review(fsrs_init(), rating=3, now=_t(0))
    assert s["state"] == "review"
    assert s["reps"] == 1
    assert s["stability"] > 0
    assert datetime.fromisoformat(due) > _t(0)


def test_easy_grows_stability_more_than_good():
    s_good, _ = fsrs_review(fsrs_init(), rating=3, now=_t(0))
    s_easy, _ = fsrs_review(fsrs_init(), rating=4, now=_t(0))
    assert s_easy["stability"] > s_good["stability"]


def test_again_increments_lapses_and_keeps_relearning():
    s, _ = fsrs_review(fsrs_init(), rating=3, now=_t(0))
    s2, _ = fsrs_review(s, rating=1, now=_t(s["stability"]))
    assert s2["lapses"] == 1
    assert s2["state"] == "relearning"


def test_repeated_good_grows_stability():
    s = fsrs_init()
    last_stability = 0.0
    now = _t(0)
    for _ in range(5):
        s, _ = fsrs_review(s, rating=3, now=now)
        assert s["stability"] >= last_stability
        last_stability = s["stability"]
        now = now + timedelta(days=max(1, int(s["stability"])))


def test_due_now_true_for_new_state():
    assert due_now(None) is True
    assert due_now(fsrs_init()) is True


def test_due_now_false_after_recent_review():
    s, _ = fsrs_review(fsrs_init(), rating=3, now=_t(0))
    assert due_now(s, now=_t(0)) is False


def test_retrievability_decays_with_time():
    s, _ = fsrs_review(fsrs_init(), rating=3, now=_t(0))
    r0 = retrievability_now(s, now=_t(0))
    r1 = retrievability_now(s, now=_t(s["stability"] * 2))
    assert r0 > r1
    assert 0.0 <= r1 <= 1.0


def test_serialize_round_trips():
    s, _ = fsrs_review(fsrs_init(), rating=3, now=_t(0))
    text = serialize(s)
    assert deserialize(text) == s


def test_deserialize_handles_empty_and_invalid():
    assert deserialize(None)["state"] == "new"
    assert deserialize("")["state"] == "new"
    assert deserialize("not json")["state"] == "new"


def test_mastery_proxy_monotonic():
    s = fsrs_init()
    proxies = []
    now = _t(0)
    for _ in range(8):
        s, _ = fsrs_review(s, rating=3, now=now)
        proxies.append(mastery_proxy(s))
        now = now + timedelta(days=max(1, int(s["stability"])))
    assert proxies == sorted(proxies)
    assert proxies[-1] <= 1.0


def test_invalid_rating_raises():
    with pytest.raises(ValueError):
        fsrs_review(fsrs_init(), rating=0)
    with pytest.raises(ValueError):
        fsrs_review(fsrs_init(), rating=5)
