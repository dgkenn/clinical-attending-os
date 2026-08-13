"""fetch_guidelines.py — Resumable, disk-aware downloader for free official medical guideline PDFs.

Downloads verified free PDFs to D:\\corpus_staging\\guidelines\\ with a manifest JSON.

Usage:
    python scripts/fetch_guidelines.py [--dry-run] [--min-free-gb 5]

Features:
    - Writes ONLY to D: drive (aborts if D: free < 5 GB)
    - Resumable: skips files already downloaded and validated
    - Polite: sets User-Agent, 2s delay between requests
    - Validates PDF header (%PDF) and minimum size (50 KB)
    - Maintains manifest JSON: {title, body, url, file, bytes, status}
"""

import json
import os
import sys
import time
import shutil
import hashlib
import argparse
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime, timezone

# Force UTF-8 output on Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# ---------------------------------------------------------------------------
# CURATED GUIDELINE CATALOGUE
# All URLs verified as freely accessible (open PDF, not paywalled)
# Status: VERIFIED = direct %PDF confirmed; UNVERIFIED = URL plausible but
#         not yet HEAD-checked
# ---------------------------------------------------------------------------

GUIDELINES = [
    # ── Surviving Sepsis ────────────────────────────────────────────────────
    {
        "title": "Surviving Sepsis Campaign Guidelines 2021",
        "body": "SCCM/ESICM",
        "url": "https://dfwhcfoundation.org/wp-content/uploads/2021/10/2021.10-Surviving_Sepsis_Campaign__International.95059.pdf",
        "filename": "Guideline - Surviving Sepsis Campaign 2021.pdf",
        "verified": True,
    },
    # ── KDIGO ───────────────────────────────────────────────────────────────
    # Note: KDIGO 2024 CKD and 2012 AKI already downloaded successfully (kdigo.org worked with browser UA)
    {
        "title": "KDIGO 2024 Clinical Practice Guideline - Chronic Kidney Disease",
        "body": "KDIGO",
        "url": "https://kdigo.org/wp-content/uploads/2024/03/KDIGO-2024-CKD-Guideline.pdf",
        "filename": "Guideline - KDIGO 2024 CKD.pdf",
        "verified": True,
    },
    {
        "title": "KDIGO 2012 Clinical Practice Guideline - Acute Kidney Injury",
        "body": "KDIGO",
        "url": "https://kdigo.org/wp-content/uploads/2016/10/KDIGO-2012-AKI-Guideline-English.pdf",
        "filename": "Guideline - KDIGO 2012 AKI.pdf",
        "verified": True,
    },
    {
        "title": "KDIGO 2021 Clinical Practice Guideline - Blood Pressure in CKD",
        "body": "KDIGO",
        "url": "https://kdigo.org/wp-content/uploads/2016/10/KDIGO_BP_Exec_Summary_final.pdf",
        "filename": "Guideline - KDIGO 2021 Blood Pressure CKD.pdf",
        "verified": True,  # Executive summary PDF from KDIGO
    },
    # ── GOLD COPD ───────────────────────────────────────────────────────────
    {
        "title": "GOLD 2024 Global Strategy for COPD - Full Report",
        "body": "GOLD (Global Initiative for Chronic Obstructive Lung Disease)",
        "url": "https://goldcopd.org/wp-content/uploads/2024/02/GOLD-2024_v1.2-11Jan24_WMV.pdf",
        "filename": "Guideline - GOLD 2024 COPD Full Report.pdf",
        "verified": True,  # verified large file (~10MB); HEAD confirms
    },
    {
        "title": "GOLD 2024 Global Strategy for COPD - Pocket Guide",
        "body": "GOLD (Global Initiative for Chronic Obstructive Lung Disease)",
        "url": "https://goldcopd.org/wp-content/uploads/2024/02/POCKET-GUIDE-GOLD-2024-ver-1.2-11Jan2024_WMV.pdf",
        "filename": "Guideline - GOLD 2024 COPD Pocket Guide.pdf",
        "verified": True,
    },
    # ── ADA Diabetes ────────────────────────────────────────────────────────
    {
        "title": "ADA Standards of Care in Diabetes 2024 - Summary Section (Diabetes Care)",
        "body": "American Diabetes Association",
        "url": "https://diabetesjournals.org/care/article-pdf/47/Supplement_1/S77/746953/dc24s005.pdf",
        "filename": "Guideline - ADA Standards of Care 2024 Section.pdf",
        "verified": True,  # Free open-access article PDF from ADA journal
    },
    {
        "title": "ADA Standards of Care in Diabetes 2024 - Overview (pathstohealthnm.org)",
        "body": "American Diabetes Association",
        "url": "https://pathstohealthnm.org/wp-content/uploads/2023/12/ADA-Standards-of-Care-2024.pdf",
        "filename": "Guideline - ADA Standards of Care 2024 Overview.pdf",
        "verified": True,
    },
    # ── ACC/AHA ─────────────────────────────────────────────────────────────
    {
        "title": "2022 AHA/ACC/HFSA Guideline for Management of Heart Failure",
        "body": "AHA/ACC/HFSA",
        "url": "https://sochicar.cl/wp-content/uploads/2022/12/j.jacc_.2021.12.012.pdf",
        "filename": "Guideline - ACC AHA 2022 Heart Failure.pdf",
        "verified": True,  # Verified: full JACC article PDF, 138 pages
    },
    {
        "title": "2023 ACC/AHA/ACCP/HRS Guideline for Atrial Fibrillation",
        "body": "ACC/AHA/ACCP/HRS",
        "url": "https://my.clevelandclinic.org/-/scassets/files/org/heart/depts/arrhythmia/2023-acc-aha-accp-hrs-guidelines-for-afib.pdf",
        "filename": "Guideline - ACC AHA 2023 Atrial Fibrillation.pdf",
        "verified": True,  # Verified: Cleveland Clinic institutional PDF, 8.2 MB
    },
    {
        "title": "JNC 8 (2014) Evidence-Based Guideline for Management of High Blood Pressure",
        "body": "JNC Panel / JAMA",
        "url": "https://family-medicine.ecu.edu/wp-content/pv-uploads/sites/82/2020/03/jnc-8-guidelines.pdf",
        "filename": "Guideline - JNC8 2014 Hypertension.pdf",
        "verified": True,  # Verified: ECU institutional PDF
    },
    # ── IDSA ────────────────────────────────────────────────────────────────
    {
        "title": "IDSA 2014 Practice Guidelines - Skin and Soft Tissue Infections",
        "body": "Infectious Diseases Society of America (IDSA)",
        "url": "https://www.idsociety.org/globalassets/idsa/practice-guidelines/practice-guidelines-for-the-diagnosis-and-management-of-skin-and-soft-tissue-infections-2014-update-by-the-infectious-diseases-society-of-america.pdf",
        "filename": "Guideline - IDSA 2014 SSTI.pdf",
        "verified": True,
    },
    {
        "title": "IDSA/SHEA 2021 Clinical Practice Guideline - Clostridioides difficile Infection",
        "body": "IDSA/SHEA",
        "url": "https://academic.oup.com/cid/article-pdf/73/5/e1029/40326165/ciab549.pdf",
        "filename": "Guideline - IDSA SHEA 2021 C difficile.pdf",
        "verified": True,  # OUP open-access, updated PDF path
    },
    {
        "title": "IDSA/ATS 2019 Executive Summary - Community-Acquired Pneumonia in Adults",
        "body": "IDSA/ATS",
        "url": "https://www.idsociety.org/globalassets/idsa/practice-guidelines/community-acquired-pneumonia-in-adults/executive_summary.pdf",
        "filename": "Guideline - IDSA ATS 2019 CAP Executive Summary.pdf",
        "verified": True,  # Direct IDSA-hosted PDF, 642 KB
    },
    # ── AASLD Liver ─────────────────────────────────────────────────────────
    {
        "title": "AASLD-EASL 2014 Practice Guidelines - Hepatic Encephalopathy in Chronic Liver Disease",
        "body": "AASLD/EASL",
        "url": "https://www.aasld.org/sites/default/files/2022-07/Hepatic%20Encephalopathy%20in%20Chronic%20Liver%20Disease%202014.pdf",
        "filename": "Guideline - AASLD EASL 2014 Hepatic Encephalopathy.pdf",
        "verified": True,
    },
    # (JNC8 now included above with verified ECU PDF)
    # ── CHEST VTE ───────────────────────────────────────────────────────────
    {
        "title": "CHEST 2021 Antithrombotic Therapy for VTE Disease (CHEST Guideline)",
        "body": "American College of Chest Physicians",
        "url": "https://advancedhealth.com/wp-content/uploads/2023/07/Antithrombotic-Therapy-for-VTE-Disease-CHEST-Guideline-2021.pdf",
        "filename": "Guideline - CHEST 2021 VTE Antithrombotic.pdf",
        "verified": True,  # third-party host, confirmed PDF
    },
    # ── WHO / Other open guidelines ─────────────────────────────────────────
    {
        "title": "WHO 2023 Guidelines on Management of Sepsis and Septic Shock in Adults",
        "body": "World Health Organization",
        "url": "https://iris.who.int/bitstream/handle/10665/374776/9789240090828-eng.pdf?sequence=1&isAllowed=y",
        "filename": "Guideline - WHO 2023 Sepsis Management.pdf",
        "verified": False,  # WHO IRIS download link; may need session cookie
    },
    # ── AASLD Cirrhosis (additional) ────────────────────────────────────────
    {
        "title": "AASLD 2021 Practice Guidance - Management of Ascites, Spontaneous Bacterial Peritonitis, Hepatorenal Syndrome",
        "body": "AASLD",
        "url": "https://www.aasld.org/sites/default/files/2021-07/AASLD-PracticeGuidance-Ascites_Aug2021update.pdf",
        "filename": "Guideline - AASLD 2021 Ascites SBP HRS.pdf",
        "verified": False,
    },
]

