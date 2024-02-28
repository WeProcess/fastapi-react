from fastapi import FastAPI, Request, Form, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from database.database import engine
from database.dependency import db_dependency
from models import models, schema
from app import userTeam, userType, user, matrix, email
from .login import *
from scurity.scurity import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, COOKIE_NAME
from datetime import timedelta


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

models.Base.metadata.create_all(bind=engine)

# @app.get("/")
# async def root(): 
#     return {"Hi Avinash Sane"}

################# Login #################
@app.post("/login", tags=["Login"])
async def login(db: db_dependency, form_data: OAuth2PasswordRequestForm = Depends()): 
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Incorrect username or password", headers ={"WWW-Authenticate": "Berar"})
    access_token_expires= timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) 
    
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires)
    # print(access_token)
    return {"access_token": access_token, "token_type": "bearer"}

################# userTeam #################
@app.get("/dashboard", tags=["Dashboard"])
async def getdashboard(db: db_dependency, current_user: User = Depends(get_current_active_user)):
    return {"current_user" : current_user}

################# userTeam #################
@app.get("/getUserTeam", tags=["User Team"])
async def getUserTeam(db: db_dependency): #, current_user: User = Depends(get_current_active_user)):
    return userTeam.getUserTeam(db)

@app.post("/addUserTeam", tags=["User Team"])
async def addUserTeam(ut: schema.UserTeamBase, db: db_dependency):
    return userTeam.addUserTeam(ut, db)

@app.put("/updateUserTeam", tags=["User Team"])
async def updateUserTeam(id:int, ut: schema.UserTeamBase, db: db_dependency):
    return userTeam.updateUserTeam(id, ut, db)

@app.delete("/deleteUserTeam", tags=["User Team"])
async def deleteUserTeam(id:int, db: db_dependency):
    return userTeam.deleteUserTeam(id, db)

################# userType #################
@app.get("/getUserType", tags=["User Type"])
async def getUserType(db: db_dependency):
    return userType.getUserType(db)

@app.post("/addUserType", tags=["User Type"])
async def addUserType(ut: schema.UserTypeBase, db: db_dependency):
    return userType.addUserType(ut, db)

@app.put("/updateUserType", tags=["User Type"])
async def updateUserType(id:int, ut: schema.UserTypeBase, db: db_dependency):
    return userType.updateUserType(id, ut, db)

@app.delete("/deleteUserType", tags=["User Type"])
async def deleteUserType(id:int, db: db_dependency):
    return userType.deleteUserType(id, db)

################# user #################
@app.get("/getUser", tags=["User"])
async def getUser(db: db_dependency):
    return user.getUser(db)

@app.post("/addUser", tags=["User"])
async def addUser(ur: schema.UserInDB, db: db_dependency):
    return user.addUser(ur, db)

@app.put("/updateUser", tags=["User"])
async def updateUser(id:int, ur: schema.UserInDB, db: db_dependency):
    return user.updateUser(id, ur, db)

@app.delete("/deleteUser", tags=["User"])
async def deleteUser(id:int, db: db_dependency):
    return user.deleteUser(id, db)


################# matrix #################
@app.get("/getmatrix", tags=["Matrix"])
async def getmatrix(db: db_dependency):
    return matrix.getmatrix(db)

@app.post("/addmatrix", tags=["Matrix"])
async def addmatrix(ur: schema.MatrixBase, db: db_dependency):
    return matrix.addmatrix(ur, db)

@app.put("/updatematrix", tags=["Matrix"])
async def updatematrix(id:int, ur: schema.MatrixBase, db: db_dependency):
    print(ur)
    return matrix.updatematrix(id, ur, db)

@app.delete("/deletematrix", tags=["Matrix"])
async def deletematrix(id:int, db: db_dependency):
    return matrix.deletematrix(id, db)


################# Email #################
@app.get("/getemail", tags=["Email"])
async def getemail(db: db_dependency):
    return email.getemail(db)

@app.post("/addemail", tags=["Email"])
async def addemail(email: schema.EmailBase, db: db_dependency):
    return email.addemail(email, db)
