from fastapi import APIRouter, Request  # <- Импортирует необходимые библиотеки для работы с FastAPI и получения информации из запроса клиента.
from sqlalchemy.orm import Session  # <- Импортирует класс Session для работы с БД
from database import engine  # <- Импортирует экземпляр базы данных engine из файла database.py
from sqlalchemy import select, insert, update, delete  # <- Импортирует операторы SQL для выполнения различных запросов, таких как выборка, вставка, обновление и удаление данных.
from models import TaskModel  # <- Импортирует модель TaskModel из файла models.py, которая сопоставляет таблицу в БД с соответствующим классом в Python.
from schemas import TaskCreateSchema, TaskUpdateSchema  # <- Импортирует схемы TaskCreateSchema и TaskUpdateSchema из файла schemas.py, которые используются для валидации входных данных.

# Создает объект роутера FastAPI с префиксом "/api/v1/tasks" для всех маршрутов, определенных ниже.
tasks_router = APIRouter(prefix="/api/v1/tasks")

# Создает функцию для обработки запросов GET по пути "/list/", которая возвращает список задач.
@tasks_router.get(path='/list/')
def list_task_point(request: Request):  # <- Функция принимает параметр request, который содержит информацию о запросе клиента.
    session:Session = Session(engine)  # <- Создает экземпляр класса Session для работы с базой данных.
    stmt = select(TaskModel)  # <- Создает SQL-запрос для выборки всех записей из таблицы, сопоставленной с моделью TaskModel.
    requst_db = session.execute(stmt)  # <- Выполняет запрос с помощью сессии, что приводит к объекту, содержащему результат запроса.
    tasks:list = requst_db.scalars().all()  # <- Извлекает все значения из результата и преобразует их в список с помощью методов scalars() и all().
    session.close()  # <- Закрывает сессию, чтобы освободить ресурсы, связанные с базой данных.
    return tasks  # <- Возвращает список задач в качестве ответа.

# Создает функцию для обработки запросов POST по пути "/create/", которая создает новую задачу.
@tasks_router.post(path='/create/')
def create_task_point(request: Request, task: TaskCreateSchema):  # <- Функция принимает параметр request и объект TaskCreateSchema, который содержит данные новой задачи.
    session = Session(engine)  # <- Создает экземпляр класса Session для работы с базой данных.
    stmt = insert(TaskModel).values(title=task.title,  # <- Создает SQL-запрос для вставки новой записи в таблицу с указанными значениями.
                                    description=task.description)
    session.execute(stmt)  # <- Выполняет запрос.
    session.commit()  # <- Подтверждает изменения в базе данных.
    session.close()  # <- Закрывает сессию.
    return task  # <- Возвращает объект TaskCreateSchema в качестве ответа.

# Создает функцию для обработки запросов PUT по пути "/update/", которая обновляет существующую задачу.
@tasks_router.put(path='/update/')
def update_task_point(request: Request, task_id:int ,new_task: TaskUpdateSchema):  # <- Функция принимает параметры request, task_id и объект TaskUpdateSchema, который содержит обновленные данные задачи.
    session = Session(engine)  # <- Создает экземпляр класса Session для работы с базой данных.
    stmt = update(TaskModel).where(TaskModel.id == task_id).values(  # <- Создает SQL-запрос для обновления записи в таблице с указанными значениями и условием, где id равен task_id.
        title=new_task.title,
        description=new_task.description,
        status=new_task.status
    )
    task = session.execute(stmt)  # <- Выполняет запрос.
    session.commit()  # <- Подтверждает изменения в базе данных.
    session.close()  # <- Закрывает сессию.
    return new_task  # <- Возвращает объект TaskUpdateSchema в качестве ответа.

# Создает функцию для обработки запросов DELETE по пути "/delete/{task_id}/", которая удаляет существующую задачу.
@tasks_router.delete(path='/delete/')
def delete_task_point(request: Request, task_id: int):  # <- Функция принимает параметры request и task_id.
    session = Session(engine)  # <- Создает экземпляр класса Session для работы с базой данных.
    stmt = delete(TaskModel).where(TaskModel.id == task_id)  # <- Создает SQL-запрос для удаления записи из таблицы с указанным условием, где id равен task_id.
    result = session.execute(stmt)  # <- Выполняет запрос.
    session.commit()  # <- Подтверждает изменения в базе данных.
    session.close()  # <- Закрывает сессию.
    return result  # <- Возвращает объект результата выполнения запроса.
