from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.subtask import SubTaskCreate, SubTaskResponse, SubTaskUpdate
from app.crud.subtask import (
    get_subtasks,
    get_subtask,
    create_subtask,
    update_subtask,
    delete_subtask,
)

router = APIRouter()


@router.get("/", response_model=list[SubTaskResponse])
def read_subtasks(db: Session = Depends(get_db)):
    return get_subtasks(db)


@router.post("/", response_model=SubTaskResponse)
def create_new_subtask(subtask: SubTaskCreate, db: Session = Depends(get_db)):
    return create_subtask(db, subtask)


@router.get("/{subtask_id}", response_model=SubTaskResponse)
def read_subtask(subtask_id: int, db: Session = Depends(get_db)):
    subtask = get_subtask(db, subtask_id)
    if not subtask:
        raise HTTPException(status_code=404, detail="SubTask not found")
    return subtask
