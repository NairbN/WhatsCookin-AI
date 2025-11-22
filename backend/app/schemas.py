from pydantic import BaseModel, EmailStr
from typing import List

# Create user schema
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True

# Login schema
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Token schema
class Token(BaseModel):
    token: str

# Recipe schema
class Recipes(BaseModel):
    name: str
    ingredients: list[str] 