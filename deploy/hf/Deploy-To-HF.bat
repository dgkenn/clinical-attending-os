@echo off
REM ==========================================================================
REM  Deploy the Clinical Attending OS tutor to your Hugging Face account.
REM  Double-click this file. It uploads your index to a PRIVATE dataset and
REM  creates your Space, then prints a DEPLOY SUMMARY. Copy that summary back
REM  to Claude. (Reads your token from deploy\hf\.hf_token)
REM ==========================================================================
cd /d "%~dp0..\.."
echo.
echo ==========================================
echo   DEPLOYING CLINICAL ATTENDING OS  -> Hugging Face
echo ==========================================
echo Ensuring huggingface_hub is installed...
python -m pip install -q huggingface_hub
echo Running deploy (index upload can take several minutes)...
echo.
python deploy\hf\deploy_to_hf.py
echo.
echo ==========================================
echo  ^>^>^>  Copy the DEPLOY SUMMARY above and paste it back to Claude.
echo ==========================================
pause
