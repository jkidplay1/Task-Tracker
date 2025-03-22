from fastapi import APIRouter, HTTPException
from task_tracker.business.auth_service import register_user, login_user
from task_tracker.data.user_model import User

router = APIRouter()

@router.post("/register")
def register(user: User):
    response = register_user(user)
    if "error" in response:
        raise HTTPException(status_code=400, detail=response["error"])
    return response

@router.post("/login")
def login(email: str, password: str):
    response = login_user(email, password)
