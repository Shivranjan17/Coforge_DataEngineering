from pathlib import Path
from langchain_openai import AzureOpenAIEmbeddings
from langchain_chroma import Chroma
 
from config.settings import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
    AZURE_OPENAI_ENDPOINT
)
 
Path("vector_store").mkdir(exist_ok=True)
 
embedding = AzureOpenAIEmbeddings(
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_deployment=AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
)
 
vector_db = Chroma(
    collection_name="coforge_hr_knowledge",
    embedding_function=embedding,
    persist_directory="./vector_store"
)


def add_documents(documents,ids):
    vector_db.add_documents(
        documents=documents,
        ids=ids
    )


def delete_document(document_id):
    existing = vector_db.get(
        where={"document_id": document_id}  
    )    
    ids = existing["ids"]
   
    if ids:
        vector_db.delete(ids=ids)
    return len(ids)  


def search_documents(question,k=3):
    results=vector_db.similarity_search(
        question,
        k=k
    )
    return [
        {
            "content":doc.page_content,
            "metadata":doc.metadata
        }
        for doc in results
    ]