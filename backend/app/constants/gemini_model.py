from enum import Enum
from pydantic import BaseModel
from typing import List, Dict


class ModelName(str, Enum):
    GEMINI_25_FLASH_PREVIEW_04_17 = "gemini-2.5-flash-preview-04-17"
    GEMINI_25_FLASH_PREVIEW = "gemini-2.5-flash-preview"
    GEMINI_20_FLASH = "gemini-2.0-flash"


class MediaType(str, Enum):
    AUDIO = "audio"
    IMAGES = "images"
    VIDEOS = "videos"
    TEXT = "text"


MediaTypeInput = Dict[MediaType, bool]
MediaTypeOutput = Dict[MediaType, bool]


class MetaData(BaseModel):
    name: ModelName
    media_type_input: MediaTypeInput
    media_type_output: MediaTypeOutput
    optimised_for: str


class GeminiModel(BaseModel):
    models: Dict[ModelName, MetaData] = {
        ModelName.GEMINI_25_FLASH_PREVIEW_04_17: MetaData(
            name=ModelName.GEMINI_25_FLASH_PREVIEW_04_17,
            media_type_input={m: True for m in MediaType},
            media_type_output={m: (m == MediaType.TEXT) for m in MediaType},
            optimised_for="Adaptive thinking, cost efficiency",
        ),
        ModelName.GEMINI_25_FLASH_PREVIEW: MetaData(
            name=ModelName.GEMINI_25_FLASH_PREVIEW,
            media_type_input={m: True for m in MediaType},
            media_type_output={m: (m == MediaType.TEXT) for m in MediaType},
            optimised_for="Enhanced thinking and reasoning, multimodal understanding, advanced coding, and more",
        ),
        ModelName.GEMINI_20_FLASH: MetaData(
            name=ModelName.GEMINI_20_FLASH,
            media_type_input={m: True for m in MediaType},
            media_type_output={m: True for m in MediaType},
            optimised_for="Next generation features, speed, thinking, realtime streaming, and multimodal generation",
        ),
    }
