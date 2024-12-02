from pydantic import BaseModel


class UserBase(BaseModel):
    login: str
    name: str


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True
