# 🧪 Fullstack Pet Project — FastAPI + PostgreSQL + Autotests + Allure

Проект для отработки end-to-end тестирования и построения API с использованием реальной базы данных PostgreSQL и автотестов с отчетностью в Allure.

---

## ⚙️ Стек технологий

- **FastAPI** — REST API backend
- **PostgreSQL** — база данных
- **SQLAlchemy** — ORM-слой
- **Pytest** — фреймворк автотестов
- **Allure** — отчётность и шаги тестирования
- **Uvicorn** — ASGI-сервер
- **pgAdmin** — графический интерфейс к PostgreSQL

---

## 📁 Структура проекта

fullstack_pet_project/
├── app/
│ ├── database/ # Подключение к PostgreSQL
│ ├── models/ # SQLAlchemy-модели
│ ├── routes/ # API эндпоинты (auth, users, posts_db)
│ └── main.py # Точка входа
├── tests/ # Pytest-тесты
├── utils/ # Allure-шаги и вспомогательные функции
├── requirements.txt
├── README.md # Документация


---

## 🚀 Как запустить проект

### 1. 📥 Установить зависимости

```bash
pip install -r requirements.txt
⚠️ Если используешь виртуальное окружение (venv), не забудь активировать:

bash
Копировать
Редактировать
venv\Scripts\activate  # Windows

2. 🧑‍💻 Убедиться, что PostgreSQL установлен
Создай базу данных blogdb, используя pgAdmin или вручную:

sql
Копировать
Редактировать
CREATE DATABASE blogdb;

3. 🟢 Запустить backend
bash
Копировать
Редактировать
uvicorn app.main:app --reload

Открой Swagger-документацию:
http://localhost:8000/docs

🔗 Основные эндпоинты
Метод	Путь	Описание
POST	/auth/login	Авторизация, возвращает токен
GET	/users/	Список из 10 предсозданных пользователей
GET	/posts-db/	Получить список всех постов
POST	/posts-db/	Создать пост; при превышении 20 — очищает базу, оставляя последний

🧪 Как запускать тесты
Стандартный запуск:
bash
Копировать
Редактировать
pytest tests/

С Allure-отчётом:
bash
Копировать
Редактировать

pytest tests/ --alluredir=allure-results
allure serve allure-results
📌 Не забудь добавить файл tests/conftest.py, если возникают проблемы с импортами:

python
Копировать
Редактировать
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


❓ Тест "зависает"
✅ Проверь:

Запущен ли FastAPI (uvicorn)

Добавлены ли timeout=5 в requests.post() / get()

Используй Ctrl+C или закрой терминал

❓ Таблица пустая, данные не сохраняются
➡️ Убедись, что:

PostgreSQL запущен

blogdb создана

Миграция проходит (init_db() вызывается в main.py)

Таблица posts реально создаётся (проверь в pgAdmin)

✨ Особенности логики
После 20 постов таблица автоматически очищается, и остаётся только последний созданный.

Тест test_cleanup_after_20_posts() проверяет это поведение шаг за шагом с отчётом в Allure.

Все тесты используют allure.step, attach_response, assert с текстами — ничего лишнего в терминал не выводится.

📌 Авторизация
На все защищённые эндпоинты (/users, /posts-db) требуется токен:

Вызови POST /auth/login

Получи токен: "access_token": "valid_token"

Передавай в заголовке:

makefile
Копировать
Редактировать
Authorization: Bearer valid_token
🧹 Планы и идеи для расширения
Подключить Alembic для миграций

Добавить модели User, Comment

Настроить docker-compose для полноценного запуска

Разделить тесты на уровни: unit, integration, E2E