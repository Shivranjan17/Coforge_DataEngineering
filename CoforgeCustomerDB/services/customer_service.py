from decimal import Decimal
from sqlalchemy import select,func
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models.customer_model import Customer





#1. ADD Customer


def add_customer(db:Session,data):
    customer = Customer(**data.model_dump())

    db.add(customer)
    try:
        db.commit()
        db.refresh(customer)
        return customer
    except IntegrityError:
        db.rollback()
        raise


#2 Get all Customers
def get_all_customers(db: Session):
    return db.scalars(
        select(Customer).order_by(Customer.customer_id)
    ).all()

#3 Search customer byID
def get_customer_by_id(db:Session,customer_id: int):
    return db.get(Customer,customer_id)

#4 Update Customer
def update_customer(db:Session,customer_id:int,data):
    customer = db.get(Customer,customer_id)

    if customer is None:
        return None
    for key,value in data.model_dump().items():
        setattr(customer,key,value)

    try:
        db.commit()
        db.refresh(customer)
        return customer
    except IntegrityError:
        db.rollback()
        raise



# 5. Delete Customer
def delete_employee(db:Session,customer_id:int):
    customer =db.get(Customer,customer_id)
    if customer is None:
        return False

    db.delete(customer)
    db.commit()
    return True
