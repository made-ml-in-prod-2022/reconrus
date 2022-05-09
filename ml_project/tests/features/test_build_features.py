from typing import Any, Callable, Literal, Union

import numpy as np
import pandas as pd
import pytest
from faker import Faker
from numpy.random import rand, randint

from ml_project.features.build_features import OneHotTransformer

INT_TYPE = 'int'
FLOAT_TYPE = 'float'


def generate_categorical_values(possible_values: list[str], size: int) -> list[int]:
    data = np.random.choice(possible_values, size=size)
    return data


def generate_numerical_values(min_value: int, max_value: int, size: int, 
                              type_: Literal[INT_TYPE, FLOAT_TYPE]) -> list[Union[float, int]]:
    if type_ == INT_TYPE:
        data = randint(min_value, max_value, size)
    elif type_ == FLOAT_TYPE:
        data = (max_value - min_value) * rand(size) + min_value
    else:
        raise ValueError('Incorrect type value')
    return data


def generate_values_from_fuction(function: Callable, sample_size: int) -> list[Any]:
    data = [function() for _ in range(sample_size)]
    return data



@pytest.fixture
def test_data():
    factory = Faker()
    
    df = pd.DataFrame(columns=['Name', 'Sex', 'Birthdate', 'Balance', 'Category'])
    sample_size = randint(100, 1000)
    
    sex_values = ['M', 'F', 'U']
    categories_values = factory.words(5)
    
    df['Name'] = generate_values_from_fuction(factory.name, sample_size)
    df['Sex'] = generate_categorical_values(sex_values, sample_size)
    df['Birthdate'] = generate_values_from_fuction(factory.date, sample_size)
    df['Balance'] = generate_numerical_values(0, 1e5, sample_size, FLOAT_TYPE)
    df['Category'] = generate_categorical_values(categories_values, sample_size)
    return df


def test_ohe_transformer(test_data):
    categorical_columns = {'Sex', 'Category'}
    transformer = OneHotTransformer(categorical_columns)
    transformer = transformer.fit(test_data)
    transformed_df, _ = transformer.transform(test_data)

    expected_columns = list(set(test_data.columns) - categorical_columns)
    for column in categorical_columns:
        unique_values = test_data[column].unique()
        new_columns = [f'{column}_{value}' for value in unique_values]
        expected_columns += new_columns

    assert len(expected_columns) == len(transformed_df.columns), (
        'Number of columns in transformed dataframe is not equal to expected one'
    )
    assert set(expected_columns) == set(transformed_df.columns), (
        'Columns in transformed dataframe are not the same to expected ones'
    )
