# Enterprise AI Knowledge Assistant

Enterprise AI Knowledge Assistant is an Agentic RAG system built with FastAPI, LangGraph, ChromaDB, BM25 Hybrid Search, Ollama, Conversation Memory, and Citation-Based Retrieval.

## Features

- PDF Upload and Processing
- Hybrid Search (BM25 + ChromaDB)
- LangGraph Agent Workflow
- Conversation Memory
- Citation-Based Answers
- Ollama Local LLM
- FastAPI Backend

## Tech Stack

- FastAPI
- LangGraph
- ChromaDB
- BM25
- Ollama
- Sentence Transformers
- Python

## Architecture

User Query
↓
Query Agent
↓
Memory Agent
↓
Search Agent
↓
Hybrid Search
(BM25 + ChromaDB)
↓
Validation Agent
↓
Citation Agent
↓
Response Agent
↓
Ollama

## Installation

```bash
git clone https://github.com/alenvarghese12/enterprise-rag-assistant.git

cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

## API Endpoints

### Upload PDF

POST /upload

### Chat

POST /chat

