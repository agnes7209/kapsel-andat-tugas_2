from fastapi import APIRouter, HTTPException, Header
from modules.users.schema.schemas import ResponseModel
from modules.users.routes.createUser import users_db

router = APIRouter()

@router.delete("/users/{user_id}", response_model=ResponseModel)
async def delete_user(
    user_id: str, 
    role: str = Header(...)
):
    if role != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")

    user_index = next((i for i, u in enumerate(users_db) if u['id'] == user_id), None)
    if user_index is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    deleted_user = users_db.pop(user_index)
    
    response_data = UserResponse(**deleted_user)

    return ResponseModel(
        success=True,
        message="User deleted successfully",
        data=response_data
    )