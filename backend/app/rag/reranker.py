def rerank_documents(query, documents):

    query_words = set(
        query.lower().split()
    )

    scored = []

    for doc in documents:

        text_words = set(
            doc.page_content.lower().split()
        )

        score = len(
            query_words.intersection(
                text_words
            )
        )

        scored.append((doc, score))

    scored.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return [doc for doc, _ in scored]