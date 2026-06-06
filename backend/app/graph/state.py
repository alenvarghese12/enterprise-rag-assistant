from typing import TypedDict, List

class AgentState(TypedDict):

    question: str

    enhanced_question: str

    retrieved_docs: list

    context: str

    citations: List[str]

    answer: str