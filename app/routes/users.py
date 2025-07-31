from fastapi import APIRouter, Depends
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.users import User
from app.models.user import User as UserModel
from app.database.session import get_db
from app.dependencies import get_current_user

router = APIRouter()

@router.get("/", response_model=list[User])
def get_users(user=Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(UserModel).all()
