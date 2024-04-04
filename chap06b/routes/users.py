from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from models.events import Event
from database.connection import get_session
from models.users import User, UserSignIn
from sqlmodel import Session, select, delete


user_router = APIRouter()


@user_router.post("/signup")
async def signup_new_user(new_user: User, session: Session = Depends(get_session)) -> dict:

    user = session.get(User, new_user.email) # session.get() finds by primary key and return an object

    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied email already exist"
        )

    session.add(new_user)
    session.commit()
    return {
        "message": "User successfully registered!"
    }  


@user_router.post("/signin")
async def signin_user(user_signin: UserSignIn, session: Session = Depends(get_session)) -> dict:
    
    user = session.get(User, user_signin.email)

    if user and user.password == user_signin.password:
        # this user exist
        return {"message": "Sign in successful"}

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="User does not exist or incorrect password"
    )
