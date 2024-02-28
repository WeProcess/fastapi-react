from models import models

def getUserTeam(db):
    userteam = db.query(models.UserTeam).all()
    return userteam

def addUserTeam(ut, db):
    userteam = models.UserTeam(userTeam=ut.userTeam)
    db.add(userteam)
    db.commit()
    return {"message": "User Team Added."}

def updateUserTeam(id, ut, db):
    userteam = db.query(models.UserTeam).filter(models.UserTeam.id==id).first()
    userteam.userTeam = ut.userTeam
    db.commit()
    return {"message": "User Team Updated."}

def deleteUserTeam(id, db):
    userteam = db.query(models.UserTeam).filter(models.UserTeam.id==id).first()
    db.delete(userteam)
    db.commit()
    return {"message": "User Team deleted."}
