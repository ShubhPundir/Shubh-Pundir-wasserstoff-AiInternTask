import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from qdrant_client import QdrantClient

client = QdrantClient(path="backend/data/qdrant_db")

response = client.scroll(
    collection_name="docs",
    limit=5,  # Fetch a few points to inspect
    with_payload=True
)

for point in response[0]:
    print("ID:", point.id)
    print("Payload:", point.payload)
    print("Contains doc_id:", "doc_id" in point.payload['metadata'])
    print("Contains page:", "page" in point.payload['metadata'])
    print("Contains paragraph:", "paragraph" in point.payload['metadata'])
    print()
