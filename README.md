# 07-01-2026_CR_FASTAPI_OLLAMA_PINECONE
FastAPI + Ollama + Pinecone vector ingestion and search API


# FastAPI + Ollama + Pinecone Vector API

This project implements a **vector ingestion and semantic search API** using **FastAPI**, **Ollama**, and **Pinecone**.

The API converts input text into embeddings using Ollama and stores them in Pinecone, enabling semantic similarity search over stored content.

---

## What It Does

- Accepts text input via API
- Generates vector embeddings using Ollama
- Stores embeddings in Pinecone Vector Database
- Retrieves semantically similar content with similarity scores

---

## How It Works

Client Request
↓
FastAPI
↓
Ollama (Embedding Generation)
↓
Pinecone (Vector Storage & Search)


---

## Tech Stack

- **Backend**: FastAPI (Python)
- **Embeddings**: Ollama (`nomic-embed-text`)
- **Vector Database**: Pinecone
- **Testing**: Pytest
- **Config Management**: Environment variables

---

## API Endpoints

- `POST /store` – Store text as vector embeddings
- `POST /search` – Retrieve semantically similar content

---

## Notes

- Focuses on vector ingestion and retrieval
- Designed as a foundation for RAG-based systems
- LLM-based answer generation can be added later
  

