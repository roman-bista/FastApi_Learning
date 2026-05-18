from fastapi import FastAPI
app=FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self,id,title,author,description,rating):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating


BOOKS=[
    Book(1, 'comp science pro', 'coding with ruby', ' a very nice book!',5),
    Book(2, 'be fast with fastapi','coding with ruby', ' a great book!',5),
    Book(3, 'master endpoints','coding with ruby', ' a awsome book !',5),
    Book(4, 'HP1','author 1', ' a very nice book!',2),
    Book(5, 'HP2','author 2', ' a very nice book!',3),
    Book(6, 'HP3','Author 3', '  description book!',1)
]
@app.get("/books")
async def read_all_books():
    return BOOKS
