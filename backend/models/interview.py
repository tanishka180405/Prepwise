from sqlalchemy import Column, String, Text, Integer, Float, DateTime, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

from database import Base


class InterviewSession(Base):
    __tablename__ = "interview_sessions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=True, index=True)

    subject = Column(String(20), nullable=False)   # ML, DL, DSA, etc.
    company = Column(String(100), default="Any")
    duration_minutes = Column(Integer, default=10)

    # Scores (0–100)
    overall_score = Column(Float, nullable=True)
    technical_score = Column(Float, nullable=True)
    communication_score = Column(Float, nullable=True)
    depth_score = Column(Float, nullable=True)

    # Full conversation log stored as JSON list
    conversation = Column(JSON, default=list)

    completed = Column(String(10), default="pending")  # pending | done | abandoned
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class ATSResult(Base):
    __tablename__ = "ats_results"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)

    filename = Column(String(255), nullable=True)
    overall_score = Column(Float, nullable=False)
    skills_score = Column(Float, nullable=False)
    formatting_score = Column(Float, nullable=False)
    keyword_score = Column(Float, nullable=False)

    found_keywords = Column(JSON, default=list)
    missing_keywords = Column(JSON, default=list)
    suggestions = Column(JSON, default=list)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
