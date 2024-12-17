from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
import schemas,models,database
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
import password_hashing as hashing
import repository.user as repo_user
router=APIRouter(
    prefix="/user",
    tags=["USERS"]
)

get_db=database.get_db


@router.post('/',status_code=status.HTTP_201_CREATED)
def create_user(request:schemas.USER,db:Session=Depends(get_db)):
    return repo_user.create_user(request,db)    

@router.get('/{id}',response_model=schemas.showuser)
def get_user(id:int,db:Session=Depends(get_db)):
    return repo_user.get_user(id,db)

