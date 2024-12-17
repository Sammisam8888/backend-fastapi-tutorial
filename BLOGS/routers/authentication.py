from fastapi import APIRouter, status, HTTPException,Depends
import schemas,database,models
from password_hashing import Hash
from sqlalchemy.orm import Session

router=APIRouter(
    tags=['AUTHENTICATION']
)

get_db=database.get_db

@router.post('/login')
def login(request:schemas.Login,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.email==request.email).first()
    if not user :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with email {request.email} not found")
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"incorrect password")
    return user
