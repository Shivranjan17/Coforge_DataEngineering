from decimal import Decimal
from sqlalchemy import select,func
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models.employee_model import Employee





#1. ADD employee

# Step 1: Convert the Pydantic employee data into a dictionary
# data.model_dump() converts the request object into key-value pairs
# Example:
# {
# "employee_name": "Rahul",
# "age": 25,
# "email": "rahul@gmail.com",
# "department": "IT",
# "designation": "Developer",
# "salary": 50000,
# "city": "Pune"
# }
#


def add_employee(db:Session,data):
    employee = Employee(**data.model_dump())
# ** unpacks the dictionary into keyword arguments
# Employee() creates a Python object representing a new employee # At this stage, the employee is NOT saved in MySQL employee = Employee(**data.model_dump())
# Step 2: Add the employee object to the SQLAlchemy session
# This tells SQLAlchemy that a new employee needs to be inserted # The employee is still NOT permanently saved in MySQL
    db.add(employee)
# Step 3: Commit the database transaction
# SQLAlchemy sends the INSERT operation to MySQL
# The new employee record is saved permanently in the database
# MySQL automatically generates the employee_id
    try:
        db.commit()
# Step 4: Refresh the employee object from the database
# This retrieves the latest employee information from MySQL
# It ensures that generated values, such as employee_id,
# are available in the Python employee object
        db.refresh(employee)
        return employee
    except IntegrityError:
        db.rollback()
        raise
# Step 5: Return the newly created employee object
# FastAPI can use this object to generate the API response
# The response may contain employee_id, employee_name,
# age, email, department, designation, salary and city
# data.model_dump() -> Converts Pydantic data into a dictionary
# ** -> Unpacks dictionary values as keyword arguments
# Employee(...) -> Creates an Employee object
#db.add(employee) -> Adds the employee to the session

#2 Display all employees
def get_all_employees(db: Session):
    return db.scalars(
        select(Employee).order_by(Employee.employee_id)
    ).all()

#3 Search employee byID
def get_employee_by_id(db:Session,employee_id: int):
    return db.get(Employee,employee_id)

#4 Update employee
def update_employee(db:Session,employee_id:int,data):
    employee = db.get(Employee,employee_id)

    if employee is None:
        return None
    for key,value in data.model_dump().items():
        setattr(employee,key,value)

    try:
        db.commit()
        db.refresh(employee)
        return employee
    except IntegrityError:
        db.rollback()
        raise



# 5. Delete Employee
def delete_employee(db:Session,employee_id:int):
    employee=db.get(Employee,employee_id)
    if employee is None:
        return False

    db.delete(employee)
    db.commit()
    return True
