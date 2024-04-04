""" This file will contain the functions required to encode and decode 
the JWT strings.
"""
import time
from datetime import datetime
from fastapi import HTTPException, status
from jose import jwt, JWTError

def create_access_token(user: str) -> str:
    payload = {
        "user": user,
        "expire": time.time() + 3600
    }
    return jwt.encode(payload, key="secret", algorithm="HS256")


def verify_access_token(token: str) -> bool:
    try:
        decoded_token = jwt.decode(token, key="secret", algorithms=["HS256"])
        expiry = decoded_token.get("expire")

        if expiry is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No access token"
            )
        
        if datetime.utcnow() > datetime.utcfromtimestamp(expiry):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid token"
            )
        
        return decoded_token
    except JWTError:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid token"
            )
