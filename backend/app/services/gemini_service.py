from google import genai
from dotenv import load_dotenv
import os
from google.genai.types import HttpOptions
import vertexai
from vertexai.preview.generative_models import GenerativeModel
from typing import List
from constants import GeminiModel

load_dotenv()


vertexai.init()
model = GenerativeModel("gemini-2.0-flash")
response = model.generate_content("Say hi")
# print(response.candidates[0].content.parts[0].text)
print(response)


class GeminiService:
    __slots__ = ["__metadata", "model"]

    def __init__(self, metadata: List[str | None], model: GeminiModel):
        self.__metadata = metadata
        self.model = model
