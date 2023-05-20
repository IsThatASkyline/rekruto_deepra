from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def index(name: str = 'Пользователь', message: str = 'Перейдите на /docs для просмотра документации'):
    return f"""
    <html>
        <head>
            <title>Hello, {name}!</title>
        </head>
        <body>
            <h1>Hello, {name}!</h1>
            <p>{message}</p>
        </body>
    </html>
    """
