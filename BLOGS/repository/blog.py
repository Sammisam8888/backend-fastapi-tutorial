from fastapi import status, HTTPException

import schemas,models
from sqlalchemy.orm import Session




def all(db:Session):
    blogs=db.query(models.Blog).all()
    return blogs

def create(request:schemas.Blog, db:Session):
    #here we use schemas.Blog becz we have defined the Blog class within the schemas.py file
    #now the request will accept the inputs from user in the format as specified in schema i.e. - a title and a body

    new_blog=models.Blog(title=request.title, body=request.body,user_id=1)

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def show(id:int,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog :
        #return {"data":"not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with id {id} not found")
    #here 404 status code signifies error/ data not found..
    return blog


def destroy(id,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
    db.commit()
    return 'successfully deleted record'

def update(id:int,request:schemas.Blog,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id).update({'title':request.title,'body':request.body})
    db.commit()
    return 'successfully updated'
