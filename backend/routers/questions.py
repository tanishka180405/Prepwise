from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func, text
from typing import Optional, List
from pydantic import BaseModel

from database import get_db
from models.question import Question, UserQuestion
from models.user import User
from routers.auth import get_current_user

router = APIRouter(prefix="/questions", tags=["Questions"])


class QuestionOut(BaseModel):
    id: str
    text: str
    answer: str
    subject: str
    difficulty: str
    type: str
    company: str
    topic: Optional[str] = None
    done: bool = False

    class Config:
        from_attributes = True


@router.get("/my-progress")
def my_progress(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Return IDs of all questions the user has completed."""
    done_ids = db.query(UserQuestion.question_id).filter(
        UserQuestion.user_id == current_user.id,
    ).all()
    return {"done_question_ids": [str(row[0]) for row in done_ids]}


@router.get("/", response_model=List[QuestionOut])
def get_questions(
    subject: Optional[str] = Query(None),
    difficulty: Optional[str] = Query(None),
    type: Optional[str] = Query(None),
    company: Optional[str] = Query(None),
    limit: int = Query(200, le=500),
    db: Session = Depends(get_db),
):
    try:
        q = db.query(Question).filter(Question.is_active == True)

        if subject and subject != "All":
            q = q.filter(Question.subject == subject)
        if difficulty and difficulty != "All":
            q = q.filter(Question.difficulty == difficulty)
        if type and type != "All":
            q = q.filter(Question.type == type)
        if company and company.lower() not in ("any", "all"):
            q = q.filter(Question.company.ilike(f"%{company}%"))

        # RANDOM() works in both SQLite and PostgreSQL
        questions = q.order_by(text("RANDOM()")).limit(limit).all()

        return [
            QuestionOut(
                id=str(ques.id),
                text=ques.text,
                answer=ques.answer,
                subject=ques.subject,
                difficulty=ques.difficulty,
                type=ques.type,
                company=ques.company or "Any",
                topic=ques.topic or "",
            )
            for ques in questions
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch questions: {str(e)}")


@router.post("/{question_id}/done", status_code=200)
def mark_done(
    question_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    existing = db.query(UserQuestion).filter(
        UserQuestion.user_id == current_user.id,
        UserQuestion.question_id == question_id,
    ).first()

    if existing:
        db.delete(existing)
        current_user.questions_done = max(0, current_user.questions_done - 1)
        db.commit()
        return {"done": False, "message": "Unmarked"}
    else:
        uq = UserQuestion(user_id=current_user.id, question_id=question_id)
        db.add(uq)
        current_user.questions_done += 1
        db.commit()
        return {"done": True, "message": "Marked as done"}