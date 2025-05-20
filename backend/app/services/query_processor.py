import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))

from langchain.chains import RetrievalQA
from app.core.llm import get_gemini_llm
from app.core.vector_store import get_vector_store

def query_documents(query: str) -> str:
    retriever = get_vector_store().as_retriever()
    llm = get_gemini_llm()

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    result = qa_chain.invoke({"query": query})
    return result["result"]
