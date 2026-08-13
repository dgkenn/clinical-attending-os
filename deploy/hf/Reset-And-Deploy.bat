@echo off
REM ==========================================================================
REM  ONE-TIME reset: wipes the Space's student DB and re-seeds it CLEAN
REM  (17 clinical topics, 0 attempts), and pushes the latest server code.
REM  Use this ONCE now. For all future updates use Deploy-To-HF.bat, which
REM  PRESERVES your study progress.
REM ==========================================================================
cd /d "%~dp0..\.."
echo.
echo ==========================================
echo   RESET + DEPLOY  (clean re-seed)
echo ==========================================
python -m pip install -q huggingface_hub
set RESET_PROGRESS=1
python deploy\hf\deploy_to_hf.py
set RESET_PROGRESS=
echo.
echo  ^>^>^>  Copy the DEPLOY SUMMARY above and paste it back to Claude.
echo ==========================================
pause
