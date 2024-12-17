from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# This will create the engine for running the database server 
database_url = 'sqlite:///./blog.db'

engine = create_engine(database_url, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


#this block will give us an instance of the database
def get_db():
    db=SessionLocal()
    try:
        yield db 
    finally :
        db.close() 
