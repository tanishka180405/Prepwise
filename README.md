# PrepWise — DS & AI Interview Preparation

PrepWise is a full-stack interview-preparation app for Data Science and AI students. It includes a 500+ question bank, Aria voice interview practice, a resume checker, authentication, and per-user performance tracking.

## Run locally on Windows

1. Install Python 3.11 or later from [python.org](https://www.python.org/downloads/). During installation, enable **Add Python to PATH**.
2. Double-click `start_prepwise.bat` in this project folder.
3. The first launch creates a local Python environment and installs dependencies. It then opens the app at `http://127.0.0.1:8765`.
4. Keep the command window open while using PrepWise.

No Docker is required. The backend uses the included SQLite database (`backend/prepwise.db`) and automatically seeds missing questions at startup.

> Use `start_prepwise.bat` instead of opening `PrepWise.html` directly. It starts the API required for the question bank and then opens the correct local URL.

## Project structure

```
PrepWise-GitHub-Ready/
├── PrepWise.html          # Frontend UI
├── index.html             # Deployment redirect
├── start_prepwise.bat     # One-click Windows launcher
├── README.md
└── backend/
    ├── main.py            # FastAPI application
    ├── seed.py            # 500+ interview questions
    ├── prepwise.db        # Local SQLite database
    ├── routers/           # Auth, questions, ATS, dashboard APIs
    └── requirements.txt
```

## GitHub upload

Create an empty repository on GitHub, then in this folder run:

```powershell
git init
git add .
git commit -m "Add PrepWise interview-prep application"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

The private `.env` file and generated Python virtual environment are intentionally not included. Copy `backend/.env.example` to `backend/.env` only if you need to customize settings.

## Main features

- 500+ conceptual, coding, situational, and HR questions across ML, DL, DSA, Python, Statistics, NLP, and Computer Vision.
- Aria voice interviews with shuffled questions, answer feedback, and an interview report.
- Resume analysis with transparent, skills-focused guidance.
- User-specific question progress and interview dashboard.
