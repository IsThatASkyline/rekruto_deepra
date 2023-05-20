from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request, name: str = 'Пользователь', message: str = 'Перейдите на /docs для просмотра документации'):
    return templates.TemplateResponse("index.html", {"request": request, "name": name, "message": message})
