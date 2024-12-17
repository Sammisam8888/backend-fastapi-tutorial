from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
import schemas,models,database
from sqlalchemy.orm import Session
from repository import blog as repo_blog

router=APIRouter(
    prefix="/blog",
    tags=["BLOGS"]
)

get_db=database.get_db

@router.get('/',response_model=List[schemas.Showblog])
def all(db:Session=Depends(get_db)):
    return repo_blog.get_all(db)


@router.post('/',status_code=201)
#status_code is optional .. 201 is the status code for the data being created. the 200 is code for ok...

#statuscode link - https://docs.python.org/3/library/http.html

def create(request:schemas.Blog, db:Session=Depends(get_db)):
    return repo_blog.create(request,db)


@router.get('/{id}',status_code=200,response_model=schemas.Showblog)
#here status code 200 signifies that the data has been found (okay)
def show(id:int,db:Session=Depends(get_db)):
    return repo_blog.show(id,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
#here the delete method in decorator will give us access rights to delete a particular record from the db
def destroy(id,db:Session=Depends(get_db)):
    return repo_blog.destroy(id,db)


#to update a record
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request:schemas.Blog,db:Session = Depends(get_db)):
    return repo_blog.update(id,request,db)

