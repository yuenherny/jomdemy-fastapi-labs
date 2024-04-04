from fastapi import APIRouter, HTTPException, status
from typing import List
from models.events import Event
from database.connection import get_connection
from models.users import User, UserSignIn


user_router = APIRouter()
users = {}


@user_router.post("/signup")
async def signup_new_user(new_user: User) -> dict:
    conn = get_connection()
    cursor = conn.cursor()

    sql = f"SELECT * FROM user WHERE email = '{new_user.email}'"
    cursor.execute(sql)
    row = cursor.fetchone() # fetchall() [{}, {}, {}] fetchone() {}

    if row:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied email already exist"
        )
    
    sql = f"INSERT INTO user (email, title, password) VALUES('{new_user.email}', '{new_user.title}', '{new_user.password}')"
    cursor.execute(sql)
    conn.commit()

    cursor.close()
    conn.close()
    return {
        "message": "User successfully registered!"
    }    


@user_router.post("/signin")
async def signin_user(user: UserSignIn) -> dict:
    conn = get_connection()
    cursor = conn.cursor()

    sql = f"SELECT * FROM user WHERE email = '{user.email}' AND password = '{user.password}'"
    cursor.execute(sql)
    row = cursor.fetchone()

    if row:
        # this user exist
        return {"message": "Sign in successful"}
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User does not exist or incorrect password"
        )
