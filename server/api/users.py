import logging
from fastapi import APIRouter, Depends, HTTPException
from repository.db import get_db
from repository.user.crud import create_user, get_user_by_login
from repository.user.schema import UserCreate, UserResponse
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/v0/users", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):

    existing_user = get_user_by_login(db, user.login)
    if existing_user:
        raise HTTPException(status_code=400, detail="Login already exists")

    return create_user(db, user)


@router.get("/v0/users/{login}", response_model=UserResponse)
def get_user(login: str, db: Session = Depends(get_db)):

    user = get_user_by_login(db=db, login=login)
    logging.error(f"!!! {user}")
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user
