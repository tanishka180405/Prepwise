@echo off
setlocal
cd /d "%~dp0backend"

if not exist ".venv\Scripts\python.exe" (
  echo Setting up PrepWise for the first time...
  python -m venv .venv
  call .venv\Scripts\activate.bat
  python -m pip install --upgrade pip
  python -m pip install -r requirements.txt
) else (
  call .venv\Scripts\activate.bat
)

start "PrepWise" http://127.0.0.1:8765
echo PrepWise is running. Keep this window open while you use the app.
python -m uvicorn main:app --host 127.0.0.1 --port 8765
