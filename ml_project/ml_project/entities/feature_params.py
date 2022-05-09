from dataclasses import dataclass
from typing import Optional


@dataclass()
class FeatureParams:
    categorical_columns: list[str]
    features_to_drop: list[str]
    target_column: Optional[str]
