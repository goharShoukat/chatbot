from fastapi import FastAPI
from .api.routes.chat import router

app = FastAPI()
app.include_router(router)
