"""Central configuration for the camera recalibration prototype."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    marker_id: int = 23
    marker_size_m: float = 0.05
    feature_min_matches: int = 12
    reprojection_threshold_px: float = 3.0

CONFIG = Config()
