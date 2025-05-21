import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))

from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from app.core.llm import get_gemini_llm
from app.core.vector_store import get_vector_store

def query_documents(query: str) -> dict:
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
            return {
                "synthesized_answer": "No relevant documents were found for your query.",
                "citations": []
            }

        print(f"Retrieved document count: {len(source_docs)}")

        # === Build context for synthesis ===
        context = "\n\n".join([doc.page_content for doc in source_docs])

        # === Use Gemini to synthesize the final answer ===
        synthesis_prompt = PromptTemplate.from_template(
            """You are an AI assistant. Based on the following excerpts from multiple documents, \
            generate a clear and concise answer to the user's query. \
            {context} \
            Answer:"""
        )

        synthesis_chain = LLMChain(llm=llm, prompt=synthesis_prompt)
        synthesized_answer = synthesis_chain.run({"context": context})

        # === Build citations ===
        citations = []
        for doc in source_docs:
            metadata = doc.metadata
            citations.append({
                "Document ID": metadata.get("doc_id") or "N/A",
                "Extracted Answer": doc.page_content.strip(),
                "Citation": f"Page {metadata.get('page') or 'N/A'}, Para {metadata.get('paragraph') or'N/A'}"
            })

        return {
            "synthesized_answer": synthesized_answer.strip(),
            "citations": citations
        }

    except Exception as e:
        return {
            "synthesized_answer": "",
            "citations": [],
            "error": f"An error occurred: {str(e)}"
        }