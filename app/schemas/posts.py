from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str
    content: str

class Post(PostCreate):
    id: int
    user_id: int

    class Config:
        from_attributes = True
