

from fastapi import FastAPI
from services.llm_service import calculate_employee_salary
from models.ai_model import SalaryResponse,SalaryRequest

app = FastAPI(
    title="AIEmployeeSalaryAgent"
)

@app.get("/")
def home():
    return{
        "message":"AI Employee Salary Agent"
    }

@app.post("/api/v1/employeeagent",response_model = SalaryResponse)
def employee_agent(request:SalaryRequest):
    response= calculate_employee_salary(request)
    return response
    