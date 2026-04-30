from fastapi import FastAPI
from database import create_db
from routers import todos, categories

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db()  # 起動時にテーブルを作成

app.include_router(todos.router)
app.include_router(categories.router)