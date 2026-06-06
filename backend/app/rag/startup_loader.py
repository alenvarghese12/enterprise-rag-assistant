import os
from app.config import UPLOAD_FOLDER
from app.services.pdf_loader import load_pdf
from app.rag.chunking import create_chunks
from app.rag.bm25_store import BM25Store

def build_bm25():

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    all_chunks = []

    for pdf in os.listdir(UPLOAD_FOLDER):

        path = os.path.join(
            UPLOAD_FOLDER,
            pdf
        )

        docs = load_pdf(path)

        chunks = create_chunks(docs, pdf)

        all_chunks.extend(chunks)

    if not all_chunks:
        return None

    return BM25Store(all_chunks)