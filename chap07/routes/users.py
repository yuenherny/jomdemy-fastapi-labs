from fastapi import APIRouter, HTTPException, status, Depends
from database.connection import get_session
from models.users import User, UserSignIn
from sqlmodel import Session
from auth.hash_password import HashPassword
from fastapi.security import OAuth2PasswordRequestForm # HTML form to login
from auth.jwt_handler import create_access_token


user_router = APIRouter()


@user_router.post("/signup")
async def signup_new_user(new_user: User, session: Session = Depends(get_session)) -> dict:

    user = session.get(User, new_user.email) # session.get() finds by primary key and return an object

    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied email already exist"
        )

    hasher = HashPassword()
    hashed_password = hasher.create_hash(new_user.password)
    new_user.password = hashed_password
    session.add(new_user)
    session.commit()
    return {
        "message": "User successfully registered!"
    }  


@user_router.post("/signin")
async def signin_user(
    user_signin: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session)
) -> dict:
    
    user_exist = session.get(User, user_signin.username)

    if user_exist:
        # this user exist
        hasher = HashPassword()
        if hasher.verify_hash(user_signin.password, user_exist.password):
            access_token = create_access_token(user_signin.username)
            return {
                "message": "Sign in successful",
                "access_token": access_token,
                "token_type": "Bearer"
            }

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="User does not exist or incorrect password"
    )
