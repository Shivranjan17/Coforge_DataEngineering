from crewai import Crew, Process
from agents.approval_agent import approval_agent
from agents.hr_policy_agent import hr_policy_analyst
from agents.leave_verification_agent import leave_verifier
from tasks.leave_task import create_tasks
 
employee_id = int(input("Enter Employee ID: "))
requested_days = int(input("Enter Leave Days: "))
 
if requested_days <= 0:
    raise ValueError("Leave days must be positive")
 
 
tasks = create_tasks(employee_id, requested_days)
 
crew = Crew(
    agents=[
        leave_verifier,
        hr_policy_analyst,
        approval_agent
    ],
    tasks=tasks,
    process=Process.sequential,
    verbose=True
)
 
 
result = crew.kickoff()
 
print("\nFINAL LEAVE WORKFLOW RESULT")
print(result.raw)
 