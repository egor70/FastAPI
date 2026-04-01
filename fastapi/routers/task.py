from fastapi import APIRouter, HTTPException, status
from typing import List
from schemas.task import Task, TaskCreate, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["tasks"])

# Хранилище задач (временное, вместо БД)
tasks_db = []
task_counter = 1


@router.get("/", response_model=List[Task])
async def get_all_tasks():
    """Получить список всех задач"""
    return tasks_db


@router.get("/{task_id}", response_model=Task)
async def get_task(task_id: int):
    """Получить задачу по ID"""
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task with id {task_id} not found"
    )


@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskCreate):
    """Создать новую задачу"""
    global task_counter

    new_task = Task(
        id=task_counter,
        title=task.title,
        description=task.description,
        completed=False
    )
    tasks_db.append(new_task)
    task_counter += 1
    return new_task


@router.put("/{task_id}", response_model=Task)
async def update_task(task_id: int, task_update: TaskUpdate):
    """Обновить задачу"""
    for i, task in enumerate(tasks_db):
        if task.id == task_id:
            # Обновляем только переданные поля
            if task_update.title is not None:
                tasks_db[i].title = task_update.title
            if task_update.description is not None:
                tasks_db[i].description = task_update.description
            if task_update.completed is not None:
                tasks_db[i].completed = task_update.completed
            return tasks_db[i]

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task with id {task_id} not found"
    )


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    """Удалить задачу"""
    for i, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db.pop(i)
            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task with id {task_id} not found"
    )


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_all_tasks():
    """Удалить все задачи"""
    tasks_db.clear()