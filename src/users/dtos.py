from pydantic import BaseModel

class UserSchema(BaseModel):
    name:str
    username:str
    enc_password:str
    email:str