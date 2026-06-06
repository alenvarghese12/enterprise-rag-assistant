from app.services.retrieval_service import retrieve_context

def search_agent(state):

    question = state["enhanced_question"]

    context, docs = retrieve_context(
        question
    )

    state["context"] = context
    state["retrieved_docs"] = docs

    return state