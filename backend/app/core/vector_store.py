from langchain_community.vectorstores import Qdrant
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from langchain_huggingface import HuggingFaceEmbeddings


def get_qdrant_client():
    client = QdrantClient(path="backend/data/qdrant_db")
    return client

def get_embeddings():
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2") # 384 dimensional vector model

def get_vector_store(collection_name: str = "docs"):
    client = get_qdrant_client()
    embeddings = get_embeddings()

    try:
        client.get_collection(collection_name)
    except ValueError:
        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE),
        )
        print(f"Creating QdrantDB's collection --> {collection_name}")

    return Qdrant(
        client=client,
        collection_name=collection_name,
        embeddings=embeddings
    )
