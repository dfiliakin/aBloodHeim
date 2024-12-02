from datetime import datetime, timedelta, timezone

from config import ACCESS_TOKEN_EXPIRE_MINUTES, HASHING_ALGORITHM, SECRET_KEY
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext

from repository.user.crud import get_user_by_login
from repository.db import get_db
from sqlalchemy.orm import Session


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")
router = APIRouter()

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Utility functions
# FIXME: Use hash!
def verify_password(plain_password, hashed_password):
    return plain_password == hashed_password


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(login: str, password: str):
    user = get_user_by_login(db=next(get_db()), login=login)
    actual_user_password = user.password if user else None
    is_password_verified = verify_password(password, actual_user_password)
    if not user or not is_password_verified:
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=HASHING_ALGORITHM)


# API Endpoints
@router.post("/v0/auth/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Handle login and return a JWT.
    """

    # DEBUG
    if form_data.username == "test":
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": "test"}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}

    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.name}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}