# ---------------------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------------------
STAGING_DIR = Path(r"D:\corpus_staging\guidelines")
MANIFEST_PATH = STAGING_DIR / "manifest.json"
MIN_FREE_GB = 5.0
MIN_PDF_BYTES = 50 * 1024  # 50 KB
REQUEST_DELAY = 2.0  # seconds between requests
USER_AGENT = (
    "Mozilla/5.0 (compatible; MedicalTutorBot/1.0; "
    "educational-guideline-downloader; contact=dgkenn@bu.edu)"
)
HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "application/pdf,application/octet-stream,*/*",
}


# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------

def free_gb(drive: str = "D:") -> float:
    """Return free space in GB on the given drive (Windows)."""
    total, used, free = shutil.disk_usage(drive)
    return free / (1024 ** 3)


def load_manifest() -> dict:
    """Load existing manifest from disk or return empty dict keyed by filename."""
    if MANIFEST_PATH.exists():
        with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
            entries = json.load(f)
        return {e["filename"]: e for e in entries}
    return {}


def save_manifest(manifest: dict):
    """Write manifest dict to JSON (sorted by filename)."""
    entries = sorted(manifest.values(), key=lambda e: e["filename"])
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2)


def validate_pdf(path: Path) -> tuple[bool, str]:
    """Check that file exists, is ≥ MIN_PDF_BYTES, and starts with %PDF."""
    if not path.exists():
        return False, "file not found"
    size = path.stat().st_size
    if size < MIN_PDF_BYTES:
        return False, f"too small ({size} bytes)"
    with open(path, "rb") as f:
        header = f.read(5)
    if header != b"%PDF-":
        return False, f"bad header: {header!r}"
    return True, f"ok ({size:,} bytes)"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()[:16]


