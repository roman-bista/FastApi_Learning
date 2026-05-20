# Contains:

# database connection
# engine
# Base class


from sqlalchemy import create_engine    #Used to create connection with database.
from sqlalchemy.orm import sessionmaker     #temporary conversation with database
from sqlalchemy.ext.declarative import declarative_base     #reates base class for SQLAlchemy models.

SQLALCHEMY_DATABASE_URL='sqlite:///./todos.db'  #using SQLite database.

engine= create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})  #Engine = actual database connection manager.

SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)  #This creates sessions for database operations.

Base=declarative_base()     #This is parent class for database models.