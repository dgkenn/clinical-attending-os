from __future__ import annotations


SESSION_STRUCTURE = [
    "warm_up_retrieval",
    "weak_topic_drilling",
    "new_material",
    "clinical_case_application",
    "teach_back",
]


def active_recall_instruction(mode: str) -> str:
    if mode in {"cross_cover", "rapid_response"}:
        return "Ask for the user's first bedside action before teaching."
    if mode in {"anesthesia_boards", "anesthesia_pimp", "oral_boards"}:
        return "Ask one anesthesia reasoning question before explanation."
    return "Ask one intern-level active recall question before explanation."


def voice_mode_rules() -> list[str]:
    return [
        "one question at a time",
        "short conversational turns",
        "ask the user to reason out loud",
        "teach briefly after the answer",
        "end with a teach-back check",
    ]
