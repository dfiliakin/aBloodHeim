from sqlalchemy.orm import Session
from .model import User
from .schema import UserCreate


def get_user_by_login(db: Session, login: str) -> User:
    return db.query(User).filter(User.login == login).first()


def create_user(db: Session, user: UserCreate):
    db_user = User(
        login=user.login,
        name=user.name,
        password=user.password,  # Hash before storing in production
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
