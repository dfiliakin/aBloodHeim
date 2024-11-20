from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from config import ALLOWED_ORIGINS

app = FastAPI()

# CORS setup to allow requests from FE
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/v1/test")
async def test_endpoint():
    return {"message": "Hello from FastAPI!"}


# Pydantic model to parse the login request body
class LoginRequest(BaseModel):
    username: str
    password: str


@app.post("/v1/login")
async def login(request: LoginRequest):
    # Simple validation (replace with real validation logic, e.g. checking against a database)
    if request.username == "admin" and request.password == "password":
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")
