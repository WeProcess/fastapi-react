from pydantic import BaseModel

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    email : str or None = None # type: ignore

class UserTeamBase(BaseModel):
    userTeam : str

class UserTypeBase(BaseModel):
    userType : str

class UserBase(BaseModel):
    full_name: str or None = None # type: ignore
    email: str or None = None # type: ignore
    disabled: bool or None = None # type: ignore   
    userType : int
    userTeam : int

class UserInDB(UserBase):
    hashed_password : str

class MatrixBase(BaseModel):
    user_id : int
    matrix_person_id : str or None = None # type: ignore  
    matrix_person_designation : str or None = None # type: ignore  
    matrix_person_name : str or None = None # type: ignore  
    matrix_person_email : str or None = None # type: ignore  
    matrix_person_number : str or None = None # type: ignore  

class EmailBase(BaseModel):
    user_id : int
    matrix_id : int
    client_name : str or None = None # type: ignore  
    client_email : str or None = None # type: ignore  
    status_of_email : bool or None = None # type: ignore  
