import time

from fastapi import FastAPI
from models.todo import TodoItem
from use_cases.todo_item import TodoItem as TodoItemUseCase
from routes.middlewares.response_time import ResponseTimeMiddleware
app = FastAPI()

app.add_middleware(ResponseTimeMiddleware)

@app.post("/items/")
async def create_item(item: TodoItem):
    use_case = TodoItemUseCase()
    _id = await use_case.create(item)
    return {"id": _id}


@app.get("/items/")
async def get_all_items():
    use_case = TodoItemUseCase()
    items = await use_case.get_all()
    return items
