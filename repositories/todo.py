from config import MONGO_URI
from motor.motor_asyncio import AsyncIOMotorClient
from models.todo import TodoItem
from models.common.pagination import Pagination, JsonApiLinks, JsonApiMeta

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

    async def create_todo_item(self, todo: dict) -> str:
        result = await self.db.todo.insert_one(todo)
        return str(result.inserted_id)

    async def get_items(self, limit: int = 10, skip: int = 0) -> Pagination:
        todos = await self.db.todo.find().skip(skip).limit(limit).to_list(length=limit)
        todo = [TodoItem(**todo) for todo in todos]
        total = await self.db.todo.count_documents({})

        links = JsonApiLinks(
            first=f"/items?limit={limit}&skip=0",
            last=f"/items?limit={limit}&skip={total - limit}",
            next=f"/items?limit={limit}&skip={skip + limit}" if skip + limit < total else None,
            prev=f"/items?limit={limit}&skip={skip - limit}" if skip - limit >= 0 else None,
        )
        meta = JsonApiMeta(total=total, count=len(todo))
        return Pagination(items=todo, links=links, meta=meta)
