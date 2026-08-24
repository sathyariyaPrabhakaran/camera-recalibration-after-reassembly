"""Core reassembly-aware extrinsic recalibration workflow."""
from __future__ import annotations

from dataclasses import dataclass
import numpy as np

from transformation import make_transform, rotation_error_deg, translation_error_mm


@dataclass
class Pose:
    rvec: np.ndarray
    tvec: np.ndarray

    @property
    def transform(self) -> np.ndarray:
        return make_transform(self.rvec, self.tvec)


def relative_transform(baseline: Pose, reassembled: Pose) -> np.ndarray:
    """Return T_baseline<-reassembled from two camera/reference poses."""
    return baseline.transform @ np.linalg.inv(reassembled.transform)


def pose_change(baseline: Pose, reassembled: Pose) -> tuple[float, float]:
    """Return translation and rotation change between poses."""
    r0 = baseline.transform[:3, :3]
    r1 = reassembled.transform[:3, :3]
    t0 = baseline.transform[:3, 3]
    t1 = reassembled.transform[:3, 3]
    return translation_error_mm(t0, t1), rotation_error_deg(r0, r1)


def accept_recalibration(feature_confidence: float, reprojection_error_px: float,
                         min_feature_confidence: float = 0.75,
                         max_reprojection_error_px: float = 5.0) -> bool:
    """Conservative gate for accepting an automatically recovered pose."""
    return (feature_confidence >= min_feature_confidence and
            reprojection_error_px <= max_reprojection_error_px)
