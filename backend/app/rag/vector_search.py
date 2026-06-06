from langchain_community.vectorstores import Chroma
from app.rag.embeddings import get_embedding_model
from app.config import CHROMA_PATH

def semantic_search(query, k=5):

    embeddings = get_embedding_model()

    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings
    )
    all_docs = db.get()

    results = db.similarity_search(
        query,
        k=k
    )

    return results