import logging
import yaml


def setup_logger(configuration_path):
    with open(configuration_path) as config_fin:
        logging.config.dictConfig(yaml.safe_load(config_fin))
    logging.debug('Configured logger')
