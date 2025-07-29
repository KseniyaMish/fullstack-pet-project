from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.post import Post
from app.schemas.posts import PostCreate, Post as PostResponse  # ← импорт схем

router = APIRouter()

@router.post("/", response_model=PostResponse)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    total_posts = db.query(func.count(Post.id)).scalar()

    new_post = Post(title=post.title, content=post.content)
    db.add(new_post)
    db.flush()  # получаем ID до коммита

    if total_posts >= 20:
        db.query(Post).filter(Post.id != new_post.id).delete(synchronize_session=False)

    db.commit()

    return new_post

@router.get("/")
def get_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()

