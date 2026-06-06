from app.services.ollama_service import generate_response
from app.memory.store import conversation_memory

def response_agent(state):

    question = state["question"]

    context = state["context"]

    prompt = f"""
    You are an enterprise knowledge assistant.

    Answer ONLY using the provided context.

    If the answer is not present in the context,
    say "I could not find that information in the documents."

    Context:
    {context}

    Question:
    {question}
    """

    answer = generate_response(prompt)

    # state["answer"] = answer
    citations_text = "\n\nSources:\n"

    for citation in state["citations"]:
        citations_text += f"- {citation}\n"

    state["answer"] = answer + citations_text
    
    
    conversation_memory["last_question"] = (
    state["question"]
    )

    conversation_memory["last_answer"] = (
    answer
    )

    return state

# app/agents/response_agent.py
# def response_agent(state):
#     question = state["question"] 
#     context = state["context"]
#     last_answer = conversation_memory.get("last_answer", "No previous context.")

#     prompt = f"""You are a precise enterprise knowledge assistant.
# Your job is to answer the Current Question using ONLY the provided Document Context.

# Rules:
# 1. Base your answer strictly on the Document Context.
# 2. If the context does not contain the answer, say exactly: "I could not find that information in the documents."
# 3. Do NOT invent information, do NOT ask follow-up questions, and do NOT write anything after your answer.

# Document Context:
# \"\"\"
# {context}
# \"\"\"

# Current Question: {question}
# Answer:"""

#     # Generate the response from your ollama service
#     answer = generate_response(prompt).strip()
    
#     # Clean up any leftover hallucinations just in case the model slipped
#     if "Question:" in answer:
#         answer = answer.split("Question:")[0].strip()
#     if "However," in answer:
#         answer = answer.split("However,")[0].strip()

#     # Append citations cleanly
#     citations_text = "\n\nSources:\n" + "\n".join([f"- {c}" for c in state.get("citations", [])])
#     state["answer"] = answer + citations_text
    
#     # Update memory metrics
#     conversation_memory["last_question"] = question
#     conversation_memory["last_answer"] = answer

#     return state