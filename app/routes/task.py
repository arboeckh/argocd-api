from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.crud.task import get_tasks, get_task, create_task, update_task, delete_task

router = APIRouter()


@router.get("/", response_model=list[TaskResponse])
def read_tasks(db: Session = Depends(get_db)):
    return get_tasks(db)


@router.post("/", response_model=TaskResponse)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task)


@router.get("/{task_id}", response_model=TaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/{task_id}", response_model=TaskResponse)
def update_existing_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    return update_task(db, task_id, task)


@router.delete("/{task_id}")
def delete_existing_task(task_id: int, db: Session = Depends(get_db)):
    return delete_task(db, task_id)
