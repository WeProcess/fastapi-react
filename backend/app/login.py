from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from models.schema import TokenData, UserInDB
from models.models import *
from database.dependency import db_dependency
from fastapi.security import OAuth2PasswordBearer
from scurity.scurity import ALGORITHM, SECRET_KEY, verify_password

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/login")


def get_user(db, email: str):
    user_data = db.query(User).filter(User.email==email).first()
    return user_data
    

def authenticate_user(db, email: str, password: str):
    user = get_user(db, email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
    
async def get_current_user(db: db_dependency, token: str = Depends(oauth2_schema)):
    credential_exception= HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                        detail="Could not validate credentials", headers={"WWW-Authenthenticate": "Berar"})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credential_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credential_exception
    
    user = get_user(db, email=token_data.email)
    if user is None:
        raise credential_exception
    return user


async def get_current_active_user(current_user: UserInDB = Depends(get_current_user)): 
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user.valuefile()