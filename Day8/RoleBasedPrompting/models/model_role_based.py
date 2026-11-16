from pydantic import BaseModel
from typing import Literal

class PythonAIRequest(BaseModel):
    learner_name:str
    question:str
    experience_level:Literal["Fresher","Intermediate","Experienced"]


class PythonAIResponse(BaseModel):
    learner_name:str
    role:str
    answer:str

    