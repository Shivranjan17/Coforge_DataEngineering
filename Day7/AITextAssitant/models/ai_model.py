from pydantic import BaseModel

class RequestAIforText(BaseModel):
    requestfromAI :str


class ResponseAIforText(BaseModel):
    #requestfromAI:str
    responsefromAI:str

