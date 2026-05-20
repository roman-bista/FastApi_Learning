database.py
→ creates DB connection

models.py
→ defines tables

main.py
→ starts app and creates tables

Concept         	            Purpose

engine------------>	            connect to DB
Base-------------->	            parent for tables
models------------>             define tables
create_all()------>	            create tables
SessionLocal------>	            DB operations
Column------------>	            define fields