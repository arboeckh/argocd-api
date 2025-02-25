from sqlalchemy.orm import Session
from schema.models.subtask import SubTask
from app.schemas.subtask import SubTaskCreate, SubTaskUpdate


def get_subtasks(db: Session):
    return db.query(SubTask).all()


def get_subtask(db: Session, subtask_id: int):
    return db.query(SubTask).filter(SubTask.id == subtask_id).first()


def create_subtask(db: Session, subtask_data: SubTaskCreate):
    new_subtask = SubTask(**subtask_data.dict())
    db.add(new_subtask)
    db.commit()
    db.refresh(new_subtask)
    return new_subtask


def update_subtask(db: Session, subtask_id: int, subtask_data: SubTaskUpdate):
    subtask = get_subtask(db, subtask_id)
    if subtask:
        for key, value in subtask_data.dict(exclude_unset=True).items():
            setattr(subtask, key, value)
        db.commit()
        db.refresh(subtask)
    return subtask


def delete_subtask(db: Session, subtask_id: int):
    subtask = get_subtask(db, subtask_id)
    if subtask:
        db.delete(subtask)
        db.commit()
    return subtask
