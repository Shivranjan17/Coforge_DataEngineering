from fastapi import FastAPI
from services.llm_service import analyze_student_performance
from models.ai_model import (StudentPerformanceResponse,StudentPerformanceAnalysis,StudentPerformanceRequest)

app=FastAPI(title="Student Performance API Is Running ")


@app.get("/")
def home():
    return{
        "message":"Chain of thoughts Programming API"
    }

@app.post("/app/v1/student_performance",response_model=StudentPerformanceResponse)

def student_performance(
    request:StudentPerformanceRequest
):

    result = analyze_student_performance(request)
    return result
