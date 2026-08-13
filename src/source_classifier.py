from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path


INTERN_LIBRARY = "intern_year_medicine"
ICU_LIBRARY = "ICU_critical_care"
ANESTHESIA_LIBRARY = "anesthesiology_boards"
PERSONAL_LIBRARY = "personal_notes"
MISSED_LIBRARY = "missed_questions"


@dataclass(frozen=True)
class SourceMetadata:
    source_name: str
    library: str
    training_phase: str
    clinical_context: str
    source_family: str
    source_rank: int


def _override(filename: str) -> SourceMetadata | None:
    path = Path(__file__).resolve().parents[1] / "source_overrides.json"
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None
    lower = filename.lower()
    for key, value in data.items():
        if key.lower() not in lower:
            continue
        return SourceMetadata(
            source_name=value.get("source_name", filename.rsplit(".", 1)[0]),
            library=value.get("library", PERSONAL_LIBRARY),
            training_phase=value.get("training_phase", "intern_year"),
            clinical_context=value.get("clinical_context", "wards"),
            source_family=value.get("source_family", "personal"),
            source_rank=int(value.get("source_rank", 50)),
        )
    return None


def infer_source_metadata(filename: str) -> SourceMetadata:
    if overridden := _override(filename):
        return overridden
    name = filename.lower()
    if any(term in name for term in ["mgh", "white book", "housestaff"]):
        return SourceMetadata("MGH Housestaff Manual", INTERN_LIBRARY, "intern_year", "wards", "intern", 95)
    if any(term in name for term in ["uhintern", "intern survival", "intern-survival", "intern-guide", "intern guide"]):
        return SourceMetadata("Intern Notes / Survival Guide", INTERN_LIBRARY, "intern_year", "wards", "intern", 100)
    if any(term in name for term in ["ucsf", "hospitalist", "medicine handbook"]):
        return SourceMetadata("Hospitalist / Intern Guide", INTERN_LIBRARY, "intern_year", "wards", "intern", 98)
    if any(term in name for term in ["onlinemeded", "online med ed"]):
        return SourceMetadata("OnlineMedEd Intern Guide", INTERN_LIBRARY, "intern_year", "wards", "intern", 85)
    if any(term in name for term in ["marino", "icu book", "critical care"]):
        return SourceMetadata("Marino ICU Book", ICU_LIBRARY, "ICU", "ICU", "icu", 100)
    if any(term in name for term in ["stanford", "ca-1", "ca1", "tutorial"]):
        return SourceMetadata("Stanford CA-1", ANESTHESIA_LIBRARY, "anesthesia_boards", "OR", "anesthesia", 100)
    if any(term in name for term in ["morgan", "mikhail"]):
        return SourceMetadata("Morgan & Mikhail", ANESTHESIA_LIBRARY, "anesthesia_boards", "OR", "anesthesia", 90)
    if "miller" in name:
        return SourceMetadata("Miller/Baby Miller", ANESTHESIA_LIBRARY, "anesthesia_boards", "OR", "anesthesia", 80)
    if "missed" in name or "question" in name:
        return SourceMetadata(filename.rsplit(".", 1)[0], MISSED_LIBRARY, "intern_year", "wards", "missed", 110)
    if "note" in name:
        return SourceMetadata(filename.rsplit(".", 1)[0], PERSONAL_LIBRARY, "intern_year", "wards", "personal", 105)
    return SourceMetadata(filename.rsplit(".", 1)[0], PERSONAL_LIBRARY, "intern_year", "wards", "personal", 50)


def infer_source_name(filename: str) -> str:
    return infer_source_metadata(filename).source_name
