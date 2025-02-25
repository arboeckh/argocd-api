from fastapi import FastAPI
from app.routes import task, subtask

app = FastAPI()

app.include_router(task.router, prefix="/tasks", tags=["tasks"])
app.include_router(subtask.router, prefix="/subtasks", tags=["subtasks"])


@app.get("/")
def root():
    return {"message": "FastAPI Task Manager is Running!"}
