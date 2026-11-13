from fastapi import FastAPI
from services.llm_service import generate_ai_response
from models.ai_model import (RequestAIforText,ResponseAIforText)


app = FastAPI(
    title="Fast Api is up and running",
    version="1.0.1"
)

@app.get("/")
def home():
    return{
        "message":"AI Text Assistant is working"
    }
@app.post("/api/v1/generate",response_model=ResponseAIforText)
def generate_text(request:RequestAIforText):
    result = generate_ai_response(request)
    return result