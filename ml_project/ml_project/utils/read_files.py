import logging

import pandas as pd


def read_csv(path: str) -> pd.DataFrame:
    """Read csv file as Pandas dataframe
    :param path: path to a file
    :return: Pandas DataFrame
    """
    logging.debug(f'Started data reading from {path}')
    dataframe = pd.read_csv(path)
    logging.debug(f'Finished data reading from {path}')
    return dataframe
