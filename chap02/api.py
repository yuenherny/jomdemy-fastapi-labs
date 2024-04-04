from fastapi import FastAPI
from todo import todo_router
from book import book_router

app = FastAPI()
app.include_router(router=todo_router)
app.include_router(router=book_router)
