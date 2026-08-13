# Cloud GPU Offload for Knowledge-Point Generation

`kp_gen_colab.ipynb` turns all 1,214 curriculum topics into atomic knowledge points
grounded in the corpus, using a vLLM-served open-source LLM on a free Colab GPU.

Estimated runtime: **~3-5 hours on a free T4** vs. 20-40+ hours on CPU.

---

## Prerequisites (do these on your local machine once)

### 1. Push the corpus to Google Drive

The Chroma vector database lives on your D: drive (~1.8 GB total).
Push it to Drive before opening the notebook:

```powershell
# Corpus (chroma DB — sqlite3 + HNSW index + chunks.jsonl)
rclone copy D:\anesthesia_attending\storage\chroma gdrive:clinical_attending_corpus/chroma --progress

# Curriculum blueprint
rclone copy C:\Users\Dean\anesthesia_attending\data\curriculum_blueprint.json gdrive:clinical_attending_corpus/ --progress

# Repo code (scripts/ and src/ only; no need for storage/ or large data/)
rclone copy C:\Users\Dean\anesthesia_attending\scripts gdrive:clinical_attending_corpus/scripts --progress
rclone copy C:\Users\Dean\anesthesia_attending\src    gdrive:clinical_attending_corpus/src    --progress
```

**Total upload: ~1.8 GB** (dominated by `chroma.sqlite3` at ~1.0 GB and `chunks.jsonl`
at ~256 MB).  On a typical home connection (50 Mbps upload) this takes 5-10 minutes.

> Your data stays in your own Google Drive and is only copied to a transient Colab
> instance that you control.  It is never transmitted to a third-party LLM API.
> Delete the Colab runtime when done.

### 2. Open the notebook in Colab

Upload `cloud/kp_gen_colab.ipynb` to Colab (or open it directly from Drive),
then select: **Runtime → Change runtime type → GPU** (leave hardware accelerator as T4).

---

## Notebook stages

| Stage | What it does |
|-------|-------------|
| 0 — GPU detect | Identifies GPU (T4 / L4 / A100) and auto-selects the right model |
| 1 — Install deps | `pip install vllm autoawq` + repo deps (torchvision excluded) |
| 2 — Pull from Drive | Mounts Drive, copies corpus + scripts + any prior progress files |
| 3 — Start vLLM server | Launches OpenAI-compatible server on `localhost:8000/v1`, polls until ready |
| 4 — Generate KPs | Runs `generate_kp_graph.py` — tier 1 first, then full run |
| 5 — Validate + sync | Parses catalog, prints counts, pushes results back to Drive |
| Interim save | Optional: run this cell every ~30 min to checkpoint progress to Drive |

---

## Recommended model

| GPU | VRAM | Model | Notes |
|-----|------|-------|-------|
| T4 (free tier) | 16 GB | `Qwen/Qwen2.5-7B-Instruct-AWQ` | AWQ 4-bit; fits with 8-9 GB VRAM to spare |
| L4 (Colab Pro) | 24 GB | `Qwen/Qwen2.5-7B-Instruct` | Full precision; better quality |
| A100 (Colab Pro+) | 40/80 GB | `Qwen/Qwen2.5-14B-Instruct-AWQ` | Best quality |

**Why Qwen2.5-7B-Instruct-AWQ on a T4?**
- AWQ 4-bit quantization: ~7 GB VRAM, leaving ~8 GB for KV cache
- Native structured-output / JSON instruction following (superior to Llama-3.1 for JSON extraction)
- HuggingFace model ID: `Qwen/Qwen2.5-7B-Instruct-AWQ` (official Qwen release, Apache 2.0)
- `--trust-remote-code` required (Qwen uses custom attention kernels)

**vLLM serve command (for reference; the notebook runs this automatically):**
```bash
python -m vllm.entrypoints.openai.api_server \
  --model Qwen/Qwen2.5-7B-Instruct-AWQ \
  --host 0.0.0.0 --port 8000 \
  --dtype auto \
  --gpu-memory-utilization 0.90 \
  --max-model-len 8192 \
  --trust-remote-code \
  --disable-log-requests
```

Note: single T4 = single GPU; `--tensor-parallel-size` is not needed and must be omitted.

---

## Throughput + time estimates

Each topic generates 1 LLM call with:
- **Input:** ~2,000-3,000 tokens (8 corpus chunks at ~250 tok each + prompt scaffolding)
- **Output:** ~800 tokens (5 KPs + illness script JSON)
- **Latency per topic:** ~12-18 s (Qwen2.5-7B-AWQ single-request on T4 @ ~60-80 tok/s)

| Scope | Topics | Estimated time (T4) | Local CPU estimate |
|-------|--------|---------------------|-------------------|
| Tier 1 only | ~170 | 35-50 min | 3-6 hours |
| Full (all tiers) | 1,214 | 3.4-6 hours | 20-40 hours |

The free T4 is comfortably faster than any CPU-only setup for this workload.

---

## Session limits and resume strategy

**Free Colab limits:**
- Hard session limit: **12 hours**
- Idle timeout: **~90 minutes** (the main practical constraint — keep the tab active)
- T4 allocation: not guaranteed; if unavailable, try again in a few hours

**Resume across sessions — fully automatic:**
`generate_kp_graph.py` writes `data/kp_generation_progress.jsonl` after each topic.
On restart, it reads this file and skips already-done topics.  The workflow is:

1. Session 1 dies mid-run → Stage 5 sync cell copies progress files to Drive
2. Open a new Colab session
3. Run Stage 2 (pulls progress files from Drive alongside the corpus)
4. Run Stage 4 full-run cell — already-done topics are skipped automatically
5. No data is lost

For the **Tier 1 first** strategy: Session 1 = ~170 topics (~50 min), Session 2 = remaining ~1,044 topics (~3-4 hours across 1-2 sessions).

---

## Pull results home

After the notebook completes (or after an interim sync):

```powershell
# Pull catalog
rclone copy gdrive:clinical_attending_corpus/kp_catalog.json C:\Users\Dean\anesthesia_attending\data\ --progress

# Pull progress log (needed for resume if the session was incomplete)
rclone copy gdrive:clinical_attending_corpus/kp_generation_progress.jsonl C:\Users\Dean\anesthesia_attending\data\ --progress
```

The `kp_catalog.json` is then available locally to seed the tutor's knowledge graph.

---

## Corpus upload size caveat

| File | Size | Notes |
|------|------|-------|
| `chroma.sqlite3` | ~1.0 GB | Main embedding store — must be uploaded |
| `chunks.jsonl` | ~256 MB | Text chunks — needed by hybrid_search BM25 path |
| HNSW index bins | ~250 MB | `data_level0.bin` × 2 — needed by Chroma ANN search |
| `chunks.jsonl.predupe.bak` | ~203 MB | **Skip this** — it's a backup, not needed |

Upload the `chroma/` folder as-is (rclone will copy all files).  The `.predupe.bak`
file is included automatically but wastes bandwidth; you can skip it:

```powershell
rclone copy D:\anesthesia_attending\storage\chroma gdrive:clinical_attending_corpus/chroma --progress --exclude "*.predupe.bak"
```

---

## torchvision note

Colab ships a pre-built `torch` + `torchvision` pair tied to the system CUDA version.
Reinstalling `torchvision` via pip frequently downgrades `torch` and breaks CUDA access.
The KP generation pipeline does **not** use vision features, so `torchvision` is
intentionally excluded from Stage 1's install list.  If other parts of the repo need it,
install it manually **after** vLLM and verify `torch.cuda.is_available()` still returns True.
