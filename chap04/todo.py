from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates


todo_router = APIRouter()
todo_list = [
    {"title": "todo 1"},
    {"title": "todo 2"}
]
templates = Jinja2Templates(directory="templates")

@todo_router.post("/todo")
def add_todo(request: Request, title: str = Form(...)):
    todo_list.append({"title": title})
    # render a page
    return templates.TemplateResponse("todo.html", {
        "request": request,
        "todos": todo_list,
        "name": "John Doe"
    })

@todo_router.get("/todo")
def show_todo(request: Request):
    return templates.TemplateResponse("todo.html", {
        "request": request,
        "todos": todo_list
    })


@todo_router.get("/todo-form")
def show_form(request: Request):
    return templates.TemplateResponse("todo_form.html", {
        "request": request
    })


@todo_router.get("/todo/{index}")
def delete_todo(request: Request, index: int):
    todo_list.pop(index)
    return RedirectResponse("/todo")