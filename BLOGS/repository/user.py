from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
import schemas,models,database
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
import password_hashing as hashing

get_db=database.get_db

def create_user(request:schemas.USER,db:Session=Depends(get_db)):

    
    new_user=models.User(name=request.name,email=request.email,password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id:int,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {id} not found")
    return user
