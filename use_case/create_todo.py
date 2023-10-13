from repository.todo import TodoItem as TodoItemRepo
from database.todo import TodoItem as TodoItemDB, create_todo_item, get_all_todos


class TodoItem:
    async def create(self, todo: TodoItemRepo):
        todo_db = TodoItemDB(**todo.model_dump())
        return await create_todo_item(todo_db)

    async def get_all(self):
        todos = await get_all_todos()
        # convert to TodoItem
        return [TodoItemRepo(**todo) for todo in todos]
