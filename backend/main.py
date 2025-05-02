import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from middleware import add_middlewares
from utils.llm import LLM

# Print the current environment when the application starts
print(f"Environment: {os.getenv('ENV', 'development')}")

app = FastAPI(docs_url="/swagger")
add_middlewares(app)

# Chat API
class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

llm = LLM()

@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        completion = llm.generate_response(prompt=request.message)
        return ChatResponse(response=completion)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Items API (example placeholder)
@app.get("/api/items")
def get_items():
    return {"items": ["item1", "item2", "item3"]}

@app.get("/api/")
def read_root_api():
    return {"message": "Hello World : api"}

@app.get("/")
def read_root():
    return {"message": "Hello World : root"}
