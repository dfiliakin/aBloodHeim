from api import auth
from api import users
from config import ALLOWED_ORIGINS, HASHING_ALGORITHM, SECRET_KEY
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
import uvicorn

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="v0/auth/login")

app = FastAPI()

# CORS setup to allow requests from FE
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth.router)
app.include_router(users.router)


@app.get("/v0/test")
async def test_endpoint(token: str = Depends(oauth2_scheme)):
    """Protected endpoint"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[HASHING_ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"message": "Access granted", "username": username}

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")


if __name__ == "__main__":

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8080,
        ssl_keyfile="key.pem",
        ssl_certfile="cert.pem",
    )
