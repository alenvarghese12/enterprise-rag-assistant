from fastapi import APIRouter
from pydantic import BaseModel

from app.services.retrieval_service import retrieve_context
from app.services.ollama_service import generate_response
from app.graph.workflow import graph

router = APIRouter()

class ChatRequest(BaseModel):
    question: str

@router.post("/chat")
async def chat(request: ChatRequest):

    result = graph.invoke(
        {
            "question": request.question
        }
    )

    return {
        "answer": result["answer"]
        
    }