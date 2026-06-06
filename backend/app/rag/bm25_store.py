from rank_bm25 import BM25Okapi

class BM25Store:

    def __init__(self, chunks):

        self.documents = chunks

        self.tokenized_docs = [
            doc.page_content.lower().split()
            for doc in chunks
        ]

        self.bm25 = BM25Okapi(self.tokenized_docs)

    def search(self, query, top_k=5):

        tokenized_query = query.lower().split()

        scores = self.bm25.get_scores(tokenized_query)

        ranked = sorted(
            zip(self.documents, scores),
            key=lambda x: x[1],
            reverse=True
        )

        return [doc for doc, _ in ranked[:top_k]]