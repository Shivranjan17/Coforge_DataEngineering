from decimal import Decimal
from pydantic import(
    BaseModel,Field,EmailStr,ConfigDict
)

class CustomerBase(BaseModel):
    customer_name: str = Field(min_length=2)
    age:int =Field(ge=18,le=70)
    email:EmailStr
    gender:str=Field(min_length=1)
   


class CustomerCreate(CustomerBase):
    pass
class CustomerUpdate(CustomerBase):
    pass
class CustomerResponse(CustomerBase):
    customer_id:int
    model_config=ConfigDict(from_attributes=True)


class CustomerDelete(CustomerBase):
     customer_id:int
     model_config=ConfigDict(from_attributes=True)

