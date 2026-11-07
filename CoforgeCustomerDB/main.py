from fastapi import FastAPI,Depends
from config.logging_config import logger
from services import customer_service as service
from schema.customer_schema import CustomerResponse, CustomerCreate ,CustomerDelete
from config.database import SessionLocal,engine,Base,get_db
from sqlalchemy.orm import Session
from models.customer_model import Customer
app = FastAPI(
    title="Fast Api is up and running",
    version="1.0.1"
)
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return{
            "Coforge Customer"
        }
@app.get("/customers",response_model=list[CustomerResponse])
def getallcustomers():

    logger.info("GetAllCustomers API called")
    db=SessionLocal()
    try:
        customers = service.get_all_customers(db)
        logger.info(f"Successfully retrived %s customers {len(customers)}",)
        return customers

    finally:
        db.close()

@app.get("/customers/{id}",response_model=CustomerResponse)
def getcustomerbyid(id: int):
    
    db=SessionLocal()
    return service.get_customer_by_id(db,id)

@app.post("/customers",response_model=CustomerResponse)
def createcustomer( customer: CustomerCreate):
    db=SessionLocal()
    return service.add_customer(db,customer)

@app.delete("/customers",response_model=CustomerResponse)
def deletecustomer(customer :CustomerDelete):
    db=SessionLocal()
    return service.delete_employee(db,customer)