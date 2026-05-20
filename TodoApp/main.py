# Starts FastAPI app and tells SQLAlchemy:
# “Create tables in database.”

from fastapi import FastAPI     #This loads all tables into memory.
import models
from database import engine     #Imports database connection.

app=FastAPI()           #Starts API app.
models.Base.metadata.create_all(bind=engine)        #Take all tables from models.py
                                                    # ↓
                                                    # Convert them into SQL
                                                    # ↓
                                                    # Create them inside database