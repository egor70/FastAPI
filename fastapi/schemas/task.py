from pydantic import BaseModel
from typing import Optional


class TaskBase(BaseModel):
    """Базовая схема задачи"""
    title: str
    description: Optional[str] = None


class TaskCreate(TaskBase):
    """Схема для создания задачи"""
    pass


class TaskUpdate(BaseModel):
    """Схема для обновления задачи (все поля опциональны)"""
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class Task(TaskBase):
    """Полная схема задачи с ID и статусом"""
    id: int
    completed: bool = False

    class Config:
        from_attributes = True  # Для совместимости с SQLAlchemy (будет использоваться позже)