from fastapi import FastAPI
from routers.employee_router import (
    router as employee_router
)
from routers.knowledge_router import(
    router as Knowledge_router
)

app=FastAPI()
@app.get("/")
def home():
    return{
        "application":"Coforge Enterprse Pipeline",
        "status":"running"
    }

@app.get("/health")
def health():
    return{
        "status":"healthy"
    }

app.include_router(employee_router)
app.include_router(Knowledge_router)