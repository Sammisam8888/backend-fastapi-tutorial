from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
import mytoken

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    return mytoken.verify_token(token)
    