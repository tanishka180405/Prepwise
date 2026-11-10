from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager
import os

from config import settings
from database import engine, Base

import models  # noqa: F401

from routers import auth, questions, ats, dashboard


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)

    # Add any newly shipped seed questions without removing a user's existing data.
    from database import SessionLocal
    from models.question import Question
    db = SessionLocal()
    try:
        from seed import QUESTIONS
        existing_texts = {text for (text,) in db.query(Question.text).all()}
        new_questions = [q for q in QUESTIONS if q["text"] not in existing_texts]
        if new_questions:
            db.add_all([Question(**q) for q in new_questions])
            db.commit()
            print(f"Added {len(new_questions)} question(s); {len(QUESTIONS)} available in the seed bank.")
        else:
            print(f"Question bank is current ({len(existing_texts)} questions).")
    except Exception as e:
        print(f"Auto-seed failed: {e}")
        db.rollback()
    finally:
        db.close()

    print(f"PrepWise API started - {settings.APP_NAME} v{settings.APP_VERSION}")
    yield
    print("PrepWise API shutting down.")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Backend API for PrepWise — DS & AI interview prep platform",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

frontend_origins = [
    origin.strip()
    for origin in settings.FRONTEND_URL.split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "null",  # permits opening PrepWise.html directly from File Explorer
        "http://localhost:8000",
        "http://localhost:5500",
        "http://localhost:8765",
        "http://127.0.0.1:5500",
        "http://127.0.0.1:8765",
        *frontend_origins,
    ],
    allow_origin_regex=r"^https?://.*$",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(questions.router)
app.include_router(ats.router)
app.include_router(dashboard.router)

# Serve Frontend (PrepWise.html or index.html)
BASE_DIR = os.path.dirname(__file__)
HTML_FILE = os.path.join(BASE_DIR, "..", "PrepWise.html")
INDEX_FILE = os.path.join(BASE_DIR, "..", "index.html")

@app.get("/", tags=["Frontend"])
def serve_frontend():
    for f in (HTML_FILE, INDEX_FILE):
        if os.path.exists(f):
            return FileResponse(f, media_type="text/html")
    return {"error": "Frontend HTML file not found."}

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "app": settings.APP_NAME}
