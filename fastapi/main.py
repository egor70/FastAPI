from fastapi import FastAPI
from routers import task

app = FastAPI(title="Task Manager API", version="1.0.0")

# Подключаем роутеры
app.include_router(task.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Task Manager API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}