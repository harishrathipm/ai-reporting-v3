from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.utils.llm import LLM

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

llm = LLM()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        completion = llm.generate_response(prompt=request.message)
        return ChatResponse(response=completion)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))