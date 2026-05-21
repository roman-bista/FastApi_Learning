# Starts FastAPI app and tells SQLAlchemy:“Create tables in database.” define routes

from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends    #Import models so SQLAlchemy knows which tables exist
from models import Todos
from database import engine, SessionLocal   #Import database connection engine and session factory
import models    

app=FastAPI()           
models.Base.metadata.create_all(bind=engine)        #Take all SQLAlchemy models
                                                    # ↓
                                                    # Convert Python classes into SQL tables
                                                    # ↓
                                                    #Create tables in database if they do not already exist

# engine = object that knows how to connect to database Engine = connection manager
# Session = active conversation
# SessionLocal=Creates database sessions


def get_db():                   #get_db()=opening session,giving session,closing session
    db = SessionLocal()         #Open a database session
    try:
        yield db                #Give this database session to the route function
    finally:
        db.close()              #After request finishes,close the database connection

# Create database connection            
# ↓
# Give it to API temporarily
# ↓
# After work is done
# ↓
# Close connection safely

# Open table
# ↓
# Customer uses table
# ↓
# Customer leaves
# ↓
# Clean and close table


# Session = conversation with database,Using a session, your app can:

# read data
# add data
# update data
# delete data
# save changes
db_dependency = Annotated[Session, Depends(get_db)]     #FastAPI:
                                                        # Run get_db()
                                                        # ↓
                                                        # Get database session
                                                        # ↓
                                                        # Inject it into db variable

@app.get("/")
async def read_all(db: db_dependency):
    return db.query(Todos).all()                         #SELECT * FROM todos;