from fastapi import APIRouter, Depends, HTTPException
from app.schemas.users import User
from app.dependencies import get_current_user

router = APIRouter()

fake_users_db = [
    {"id": i, "username": f"user{i}", "email": f"user{i}@example.com"} for i in range(1, 11)
]

@router.get("/", response_model=list[User])
def get_users(user: str = Depends(get_current_user)):
    return fake_users_db
