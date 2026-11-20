from crewai import Agent
from config.settings import llm
from tools.sql_tools import execute_employee_sql


sql_generator=Agent(
    role="SQL Generator",
    goal="Convert natural language into MySQL SELECT queries" ,
    backstory=(
        "You are a SQL developer who creates"
        "simple employee analytics queries"
    ),
    tool=[execute_employee_sql],
    llm=llm,
    verbose=True,
    allow_dalegation =False

)