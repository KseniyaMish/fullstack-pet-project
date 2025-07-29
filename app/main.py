from fastapi import FastAPI

# Роуты
from app.routes import auth, users, posts_db

# Инициализация приложения
app = FastAPI()

# Подключение роутеров
app.include_router(auth.router, prefix="/auth")
app.include_router(users.router, prefix="/users")
app.include_router(posts_db.router, prefix="/posts-db", tags=["Posts with DB"])

# Инициализация базы данных
from app.database.init_db import init_db
init_db()
