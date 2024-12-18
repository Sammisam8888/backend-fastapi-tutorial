from fastapi import APIRouter, Depends, status
import schemas,database,oauth2
from sqlalchemy.orm import Session


import repository.user as repo_user
router=APIRouter(
    prefix="/user",
    tags=["USERS"]
)

get_db=database.get_db


@router.post('/',status_code=status.HTTP_201_CREATED)
def create_user(request:schemas.USER,db:Session=Depends(get_db),current_user :schemas.USER=Depends(oauth2.get_current_user)):
    return repo_user.create_user(request,db)    

@router.get('/{id}',response_model=schemas.showuser)
def get_user(id:int,db:Session=Depends(get_db),current_user :schemas.USER=Depends(oauth2.get_current_user)):
    return repo_user.get_user(id,db)

