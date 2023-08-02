# pylint: disable=missing-module-docstring
from fastapi import FastAPI
from v1.endpoints.facial_recognition_routes import router as facial_recognition

app = FastAPI()

app.include_router(facial_recognition,
                   prefix="/facial_recognition", tags=["facial recognition"])
