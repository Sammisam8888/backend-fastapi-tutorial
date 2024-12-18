from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import timedelta
import schemas, database, models, mytoken
from password_hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    tags=['AUTHENTICATION']
)

get_db = database.get_db

@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with email {request.username} not found"
        )
    
    if not Hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password"
        )
    
    # Generate access token
    access_token = mytoken.create_access_token(
        data={"sub": user.email}
    )
    
    # Return the token
    return {"access_token":access_token,"token_type":"bearer"}
