from fastapi import FastAPI, HTTPException

from models.rag_model import (
    RAGRequest,
    HRPolictyResponse
)

from services.ingestion_service import create_vector_store
from services.rag_service import ask_hr_policy

app = FastAPI(
    title="HR Policy RAG API",
    version="1.0.0",
    description="HR Policy Assistant using Azure OpenAI and FAISS"
)


# -----------------------------------------
# Health Check Endpoint
# -----------------------------------------
@app.get("/")
def home():
    return {
        "message": "HR Policy RAG API is running"
    }


# -----------------------------------------
# Create Vector Store Endpoint
# -----------------------------------------
@app.post("/ingest")
def ingest_policy():
    try:
        result = create_vector_store()
        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# -----------------------------------------
# Ask Question Endpoint
# -----------------------------------------
@app.post(
    "/ask",
    response_model=HRPolictyResponse
)
def ask_question(request: RAGRequest):

    try:
        response = ask_hr_policy(
            request.question
        )

        return response

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )