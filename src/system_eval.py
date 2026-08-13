from __future__ import annotations

from dataclasses import dataclass

from .tutor_engine import answer_query, grade_user_answer


@dataclass(frozen=True)
class PromptCase:
    query: str
    expected_mode: str | None = None
    must_have_source: str | None = None
    min_sources: int = 1


PROMPT_CASES = [
    PromptCase("i am just starting out my anesthisology resiendcy, lets build out a learning plan. teach me the first topic", "session_start", "Stanford CA-1"),
    PromptCase("Teach me LAST for my BASICS exam", "crisis", "Stanford CA-1"),
    PromptCase("Teach me malignant hyperthermia management for BASICS", "crisis", "Stanford CA-1"),
    PromptCase("Teach me shunt physiology", "physiology"),
    PromptCase("MAC increases and decreases", "teach"),
    PromptCase("succinylcholine contraindications", "drug"),
    PromptCase("high spinal treatment", "teach"),
    PromptCase("bronchospasm after induction", "teach"),
    PromptCase("difficult airway algorithm for CA-1", "teach", "Stanford CA-1"),
    PromptCase("anaphylaxis under anesthesia", "crisis"),
    PromptCase("laryngospasm treatment", "teach"),
    PromptCase("aspiration management", "teach"),
    PromptCase("hypotension after induction", "crisis"),
    PromptCase("hypoxemia after induction", "teach"),
    PromptCase("oxygen failure in the OR CA-1", "teach", "Stanford CA-1"),
    PromptCase("propofol drug review", "drug"),
    PromptCase("ketamine hemodynamics", "drug"),
    PromptCase("etomidate adrenal suppression", "physiology"),
    PromptCase("rocuronium versus succinylcholine", "drug"),
    PromptCase("sugammadex dosing and cautions", "teach"),
    PromptCase("neostigmine reversal", "teach"),
    PromptCase("local anesthetic max doses", "teach"),
    PromptCase("epidural test dose", "teach"),
    PromptCase("spinal anesthesia hypotension", "teach"),
    PromptCase("obstetric aspiration risk", "teach"),
    PromptCase("pediatric inhalational induction", "teach"),
    PromptCase("geriatric anesthetic considerations", "teach"),
    PromptCase("one lung ventilation hypoxemia", "physiology"),
    PromptCase("cardiac tamponade anesthetic goals", "teach"),
    PromptCase("aortic stenosis anesthetic goals", "teach"),
    PromptCase("increased intracranial pressure anesthetic management", "teach"),
    PromptCase("trauma RSI priorities", "teach"),
    PromptCase("massive transfusion complications", "teach"),
    PromptCase("hyperkalemia treatment in OR", "teach"),
    PromptCase("metabolic acidosis compensation", "teach"),
    PromptCase("renal failure anesthesia concerns", "teach"),
    PromptCase("hepatic disease anesthesia concerns", "teach"),
    PromptCase("OSA postoperative risk", "teach"),
    PromptCase("PONV risk factors", "teach"),
    PromptCase("delayed emergence differential", "teach"),
    PromptCase("extubation criteria", "teach"),
    PromptCase("standard monitors CA-1", "teach", "Stanford CA-1"),
    PromptCase("arterial line damping", "teach"),
    PromptCase("capnography phases", "teach"),
    PromptCase("ventilator pressure control versus volume control", "teach"),
    PromptCase("opioid respiratory depression", "physiology"),
    PromptCase("remifentanil context sensitive half time", "physiology"),
    PromptCase("neuromuscular monitoring train of four", "teach"),
    PromptCase("oral boards obese OSA lap chole", "oral_boards"),
    PromptCase("OR prep for lap chole in obese OSA patient", "OR_prep"),
]


GRADING_CASES = [
    ("LAST treatment", "Stop local anesthetic, support ABCs, give benzodiazepines for seizures, and give intralipid bolus then infusion.", "LAST", "treatment", "correct"),
    ("LAST treatment", "Give lipid and oxygen.", "LAST", "treatment", "partial"),
    ("LAST treatment", "Give more bupivacaine and watch.", "LAST", "treatment", "incorrect"),
    ("malignant hyperthermia management", "Stop volatiles and succinylcholine, call for MH cart, give dantrolene, oxygen, cool, treat hyperkalemia.", "Malignant hyperthermia", "management", "correct"),
    ("malignant hyperthermia management", "Cool the patient and call for help.", "Malignant hyperthermia", "management", "partial"),
    ("shunt physiology", "Perfusion without ventilation causes hypoxemia that corrects poorly with oxygen.", "Respiratory physiology", "shunt", "correct"),
    ("shunt physiology", "It is an oxygen problem.", "Respiratory physiology", "shunt", "incorrect"),
    ("succinylcholine contraindications", "Avoid in burns after 24 hours, denervation, immobilization, neuromuscular disease, MH history due to hyperkalemia.", "Neuromuscular blockers", "succinylcholine", "correct"),
    ("high spinal treatment", "Support airway and ventilation, treat hypotension and bradycardia with vasopressors and fluids.", "High spinal", "treatment", "correct"),
    ("high spinal treatment", "Put the patient in PACU.", "High spinal", "treatment", "incorrect"),
]


TEACH_COMPATIBLE_MODES = {
    "teach",
    "intern_teach",
    "cross_cover",
    "ICU_teach",
    "anesthesia_transition",
    "anesthesia_boards",
    "drug",
    "crisis",
    "physiology",
    "OR_prep",
}


def mode_matches(expected: str | None, actual: str) -> bool:
    if expected is None:
        return True
    if expected == "teach":
        return actual in TEACH_COMPATIBLE_MODES
    return expected == actual


def eval_prompts() -> list[dict]:
    rows = []
    for case in PROMPT_CASES:
        response = answer_query(case.query, "teach")
        source_books = [source.book for source in response.sources]
        rows.append(
            {
                "query": case.query,
                "ok": (
                    mode_matches(case.expected_mode, response.mode)
                    and len(response.sources) >= case.min_sources
                    and (case.must_have_source is None or case.must_have_source in source_books[:3])
                    and bool(response.answer.strip())
                ),
                "mode": response.mode,
                "source_books": source_books[:3],
                "insufficient_context": response.insufficient_context,
            }
        )
    return rows


def eval_grading() -> list[dict]:
    rows = []
    for question, answer, topic, subtopic, expected in GRADING_CASES:
        result, mistake_type = grade_user_answer(question, answer, "ideal", topic, subtopic)
        rows.append({"question": question, "expected": expected, "actual": result, "mistake_type": mistake_type, "ok": result == expected})
    return rows


def main() -> None:
    prompt_rows = eval_prompts()
    grade_rows = eval_grading()
    print(f"prompt_eval: {sum(row['ok'] for row in prompt_rows)}/{len(prompt_rows)} pass")
    for row in prompt_rows:
        if not row["ok"]:
            print(f"FAIL prompt | mode={row['mode']} | sources={row['source_books']} | {row['query']}")
    print(f"grading_eval: {sum(row['ok'] for row in grade_rows)}/{len(grade_rows)} pass")
    for row in grade_rows:
        if not row["ok"]:
            print(f"FAIL grading | expected={row['expected']} actual={row['actual']} | {row['question']}")


if __name__ == "__main__":
    main()
