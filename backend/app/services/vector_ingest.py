# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))

from langchain.schema.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

from app.core.vector_store import get_vector_store

def ingest_to_qdrant(doc_id: str, content: str, collection_name=None):
    store = get_vector_store(collection_name=collection_name or "docs")

    # Split the content into smaller chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    # Create base Document object with metadata
    base_doc = Document(
        page_content=content,
        metadata={"doc_id": doc_id}
    )

    # Split the document into smaller chunks
    split_docs = splitter.split_documents([base_doc])

    # Add to vector store
    store.add_documents(split_docs)
    print(f"Ingested {len(split_docs)} chunks for doc_id={doc_id}")