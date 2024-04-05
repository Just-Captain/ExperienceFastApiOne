# Импортируем необходимые модули из библиотеки FastAPI
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

# Создаем объект маршрутизатора для обработки URL-адресов, связанных с задачами
task_template = APIRouter()

# Настраиваем шаблонизатор Jinja2 для использования шаблонов из каталога "templates"
templates = Jinja2Templates(directory='templates')

# Определяем обработчик для главного URL-адреса "/"
@task_template.get('/')
def index(request: Request):
    """
    Обработчик для отображения главной страницы
    """
    # Отображаем шаблон "index.html", передавая в него объект запроса
    return templates.TemplateResponse(request=request, name='index.html')
