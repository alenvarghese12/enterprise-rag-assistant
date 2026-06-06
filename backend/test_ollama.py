# from app.services.ollama_service import generate_response

# response = generate_response("What is AI?")

# print("\nResponse:")
# print(response)


# import app.core.state as state

# from app.rag.startup_loader import build_bm25
# from app.graph.workflow import graph

# state.bm25_store = build_bm25()

# result = graph.invoke(
#     {
#         "question": "Can it be carried forward?"
#     }
# )

# print(result["answer"])



from app.graph.workflow import graph
import app.core.state as state
from app.rag.startup_loader import build_bm25

state.bm25_store = build_bm25()

result1 = graph.invoke(
    {
        "question":
        "What is the leave policy?"
    }
)

print(result1["answer"])

result2 = graph.invoke(
    {
        "question":
        "Can it be carried forward?"
    }
)

print(result2["answer"])