import os

def citation_agent(state):

    citations = []

    docs = state.get("retrieved_docs", [])

    for doc in docs:

        source = doc.metadata.get("source", "Unknown")
        page = doc.metadata.get("page", "N/A")

        # Keep only filename
        source = os.path.basename(source)

        citation = f"{source} Page {page}"

        if citation not in citations:
            citations.append(citation)

    state["citations"] = citations

    return state