import logging

import pandas as pd


def parse_requirements(requirements_path: str) -> list[str]:
    """Parses pip requirements file
    :param requirements_path: path to requirements file
    :return: list of required packages
    """
    with open(requirements_path) as f:
        requirements_file_lines = f.read().splitlines()
    processed_lines = map(lambda x: x.strip(), requirements_file_lines)
    required_packages = filter(lambda x: x and not x.startswith('#'), processed_lines)
    return list(required_packages)


def read_csv(path: str) -> pd.DataFrame:
    """Read csv file as Pandas dataframe
    :param path: path to a file
    :return: Pandas DataFrame
    """
    logging.debug(f'Started data reading from {path}')
    dataframe = pd.read_csv(path)
    logging.debug(f'Finished data reading from {path}')
    return dataframe
