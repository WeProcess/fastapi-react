from fastapi import HTTPException, status
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "karmaglo$§%§$baltech"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") 

COOKIE_NAME = "Authorization"

def verify_password(plain_password, hash_password):
    return pwd_context.verify(plain_password, hash_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta or None = None): # type: ignore
    credential_exception= HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                        detail="Could not validate credentials", headers={"WWW-Authenthenticate": "Berar"})
    try:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta    
        else:
            expire = datetime.utcnow() + timedelta(minutes=1)

        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    except JWTError:
        raise credential_exception
    
    return encoded_jwt