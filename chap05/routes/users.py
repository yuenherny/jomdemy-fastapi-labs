from fastapi import APIRouter, HTTPException, status
from typing import List
from models.events import Event
from models.users import User, UserSignIn


user_router = APIRouter()
users = {}


@user_router.post("/signup")
async def signup_new_user(new_user: User) -> dict:
    if new_user.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied email already exist"
        )
    users[new_user.email] = new_user
    return {
        "message": "User successfully registered!"
    }


@user_router.post("/signin")
async def signin_user(user: UserSignIn) -> dict:
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User does not exist"
        )
    
    if user.password != users[user.email].password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Incorrect credentials"
        )
    
    return {
        "message": "Sign in successful"
    }