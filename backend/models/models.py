from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from database.database import Base

class UserTeam(Base):
    __tablename__="UserTeam"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    userTeam = Column(String, index=True)

class UserType(Base):
    __tablename__="UserType"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    userType = Column(String, index=True)

class User(Base):
    __tablename__="User"

    id = Column(Integer, primary_key=True, autoincrement=True,  index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, index=True)
    disabled = Column(Boolean, default=False)
    userType = Column(Integer, ForeignKey("UserType.id"), index=True)
    userTeam = Column(Integer, ForeignKey("UserTeam.id"), index=True)

class Matrix(Base):
    __tablename__="Matrix"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_id = Column(Integer, ForeignKey("User.id"), index=True)
    matrix_person_id = Column(String, index=True)
    matrix_person_designation = Column(String, index=True)
    matrix_person_name = Column(String, index=True)
    matrix_person_email = Column(String, index=True)
    matrix_person_number = Column(String, index=True)

class Email(Base):
    __tablename__="Email"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_id = Column(Integer, ForeignKey("User.id"), index=True)
    matrix_id = Column(Integer, ForeignKey("Matrix.id"), index=True)
    client_name = Column(String, index=True)
    client_email = Column(String, index=True)
    status_of_email = Column(Boolean, default=False)
