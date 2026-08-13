from __future__ import annotations

import json
import statistics
import time
from pathlib import Path
from typing import Any

from fastapi.testclient import TestClient

from .api import app
from .config import settings
from .retrieval import hybrid_search, retrieval_confidence
from .student_model import get_due_reviews, get_student_dashboard, get_topic_summary, initialize_database


MEDICINE_QUERIES = [
    "afib with RVR intern management",
    "hyperkalemia treatment",
    "hyponatremia workup",
    "hypoxemia on night float",
    "sepsis initial management",
    "GI bleed admission plan",
    "AKI differential",
    "altered mental status workup",
    "chest pain admission workup",
    "alcohol withdrawal management",
    "fever on cross-cover",
    "hypotension on the wards",
]

ICU_QUERIES = [
    "shock differential",
    "vasopressor choice septic shock",
    "ARDS ventilator strategy",
    "ventilator high pressure alarm",
    "sedation ICU delirium",
    "extubation readiness",
    "acid base approach ICU",
    "massive transfusion ICU",
]

ANESTHESIA_QUERIES = [
    "shunt physiology",
    "MAC increases decreases",
    "succinylcholine contraindications",
    "LAST treatment",
    "malignant hyperthermia management",
    "hypotension after induction",
    "bronchospasm after intubation",
    "difficult airway algorithm",
    "neuromuscular blockade reversal",
    "aspiration during induction",
]


def _source_family_hit(results: list[dict[str, Any]], expected: str) -> bool:
    if expected == "medicine":
        return any(r["library"] == "intern_year_medicine" for r in results[:3])
    if expected == "ICU":
        return any(r["library"] == "ICU_critical_care" or r["source"] == "Marino ICU Book" for r in results[:3])
    if expected == "anesthesia":
        return any(r["library"] == "anesthesiology_boards" for r in results[:3])
    return False


def _query_mode(query: str, family: str) -> str:
    if family == "medicine":
        return "cross_cover" if any(term in query for term in ["night", "cross-cover", "fever", "hypotension"]) else "intern_teach"
    if family == "ICU":
        return "ICU_teach"
    if "LAST" in query or "malignant" in query or "bronchospasm" in query or "aspiration" in query:
        return "crisis"
    if "succinylcholine" in query or "reversal" in query:
        return "drug"
    return "anesthesia_boards"


def _run_retrieval_audit() -> tuple[list[dict[str, Any]], list[float]]:
    rows: list[dict[str, Any]] = []
    latencies: list[float] = []
    for family, queries in [("medicine", MEDICINE_QUERIES), ("ICU", ICU_QUERIES), ("anesthesia", ANESTHESIA_QUERIES)]:
        for query in queries:
            mode = _query_mode(query, family)
            start = time.perf_counter()
            results, insufficient = hybrid_search(query, mode=mode, max_results=5)
            latencies.append(time.perf_counter() - start)
            dumped = [r.model_dump() for r in results]
            rows.append(
                {
                    "query": query,
                    "mode": mode,
                    "expected_family": family,
                    "retrieval_confidence": retrieval_confidence(results),
                    "insufficient_context": insufficient,
                    "expected_source_hit_top3": _source_family_hit(dumped, family),
                    "top_results": [
                        {
                            "source": r.source or r.book,
                            "library": r.library,
                            "page": r.page,
                            "section": r.section,
                            "score": r.score,
                            "preview": (r.excerpt or r.text)[:240].replace("\n", " "),
                        }
                        for r in results[:5]
                    ],
                }
            )
    return rows, latencies


def _chroma_count() -> int | None:
    try:
        import chromadb

        client = chromadb.PersistentClient(path=str(settings.chroma_dir))
        col = client.get_collection(settings.vector_collection_name())
        return int(col.count())
    except Exception:
        return None


def _file_size(path: Path) -> int:
    if path.is_file():
        return path.stat().st_size
    if path.is_dir():
        return sum(p.stat().st_size for p in path.rglob("*") if p.is_file())
    return 0


