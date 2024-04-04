"""This file will contain the functions that will be used to encrypt the 
password of a user during sign-up and compare passwords during sign-in. 
"""
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])


class HashPassword:

    def create_hash(self, password: str) -> str:
        """Hash plain text"""
        return pwd_context.hash(secret=password)
    
    def verify_hash(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(secret=plain_password, hash=hashed_password)
