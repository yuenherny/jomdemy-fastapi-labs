from fastapi import APIRouter, Path, HTTPException, status
from model import TodoItem, TodoItems

todo_router = APIRouter()

todo_list = []


@todo_router.get("/todo", response_model=TodoItems)
def todo_home() -> dict:
    return {"todos": todo_list}


@todo_router.post("/todo", status_code=201)
def add_todo(todo: TodoItem) -> dict:
    todo_list.append(todo)
    return {"todos": todo_list}


@todo_router.get("/todo/{id}")
def get_single_todo(
    id: int = Path(..., title="the id of the todo to retrieve")
) -> dict:
    for todo in todo_list:
        if todo.id == id:
            return {"todo": todo}
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist"
    )


@todo_router.delete("/todo/{id}")
def delete_single_todo(id: int) -> dict:
    for index, todo in enumerate(todo_list):
        if todo.id == id:
            todo_list.pop(index)
            return {"todo": todo}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist"
    )


@todo_router.put("/todo/{id}")
def update_single_todo(id: int, new_todo: TodoItem) -> dict:
    for todo in todo_list:
        if todo.id == id:
            todo.item = new_todo.item
            return {"todos": todo_list}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist"
    )
