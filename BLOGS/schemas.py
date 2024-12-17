from pydantic import BaseModel
from typing import List

#default schema to see a data object
class BlogBase(BaseModel):
    title:str
    body:str
    # user_id:int

class Blog(BlogBase):
    class Config():
        orm_mode=True

class USER(BaseModel):
    name:str
    email:str
    password:str

class showuser(BaseModel):
    name:str
    email:str
    blogs:List[Blog] =[]
    class Config():
        orm_mode=True

class showuserblog(BaseModel):
    name:str
    email:str
    class Config():
        orm_mode=True
#schema to see a data object in a particular format
class Showblog(BaseModel):
    title:str
    body:str
    creator:showuserblog
    class Config():
        orm_mode=True

class Login(BaseModel):
    email:str
    password:str