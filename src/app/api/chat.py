from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.app.services.gemini_service import GeminiRAGService

router = APIRouter()

# Lazy loading du service
_gemini_service = None


def get_gemini_service():
    global _gemini_service
    if _gemini_service is None:
        _gemini_service = GeminiRAGService()
    return _gemini_service


class ChatRequest(BaseModel):
    message: str
    history: list[dict] = []


class ChatResponse(BaseModel):
    response: str
    sources: list[str] = []


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Chat endpoint that uses RAG to answer questions about the portfolio
    """
    try:
        if not request.message or not request.message.strip():
            raise HTTPException(status_code=400, detail="Message cannot be empty")

        service = get_gemini_service()
        result = await service.get_response(request.message, request.history)

        return ChatResponse(response=result["answer"], sources=result["sources"])
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error processing request: {str(e)}"
        )
