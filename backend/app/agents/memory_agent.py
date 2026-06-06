from app.memory.store import conversation_memory

def memory_agent(state):

    question = state["question"]

    last_question = conversation_memory.get(
        "last_question",
        ""
    )

    enhanced_question = question

    if (
        question.lower().startswith("can it")
        and last_question
    ): 

        enhanced_question = (
            f"{question} "
            f"regarding {last_question}"
        )

    state["enhanced_question"] = enhanced_question

    print(
    "Previous Question:",
    last_question
    )

    print(
    "Enhanced Question:",
    enhanced_question
    )

    return state