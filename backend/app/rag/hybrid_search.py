from app.rag.vector_search import semantic_search

class HybridSearch:

    def __init__(self, bm25_store):

        self.bm25_store = bm25_store

    def search(self, query):

        bm25_results = self.bm25_store.search(
            query,
            top_k=5
        )

        semantic_results = semantic_search(
            query,
            k=5
        )

        combined = bm25_results + semantic_results

        unique_docs = []

        seen = set()

        for doc in combined:

            text = doc.page_content

            if text not in seen:

                seen.add(text)

                unique_docs.append(doc)

        return unique_docs[:10]