from passlib.context import CryptContext

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

class Hash():

    def bcrypt(password:str):
        hashedpassword=pwd_context.hash(password)
        return hashedpassword
    
    def verify(hashedpassword:str,password:str):
        return pwd_context.verify(password,hashedpassword)