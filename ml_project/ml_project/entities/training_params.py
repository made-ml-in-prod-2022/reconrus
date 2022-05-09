from dataclasses import dataclass

from ml_project.entities.splitting_params import SplittingParams
from ml_project.entities.feature_params import FeatureParams 


@dataclass()
class TrainingParams:
    model_type: str
    random_state: int
    output_column: str
    logging_config: str
    model_output_path: str
    splitting_params: SplittingParams
    feature_params: FeatureParams
    model_params: dict
    data_path: str
    transformer_path: str
