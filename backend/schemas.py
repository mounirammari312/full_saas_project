from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

class UserCreate(BaseModel):
    email: str
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    email: str
    username: str
    is_active: bool
    class Config:
        from_attributes = True

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: Optional[str] = "medium"

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    priority: Optional[str] = None

class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    priority: str
    created_at: datetime
    owner_id: int
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str