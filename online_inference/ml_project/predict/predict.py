import logging

import pandas as pd

from ml_project.features.build_features import OneHotTransformer


def predict_label(parameters: dict, model, transformer: OneHotTransformer) -> list[int]:
    prepared_parameters = {key: [value] for key, value in parameters.items()}
    parameters_df = pd.DataFrame(prepared_parameters)
    logging.debug(f"Processing data")
    processed_data, _ = transformer.transform(parameters_df, None)
    logging.debug(f"Finished processing")

    logging.debug(f"Started prediction")
    y = model.predict(processed_data)
    logging.debug(f"Finished prediction")
    return y.tolist()[0]
