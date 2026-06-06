import os

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from app.services.pdf_loader import load_pdf

from app.rag.chunking import create_chunks
from app.rag.vector_store import create_vector_store
import app.core.state as state
from app.rag.startup_loader import build_bm25


router = APIRouter()

@router.post("/upload")

async def upload_pdf(
    file: UploadFile = File(...)
):

    path = f"uploads/{file.filename}"

    with open(path, "wb") as buffer:

        buffer.write(
            await file.read()
        )

    docs = load_pdf(path)

    chunks = create_chunks(docs)

    create_vector_store(chunks)

    # Rebuild the BM25 store with the new document
    state.bm25_store = build_bm25()

    return {
        "message": "Document Indexed"
    }