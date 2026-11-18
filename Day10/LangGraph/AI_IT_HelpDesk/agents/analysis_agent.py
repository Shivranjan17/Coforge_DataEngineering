from pydantic import BaseModel,Field
from typing import Literal
from config.settings import llm

class IssueAnalysis(BaseModel):
    category: Literal["Password","Network","Software","Email","Hardware","Other"]
    priority: Literal["Low","Medium","High","Critical"]
    reason:str = Field(description="Short reason for the classification")

analysis_llm = llm.with_structured_output(IssueAnalysis)


def analyze_issue(state):
    prompt=f"""
You are an IT HelpDesk Analysis Agent.
Analyze the employee's IT issue.

Category must be one of:
Password,Network,Software,Email,Hardware,Other.

Priority must beone of:
Low ,Medium,High,Critical.

Use Criticcal for stolen devices,suspected security
breaches,or other urgent security incidents.

Employee Issue:
{state["issue"]}



"""

    result = analysis_llm.invoke(prompt)

    return {
    "category":result.category,
    "priority":result.priority
    }