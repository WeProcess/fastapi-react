from models import models
from scurity.scurity import get_password_hash

def getdashboard(db):
    User = db.query(models.User).all()
    return User

def getKAO(db):
    User = db.query(models.User).filter(models.User.usertp).filter(models.UserType.userType=='KAO').all()
    return User

def addUser(ur, db):
    User = models.User(full_name=ur.full_name, 
                       email=ur.email, 
                       hashed_password = get_password_hash(ur.hashed_password), 
                       userType=ur.userType, 
                       userTeam=ur.userTeam
                       )
    db.add(User)
    db.commit()
    return {"message": "User Added."}

def updateUser(id, ur, db):
    User = db.query(models.User).filter(models.User.id==id).first()
    User.full_name = ur.full_name
    User.email = ur.email
    User.hashed_password = get_password_hash(ur.hashed_password)
    User.disabled = ur.disabled
    User.userType = ur.userType
    User.userTeam = ur.userTeam
    db.commit()
    return {"message": "User Updated."}

def deleteUser(id, db):
    User = db.query(models.User).filter(models.User.id==id).first()
    db.delete(User)
    db.commit()
    return {"message": "User deleted."}
