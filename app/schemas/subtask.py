from pydantic import BaseModel
from typing import Optional


# Base schema for SubTask
class SubTaskBase(BaseModel):
    title: str
    task_id: int


# Schema for Creating a SubTask
class SubTaskCreate(SubTaskBase):
    pass


# Schema for Updating a SubTask
class SubTaskUpdate(BaseModel):
    title: Optional[str] = None


# Response Schema
class SubTaskResponse(SubTaskBase):
    id: int

    class Config:
        from_attributes = True  # ORM mode
