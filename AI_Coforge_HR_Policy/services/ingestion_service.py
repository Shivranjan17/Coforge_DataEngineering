from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
 
BASE_DIR = Path(__file__).resolve().parent.parent
DOCUMENT_PATH = BASE_DIR / "data" / "Hr_Policy.txt"
VECTOR_PATH = BASE_DIR / "vector_store"


EMBEDDING_MODEL="sentence-transformers/all-MiniLM-L6-v2"
def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )


def create_vector_store():
    #Step1 : Load document 
    loader=TextLoader(
        str(DOCUMENT_PATH),
        encoding="utf-8"
    )

    documents=loader.load()
    #step2:Split document
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    chunks=splitter.split_documents(documents)

    #Step3:Generate embeddings

    embeddings=get_embeddings()

    #Step 4:Create Faiss index
    vector_store=FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    #Step5:Save Index
    vector_store.save_local(str(VECTOR_PATH))
    return{
        "message":"Vector store created",
        "total_chunks":len(chunks)
    }
#TextLoader-> Reads the policy file
#RecursiveCharacterTextSplitter->Creates overlapping chunks
#HuggingFaceEmbeddings->Converts text into vectorss
