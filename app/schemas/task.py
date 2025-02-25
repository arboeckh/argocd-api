from pydantic import BaseModel
from typing import Optional, List
from app.schemas.subtask import SubTaskResponse


# Base schema for Task
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None


# Schema for Creating a Task
class TaskCreate(TaskBase):
    pass


# Schema for Updating a Task
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Response Schema (Including Subtasks)
class TaskResponse(TaskBase):
    id: int
    subtasks: List[SubTaskResponse] = []

    class Config:
        from_attributes = True  # ORM mode
