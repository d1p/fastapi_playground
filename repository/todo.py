from pydantic import BaseModel
from typing import Optional


class TodoItem(BaseModel):
    name: str
    description: Optional[str] = None
    completed: bool = False
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    due_date: Optional[str] = None
    completed_at: Optional[str] = None
    deleted_at: Optional[str] = None
    deleted: bool = False

    class Config:
        orm_mode = True