def _api_smoke() -> tuple[dict[str, Any], list[float]]:
    validation_db = settings.sqlite_db_path.parent / "_e2e_validation.db"
    settings.sqlite_db_path = validation_db
    initialize_database()
    client = TestClient(app)
    headers = {"X-API-Key": settings.api_key}
    latencies: list[float] = []

    def timed(method: str, path: str, **kwargs) -> Any:
        start = time.perf_counter()
        response = getattr(client, method)(path, **kwargs)
        latencies.append(time.perf_counter() - start)
        return response

    no_auth = client.post("/search", json={"query": "hyperkalemia"})
    health = timed("get", "/health")
    openapi = timed("get", "/openapi.json")
    search = timed("post", "/search", json={"query": "Teach me hyperkalemia as an intern.", "mode": "intern_teach"}, headers=headers)
    default_session = timed("post", "/start_session", json={"duration_minutes": 30, "mode": "default"}, headers=headers)
    icu_session = timed("post", "/start_session", json={"duration_minutes": 30, "mode": "ICU_teach", "training_phase": "ICU"}, headers=headers)
    anesthesia_session = timed("post", "/start_session", json={"duration_minutes": 30, "mode": "anesthesia_boards", "training_phase": "anesthesia_boards"}, headers=headers)
    submit_bad = timed(
        "post",
        "/submit_answer",
        json={
            "session_id": default_session.json()["session_id"],
            "question": "How do you treat hyperkalemia?",
            "user_answer": "I would recheck it later.",
            "topic": "Hyperkalemia",
            "subtopic": "intern management",
            "result": "incorrect",
            "mistake_type": "prioritization",
            "ideal_answer": "Check ECG, stabilize myocardium with calcium if ECG changes, shift potassium with insulin/dextrose, remove potassium and escalate.",
            "retrieval_sources": "MGH Housestaff Manual",
        },
        headers=headers,
    )
    due_after_bad = timed("get", "/due_reviews", headers=headers)
    for _ in range(3):
        timed(
            "post",
            "/submit_answer",
            json={
                "session_id": default_session.json()["session_id"],
                "question": "How do you treat hyperkalemia?",
                "user_answer": "ECG first, calcium for ECG changes, insulin/dextrose shift, remove potassium, call senior if unstable.",
                "topic": "Hyperkalemia",
                "subtopic": "intern management",
                "result": "correct",
                "mistake_type": "other",
                "ideal_answer": "ECG, calcium when indicated, shifting therapies, elimination, escalation.",
            },
            headers=headers,
        )
    summary_after_correct = get_topic_summary("Hyperkalemia")
    timed("post", "/mark_mastered", params={"topic": "Hyperkalemia", "subtopic": "intern management"}, headers=headers)
    timed("post", "/mark_weak", params={"topic": "Hyperkalemia", "subtopic": "intern management"}, headers=headers)
    timed("post", "/set_default_phase", json={"default_training_phase": "anesthesia_boards"}, headers=headers)
    changed_default = timed("post", "/start_session", json={"duration_minutes": 20, "mode": "default"}, headers=headers)
    timed("post", "/set_default_phase", json={"default_training_phase": "intern_year"}, headers=headers)
    reset_default = timed("post", "/start_session", json={"duration_minutes": 20, "mode": "default"}, headers=headers)
    dashboard = timed("get", "/student_dashboard", headers=headers)

    return (
        {
            "auth_required": no_auth.status_code == 401,
            "health": health.status_code,
            "openapi": openapi.status_code,
            "search": search.status_code,
            "default_session": default_session.json(),
            "icu_session": icu_session.json(),
            "anesthesia_session": anesthesia_session.json(),
            "submit_bad": submit_bad.json(),
            "due_after_bad_contains_hyperkalemia": any(row.get("topic") == "Hyperkalemia" for row in due_after_bad.json()),
            "summary_after_repeated_correct": summary_after_correct,
            "changed_default_phase": changed_default.json().get("training_phase"),
            "reset_default_phase": reset_default.json().get("training_phase"),
            "dashboard_status": dashboard.status_code,
        },
        latencies,
    )


