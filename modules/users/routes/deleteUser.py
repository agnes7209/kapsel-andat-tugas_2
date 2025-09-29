from fastapi import APIRouter, HTTPException, Query
from modules.users.schema.schemas import ResponseModel
from modules.users.routes.createUser import users_db

router = APIRouter()

@router.delete("/users/{username}", response_model=ResponseModel)
def delete_user(username: str, requester_role: str = Query(...)):
    if requester_role != "admin":
        raise HTTPException(status_code=403, detail="Only admin can delete users")

    for idx, u in enumerate(users_db):
        if u.username == username:
            deleted_user = users_db.pop(idx)
            return ResponseModel(success=True, message="User deleted successfully", data=deleted_user)

    raise HTTPException(status_code=404, detail="User not found")