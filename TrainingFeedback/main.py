from fastapi import FastAPI,Depends

from services import employee_service as service
from schemes.employee_schema import EmployeeResponse, EmployeeCreate
from config.database import SessionLocal,engine,Base,get_db
from sqlalchemy.orm import Session
from models.employee_model import Employee
app = FastAPI(
    title="Fast Api is up and running",
    version="1.0.1"
)
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return{
            "msg":"Fastapi is up and running "
        }
@app.get("/employees",response_model=list[EmployeeResponse])
def getallemployee():
    db=SessionLocal()
    return service.get_all_employees(db)

@app.get("/employees/{id}",response_model=EmployeeResponse)
def getemployeebyid(id: int):
    
    db=SessionLocal()
    return service.get_employee_by_id(db,id)

@app.post("/employees",response_model=EmployeeResponse)
def createemployee( employee: EmployeeCreate):
    db=SessionLocal()
    return service.add_employee(db,employee)
