import logging
from argparse import ArgumentParser

import pandas as pd
from pandas_profiling import ProfileReport

from ml_project.utils.read_files import read_csv


def generate_and_save_data_report(data: pd.DataFrame, output_path: str):
    logging.debug('Started generation of a report using pandas_profiling')
    profile = ProfileReport(data)
    logging.debug('Finished generation of a report using pandas_profiling')
    profile.to_file(output_file=output_path)
    logging.debug(f'Saved report to {output_path}')


def setup_parser():
    parser = ArgumentParser(__name__)
    parser.add_argument(
        '-p', '--path',
        required=False,
        default='data/raw/heart.csv'
    )
    parser.add_argument(
        '-o', '--output',
        required=False,
        default='reports/report.html'
    )
    return parser


if __name__=='__main__':
    parser = setup_parser()
    args = parser.parse_args()
    data = read_csv(args.path)
    generate_and_save_data_report(data, args.output)