def download_pdf(url: str, dest: Path, dry_run: bool = False) -> tuple[bool, str]:
    """Download url → dest. Returns (success, message)."""
    if dry_run:
        return True, "dry-run: skipped download"

    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            content_type = resp.headers.get("Content-Type", "")
            if "html" in content_type.lower():
                # PMC-style "preparing to download" page — try to extract PDF URL
                body = resp.read(4096).decode("utf-8", errors="replace")
                if "Preparing to download" in body or "redirecting" in body.lower():
                    return False, f"HTML redirect/prepare page (Content-Type: {content_type})"
                return False, f"HTML content returned (Content-Type: {content_type})"
            # Stream to file
            dest.parent.mkdir(parents=True, exist_ok=True)
            tmp = dest.with_suffix(".tmp")
            if tmp.exists():
                tmp.unlink()
            with open(tmp, "wb") as f:
                while True:
                    chunk = resp.read(65536)
                    if not chunk:
                        break
                    f.write(chunk)
            if dest.exists():
                dest.unlink()
            tmp.rename(dest)
            return True, f"downloaded ({dest.stat().st_size:,} bytes)"
    except urllib.error.HTTPError as e:
        return False, f"HTTP {e.code}: {e.reason}"
    except urllib.error.URLError as e:
        return False, f"URL error: {e.reason}"
    except Exception as e:
        return False, f"error: {e}"


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Download verified free medical guidelines")
    parser.add_argument("--dry-run", action="store_true", help="Simulate without writing")
    parser.add_argument("--min-free-gb", type=float, default=MIN_FREE_GB)
    parser.add_argument("--force", action="store_true", help="Re-download already completed files")
    args = parser.parse_args()

    # Disk guard
    free = free_gb("D:")
    print(f"D: drive free: {free:.1f} GB")
    if free < args.min_free_gb:
        print(f"ERROR: D: drive has only {free:.1f} GB free (minimum {args.min_free_gb} GB). Aborting.")
        sys.exit(1)

    if not args.dry_run:
        STAGING_DIR.mkdir(parents=True, exist_ok=True)

    manifest = load_manifest()
    print(f"Manifest loaded: {len(manifest)} existing entries\n")

    results = {"downloaded": [], "skipped": [], "failed": [], "skip_catalogue": []}

    for g in GUIDELINES:
        fname = g["filename"]
        title = g["title"]
        body = g["body"]
        url = g["url"]
        dest = STAGING_DIR / fname

        # Entries marked skip in catalogue
        if g.get("skip"):
            reason = g.get("skip_reason", "catalogue skip")
            print(f"[SKIP-CAT] {title}\n          Reason: {reason}\n")
            results["skip_catalogue"].append({
                "title": title, "body": body, "url": url,
                "filename": fname, "status": "skipped", "reason": reason,
            })
            continue

        # Already done?
        if fname in manifest and manifest[fname].get("status") == "ok" and not args.force:
            ok, msg = validate_pdf(dest)
            if ok:
                print(f"[SKIP-OK] {title} — already downloaded\n")
                results["skipped"].append(manifest[fname])
                continue
            else:
                print(f"[RE-DL]   {title} — existing file invalid ({msg}), re-downloading\n")

        print(f"[FETCH]   {title}")
        print(f"          {url}")

        success, msg = download_pdf(url, dest, dry_run=args.dry_run)

        if success and not args.dry_run:
            ok, valmsg = validate_pdf(dest)
            if not ok:
                success = False
                msg = f"downloaded but invalid: {valmsg}"
                if dest.exists():
                    dest.unlink()

        entry = {
            "title": title,
            "body": body,
            "url": url,
            "filename": fname,
            "file": str(dest) if (success and not args.dry_run) else None,
            "bytes": dest.stat().st_size if (success and not args.dry_run and dest.exists()) else None,
            "sha256_prefix": sha256_file(dest) if (success and not args.dry_run and dest.exists()) else None,
            "status": "ok" if success else "failed",
            "message": msg,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        if success:
            print(f"          OK {msg}")
            results["downloaded"].append(entry)
        else:
            print(f"          FAIL {msg}")
            results["failed"].append(entry)

        manifest[fname] = entry

        if not args.dry_run:
            save_manifest(manifest)

        # Check disk after each download
        free = free_gb("D:")
        if free < args.min_free_gb:
            print(f"\nWARNING: D: drive now only {free:.1f} GB free. Stopping to preserve disk space.")
            break

        time.sleep(REQUEST_DELAY)

    # Final disk check
    free = free_gb("D:")
    print(f"\n{'='*70}")
    print(f"D: free after run: {free:.1f} GB")
    print(f"Downloaded:        {len(results['downloaded'])}")
    print(f"Skipped (ok):      {len(results['skipped'])}")
    print(f"Failed:            {len(results['failed'])}")
    print(f"Skipped (paywall): {len(results['skip_catalogue'])}")
    print(f"Manifest:          {MANIFEST_PATH}")

    if results["downloaded"]:
        total_bytes = sum(e["bytes"] or 0 for e in results["downloaded"])
        print(f"Total downloaded:  {total_bytes / 1024**2:.1f} MB")
        print("\nDownloaded:")
        for e in results["downloaded"]:
            mb = (e["bytes"] or 0) / 1024**2
            print(f"  {e['filename']} ({mb:.1f} MB)")

    if results["failed"]:
        print("\nFailed:")
        for e in results["failed"]:
            print(f"  {e['filename']}: {e['message']}")

    if results["skip_catalogue"]:
        print("\nSkipped (paywalled/not free):")
        for e in results["skip_catalogue"]:
            print(f"  {e['title']}: {e['reason']}")


if __name__ == "__main__":
    main()
