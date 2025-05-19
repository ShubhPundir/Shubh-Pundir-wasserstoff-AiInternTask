import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.app.services.vector_ingest import ingest_to_qdrant

ingest_to_qdrant("doc-001", "This is a sample paragraph about AI and machine learning.", 'Test')
ingest_to_qdrant("doc-002", "This text is about climate change and global warming.", 'Test')
