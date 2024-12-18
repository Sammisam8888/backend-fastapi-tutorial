from fastapi import FastAPI
import models 
from database import engine
from routers.blog import router as blog_router
from routers.user import router as user_router
from routers.authentication import router as authentication_router

app = FastAPI()

models.Base.metadata.create_all(engine)
#here we are migrating all the tables


app.include_router(authentication_router)
app.include_router(blog_router)
app.include_router(user_router)
