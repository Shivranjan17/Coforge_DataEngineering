
from config.settings import (AZURE_OPENAI_ENDPOINT,AZURE_OPENAI_API_KEY,AZURE_OPENAI_API_VERSION,AZURE_OPENAI_DEPLOYMENT)
from models.ai_model import (TrainerFeedbackRequest,TrainerFeedbackResponse)
from prompts.ai_prompt import (SYSTEMPROMPT,HUMANPROMPT)
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

import json

llm = AzureChatOpenAI(
   api_key= AZURE_OPENAI_API_KEY,
   azure_endpoint=AZURE_OPENAI_ENDPOINT,
   azure_deployment=AZURE_OPENAI_DEPLOYMENT,
   api_version=AZURE_OPENAI_API_VERSION

)

structured_LLM=llm.with_structured_output(TrainerFeedbackResponse)

#Create the Prompt 
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
chain=prompt | structured_LLM

def analyze_feedback(request:TrainerFeedbackRequest)->TrainerFeedbackResponse:
    result = chain.invoke({
        "trainer_name" :request.trainer_name,
        "training_topic":request.training_topic,
        "learner_name":request.learner_name,
        "rating":request.rating,
        "feedback":request.feedback
    })

    return result