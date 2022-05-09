import logging
from typing import Optional

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

logger = logging.getLogger(__name__)

# https://towardsdatascience.com/pipelines-custom-transformers-in-scikit-learn-the-step-by-step-guide-with-python-code-4a7d9b068156
class OneHotTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, categorical_columns: list[str]):
        self.categorical_columns = categorical_columns
        self.transformed_columns = []

    def fit(self, X, y=None):
        assert all([column in X.columns for column in self.categorical_columns]), (
               'Categorical columns in Transformer are not part of a DataFrame'
        )
        transformed_df = pd.get_dummies(X, columns=self.categorical_columns) 
        self.transformed_columns = transformed_df.columns
        return self

    def transform(self, X: pd.DataFrame, y: Optional[pd.Series] = None
                 ) -> tuple[pd.DataFrame, Optional[pd.Series]]:
        assert all([column in X.columns for column in self.categorical_columns]), (
               'Categorical columns in Transformer are not part of a DataFrame'
        )
        X = pd.get_dummies(X, columns=self.categorical_columns)
        missing_columns = set(self.transformed_columns) - set(X.columns)
        for column in missing_columns:
            X[column] = np.zeros(len(X))

        assert len(X.columns) == len(self.transformed_columns)
        X = X[self.transformed_columns]
        return X, y
