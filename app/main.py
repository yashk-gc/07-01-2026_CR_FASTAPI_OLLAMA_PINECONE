from fastapi import FastAPI
from pydantic import BaseModel

from app.ollama import generate_embedding
from app.pinecone_db import store_embedding, search_embeddings

app = FastAPI(title="Vector Ingestion API")


class StoreRequest(BaseModel):
    query: str


@app.post("/store")
def store_vector(request: StoreRequest):
    embedding = generate_embedding(request.query)

    vector_id = store_embedding(
        text=request.query,
        embedding=embedding
    )

    return {
        "status": "stored",
        "id": vector_id,
        "dimension": len(embedding)
    }


@app.post("/search")
def search_vector(request: StoreRequest):
    query_embedding = generate_embedding(request.query)

    matches = search_embeddings(query_embedding)

    response = []
    for match in matches:
        response.append({
            "score": match["score"],
            "text": match["metadata"]["text"]
        })

    return {
        "query": request.query,
        "results": response
    }
