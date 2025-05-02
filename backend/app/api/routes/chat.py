import logging
import json
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.utils.llm import LLM

logger = logging.getLogger(__name__)

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    type: str  # e.g., 'text', 'table', 'image', 'chart', etc.
    data: dict  # Contains the actual content based on the type

llm = LLM()

def generate_initial_response(message):
    logger.info("Generating initial response for message: %s", message)
    return llm.generate_response(prompt=message)

def determine_display_format(initial_response):
    logger.info("Determining display format for response: %s", initial_response)
    prompt = (
        "Analyze the following response and determine the best display format for it. "
        "The options are: 'text', 'table', 'image', 'chart', or 'card'.\n"
        f"Response: {initial_response}"
    )
    return llm.generate_response(prompt=prompt)

def convert_to_json_format(initial_response, display_format):
    logger.info("Converting response to JSON format. Response: %s, Format: %s", initial_response, display_format)
    if display_format.strip().lower() == 'image':
        # Example logic for image response formatting
        return json.dumps({
            "type": "image",
            "data": {
                "src": initial_response,  # Assuming the LLM returns the image URL as the response
                "alt": "Generated image based on user query"
            }
        })

    prompt = (
        "Convert the following response into a JSON format suitable for rendering "
        "in a React component. The format should include the type and data fields.\n"
        f"Response: {initial_response}\n"
        f"Display Format: {display_format}"
    )
    return llm.generate_response(prompt=prompt)

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        # Step 1: Generate the initial response
        initial_response = generate_initial_response(request.message)

        # Step 2: Determine the best display format
        display_format = determine_display_format(initial_response)

        # Step 3: Convert the response into a JSON format
        converted_response = convert_to_json_format(initial_response, display_format)

        # Parse the converted response into the expected format
        logger.info("Final converted response: %s", converted_response)
        try:
            response_data = json.loads(converted_response)  # Use json.loads for safer parsing
        except json.JSONDecodeError as e:
            logger.error("JSON decoding failed: %s", str(e))
            raise HTTPException(status_code=500, detail="Invalid JSON format in LLM response")

        return ChatResponse(type=response_data["type"], data=response_data["data"])
    except Exception as e:
        logger.error("Error occurred: %s", str(e))
        raise HTTPException(status_code=500, detail=str(e))