from fastapi import FastAPI
from services.llm_service import analyze_python_role_based

from models.model_role_based import (
    PythonAIResponse,
    PythonAIRequest
)

app = FastAPI(
    title="Role Based Programming API"
)

@app.get("/")
def home():
    return{
        "message":"Role Based Programming API"
    }


@app.post("/v1/api/analyze_data",response_model=PythonAIResponse)
def analyze(
        request:PythonAIRequest
):
    result = analyze_python_role_based(request)
    return result
