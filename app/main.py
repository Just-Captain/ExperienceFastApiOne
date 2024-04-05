from fastapi import FastAPI  # <- Импортирует класс FastAPI для создания приложения FastAPI.
from fastapi.staticfiles import StaticFiles  # <- Импортирует класс StaticFiles для обработки статических файлов.
import uvicorn  # <- Импортирует uvicorn для запуска сервера FastAPI.
from database import engine  # <- Импортирует экземпляр базы данных engine из файла database.py.
from models import TaskModel  # <- Импортирует модель TaskModel из файла models.py.
from routers import tasks_router  # <- Импортирует роутер tasks_router из файла routers.py.
from urls import task_template  # <- Импортирует роутер task_template из файла urls.py.

# Создает экземпляр приложения FastAPI.
app = FastAPI()

# Монтирует статические файлы в приложение FastAPI, делая их доступными по пути "/static".
app.mount('/static', StaticFiles(directory="static"), name="static")

# Включает роутер tasks_router в приложение FastAPI.
app.include_router(tasks_router)

# Включает роутер task_template в приложение FastAPI.
app.include_router(task_template)

# Проверяет, является ли текущий модуль основным модулем (вызывается непосредственно, а не импортируется), и если это так, выполняет следующие действия.
if __name__ == '__main__':
    # Создает все таблицы, определенные в модели TaskModel, в базе данных.
    TaskModel.metadata.create_all(engine)

    # Выводит сообщение о запуске сервера.
    print('Starting server')

    # Запускает сервер FastAPI с помощью uvicorn, слушая порт 8000 и перезапускаясь при любых изменениях в коде.
    uvicorn.run('main:app', port=8000, reload=True)

    # Выводит сообщение об остановке сервера.
    print('Server stopped')