def run_validation() -> dict[str, Any]:
    start = time.perf_counter()
    config = {
        "free_local_mode": settings.free_local_mode,
        "backend_mode": settings.backend_mode,
        "embedding_provider": settings.embedding_provider,
        "api_generation_enabled": settings.api_generation_enabled,
        "default_training_phase": settings.default_training_phase,
        "openai_api_key_present": bool(settings.openai_api_key),
    }
    manifest_path = settings.chroma_dir / "ingestion_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else []
    retrieval_rows, search_latencies = _run_retrieval_audit()
    api_status, api_latencies = _api_smoke()
    low_conf_results, low_conf = hybrid_search("zzzxqv plorbit narnulon qwertovia", mode="intern_teach", max_results=3)
    report = {
        "config": config,
        "manifest": manifest,
        "row_counts": {
            "jsonl_rows": sum(1 for _ in (settings.chroma_dir / "chunks.jsonl").open(encoding="utf-8")),
            "chroma_count": _chroma_count(),
        },
        "storage_bytes": {
            "chroma": _file_size(settings.chroma_dir),
            "sqlite": _file_size(settings.sqlite_db_path),
        },
        "retrieval_audit": retrieval_rows,
        "api_status": api_status,
        "safety": {
            "low_confidence_query_confidence": retrieval_confidence(low_conf_results),
            "low_confidence_insufficient_context": low_conf,
            "max_excerpt_chars": max((len(r["top_results"][0]["preview"]) for r in retrieval_rows if r["top_results"]), default=0),
            "backend_generation_guard": "FREE_LOCAL_MODE blocks LLM generation paths",
        },
        "performance": {
            "avg_search_latency_s": round(statistics.mean(search_latencies), 3),
            "max_search_latency_s": round(max(search_latencies), 3),
            "avg_api_latency_s": round(statistics.mean(api_latencies), 3),
            "max_api_latency_s": round(max(api_latencies), 3),
            "validation_runtime_s": round(time.perf_counter() - start, 3),
        },
    }
    return report


def write_markdown(report: dict[str, Any]) -> Path:
    out = settings.log_dir / "clinical_attending_os_validation_report.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    manifest = report["manifest"]
    retrieval = report["retrieval_audit"]
    failures = [row for row in retrieval if not row["expected_source_hit_top3"] or row["retrieval_confidence"] == "low"]
    lines = [
        "# Clinical Attending OS Validation Report",
        "",
        f"Overall retrieval audit: {len(retrieval) - len(failures)}/{len(retrieval)} acceptable.",
        f"JSONL rows: {report['row_counts']['jsonl_rows']}; Chroma rows: {report['row_counts']['chroma_count']}.",
        "",
        "## Config",
    ]
    for key, value in report["config"].items():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Source Classification"])
    for item in manifest:
        lines.append(
            f"- {Path(item['file']).name}: {item['source_name']} | {item['library']} | pages={item['pages']} | passages={item.get('passage_chunks')} | facts={item.get('fact_chunks')}"
        )
    lines.extend(["", "## Retrieval Audit"])
    for row in retrieval:
        status = "PASS" if row["expected_source_hit_top3"] and row["retrieval_confidence"] != "low" else "WARN"
        top = row["top_results"][0] if row["top_results"] else {}
        lines.append(
            f"- {status}: {row['query']} | mode={row['mode']} | confidence={row['retrieval_confidence']} | top={top.get('source')} {top.get('library')} p.{top.get('page')}"
        )
    lines.extend(["", "## API And Memory"])
    api = report["api_status"]
    lines.append(f"- API key auth required: {api['auth_required']}")
    lines.append(f"- /health status: {api['health']}; /openapi.json status: {api['openapi']}; /search status: {api['search']}")
    lines.append(f"- default session phase: {api['default_session'].get('training_phase')}")
    lines.append(f"- ICU override phase: {api['icu_session'].get('training_phase')}")
    lines.append(f"- anesthesia override phase: {api['anesthesia_session'].get('training_phase')}")
    lines.append(f"- due reviews include missed hyperkalemia: {api['due_after_bad_contains_hyperkalemia']}")
    lines.append(f"- set_default_phase changed to: {api['changed_default_phase']}; reset to: {api['reset_default_phase']}")
    lines.extend(["", "## Safety"])
    for key, value in report["safety"].items():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Performance"])
    for key, value in report["performance"].items():
        lines.append(f"- {key}: {value}")
    lines.extend(
        [
            "",
            "## Run Locally",
            "```powershell",
            "cd C:\\Users\\Dean\\anesthesia_attending",
            "uvicorn src.api:app --host 0.0.0.0 --port 8000",
            "```",
            "",
            "Next: expose with cloudflared or ngrok, replace the OpenAPI server URL, and configure `X-API-Key` in Custom GPT Actions.",
        ]
    )
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def main() -> None:
    report = run_validation()
    path = write_markdown(report)
    print(json.dumps({"report": str(path), "summary": report["performance"], "row_counts": report["row_counts"]}, indent=2))


if __name__ == "__main__":
    main()
