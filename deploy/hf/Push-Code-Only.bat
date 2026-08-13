@echo off
REM ==========================================================================
REM  FAST code-only deploy of Clinical Attending OS to Hugging Face.
REM  Use this when only the SERVER CODE or CURRICULUM changed (the Chroma index
REM  is unchanged). It pushes the Space code + curriculum blueprint and lets the
REM  Space rebuild + re-seed the curriculum. It does NOT re-upload the 1.5 GB
REM  index and does NOT touch your saved study progress.
REM  Double-click this file, then paste the output back to Claude.
REM  (Reads your token from deploy\hf\.hf_token)
REM ==========================================================================
cd /d "%~dp0..\.."
echo.
echo ==========================================
echo   PUSHING CODE + CURRICULUM  -^> Hugging Face  (no index upload)
echo ==========================================
echo Ensuring huggingface_hub is installed...
python -m pip install -q huggingface_hub
echo Pushing Space code...
echo.
python deploy\hf\push_code_only.py
echo.
echo ==========================================
echo  ^>^>^>  Done. The Space will rebuild in ~2-3 min. Paste this output to Claude.
echo ==========================================
pause
