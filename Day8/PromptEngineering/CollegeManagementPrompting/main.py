from fastapi import FastAPI
from services.llm_service import analyze_student_profile
from models.ai_model import( StudentResponse,StudentAnalysis,StudentRequest)

app= FastAPI(title="Student Profile Analysis")

@app.get("/")
def home():
    return{
        "message":"One Shot  Programming API"
    }


@app.post("/api/v1/profile-analyzer",response_model=StudentResponse)
def analyzer(
    request:StudentRequest
):
    result = analyze_student_profile(request)
    return result