from fastapi import FastAPI
from fastapi import FastAPI,HTTPException
from models.helpdesk_models import HelpdeskRequest,HelpdeskResponse
from services.llm_service import process_helpdesk_request

app = FastAPI(
    title="Coforge AI Helpdesk Support "
)

@app.post("/analyze", response_model=HelpdeskResponse)
def analyze_employee_issue(request: HelpdeskRequest):
    try:
        result = process_helpdesk_request(request)
        return result
    except Exception:
        raise HTTPException(status_code=500,detail="Unable to process request")


@app.get("/health")
def health():
    return {"status": "healthy"}
