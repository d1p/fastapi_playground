from config import MONGO_URI
from motor.motor_asyncio import AsyncIOMotorClient
from repository.todo import TodoItem

client = AsyncIOMotorClient(MONGO_URI)
db = client.todo


async def get_all_todos():
    todos = await db.todo.find().to_list(length=100)
    return todos


async def get_todo_by_id(id: str):
    todo = await db.todo.find_one({"_id": id})
    return todo


async def create_todo_item(todo: TodoItem) -> int:
    result = await db.todo.insert_one(todo.model_dump())
    return str(result.inserted_id)
