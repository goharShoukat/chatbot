from fastapi import APIRouter
from starlette.responses import StreamingResponse

from ...services.ollama_service import OllamaService
from ...schemas import ChatRequest

router = APIRouter()


ai_service = OllamaService()


@router.post("/chat/stream")
async def chat_stream(request: ChatRequest):
    return StreamingResponse(
        ai_service.get_chat_stream(request.query), media_type="text/event-stream"
    )
