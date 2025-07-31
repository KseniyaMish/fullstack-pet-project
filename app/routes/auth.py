from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.database.session import get_db
from app.routes.posts_db import router
from app.schemas.auth import LoginSchema


@router.post("/login", response_model=None)
def login(data: LoginSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == data.username).first()
    if not user or user.hashed_password != data.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = user.username  # временно
    return {"access_token": token, "token_type": "bearer"}
