from fastapi import APIRouter, Path, Query
from pydantic import BaseModel

book_router = APIRouter()

books = []

class Book(BaseModel):
    id: int
    name: str
    publisher: str
    isbn: str


# CREATE: a node that receives a body of data
@book_router.post("/book")
def book_validate(book: Book) -> dict:
    books.append(book)
    return {"books": books}


# RETRIEVE: a node to get all books
@book_router.get("/book")
def book_all() -> dict:
    return {"books": books}


@book_router.put("/book/{id}")
def book_update(
    book: Book,
    id: int = Path(..., title="book id", gt=0, lt=100),
) -> dict:
    for book2 in books:
        if book2.id == id:
            book2.name = book.name
    return {"books": books}


@book_router.delete("/book/{id}")
def book_delete(id: int) -> dict:
    index = 0
    for book in books:
        if book.id == id:
            books.pop(index)
        index += 1

    return {"books": books}

# Retrieve a single record with a query parameter
@book_router.get("/single-book")
def book_single(id: int = Query(None)) -> dict:
    print(f"id = {id}")
    for book in books:
        if book.id == id:
            return {"book": book}
        
    return {"message": "Book is not found"}
