from pydantic import BaseModel,Field


class HelpdeskRequest(BaseModel):
    employeeId:str
    employeeName:str
    issue:str=Field(min_legth=5)


class HelpdeskResponse(BaseModel):
    employeeId:str
    category:str
    priority:str
    agentUsed:str
    toolsCalled:list[str]
    resolution:list[str]
    reviewStatus:str
    ticketId:str | None=None
    status:str