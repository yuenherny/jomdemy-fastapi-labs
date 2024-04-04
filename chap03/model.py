from pydantic import BaseModel
from typing import List


class TodoItem(BaseModel):
    id: int
    item: str

    # give more info in the documentation
    class Config:
        json_schema_extra = {
            "example": {
                "id": 10,
                "item": "read the next chapter of the book"
            }
        }


class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        json_schema_extra = {
            "example": {
                "todos": [
                    {"item": "Example 1", "id": 10},
                    {"item": "Example 2", "id": 11}
                ]
            }
        }