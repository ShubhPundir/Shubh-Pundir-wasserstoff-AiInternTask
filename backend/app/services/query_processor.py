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
        source_docs = result.get("source_documents") or []        

        if not source_docs:
            return "No relevant documents were found for your query."


        # print("\n=== Retrieved Source Docs ===")
        # for doc in source_docs:
        #     print(doc.page_content[:200])  # Show a preview
        # print("=================================\n")
        
        print(f"Retrieved document count: {len(source_docs)}")
        
        return result["result"]
    except Exception as e:
        return f"an error occured: {str(e)}"