from models import models
from database.dependency import db_dependency

def getemail(db: db_dependency):
    
    Email = db.query(models.Email).all()
    return Email

def addemail(email, db: db_dependency):
    Email = models.Email(user_id=email.user_id, 
                       matrix_id=email.matrix_id, 
                       client_name = email.client_name, 
                       status_of_email=email.status_of_email,
                       )
    
    

    db.add(Email)
    db.commit()
    return {"message": "Email Added."}
