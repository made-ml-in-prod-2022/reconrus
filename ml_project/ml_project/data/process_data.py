from typing import Optional

import numpy as np
import pandas as pd

from ml_project.features.build_features import OneHotTransformer
from ml_project.utils.read_files import read_csv


def split_data(X: pd.DataFrame, y: Optional[np.array], val_size: float
              ) -> tuple[pd.DataFrame, np.array, pd.DataFrame, np.array]:
    """Splits training data into two parts

    :param data: dataframe to split
    :param split_ratio: ratio of a data that'll go to the first dataframe
    :return: X_train, y_train, X_valid, y_valid
    """
    msk = np.random.rand(len(X)) < val_size
    X_train, X_valid = X[~msk], X[msk]
    y_train, y_valid = y[~msk], y[msk]
    return X_train, y_train, X_valid, y_valid


def split_features_and_target(data: pd.DataFrame, target_column: str) -> tuple[pd.DataFrame, np.array]:
    assert target_column in data.columns, (
        f'Target column {target_column} not in dataframe. Columns: {data.columns}'
    )
    X = data.loc[:, data.columns != target_column]
    y = data[target_column].to_numpy()
    return X, y


def process_data(transformer: OneHotTransformer, X: pd.DataFrame, y: Optional[np.array] = None,
                 val_size: Optional[float] = None, drop_columns: Optional[list[str]] = None,
                 ) -> tuple[pd.DataFrame, np.array, Optional[pd.DataFrame], Optional[np.array]]:
    
    X = X.drop(labels=drop_columns, axis=1) if drop_columns else X
    
    if y is not None and val_size:
        X_train, y_train, X_valid, y_valid = split_data(X, y, val_size)
        X_valid, y_valid = transformer.transform(X_valid, y_valid)
    else: 
        X_train, y_train = X, y
        X_valid, y_valid = None, None

    X_train, y_train = transformer.transform(X_train, y_train)
    return X_train, y_train, X_valid, y_valid
