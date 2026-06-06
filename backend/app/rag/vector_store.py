from langchain_community.vectorstores import Chroma
from app.rag.embeddings import get_embedding_model
from app.config import CHROMA_PATH

def create_vector_store(chunks):

    embeddings = get_embedding_model()

    db = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=CHROMA_PATH
    )

    db.persist()

    return db