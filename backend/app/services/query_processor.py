import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))

from langchain.chains import RetrievalQA
from app.core.llm import get_gemini_llm
from app.core.vector_store import get_vector_store

def query_documents(query: str) -> str:
    try:
        retriever = get_vector_store().as_retriever()
        llm = get_gemini_llm()

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            return_source_documents=True
        )
        result = qa_chain.invoke({"query": query})
        
        print("\n=== Retrieved Source Docs ===")
        for doc in result['source_documents']:
            print(doc.page_content[:200])  # print preview
        print("=============================\n")
        
        return result["result"]
    except Exception as e:
        return f"an error occured: {str(e)}"