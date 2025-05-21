import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import get_MONGO_ATLAS_URI

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# load_dotenv()

# uri: str = os.getenv("MONGO_ATLAS_URI")
uri = get_MONGO_ATLAS_URI()

client = MongoClient(uri, server_api=ServerApi("1"))

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['chat-query']
parsed_docs = db['parsed_docs']
