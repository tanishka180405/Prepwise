from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager
import os

from config import settings
from database import engine, Base

import models  # noqa: F401

from routers import auth, questions, ats


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

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8000",
        "http://localhost:5500",
        "http://127.0.0.1:5500",
        settings.FRONTEND_URL,
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(questions.router)
app.include_router(ats.router)

# Serve PrepWise.html from one folder above backend/
HTML_FILE = os.path.join(os.path.dirname(__file__), "..", "PrepWise.html")

@app.get("/", tags=["Frontend"])
def serve_frontend():
    if os.path.exists(HTML_FILE):
        return FileResponse(HTML_FILE, media_type="text/html")
    return {"error": "PrepWise.html not found. Place it one folder above backend/."}

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "app": settings.APP_NAME}
