import logging
from typing import Any

import hydra
import numpy as np
import pickle

from ml_project.data.process_data import process_data, split_data, split_features_and_target
from ml_project.entities.training_params import TrainingParams
from ml_project.features.build_features import OneHotTransformer
from ml_project.models.trainer import evaluate, train_model
from ml_project.models.predict import predict
from ml_project.utils.logger import setup_logger
from ml_project.utils.read_files import read_csv


def save_model(model: Any, model_path: str):
    logging.debug(f'Started model saving to {model_path}')
    with open(model_path, 'wb+') as fout:
        pickle.dump(model, fout)
    logging.debug(f'Saved model to {model_path}')


@hydra.main(config_path='configs', config_name='train_config')
def train_pipeline(params: TrainingParams):    
    setup_logger(params.logging_config)

    data = read_csv(params.data_path)

    X, y = split_features_and_target(data, params.feature_params.target_column)

    transformer = OneHotTransformer(params.feature_params.categorical_columns)
    transformer = transformer.fit(X)
    save_model(transformer, params.transformer_path)

    X_train, y_train, X_valid, y_valid = process_data(transformer, X, y, params.splitting_params.val_size)
    model = train_model(X_train, y_train, params.model_type, **params.model_params)

    predictions = predict(model, X_valid)
    metrics = evaluate(predictions, y_valid)
    logging.info(f'Training finished. Got following metrics:\n{metrics}')
    
    save_model(model, params.model_output_path)

if __name__=='__main__':
    train_pipeline()
