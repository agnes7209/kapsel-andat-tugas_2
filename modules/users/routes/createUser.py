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
        # Mengecek apakah username sudah ada di database
        if any(u['username'] == user.username for u in users_db):
            raise HTTPException(
                status_code=400, 
                detail="Username already exists"
            )
        
        # Mengecek apakah email sudah ada di database
        if any(u['email'] == user.email for u in users_db):
            raise HTTPException(
                status_code=400, 
                detail="Email already exists"
            )
        
        # Berisi data input user dan response otomatis yang ditentukan 
        user_data = {
            "id": str(uuid.uuid4()),
            "username": user.username,
            "email": user.email,
            "password": user.password,  
            "role": user.role,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }
        
        # Memasukkan data input user ke database sementara
        users_db.append(user_data)
        
        # Input user akan dipetakan dengan parameter UserResponse di schemas.py
        response_data = UserResponse(**user_data)
        
        # Output setelah user membuat akun 
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