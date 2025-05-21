# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))

from langchain.schema.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

from app.core.vector_store import get_vector_store

def ingest_to_qdrant(doc_id: str, full_doc: list[tuple[int, str]], collection_name=None):
    store = get_vector_store(collection_name=collection_name or "docs") ## docs is the default collection name

    # Split the content into smaller chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    all_chunks = []

    for page_num, page_text in full_doc:
        paragraphs = [p.strip() for p in page_text.split('\n\n') if p.strip()]
        for para_num, paragraph in enumerate(paragraphs, start=1):
            doc = Document(
                page_content=paragraph,
                metadata={
                    "doc_id": doc_id,
                    "page": page_num,
                    "paragraph": para_num
                }
            )
            chunks = splitter.split_documents([doc])
            all_chunks.extend(chunks)

    store.add_documents(all_chunks)
    print(f"    Ingested {len(all_chunks)} chunks for doc_id={doc_id}")
