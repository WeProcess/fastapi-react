from fastapi import FastAPI, Request, Form, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from database.database import engine
from database.dependency import db_dependency
from models import models, schema
from app import userTeam, userType, user, matrix, email, dashboard
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

################# dashboard #################
@app.get("/dashboard", tags=["Dashboard"])
async def get_dashboard(db: db_dependency, current_user: User = Depends(get_current_active_user)):
    # print(dashboard.getdashboard(db))
    kao_user = dashboard.getKAO(db)
    
    return {"kao_user": kao_user,"current_user" : current_user}

################# userTeam #################
@app.get("/getUserTeam", tags=["User Team"])
async def get_User_Team(db: db_dependency, current_user: User = Depends(get_current_active_user)):
    return {"user_team" : userTeam.getUserTeam(db), "current_user" : current_user}

@app.post("/addUserTeam", tags=["User Team"])
async def add_User_Team(ut: schema.UserTeamBase, db: db_dependency, current_user: User = Depends(get_current_active_user)):
    return {"user_team" : userTeam.addUserTeam(ut, db), "current_user" : current_user}

@app.put("/updateUserTeam", tags=["User Team"])
async def update_User_Team(id:int, ut: schema.UserTeamBase, db: db_dependency, current_user: User = Depends(get_current_active_user)):
    return {"user_team" : userTeam.updateUserTeam(id, ut, db), "current_user" : current_user}

@app.delete("/deleteUserTeam", tags=["User Team"])
async def delete_User_Team(id:int, db: db_dependency, current_user: User = Depends(get_current_active_user)):
    return {"user_team" : userTeam.deleteUserTeam(id, db), "current_user" : current_user}

################# userType #################
@app.get("/getUserType", tags=["User Type"])
async def get_User_Type(db: db_dependency, current_user: User = Depends(get_current_active_user)):
    return {"user_type" : userType.getUserType(db), "current_user" : current_user}

@app.post("/addUserType", tags=["User Type"])
async def add_User_Type(ut: schema.UserTypeBase, db: db_dependency, current_user: User = Depends(get_current_active_user)):
    return {"user_type" : userType.addUserType(ut, db), "current_user" : current_user}

@app.put("/updateUserType", tags=["User Type"])
async def update_User_Type(id:int, ut: schema.UserTypeBase, db: db_dependency, current_user: User = Depends(get_current_active_user)):
    return userType.updateUserType(id, ut, db)

@app.delete("/deleteUserType", tags=["User Type"])
async def delete_User_Type(id:int, db: db_dependency, current_user: User = Depends(get_current_active_user)):
    return {"user_type" : userType.deleteUserType(id, db), "current_user" : current_user}

################# user #################
@app.get("/getUser", tags=["User"])
async def get_User(db: db_dependency, current_user: User = Depends(get_current_active_user)):
    user_var = user.getUser(db)
    for auser_var in user_var:
        print(auser_var.valuefile())

    return {"user" : user_var, "current_user" : current_user}

@app.post("/addUser", tags=["User"])
async def add_User(ur: schema.UserInDB, db: db_dependency, current_user: User = Depends(get_current_active_user)):
    return {"user" : user.addUser(ur, db), "current_user" : current_user}

@app.put("/updateUser", tags=["User"])
async def update_User(id:int, ur: schema.UserInDB, db: db_dependency, current_user: User = Depends(get_current_active_user)):
    return {"user" : user.updateUser(id, ur, db), "current_user" : current_user}

@app.delete("/deleteUser", tags=["User"])
async def delete_User(id:int, db: db_dependency, current_user: User = Depends(get_current_active_user)):
    return {"user" : user.deleteUser(id, db), "current_user" : current_user}

################# matrix #################
@app.get("/getMatrix", tags=["Matrix"])
async def get_matrix(db: db_dependency, current_user: User = Depends(get_current_active_user)):
    return {"matrix" : matrix.getmatrix(db), "current_user" : current_user}

@app.post("/addMatrix", tags=["Matrix"])
async def add_matrix(ur: schema.MatrixBase, db: db_dependency, current_user: User = Depends(get_current_active_user)):
    return {"matrix" : matrix.addmatrix(ur, db), "current_user" : current_user}

@app.put("/updateMatrix", tags=["Matrix"])
async def update_matrix(id:int, ur: schema.MatrixBase, db: db_dependency, current_user: User = Depends(get_current_active_user)):
    return {"matrix" : matrix.updatematrix(id, ur, db), "current_user" : current_user}

@app.delete("/deleteMatrix", tags=["Matrix"])
async def delete_matrix(id:int, db: db_dependency, current_user: User = Depends(get_current_active_user)):
    return {"matrix" : matrix.deletematrix(id, db), "current_user" : current_user}


################# Email #################
@app.get("/getEmail", tags=["Email"])
async def get_email(db: db_dependency, current_user: User = Depends(get_current_active_user)):
    return {"email" : email.getemail(db), "current_user" : current_user}

@app.post("/addEmail", tags=["Email"])
async def add_email(email: schema.EmailBase, db: db_dependency, current_user: User = Depends(get_current_active_user)):
    return {"email" : email.addemail(email, db), "current_user" : current_user}
