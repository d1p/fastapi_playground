import pytest
from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI


@pytest.fixture(autouse=True)
def mongodb():
    client = AsyncIOMotorClient(MONGO_URI)
    db = client.todo
    db.todo.delete_many({})
    return client
