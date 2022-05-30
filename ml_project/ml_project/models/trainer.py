import logging
from pydoc import locate
from typing import Any

import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score, f1_score, precision_score,
    recall_score, roc_auc_score,
)

from ml_project.entities.training_params import TrainingParams


def train_model(X: pd.DataFrame, y: pd.Series, model_type: str, **model_params):
    model_type = locate(model_type)
    model = model_type(**model_params)

    logging.debug(f'Started {model_type} model training')
    model.fit(X, y)
    logging.debug('Finished model training')
    return model


def evaluate(predictions: np.array, target: np.array) -> dict[str, float]:
    return {
        'accuracy': round(accuracy_score(target, predictions), 4),
        'roc_auc': round(roc_auc_score(target, predictions), 4),
        'f1': round(f1_score(target, predictions), 4),
        'precision': round(precision_score(target, predictions), 4),
        'recall': round(recall_score(target, predictions), 4)
    }
