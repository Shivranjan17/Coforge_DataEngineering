from config.settings import (AZURE_OPENAI_API_KEY,AZURE_OPENAI_API_VERSION,AZURE_OPENAI_DEPLOYMENT,AZURE_OPENAI_ENDPOINT)
import json
from models.ai_model import (StudentPerformanceAnalysis,StudentPerformanceRequest,StudentPerformanceResponse)
from prompts.ai_prompt import (SYSTEM_PROMPT,HUMAN_PROMPT)
from openai import AzureOpenAI

llm = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT,
    api_version=AZURE_OPENAI_API_VERSION,
)

def analyze_student_performance(request:StudentPerformanceRequest)->StudentPerformanceResponse:
   
   user_prompt=HUMAN_PROMPT.format(
   
    student_id=request.student_id,
    student_name=request.student_name,
    python_marks=request.python_marks,
    sql_marks=request.sql_marks,
    fastapi_marks=request.fastapi_marks
   )

   response = llm.chat.completions.create(
      model=AZURE_OPENAI_DEPLOYMENT,
      messages=[
            {
               "role":"system",
               "content":SYSTEM_PROMPT
            },
            {
               "role":"user",
               "content":user_prompt
            }

         
      ],
      response_format={"type":"json_object"}
   )
   content=response.choices[0].message.content

   if not content:
      raise ValueError("AI Return Empty Response")
   ai_analysis=StudentPerformanceAnalysis(**json.loads(content))
   return StudentPerformanceResponse(
      student_id=request.student_id,
      student_name=request.student_name,
      analysis= ai_analysis
     # improvement_suggestion= []
   )
