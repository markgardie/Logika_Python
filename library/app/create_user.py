from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import User, Base
from app.auth import get_password_hash

Base.metadata.create_all(bind=engine)

def create_initial_user(db: Session, login: str, password: str):
    # Перевірка, чи вже існує користувач
    existing_user = db.query(User).filter(User.login == login).first()
    if existing_user:
        print(f"Користувач {login} вже існує!")
        return
    
    # Створення користувача з хешованим паролем
    hashed_password = get_password_hash(password)
    new_user = User(login=login, password=hashed_password)
    db.add(new_user)
    db.commit()
    print(f"Користувач {login} успішно створений!")

if __name__ == "__main__":
    db = SessionLocal()
    create_initial_user(db, "admin", "secretpassword")
    db.close()