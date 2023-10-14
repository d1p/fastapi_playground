from models.todo import TodoItem
from repositories.todo import TodoItemRepository


class TodoItem:
    async def create(self, todo: TodoItem) -> str:
        todo_id = await TodoItemRepository.create_todo_item(**todo.model_dump())
        return todo_id

    async def get_all(self) -> list[TodoItem]:
        return await TodoItemRepository().get_all_todos()
