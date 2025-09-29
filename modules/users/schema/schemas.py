import re
import uuid
from enum import Enum
from datetime import datetime
from typing import Optional
#pip install email-validator
from pydantic import BaseModel, Field, EmailStr, validator

class RoleEnum(str, Enum):
    admin = "admin"
    staff = "staff"

class UserCreate(BaseModel):
    username: str = Field(
        ...,
        min_length=6,
        max_length=15,
        pattern=r'^[a-z0-9]+$',
        description='must be lowercase alphanumeric'
    )
    email: EmailStr = Field(..., description='must be a valid email address')
    password: str = Field(..., min_length=8, max_length=20)
    role: RoleEnum

    @validator('username')
    def validate_username(cls, v):
        if not v.islower():
            raise ValueError('username must be lowercase')
        if not re.match(r'^[a-z0-9]+$', v):
            raise ValueError('username must be alphanumeric')
        return v

    @validator('password')
    def validate_password(cls, v):
        errors = []
        if len(v) < 8 or len(v) > 20:
            errors.append('must be between 8 and 20 characters')
        if not re.search(r'[A-Z]', v):
            errors.append('must contain at least one uppercase letter')
        if not re.search(r'[a-z]', v):
            errors.append('must contain at least one lowercase letter')
        if not re.search(r'[0-9]', v):
            errors.append('must contain at least one digit')
        if not re.search(r'[!@]', v):
            errors.append('must contain at least one special character (! or @)')
        if not re.match(r'^[A-Za-z0-9!@]+$', v):
            errors.append('can only contain alphanumeric characters and ! or @')
        
        if errors:
            raise ValueError('Password ' + ', '.join(errors))
        return v

class UserResponse(BaseModel):
    id: str
    username: str
    email: str
    role: RoleEnum
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class ResponseModel(BaseModel):
    success: bool
    message: str
    data: Optional[UserResponse] = None