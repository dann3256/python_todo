from routers import todos ,categories
from fastapi import FastAPI

app = FastAPI()
app.include_router(todos.router)
app.include_router(categories.router)
