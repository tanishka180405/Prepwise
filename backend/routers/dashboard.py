from datetime import date, datetime, timezone
from typing import List

from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from database import get_db
from models.interview import InterviewSession
from models.question import Question, UserQuestion
from models.user import User
from routers.auth import get_current_user

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


class InterviewResultIn(BaseModel):
    subject: str = Field(min_length=1, max_length=20)
    overall_score: float = Field(ge=0, le=100)
    technical_score: float = Field(ge=0, le=100)
    communication_score: float = Field(ge=0, le=100)
    depth_score: float = Field(ge=0, le=100)
    duration_minutes: int = Field(default=0, ge=0, le=120)
    conversation: List[dict] = Field(default_factory=list)


def update_streak(user: User) -> None:
    today = date.today()
    previous = user.last_active.date() if user.last_active else None
    if previous == today:
        return
    user.streak_days = (user.streak_days or 0) + 1 if previous and (today - previous).days == 1 else 1
    user.last_active = datetime.now(timezone.utc)


@router.post("/interviews")
def save_interview(payload: InterviewResultIn, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    session = InterviewSession(
        user_id=current_user.id, subject=payload.subject, duration_minutes=payload.duration_minutes,
        overall_score=payload.overall_score, technical_score=payload.technical_score,
        communication_score=payload.communication_score, depth_score=payload.depth_score,
        conversation=payload.conversation, completed="done",
    )
    db.add(session)
    current_user.interview_sessions = (current_user.interview_sessions or 0) + 1
    update_streak(current_user)
    db.commit()
    return {"saved": True, "id": str(session.id)}


@router.get("/summary")
def dashboard_summary(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    sessions = db.query(InterviewSession).filter(
        InterviewSession.user_id == current_user.id, InterviewSession.completed == "done"
    ).order_by(InterviewSession.created_at.desc()).limit(5).all()
    completed_questions = db.query(UserQuestion, Question).join(Question, Question.id == UserQuestion.question_id).filter(
        UserQuestion.user_id == current_user.id
    ).order_by(UserQuestion.marked_at.desc()).limit(5).all()
    activities = [
        {"kind": "interview", "label": f"AI interview - {item.subject}", "value": f"Score: {round(item.overall_score or 0)}/100"}
        for item in sessions
    ] + [
        {"kind": "question", "label": f"Completed: {question.subject} - {question.topic or 'Practice question'}", "value": "Done"}
        for _, question in completed_questions
    ]
    latest = sessions[0] if sessions else None
    return {
        "questions_done": current_user.questions_done or 0,
        "interview_sessions": current_user.interview_sessions or 0,
        "streak_days": current_user.streak_days or 0,
        "latest_interview_score": round(latest.overall_score) if latest and latest.overall_score is not None else None,
        "latest_interview_subject": latest.subject if latest else None,
        "activities": activities[:5],
    }
