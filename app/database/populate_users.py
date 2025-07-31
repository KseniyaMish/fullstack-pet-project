import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from app.database.session import SessionLocal
from app.database.init_db import init_db
from app.models.user import User

def populate():
    init_db()

    db = SessionLocal()

    existing_users = db.query(User).count()
    if existing_users >= 10:
        db.close()
        return

    for i in range(1, 11):
        user = User(
            username=f"user{i}",
            email=f"user{i}@example.com",
            hashed_password="hashed_password"
        )
        db.add(user)
    db.commit()
    db.close()

if __name__ == "__main__":
    populate()
