from fastapi import APIRouter, HTTPException, Header
from typing import List, Optional
from modules.users.schema.schemas import UserResponse, ResponseModel

router = APIRouter()

# Simulasi database (harus sama dengan createUser.py)
users_db = []

def verify_admin(role: str):
    if role != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")

@router.get("/users", response_model=ResponseModel)
async def read_all_users(role: str = Header(...)):
    verify_admin(role)
    
    return ResponseModel(
        success=True,
        message="Users retrieved successfully",
        data=users_db
    )

@router.get("/users/{user_id}", response_model=ResponseModel)
async def read_user(
    user_id: str,
    role: str = Header(...),
    x_user_id: Optional[str] = Header(None)
):
    user = next((u for u in users_db if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if role == "staff" and user.id != x_user_id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    return ResponseModel(
        success=True,
        message="User retrieved successfully",
        data=user
    )