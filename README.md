# ⚡ PrepWise — DS & AI Interview Prep Platform

A full-stack interview preparation platform built for Data Science & AI B.Tech students.

## 🗂️ Project Structure

```
prepwise/
├── PrepWise.html          ← Phase 1 & 3: Complete frontend (open directly in browser)
├── docker-compose.yml     ← Phase 2: PostgreSQL + Redis setup
├── README.md
└── backend/               ← Phase 2 & 3: FastAPI backend
    ├── main.py            ← App entry point
    ├── config.py          ← Settings from .env
    ├── database.py        ← SQLAlchemy + PostgreSQL
    ├── seed.py            ← Seed 27 DSAI questions into DB
    ├── requirements.txt   ← All Python dependencies
    ├── .env.example       ← Copy to .env and fill values
    ├── models/
    │   ├── user.py        ← User table
    │   ├── question.py    ← Questions + UserQuestion tables
    │   └── interview.py   ← InterviewSession + ATSResult tables
    ├── routers/
    │   ├── auth.py        ← /auth/register, /auth/login, /auth/me
    │   ├── questions.py   ← /questions (filtered), /questions/{id}/done
    │   └── ats.py         ← /ats/check (PDF upload + scoring)
    └── services/
        ├── auth.py        ← JWT + bcrypt helpers
        └── redis_client.py← Redis connection
```

## 🚀 Quick Start

### 1. Open the Frontend
Just double-click `PrepWise.html` or open with Live Server in VS Code.

### 2. Start the Backend

**Step 1 — Copy environment file**
```bash
cd backend
cp .env.example .env
# Edit .env with your values
```

**Step 2 — Start PostgreSQL + Redis**
```bash
docker-compose up -d
```

**Step 3 — Install Python dependencies**
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

**Step 4 — Seed the database**
```bash
python seed.py
```

**Step 5 — Start the API**
```bash
uvicorn main:app --reload --port 8000
```

API runs at → http://localhost:8000
Swagger docs → http://localhost:8000/docs

## ✅ Phases Completed

| Phase | Status | What was built |
|-------|--------|---------------|
| Phase 1 | ✅ Done | Full frontend — Landing, Dashboard, Question Bank, ATS, AI Voice Interview |
| Phase 2 | ✅ Done | FastAPI backend — DB models, Docker, folder structure |
| Phase 3 | ✅ Done | Auth — JWT login, signup, logout, route protection |
| Phase 4 | 🔜 Next | Wire question bank to PostgreSQL via fetch() |
| Phase 5 | 🔜 Next | Real ATS scoring with spaCy + PyMuPDF |
| Phase 6 | 🔜 Next | Deploy to Vercel + Railway |

## 🛠️ Tech Stack

- **Frontend** — HTML, CSS, JavaScript (vanilla), Web Speech API
- **Backend** — FastAPI, Python 3.11+
- **Database** — PostgreSQL + SQLAlchemy + Alembic
- **Cache** — Redis
- **Auth** — JWT (python-jose) + bcrypt (passlib)
- **NLP** — spaCy, PyMuPDF
- **DevOps** — Docker, docker-compose

## 📬 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /auth/register | Create account |
| POST | /auth/login | Login, get JWT |
| POST | /auth/refresh | Refresh access token |
| GET  | /auth/me | Get current user |
| GET  | /questions | Get filtered questions |
| POST | /questions/{id}/done | Mark question done |
| POST | /ats/check | Upload PDF, get ATS score |
| GET  | /ats/history | Past ATS results |
| GET  | /health | Health check |

