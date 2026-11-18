from typing import TypedDict
class HelpdeskState(TypedDict):
    employeeId:str
    employeeName:str
    issue:str

    category:str
    priority:str
    resolution:list[str]
    toolsCalled:list[str]

    reviewStatus:str
    reviewReason:str
    ticketId:str| None
    status:str
    finalResponse:dict