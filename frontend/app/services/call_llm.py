import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
FAST_API_HOST = f"{os.getenv('FAST_API_HOST')}/chat/stream"


def call_llm(text: str):
    payload = {"query": text}
    foo = requests.post(FAST_API_HOST, data=json.dumps(payload), stream=False)
    bar = foo.content.decode("utf-8")
    return bar
