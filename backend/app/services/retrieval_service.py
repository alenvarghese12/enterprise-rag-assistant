from app.rag.hybrid_search import HybridSearch
from app.rag.reranker import rerank_documents
from app.rag.context_builder import build_context
import app.core.state as state

def retrieve_context(query):

    if state.bm25_store is None:
        raise Exception(
            "BM25 store not initialized"
        )

    hybrid = HybridSearch(
        state.bm25_store
    )

    results = hybrid.search(query)

    ranked = rerank_documents(
        query,
        results
    )

    top_docs = ranked[:5]

    context = build_context(
        top_docs
    )

    return context, top_docs