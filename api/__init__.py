from fastapi import FastAPI
from .v1.api import router

app = FastAPI()
app.mount("/v1", router)
