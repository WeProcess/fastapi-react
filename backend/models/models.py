from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from database.database import Base
from sqlalchemy.orm import relationship

class UserTeam(Base):
    __tablename__="UserTeam"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    userTeam = Column(String, index=True)

    usr1 = relationship('User', back_populates='usertm')

class UserType(Base):
    __tablename__="UserType"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    userType = Column(String, index=True)

    usr = relationship('User', back_populates='usertp')
    

class User(Base):
    __tablename__="User"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, index=True)
    disabled = Column(Boolean, default=False)
    userTeam = Column(Integer, ForeignKey("UserTeam.id"), index=True)
    userType = Column(Integer, ForeignKey("UserType.id"), index=True)
    
    usertm = relationship('UserTeam', back_populates='usr1')
    usertp = relationship('UserType', back_populates='usr')

    def valuefile(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "email": self.email,
            "disabled": self.disabled,
            "usertp": self.usertp,
            "usertm": self.usertm,
        }

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
