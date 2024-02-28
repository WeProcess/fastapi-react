from models import models
from database.dependency import db_dependency

def getmatrix(db: db_dependency):
    
    Matrix = db.query(models.Matrix).all()
    return Matrix

def addmatrix(mat, db: db_dependency):
    Matrix = models.Matrix(user_id=mat.user_id, 
                       matrix_person_id=mat.matrix_person_id, 
                       matrix_person_designation = mat.matrix_person_designation, 
                       matrix_person_name=mat.matrix_person_name, 
                       matrix_person_email=mat.matrix_person_email, 
                       matrix_person_number=mat.matrix_person_number
                       )
    db.add(Matrix)
    db.commit()
    return {"message": "Matrix Added."}

def updatematrix(id, mat, db: db_dependency):
    Matrix = db.query(models.Matrix).filter(models.Matrix.id==id).first()
    Matrix.matrix_person_id = mat.matrix_person_id
    Matrix.matrix_person_designation = mat.matrix_person_designation
    Matrix.matrix_person_name = mat.matrix_person_name
    Matrix.matrix_person_email = mat.matrix_person_email
    Matrix.matrix_person_number = mat.matrix_person_number
    db.commit()
    return {"message": "Matrix Updated."}

def deletematrix(id, db: db_dependency):
    Matrix = db.query(models.Matrix).filter(models.Matrix.id==id).first()
    db.delete(Matrix)
    db.commit()
    return {"message": "Matrix deleted."}
