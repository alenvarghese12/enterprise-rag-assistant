from contextlib import asynccontextmanager
from fastapi import FastAPI
# from app.services.ollama_service import generate_response
from app.api.chat import router as chat_router
from app.api.upload import router as upload_router
from app.rag.startup_loader import build_bm25
# from app.rag.bm25_store import bm25_store
import app.core.state as state

__all__ = ["app"]

@asynccontextmanager
async def lifespan(_: FastAPI):
    # Startup
    # global bm25_store
    # bm25_store = build_bm25()
    state.bm25_store = build_bm25()
    print("BM25 Loaded Successfully")
    yield
    # Shutdown

app = FastAPI(
    title="Enterprise AI Knowledge Assistant",
    lifespan=lifespan
)

@app.get("/")
def root():
    return {
        "message": "Enterprise AI Assistant Running"
    }

# @app.post("/chat")
# def chat(question: str):
#     answer = generate_response(question)
#     return {"answer": answer}

app.include_router(chat_router)

app.include_router(upload_router)