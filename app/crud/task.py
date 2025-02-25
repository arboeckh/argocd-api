from sqlalchemy.orm import Session
from schema.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


def get_tasks(db: Session):
    return db.query(Task).all()


def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()


def create_task(db: Session, task_data: TaskCreate):
    new_task = Task(**task_data.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def update_task(db: Session, task_id: int, task_data: TaskUpdate):
    task = get_task(db, task_id)
    if task:
        for key, value in task_data.dict(exclude_unset=True).items():
            setattr(task, key, value)
        db.commit()
        db.refresh(task)
    return task


def delete_task(db: Session, task_id: int):
    task = get_task(db, task_id)
    if task:
        db.delete(task)
        db.commit()
    return task
