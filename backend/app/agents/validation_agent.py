def validation_agent(state):

    context = state["context"]

    if not context:

        state["answer"] = (
            "No relevant information found."
        )

    return state