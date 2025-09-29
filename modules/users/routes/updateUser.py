from fastapi import APIRouter, HTTPException, Header
from typing import Optional
from modules.users.schema.schemas import UserCreate, UserResponse, ResponseModel
from datetime import datetime

router = APIRouter()

# Simulasi database (harus sama dengan createUser.py)
users_db = []

@router.put("/users/{user_id}", response_model=ResponseModel)
async def update_user(
    user_id: str,
    user_update: UserCreate,
    role: str = Header(...),
    x_user_id: Optional[str] = Header(None)
):
    if role == "staff" and user_id != x_user_id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    user_index = next((i for i, u in enumerate(users_db) if u.id == user_id), None)
    if user_index is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Check duplicate username
    if any(u.username == user_update.username and u.id != user_id for u in users_db):
        raise HTTPException(status_code=400, detail="Username already exists")
    
    # Check duplicate email
    if any(u.email == user_update.email and u.id != user_id for u in users_db):
        raise HTTPException(status_code=400, detail="Email already exists")
    
    updated_user = UserResponse(
        id=user_id,
        username=user_update.username,
        email=user_update.email,
        password=user_update.password,  # In production, hash the password
        role=user_update.role,
        created_at=users_db[user_index].created_at,
        updated_at=datetime.now()
    )
    
    users_db[user_index] = updated_user
    
    return ResponseModel(
        success=True,
        message="User updated successfully",
        data=updated_user
    )