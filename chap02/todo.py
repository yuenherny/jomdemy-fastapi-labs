from fastapi import APIRouter

todo_router = APIRouter()

todo_list = ["work", "more work"]


@todo_router.get("/todo")
def todo_home() -> dict:
    return {"message": "todo home"}


@todo_router.post("/todo")
async def add_todo() -> dict:
    return {"todo": todo_list}
