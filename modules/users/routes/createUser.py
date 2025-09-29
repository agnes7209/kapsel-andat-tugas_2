from fastapi import APIRouter, HTTPException
from modules.users.schema.schemas import UserCreate, UserResponse, ResponseModel
import uuid
from datetime import datetime

router = APIRouter()

# Simulasi database
users_db = []

@router.post("/users", response_model=ResponseModel, status_code=201)
async def create_user(user: UserCreate):
    try:
        # Check if username already exists
        if any(u['username'] == user.username for u in users_db):
            raise HTTPException(
                status_code=400, 
                detail="Username already exists"
            )
        
        # Check if email already exists
        if any(u['email'] == user.email for u in users_db):
            raise HTTPException(
                status_code=400, 
                detail="Email already exists"
            )
        
        user_data = {
            "id": str(uuid.uuid4()),
            "username": user.username,
            "email": user.email,
            "password": user.password,  # In production, hash this!
            "role": user.role,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }
        
        users_db.append(user_data)
        
        response_data = UserResponse(**user_data)
        
        return ResponseModel(
            success=True,
            message="User created successfully",
            data=response_data
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Internal server error: {str(e)}"
        )