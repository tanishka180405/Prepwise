from sqlalchemy import Column, String, Text, Boolean, DateTime, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

from database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    text = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)

    # Categorisation
    subject = Column(String(20), nullable=False, index=True)
    # ML | DL | DSA | Python | Stats | NLP | CV

    difficulty = Column(String(10), nullable=False, index=True)
    # Easy | Medium | Hard

    type = Column(String(20), nullable=False)
    # Conceptual | Coding | HR

    company = Column(String(100), default="Any")
    topic = Column(String(100), nullable=True)

    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class UserQuestion(Base):
    """Tracks which questions a user has marked as done."""
    __tablename__ = "user_questions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id", ondelete="CASCADE"), nullable=False)
    done = Column(Boolean, default=True)
    marked_at = Column(DateTime(timezone=True), server_default=func.now())
