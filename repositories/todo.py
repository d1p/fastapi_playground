from config import MONGO_URI
from motor.motor_asyncio import AsyncIOMotorClient
from models.todo import TodoItem


class TodoItemRepository:
    def __init__(self):
        self.client = AsyncIOMotorClient(MONGO_URI)
        self.db = self.client.todoItem

    async def get_all_todos(self) -> list[TodoItem]:
        todos = await self.db.todo.find().to_list(length=100)
        return [TodoItem(**todo) for todo in todos]

    async def get_todo_by_id(self, _id: str):
        todo = await self.db.todo.find_one({"_id": _id})
        return TodoItem(**todo)

    async def create_todo_item(self, todo: TodoItem) -> str:
        result = await self.db.todo.insert_one(todo.model_dump())
        return str(result.inserted_id)
