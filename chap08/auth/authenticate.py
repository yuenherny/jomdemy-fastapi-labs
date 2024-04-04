""" This file will contain the authenticate dependency, which will be 
injected into our routes to enforce authentication and authorization.

This function will protect all nodes / routes.
"""
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from auth.jwt_handler import verify_access_token


# login path is "/user/signin"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/signin")

async def authenticate(token: str = Depends(oauth2_scheme)) -> str:
    if not token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Please sign in for access"
        )
    
    decoded_token = verify_access_token(token)
    return decoded_token.get("user")
