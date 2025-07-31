from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from typing import List

from app.database.session import get_db
from app.dependencies import get_current_user
from app.models.post import Post
from app.models.user import User
from app.schemas.posts import PostCreate, Post as PostResponse  # схемы для валидации

router = APIRouter()


@router.post("/", response_model=PostResponse)
def create_post(
    post: PostCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    total_posts = db.query(func.count(Post.id)).scalar()

    new_post = Post(
        title=post.title,
        content=post.content,
        user_id=current_user.id
    )

    db.add(new_post)
    db.flush()  # получаем ID до коммита

    if total_posts >= 20:
        db.query(Post).filter(Post.id != new_post.id).delete(synchronize_session=False)

    db.commit()
    db.refresh(new_post)

    return new_post


@router.get("/", response_model=List[PostResponse])
def get_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()
