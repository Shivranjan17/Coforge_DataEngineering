from fastapi import FastAPI, HTTPException

from models.ai_model import (
    LearnerRequest,
    LearnerResponse
)

from services.llm_service import analyze_learner


app = FastAPI()

@app.post(
    "/app/v1/analyze",
    response_model=LearnerResponse
)
def analyze(data: LearnerRequest):
    return analyze_learner(data)