from config.settings import (AZURE_OPENAI_ENDPOINT,AZURE_OPENAI_API_KEY,AZURE_OPENAI_DEPLOYMENT)
from models.ai_model import (RequestAIforText,ResponseAIforText)
from prompts.ai_prompt import (System_Prompt,Human_Prompt)
from openai import OpenAI



#Step 1 Create LLM client outside the function

llm= OpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    base_url=f"{AZURE_OPENAI_ENDPOINT.rstrip('/')}/openai/v1/"
)

# Step 2: Define the service function
def generate_ai_response(request:RequestAIforText)->ResponseAIforText:
#def generate_ai_response(requestfromAI:str)->str:
    #Prepare the human prompt
    
    user_prompt=Human_Prompt.format(requestfromAI=request.requestfromAI)
    
    
    #Step 3 : Invoke the LLM
    response = llm.responses.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        instructions=System_Prompt,
        input=user_prompt
    )

    #Step 4: Extract the generated response
    ai_text = response.output_text

    #Step5 : Return the Pydantic response
    return ResponseAIforText(
        responsefromAI=ai_text)