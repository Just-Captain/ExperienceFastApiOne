from sqlalchemy import create_engine  # <- Импортирует функцию create_engine для создания экземпляра движка базы данных.
from sqlalchemy.orm import DeclarativeBase  # <- Импортирует базовый класс DeclarativeBase для определения моделей базы данных.

# Создает экземпляр движка базы данных для базы данных SQLite с именем файла "db.sqlite".
# Параметр echo=True включает вывод всех выполняемых SQL-запросов в консоль.
engine = create_engine("sqlite:///db.sqlite", echo=True)

# Определяет базовый класс Model, который наследуется всеми моделями базы данных в приложении.
class Model(DeclarativeBase):
    pass  # <- Пустой класс, который служит базовым классом для всех моделей.
