from sqlalchemy.orm import Mapped, mapped_column  # <- Импортирует класс Mapped и функцию mapped_column из sqlalchemy.orm для сопоставления атрибутов класса с соответствующими столбцами в базе данных.
from sqlalchemy import Boolean  # <- Импортирует тип данных Boolean из sqlalchemy для определения типа данных столбца status.
from database import Model  # <- Импортирует базовый класс Model из файла database.py, который предоставляет общую функциональность для всех моделей.

# Определяет модель TaskModel, которая наследуется от Model, и представляет таблицу "task_table" в базе данных.
class TaskModel(Model):
    __tablename__ = "task_table"  # <- Указывает имя таблицы, с которой сопоставляется модель.

    # Определяет атрибуты модели, которые сопоставляются со столбцами таблицы.
    id: Mapped[int] = mapped_column(primary_key=True)  # <- Определяет столбец id как первичный ключ с типом данных int.
    title: Mapped[str]  # <- Определяет столбец title с типом данных str.
    description: Mapped[str]  # <- Определяет столбец description с типом данных str.
    status: Mapped[bool] = mapped_column(Boolean, default=False)  # <- Определяет столбец status с типом данных bool и значением по умолчанию False.
