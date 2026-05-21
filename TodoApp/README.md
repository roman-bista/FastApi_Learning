database.py
→ creates DB connection

models.py
→ defines tables

main.py
→ starts FastAPI app and defines routes

Concept Purpose

engine------------> manages DB connectivity
Base--------------> parent class for ORM models
models------------> define tables
create_all()------> create tables
Session ---------> active DB conversation
SessionLocal------> creates DB sessions
Column------------> define fields

database.py → DB infrastructure
models.py → table structure
main.py → API logic/routes
todos.db → actual stored data
