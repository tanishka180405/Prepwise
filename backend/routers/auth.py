from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import JWTError
from pydantic import BaseModel
from typing import Optional

from database import get_db
from models.user import User
from services.auth import (
    hash_password, authenticate_user, get_user_by_email,
    create_access_token, create_refresh_token, decode_token,
)

router = APIRouter(prefix="/auth", tags=["Auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str
    college: Optional[str] = None

class RefreshRequest(BaseModel):
    refresh_token: str

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    exc = HTTPException(status_code=401, detail="Invalid or expired token")
    try:
        payload = decode_token(token)
        user_id = payload.get("sub")
        if not user_id or payload.get("type") != "access":
            raise exc
    except JWTError:
        raise exc
    user = db.query(User).filter(User.id == user_id).first()
    if not user or not user.is_active:
        raise exc
    return user

@router.post("/register", status_code=201)
def register(payload: RegisterRequest, db: Session = Depends(get_db)):
    try:
        if get_user_by_email(db, payload.email):
            raise HTTPException(status_code=409, detail="Email already registered")
        user = User(
            name=payload.name.strip(),
            email=payload.email.lower().strip(),
            hashed_password=hash_password(payload.password),
            college=payload.college,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        access = create_access_token({"sub": str(user.id)})
        refresh = create_refresh_token({"sub": str(user.id)})
        return {"access_token": access, "refresh_token": refresh, "token_type": "bearer", "user_id": str(user.id), "name": user.name, "email": user.email}
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Registration failed: {str(e)}")

@router.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    try:
        user = authenticate_user(db, form.username, form.password)
        if not user:
            raise HTTPException(status_code=401, detail="Incorrect email or password")
        access = create_access_token({"sub": str(user.id)})
        refresh = create_refresh_token({"sub": str(user.id)})
        return {"access_token": access, "refresh_token": refresh, "token_type": "bearer", "user_id": str(user.id), "name": user.name, "email": user.email}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Login failed: {str(e)}")

@router.post("/refresh")
def refresh_token(payload: RefreshRequest, db: Session = Depends(get_db)):
    try:
        data = decode_token(payload.refresh_token)
        if data.get("type") != "refresh":
            raise HTTPException(status_code=401, detail="Invalid refresh token")
        user = db.query(User).filter(User.id == data.get("sub")).first()
        if not user:
            raise HTTPException(status_code=401, detail="User not found")
        return {"access_token": create_access_token({"sub": str(user.id)}), "token_type": "bearer"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Token refresh failed: {str(e)}")

@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return {"id": str(current_user.id), "name": current_user.name, "email": current_user.email, "college": current_user.college, "questions_done": current_user.questions_done, "interview_sessions": current_user.interview_sessions, "streak_days": current_user.streak_days}