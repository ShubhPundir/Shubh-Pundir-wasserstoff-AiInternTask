# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))

from langchain.schema.document import Document
from app.core.vector_store import get_vector_store

def ingest_to_qdrant(doc_id: str, content: str, collection_name=None):
    if collection_name:
        store = get_vector_store(collection_name=collection_name)
    else:
        store = get_vector_store()

    langchain_doc = Document(
        page_content=content,
        metadata={"doc_id": doc_id}
    )
    store.add_documents([langchain_doc])
