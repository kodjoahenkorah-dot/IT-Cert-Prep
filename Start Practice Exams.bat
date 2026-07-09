@echo off
REM One-click launcher for the practice exam app (Windows).
REM Double-click this file: it starts the server and opens your browser.
cd /d "%~dp0"
start "" /min cmd /c "timeout /t 2 >nul & start http://127.0.0.1:5000"
python app.py
pause
