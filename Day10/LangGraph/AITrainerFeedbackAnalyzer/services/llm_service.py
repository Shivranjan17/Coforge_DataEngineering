from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from config.settings import (AZURE_OPENAI_ENDPOINT,AZURE_OPENAI_API_KEY,AZURE_OPENAI_API_VERSION,AZURE_OPENAI_DEPLOYMENT)
from models.training_model import (TrainerRequest,TrainerResponse)
from prompts.training_prompt import (SYSTEMPROMPT,HUMANPROMPT)
 
llm = AzureChatOpenAI(
   api_key= AZURE_OPENAI_API_KEY,
   azure_endpoint=AZURE_OPENAI_ENDPOINT,
   azure_deployment=AZURE_OPENAI_DEPLOYMENT,
   api_version=AZURE_OPENAI_API_VERSION
)
 
structured_llm = llm.with_structured_output(
    TrainerResponse
)
 
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system" ,SYSTEMPROMPT
        ),
        (
            "human",HUMANPROMPT
        )
 
    ]
)
 
chain = prompt | structured_llm
 
def analyze_feedback(request:TrainerRequest) -> TrainerResponse:
 
    result = chain.invoke({
        "trainer_name": request.trainer_name,
        "learner_name": request.learner_name,
        "trainer_rating": request.trainer_rating,
        "trainer_feedback": request.trainer_feedback,
        "training_topic": request.training_topic
    })
 
    return result  