from dotenv import load_dotenv
import os
from ollama import Client

load_dotenv()
OLLAMA_API_HOST = f"{os.getenv('OLLAMA_API_HOST')}"


class OllamaService:
    def __init__(self, address: str = OLLAMA_API_HOST, model: str = "llama3"):
        self._address = address
        self._model = model

    def get_chat_stream(self, query: str):
        client = Client(host=self._address)
        chat_messages: list[dict[str, str]] = [{"role": "user", "content": query}]

        stream = client.chat(model=self._model, messages=chat_messages, stream=True)

        for chunk in stream:
            yield chunk["message"]["content"]
