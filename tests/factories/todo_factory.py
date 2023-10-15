import factory
from factory import fuzzy

from models.todo import TodoItem


class TodoItemFactory(factory.Factory):
    class Meta:
        model = TodoItem

    name = fuzzy.FuzzyText(length=10)
    description = fuzzy.FuzzyText(length=10)
    completed = fuzzy.FuzzyChoice([True, False])
    deleted = fuzzy.FuzzyChoice([True, False])
