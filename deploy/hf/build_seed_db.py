"""Regenerate the clean seed student DB shipped to the HF Space.

Produces `deploy/hf/seed_student_model.db`: the real high-yield clinical topics
only (no dev/test artifacts, no duplicates), each at a pristine 'new' state with
zero attempts. The deploy script uploads this to the private STATE_DATASET so the
Space boots with a clean, sensible study queue.

Run: python deploy/hf/build_seed_db.py
"""
import os
import pathlib
import sys

SEED = pathlib.Path(__file__).resolve().parent / "seed_student_model.db"
ROOT = pathlib.Path(__file__).resolve().parents[2]

# Point the project's DB layer at the seed file BEFORE importing it.
os.environ["SQLITE_DB_PATH"] = str(SEED)
sys.path.insert(0, str(ROOT))

if SEED.exists():
    SEED.unlink()

from src.student_model import initialize_database, get_or_create_topic  # noqa: E402

TOPICS = [
    "Admission orders", "Afib with RVR", "Airway", "Cardiovascular physiology",
    "Consults", "Cross-cover pages", "Electrolytes", "Hyperkalemia", "Hypoxemia",
    "IV anesthetics", "Malignant hyperthermia", "Monitoring",
    "Oxygenation and ventilation", "Respiratory physiology", "Sepsis", "Shock",
    "Vasopressors",
]

initialize_database()
for t in TOPICS:
    get_or_create_topic(t, training_phase="intern_year")

print(f"Seed built: {SEED} — {len(TOPICS)} clean clinical topics, 0 attempts")
