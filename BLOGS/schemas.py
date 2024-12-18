from pydantic import BaseModel
from typing import List, Optional


#default schema to see a data object
class BlogBase(BaseModel):
    title:str
    body:str
    # user_id:int

class Blog(BlogBase):
    class Config():
        from_attribute=True

class USER(BaseModel):
    name:str
    email:str
    password:str

class showuser(BaseModel):
    name:str
    email:str
    blogs:List[Blog] =[]
    class Config():
        from_attributes=True

class showuserblog(BaseModel):
    name:str
    email:str
    class Config():
        from_attributes=True
#schema to see a data object in a particular format
class Showblog(BaseModel):
    title:str
    body:str
    creator:showuserblog
    class Config():
        from_attributes=True

class Login(BaseModel):
    email:str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str]=None

