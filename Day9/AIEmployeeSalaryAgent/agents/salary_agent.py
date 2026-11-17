from langchain.agents import create_agent
from langchain_openai import AzureChatOpenAI


from config.settings import(AZURE_OPENAI_API_KEY,AZURE_OPENAI_API_VERSION,AZURE_OPENAI_DEPLOYMENT,AZURE_OPENAI_ENDPOINT)
from prompts.ai_prompt import (SALARY_SYSTEM_PROMPT)
from models.ai_model import SalaryRequest,SalaryResponse
from tools.ai_tools import calculate_basic_salary,calculate_da,calculate_gross_salary,calculate_hra

def create_salary_agent():
    #Step1:Connect to Azure OpenAI
    llm = AzureChatOpenAI(
        api_key=AZURE_OPENAI_API_KEY,
        azure_deployment=AZURE_OPENAI_DEPLOYMENT,
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_version=AZURE_OPENAI_API_VERSION,
        temperature=0
    )

    #Step2 Register four tools
    salary_tools=[
        calculate_basic_salary,
        calculate_hra,
        calculate_gross_salary,
        calculate_da
    ]

    #Step3 Create AI agent
    agent=create_agent(
        model=llm,
        tools=salary_tools,
        system_prompt=SALARY_SYSTEM_PROMPT
    )
    return agent