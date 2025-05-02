from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from app.core.config import Config

class LLM:
    def __init__(self):
        self.chat_model = ChatOpenAI(
            model="gpt-4",
            openai_api_key=Config.OPENAI_API_KEY,
            temperature=0.7,
            max_tokens=150,
        )

    def generate_response(self, prompt):
        messages = [
            SystemMessage(content="You are a helpful assistant."),
            HumanMessage(content=prompt),
        ]
        response = self.chat_model.invoke(messages)
        return response.content