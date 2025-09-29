from fastapi import FastAPI
from modules.users.routes import createUser, readUser, updateUser, deleteUser

app = FastAPI(title="Users CRUD API")

app.include_router(createUser.router, tags=["Create"])
app.include_router(readUser.router, tags=["Read"])
app.include_router(updateUser.router, tags=["Update"])
app.include_router(deleteUser.router, tags=["Delete"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)