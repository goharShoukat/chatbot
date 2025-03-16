import requests
import json
import os

OLLAMA_API_HOST = f"{os.getenv('OLLAMA_API_HOST')}/chat/stream"


def call_llm(text: str):
    payload = {"query": text}
    foo = requests.post(OLLAMA_API_HOST, data=json.dumps(payload), stream=False)
    bar = foo.content.decode("utf-8")
    return bar
