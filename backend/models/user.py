from sqlalchemy import Column, String, Boolean, DateTime, Integer, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)

    # Profile
    college = Column(String(200), nullable=True)
    domain = Column(String(50), default="DSAI")    # always DSAI for PrepWise

    # Progress tracking
    questions_done = Column(Integer, default=0)
    interview_sessions = Column(Integer, default=0)
    streak_days = Column(Integer, default=0)
    last_active = Column(DateTime(timezone=True), nullable=True)

    # Flags
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<User {self.email}>"
