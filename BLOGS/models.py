from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

# import schemas
class Blog(Base):
    #Blog is the extended Base of the database

    __tablename__="blogs" 
    #without defining tablename it will show error

    id=Column(Integer, primary_key=True,index=True)

    title=Column(String)

    body=Column(String)

    user_id=Column(Integer,ForeignKey('users.id'))
    creator =relationship("User",back_populates="blogs")

    #here the foreign key references the previously existing user id


class User(Base):
    __tablename__="users"

    id=Column(Integer, primary_key=True, index=True)

    name=Column(String)

    email=Column(String)

    password=Column(String)

    blogs=relationship("Blog",back_populates="creator")

    #backpopulates signifies that i want the primary key to reference to the creator