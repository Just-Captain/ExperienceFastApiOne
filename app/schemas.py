# Импортируем класс BaseModel из библиотеки pydantic
from pydantic import BaseModel

# Определяем схему данных для создания новой задачи
class TaskCreateSchema(BaseModel):
    """
    Схема данных для создания новой задачи
    """
    title: str
    description: str

# Определяем схему данных для обновления существующей задачи
class TaskUpdateSchema(TaskCreateSchema):
    """
    Схема данных для обновления существующей задачи
    """
    status: bool
