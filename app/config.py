import os
from dotenv import load_dotenv

load_dotenv()


OLLAMA_URL = "http://localhost:11434/api/embeddings"
EMBEDDING_MODEL = "nomic-embed-text"
EMBEDDING_DIMENSION = 768

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

if not PINECONE_API_KEY:
    raise ValueError("PINECONE_API_KEY is not set")

if not PINECONE_INDEX_NAME:
    raise ValueError("PINECONE_INDEX_NAME is not set")
