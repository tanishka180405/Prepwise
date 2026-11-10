# PrepWise — DS & AI Interview Preparation

PrepWise is a full-stack interview-preparation platform for Data Science and AI students. It includes a 500+ question bank, Aria voice interview practice, an ATS resume checker, authentication, and per-user performance tracking.

---

## 🚀 Live Deployment Guide

Deploy PrepWise live in 3 steps:

### Step 1: Upload to GitHub

1. Create a new repository on [GitHub](https://github.com/new) (e.g. `prepwise`).
2. In this folder (`PrepWise-GitHub-Ready`), run:

```powershell
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/prepwise.git
git push -u origin main
```

---

### Step 2: Deploy Backend (Render — Free)

1. Sign up / Log in to [Render.com](https://render.com).
2. Click **New +** → **Web Service**.
3. Connect your GitHub repository (`prepwise`).
4. Set the following fields:
   - **Name**: `prepwise-backend` (or your choice)
   - **Root Directory**: `backend`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install --upgrade pip && pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Instance Type**: `Free`
5. In **Environment Variables**, add:
   - `PYTHON_VERSION` = `3.11.9`
   - `SECRET_KEY` = (click generate or enter a 32+ character random secret)
   - `FRONTEND_URL` = `https://your-frontend.vercel.app` (or `*`)
6. Click **Create Web Service**.
7. Once deployed, copy your backend URL (e.g. `https://prepwise-backend-xxxx.onrender.com`).

*(Note: Render automatically creates and seeds the database on initial boot!)*

---

### Step 3: Deploy Frontend (Vercel — Free)

1. Log in to [Vercel](https://vercel.com).
2. Click **Add New...** → **Project**.
3. Import your GitHub repository (`prepwise`).
4. In Project Settings:
   - **Framework Preset**: `Other`
   - **Root Directory**: `./` (leave default)
   - **Build Command**: (leave empty)
   - **Output Directory**: (leave empty)
5. Click **Deploy**.
6. You will get a live URL (e.g. `https://prepwise.vercel.app`).

#### Connecting Frontend to your Live Backend:
- If your Render backend is named `prepwise-backend.onrender.com`, it connects automatically!
- If your backend URL has a different name, open your live frontend website, open Developer Console (F12), and run:
  ```javascript
  setBackendUrl("https://your-backend-url.onrender.com");
  ```
  Or pass your backend URL once via query parameter / local storage `pw_api_url`.

---

## 💻 Run Locally on Windows

1. Install Python 3.11 or later from [python.org](https://www.python.org/downloads/) (enable **Add Python to PATH**).
2. Double-click `start_prepwise.bat` in this project folder.
3. The launcher will set up the virtual environment, install dependencies, seed the database, and launch `http://127.0.0.1:8765`.

---

## 📁 Project Structure

```
PrepWise-GitHub-Ready/
├── index.html             # Production frontend entry point
├── PrepWise.html          # Frontend UI application
├── vercel.json            # Vercel deployment configuration
├── render.yaml            # Render infrastructure as code
├── start_prepwise.bat     # Windows one-click local launcher
├── README.md              # Project documentation & deployment guide
└── backend/
    ├── main.py            # FastAPI main application & CORS setup
    ├── seed.py            # 500+ interview questions seed bank
    ├── database.py        # SQLAlchemy SQLite / PostgreSQL engine
    ├── config.py          # App settings & JWT configuration
    ├── build.sh           # Cloud build script
    ├── routers/           # Auth, questions, ATS, dashboard APIs
    ├── models/            # User, Question, Interview database models
    ├── services/          # Auth & password hashing services
    └── requirements.txt   # Lean Python dependencies
```

---

## 🌟 Main Features

- **500+ Questions**: ML, DL, DSA, Python, Statistics, NLP, and Computer Vision questions with model answers.
- **Aria Voice Interviewer**: Realistic voice interview practice with shuffled questions and detailed feedback.
- **ATS Resume Checker**: Skills extraction, scoring, and resume optimization tips.
- **Analytics & Dashboard**: Track completed questions, scores, and interview performance over time.
