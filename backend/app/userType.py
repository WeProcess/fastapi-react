from models import models

def getUserType(db):
    UserType = db.query(models.UserType).all()
    return UserType

def addUserType(ut, db):
    UserType = models.UserType(userType=ut.userType)
    db.add(UserType)
    db.commit()
    return {"message": "User Type Added."}

def updateUserType(id, ut, db):
    UserType = db.query(models.UserType).filter(models.UserType.id==id).first()
    UserType.userType = ut.userType
    db.commit()
    return {"message": "User Type Updated."}

def deleteUserType(id, db):
    UserType = db.query(models.UserType).filter(models.UserType.id==id).first()
    db.delete(UserType)
    db.commit()
    return {"message": "User Type deleted."}