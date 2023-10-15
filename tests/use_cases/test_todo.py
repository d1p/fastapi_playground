import pytest
from tests.fixtures.mongodb import mongodb
from use_cases.todo_item import TodoItem as TodoItemUseCase
from tests.factories.todo_factory import TodoItemFactory


@pytest.fixture(scope="module")
def todos():
    # return 10 todos
    return [TodoItemFactory() for _ in range(10)]


@pytest.mark.asyncio
async def test_get_all_todos(mongodb, mocker, todos):
    # tests use case calls repository method and returns the result
    mocker.patch("repositories.todo.TodoItemRepository.get_all_todos", return_value=todos)
    use_case = TodoItemUseCase()
    assert await use_case.get_all() == todos
