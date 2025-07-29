from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# Убедись, что этот URL соответствует твоей базе данных
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/blogdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ Вот эта функция обязательно должна быть
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
