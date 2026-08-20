"""The four recording failures found by diffing the 2026-08-18 session
transcript against the database. Every fixture below is REAL text from that
session, not invented — these are regression tests for things that actually
happened and were silently mis-recorded.

See docs/KNOWLEDGE_GRANULARITY.md for why this matters more than it looks: the
maintainer's stated condition for continuing to use the system is that it stop
quizzing him on what he already knows and reliably quiz him on what he doesn't.
Both halves of that failed here, in opposite directions.
"""
from __future__ import annotations

from src.answer_evidence import (
    detect_parroting,
    evidence_supports,
    fact_was_covered,
    looks_like_meta_summary,
)

# The exact ARDS exchange, 47 seconds apart.
ARDS_TUTOR = (
    "Berlin criteria for ARDS: PaO2 over FiO2 less than or equal to 300 (not 200 - "
    "that's actually the moderate category cutoff), plus bilateral opacities, plus a "
    "non-cardiac cause for the edema. The mortality-reducing intervention is NOT high "
    "PEEP - it's low tidal volume ventilation, 6 mL per kg of ideal body weight, not "
    "actual weight, since lung size tracks height. PEEP gets titrated for oxygenation, "
    "but tidal volume is the one proven to save lives."
)
ARDS_PARROT = "You just told me since because lung size tracks height, not fat."
# What the grader stored instead — the giveaway phrase scrubbed out.
ARDS_CLEANED = "Because lung size tracks height, not fat."


class TestParroting:
    def test_the_ards_restatement_is_caught(self):
        """Graded `correct`; the fact jumped to 3-of-5 on a 3-day interval."""
        parroted, reason = detect_parroting(ARDS_PARROT, ARDS_TUTOR)
        assert parroted
        assert reason

    def test_caught_even_without_the_admission_phrase(self):
        """The grader's cleaned summary deleted 'you just told me'. Overlap with
        the preceding tutor turn must still catch it, or the fix depends on the
        user volunteering that they were parroting."""
        parroted, _ = detect_parroting(ARDS_CLEANED, ARDS_TUTOR)
        assert parroted

    def test_genuine_recall_is_not_flagged(self):
        """The Frank-Starling answer: his own words, his own framing, and the
        tutor had NOT just supplied it. Must survive."""
        parroted, _ = detect_parroting(
            "Because they're on the exponential or pre-exponential part of the curve.",
            "Prerenal nailed: BUN/Cr over 20, FeNa under 1 percent, concentrated urine.")
        assert not parroted

    def test_no_prior_turn_means_no_parroting(self):
        assert detect_parroting("lung size tracks height", "")[0] is False

    def test_empty_answer_is_not_parroting(self):
        assert detect_parroting("", ARDS_TUTOR)[0] is False

    def test_long_elaboration_reusing_vocabulary_is_not_parroting(self):
        """A long answer that reuses the tutor's terms while adding reasoning is
        engagement, not echo. Flagging it would punish the best answers."""
        long_answer = (
            "So the reason you use ideal body weight is that lung size tracks height "
            "rather than adiposity, which means a heavier patient at the same height "
            "has the same lung volume. If I dosed tidal volume off actual weight in an "
            "obese patient I would be delivering a much larger breath than the lung can "
            "accommodate, which causes volutrauma and drives the ventilator-induced "
            "injury that low tidal volume ventilation exists to prevent. It also "
            "explains why the ARDSNet protocol specifies a height-based calculation "
            "for every patient rather than adjusting per body habitus at the bedside."
        )
        assert detect_parroting(long_answer, ARDS_TUTOR)[0] is False


class TestEvidence:
    def test_paraphrase_of_what_he_said_counts(self):
        verbatim = ("To answer the anemia bundle one first, we need to see if they're "
                    "stable or unstable. If they're stable, then the threshold for "
                    "transfusion seven, hemoglobin of seven.")
        assert evidence_supports("transfusion threshold hemoglobin of 7", verbatim)

    def test_invented_evidence_is_rejected(self):
        """The real risk: a grader that fabricates the quote backing a correct
        verdict. That is how unearned credit gets written."""
        verbatim = "Downtrend in creatinine. I'm not sure what you're getting at."
        assert not evidence_supports(
            "explained post-obstructive diuresis and fluid replacement", verbatim)

    def test_empty_evidence_never_supports_anything(self):
        assert not evidence_supports("", "I said a great many things")


