from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from task_tracker.business.auth_service import register_user, authenticate_user

router = APIRouter()

class UserRegister(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/register")
def register(user: UserRegister):
    success = register_user(user.username, user.password)
    if not success:
        raise HTTPException(status_code=400, detail="Username already exists")
    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: UserLogin):
    token = authenticate_user(user.username, user.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"access_token": token, "token_type": "bearer"}
