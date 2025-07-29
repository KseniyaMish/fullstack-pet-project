from app.database.session import engine
from app.models.post import Post
from app.database.session import Base

def init_db():
    Base.metadata.create_all(bind=engine)
