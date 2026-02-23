from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from google.api_core.exceptions import ResourceExhausted
from src.app.services.gemini_service import GeminiRAGService
from typing import Callable, Any
import logging
import time

# Configure logging
_logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

router = APIRouter()

# Lazy loading du service
_gemini_service = None


def get_gemini_service() -> GeminiRAGService:
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


def handle_chat_request(chat_func: Callable) -> Callable:
    """
    Decorator handling validation, error handling and logging for chat endpoints.
    Injects service and start_time into the decorated function.
    """

    async def wrapper(request: ChatRequest):
        endpoint_name = "STREAM" if "stream" in chat_func.__name__ else "CHAT"
        try:
            if not request.message or not request.message.strip():
                raise HTTPException(status_code=400, detail="Message cannot be empty")

            _logger.info(f"{endpoint_name}_Q: {request.message}")

            return await chat_func(request)
        except ResourceExhausted:
            _logger.warning(f"{endpoint_name}_RATE_LIMIT | Q: {request.message}")
            raise HTTPException(
                status_code=429,
                detail="Rate limit exceeded. Please try again in a few moments.",
            )
        except Exception as e:
            _logger.error(f"{endpoint_name}_ERROR: {str(e)} | Q: {request.message}")
            raise HTTPException(
                status_code=500, detail=f"Error processing request: {str(e)}"
            )

    return wrapper


def log_chat_response(
    endpoint_name: str, answer: str, sources: list[str] | Any, start_time: float
) -> None:
    duration = time.time() - start_time
    sources_str = ", ".join(
        [s.split("/")[-1].replace(".md", "") for s in sources[:3] if s.strip()]
    )
    _logger.info(f"{endpoint_name}_A: {answer}")
    _logger.info(
        f"{endpoint_name}_META: Duration={duration:.2f}s | Sources={sources_str}"
    )


@router.post("/chat", response_model=ChatResponse)
@handle_chat_request
async def chat(request: ChatRequest):
    """
    Chat endpoint that uses RAG to answer questions about the portfolio
    """
    start_time = time.time()
    service = get_gemini_service()
    result = await service.get_response(request.message, request.history)

    log_chat_response("CHAT", result["answer"], result["sources"], start_time)

    return ChatResponse(response=result["answer"], sources=result["sources"])


@router.post("/chat/stream")
@handle_chat_request
async def chat_stream(request: ChatRequest):
    """
    Streaming chat endpoint that sends response word by word
    """
    start_time = time.time()
    service = get_gemini_service()

    async def generate():
        accumulated_response = ""
        sources: list[str] | Any = []
        async for chunk in service.get_response_stream(
            request.message, request.history
        ):
            if "__SOURCES__:" in chunk:
                sources = chunk.split("__SOURCES__:")[1].split(",")
            else:
                accumulated_response += chunk
            yield chunk
        log_chat_response("STREAM", accumulated_response, sources, start_time)

    return StreamingResponse(generate(), media_type="text/plain")
