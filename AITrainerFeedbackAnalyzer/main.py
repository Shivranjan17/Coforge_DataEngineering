from fastapi import FastAPI
from services.llm_service import analyze_feedback
from models.ai_model import TrainerFeedbackResponse,TrainerFeedbackRequest

app = FastAPI(
    title="AITrainerFeedbackAnalyzer"
)

@app.get("/")
def home():
    return{
        "message":"AI Trainer Feedbacl"
    }

@app.post("/api/v1/analyzer",response_model = TrainerFeedbackResponse)
def trainer_feedback(request:TrainerFeedbackRequest):
    response= analyze_feedback(request)
    return response
    