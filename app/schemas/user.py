from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=150)
    email: EmailStr
    password: str = Field(min_length=2, max_length=120)

class UserResponse(BaseModel):
    model_config = ConfigDict(from_atrributes=True)

    id: UUID
    name:str
    is_active:bool
    created_at: datetime
    updated_at: datetime