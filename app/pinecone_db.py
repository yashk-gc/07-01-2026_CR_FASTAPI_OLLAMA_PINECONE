import uuid
from pinecone import Pinecone
from app.config import PINECONE_API_KEY, PINECONE_INDEX_NAME

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX_NAME)


def store_embedding(text: str, embedding: list[float]) -> str:
    vector_id = str(uuid.uuid4())

    index.upsert(
        vectors=[
            {
                "id": vector_id,
                "values": embedding,
                "metadata": {
                    "text": text
                }
            }
        ]
    )

    return vector_id

def search_embeddings(query_embedding: list[float], top_k: int = 3):
    result = index.query(
        vector=query_embedding,
        top_k=top_k,
        include_metadata=True
    )

    return result["matches"]
