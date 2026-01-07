import requests
from app.config import OLLAMA_URL, EMBEDDING_MODEL


def generate_embedding(text: str) -> list[float]:
    payload = {
        "model": EMBEDDING_MODEL,
        "prompt": text
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    return response.json()["embedding"]
