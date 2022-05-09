from dataclasses import dataclass

from ml_project.entities.feature_params import FeatureParams 


@dataclass()
class PredictionParams:
    model_path: str
    data_path: str
    output_path: str
    output_column: str
    logging_config: str
    transformer_path: str
    feature_parameters: FeatureParams