class TestMetaSummary:
    def test_the_vasopressor_summary_is_flagged(self):
        """Stored instead of the actual teaching; the content is gone."""
        flagged, _ = looks_like_meta_summary(
            "Dose range is right. Rationale corrected to receptor mechanism rather "
            "than renal protection. Epinephrine as next step confirmed correct.")
        assert flagged

    def test_the_sepsis_summary_is_flagged(self):
        flagged, _ = looks_like_meta_summary(
            "Workup elements reasonable, sequencing corrected, and septic shock "
            "definition corrected to the precise MAP/lactate/vasopressor criteria.")
        assert flagged

    def test_real_teaching_is_not_flagged(self):
        """The ARDS reply is real teaching and must pass, even though it contains
        corrective language — the distinction is teaching vs describing teaching."""
        assert looks_like_meta_summary(ARDS_TUTOR)[0] is False

    def test_conversational_correction_is_not_flagged(self):
        assert looks_like_meta_summary(
            "Right idea on alveolar recruitment, but the bigger piece is "
            "hemodynamic: positive intrathoracic pressure reduces venous return, "
            "which drops preload on an overloaded heart.")[0] is False

    def test_empty_response_is_not_flagged(self):
        assert looks_like_meta_summary("")[0] is False


class TestFactCoverage:
    ADHF_TURN = (
        "You're called to see a patient in acute decompensated heart failure who's now "
        "hypotensive, looking like a cardiogenic-shock picture. Does your diuretic "
        "strategy change? | I would imagine that you don't want to aggressively diurese "
        "a patient who is hypotensive. | Confirmed the cardiogenic shock ADHF picture: "
        "avoid diuresis, prioritize vasopressors and inotropic support. For hypertensive "
        "ADHF, taught IV nitroglycerin as the add-on to furosemide."
    )

    def test_a_fact_this_turn_actually_taught_is_covered(self):
        assert fact_was_covered(
            "ADHF with low BP (cardiogenic shock): avoid diuresis, use "
            "vasopressors/inotropes", self.ADHF_TURN)

    def test_the_bipap_card_written_before_the_bipap_question_is_not_covered(self):
        """Created at 15:53 with the cardiogenic-shock answer; the BiPAP question
        was not asked until 15:54. Nothing in that turn taught it."""
        assert not fact_was_covered(
            "BiPAP/CPAP mechanism in ADHF: positive pressure increases intrathoracic "
            "pressure reducing preload, offloads work of breathing, recruits flooded "
            "alveoli", self.ADHF_TURN)

    def test_blank_point_is_never_covered(self):
        assert not fact_was_covered("", self.ADHF_TURN)


class TestEndToEnd:
    """The checks above are pure functions; these assert the wiring in
    submit_answer actually changes what lands in the database.

    Run under pytest ONLY — conftest.isolate_student_db redirects the whole
    session to a throwaway copy. An earlier version of this was run as an
    ad-hoc script instead, which bypassed that fixture: the fuzzy fact matcher
    recognised the probe's ARDS text as the maintainer's REAL ARDS card and
    redirected the write onto it, knocking a genuine 3-of-5 'learning' card to
    'weak' with an extra lapse. Never exercise these paths outside pytest.
    """

    TUTOR = ("The mortality-reducing intervention is low tidal volume ventilation, "
             "6 mL per kg of ideal body weight, since lung size tracks height.")
    POINT = "ProbeFact: distinctive threshold for the fictional probe-state index"

    def test_parroting_is_downgraded_and_recorded_as_exposure(self):
        from src.mcp_endpoints import submit_answer

        submit_answer(
            topic="EvidenceProbeTopic", question="ARDS criteria and the vent change?",
            user_answer="P/F over 200, increase PEEP", is_correct=False, result="incorrect",
            user_answer_verbatim="I think it's over two hundred, and increased PEEP.",
            tutor_response=self.TUTOR, confidence_reported=2)

        out = submit_answer(
            topic="EvidenceProbeTopic", question="Teach-back: why ideal body weight?",
            user_answer="Because lung size tracks height, not fat.",
            is_correct=True, result="correct", confidence_reported=3,
            teach_back_quality=0.5,
            user_answer_verbatim="You just told me since because lung size tracks height, not fat.",
            tutor_response="Right - lung volume scales with height.",
            knowledge_points=[{"point": self.POINT, "correct": True,
                               "evidence": "lung size tracks height"}])

        assert out["graded_as_exposure"] is True
        assert out["facts_downgraded_from_parroting"], "the fact must lose its credit"
        assert any("exposure" in w for w in out["warnings"])

    def test_a_fact_this_turn_never_touched_is_filed_as_new_not_failed(self):
        from src.mcp_endpoints import submit_answer
        from src.student_model import conn

        stray = "ProbeFact: tracheostomy decannulation needs a capped trial and cough"
        out = submit_answer(
            topic="EvidenceProbeTopic2", question="Vasopressin timing in septic shock?",
            user_answer="around 5-10", is_correct=False, result="partial",
            user_answer_verbatim="I think you add vasopressin around five to ten.",
            tutor_response="Dose range is right. Rationale corrected to receptor mechanism.",
            knowledge_points=[{"point": stray, "correct": False}])

        assert stray[:80] in out["facts_not_covered_this_turn"]
        # Flagged as a meta-summary in the same call.
        assert any("summary" in w for w in out["warnings"])
        with conn() as db:
            row = db.execute(
                "SELECT status, times_seen, next_review_date, first_presented_at "
                "FROM knowledge_points WHERE point = ?", (stray,)).fetchone()
        assert row is not None, "the content is real and must be kept"
        assert row["status"] == "new"
        assert row["times_seen"] == 0, "it was never put to the user"
        assert row["next_review_date"] is None, "new material is not an overdue review"
        assert row["first_presented_at"] is None

    def test_grounded_in_is_persisted_on_the_attempt_row(self):
        """Previously accepted, written only to the tool log, and never stored —
        so an audit selecting it died with 'no such column: grounded_in'."""
        from src.mcp_endpoints import submit_answer
        from src.student_model import conn

        submit_answer(
            topic="EvidenceProbeTopic3", question="probe question for grounding",
            user_answer="a distinct probe answer body", is_correct=True,
            user_answer_verbatim="a distinct probe answer body",
            tutor_response="You had that right, and here is the mechanism behind it.",
            grounded_in="Marino ICU Book - lung protective ventilation")
        with conn() as db:
            row = db.execute(
                "SELECT grounded_in FROM question_attempts WHERE topic = ? "
                "ORDER BY attempt_id DESC LIMIT 1", ("EvidenceProbeTopic3",)).fetchone()
        assert row["grounded_in"] == "Marino ICU Book - lung protective ventilation"


