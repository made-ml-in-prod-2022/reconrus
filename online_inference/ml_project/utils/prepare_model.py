import logging
import os

import pickle
import requests
from sklearn.base import BaseEstimator
from sklearn.linear_model import LogisticRegression

from ..features.build_features import OneHotTransformer

MODEL_URL = os.environ["MODEL_URL"]
TOKENIZER_URL = os.environ["TOKENIZER_URL"]

MODEL_PATH = "models/model.pkl"
TOKENIZER_PATH = "models/tokenizer.pkl"


def download_model(url: str, path_to_store: str) -> None:
    logging.debug(f"Downloading model to {path_to_store}")
    response = requests.get(url)
    with open(path_to_store, "wb+") as fout:
        fout.write(response.content)
    logging.debug(f"Finished model downloading to {path_to_store}")


def _load_model(model_path: str, model_url: str) -> BaseEstimator:
    dir_path = os.path.dirname(model_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    if not os.path.exists(model_path):
        download_model(model_url, model_path)

    logging.debug(f"Started model loading from {model_path}")
    with open(model_path, "rb") as fin:
        model = pickle.load(fin)
    logging.debug(f"Loaded model from {model_path}")
    return model


def load_model() -> LogisticRegression:
    return _load_model(MODEL_PATH, MODEL_URL)


def load_tokenizer() -> OneHotTransformer:
    return _load_model(TOKENIZER_PATH, TOKENIZER_URL)
