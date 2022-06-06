import os
from http import HTTPStatus
from posixpath import dirname
from typing import Literal

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel, Field

from ml_project.predict.predict import predict_label
from ml_project.utils.logger import setup_logger
from ml_project.utils.prepare_model import load_model, load_tokenizer


class Request(BaseModel):
    age: int = Field(ge=0, le=130)
    sex: Literal[0, 1]
    cp: Literal[0, 1, 2, 3]
    trestbps: int = Field(ge=0)
    chol: int = Field(ge=0)
    fbs: Literal[0, 1]
    restecg: Literal[0, 1, 2]
    thalach: int = Field(ge=0)
    exang: Literal[0, 1]
    oldpeak: float = Field(ge=0)
    slope: Literal[0, 1, 2]
    ca: Literal[0, 1, 2, 3]
    thal: Literal[0, 1, 2]


model = None
tokenizer = None

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_error_handler(request, exc):
    return PlainTextResponse(status_code=HTTPStatus.BAD_REQUEST)


@app.on_event("startup")
def load_models():
    global model
    global tokenizer
    model = load_model()
    tokenizer = load_tokenizer()


@app.post("/predict")
async def predict(request: Request):
    data = dict(request)
    label = predict_label(data, model, tokenizer)
    return label


@app.get("/health")
async def health():
    if model is None or tokenizer is None:
        raise HTTPException(HTTPStatus.SERVICE_UNAVAILABLE)


if __name__ == "__main__":
    parent_dir = dirname(os.path.abspath(__file__))
    config_path = os.path.join(parent_dir, "configs", "logging_config.yaml")
    setup_logger(config_path)

    uvicorn.run(app, host="0.0.0.0", port=8000)