class TestSummaryMustNotRewriteTheAnswer:
    """The worst recording failure observed: the graded summary corrected the
    user's answer, then graded the correction.

    He said naloxone "point one to point three mgs PER KG". The summary recorded
    "0.1 to 0.3 mg PER DOSE" and the reply called it "a touch conservative". For
    a 70 kg adult that is 7-21 mg against a correct flat 0.4 mg — 18 to 52 times
    too high. The day before, the same answer was recorded correctly as "per kg
    ... should be a flat 0.4 mg", so this was a regression, not a limitation.
    """

    def test_per_kg_silently_becoming_per_dose_is_caught(self):
        from src.answer_evidence import summary_contradicts_verbatim
        hit, why = summary_contradicts_verbatim(
            "0.1 to 0.3 mg per dose, redose every 2-3 minutes.",
            "point one to point three mgs per kg and redose every two to three minutes.")
        assert hit
        assert "PER KG" in why and "PER DOSE" in why

    def test_dropping_per_kg_entirely_is_caught(self):
        from src.answer_evidence import summary_contradicts_verbatim
        hit, _ = summary_contradicts_verbatim(
            "Said 0.1 to 0.3 mg, redose q2-3 min",
            "point one to point three mgs per kg")
        assert hit

    def test_a_summary_that_preserves_the_error_passes(self):
        """Recording the mistake faithfully is the whole point — that must not
        itself be flagged."""
        from src.answer_evidence import summary_contradicts_verbatim
        hit, _ = summary_contradicts_verbatim(
            "Said 0.1-0.3 mg per kg, which is weight-based and wrong; correct is a flat 0.4 mg",
            "point one to point three mgs per kg")
        assert not hit

    def test_an_answer_with_no_weight_based_dose_is_untouched(self):
        from src.answer_evidence import summary_contradicts_verbatim
        assert not summary_contradicts_verbatim(
            "Gave 0.4 mg flat IV, correct", "zero point four milligrams")[0]

    def test_submit_answer_warns_on_the_contradiction(self):
        from src.mcp_endpoints import submit_answer
        out = submit_answer(
            topic="ContradictProbeTopic", question="naloxone IV dose?",
            user_answer="0.1 to 0.3 mg per dose", is_correct=False, result="partial",
            user_answer_verbatim="point one to point three mgs per kg",
            tutor_response="Close, the standard is 0.4 mg.")
        assert out["summary_contradicts_verbatim"] is True
        assert any("contradicts" in w for w in out["warnings"])
