"""Verification metrics for reassembly-aware recalibration."""

from __future__ import annotations

import numpy as np


def is_acceptable(reprojection_rmse_px: float, threshold_px: float = 2.0) -> bool:
    """Return True when the estimated pose has an acceptable reprojection error."""
    if not np.isfinite(reprojection_rmse_px):
        return False
    return float(reprojection_rmse_px) <= threshold_px


def summary(reprojection_rmse_px: float, threshold_px: float = 2.0) -> dict:
    """Return a small machine-readable verification report."""
    return {
        "reprojection_rmse_px": float(reprojection_rmse_px),
        "threshold_px": float(threshold_px),
        "status": "PASS" if is_acceptable(reprojection_rmse_px, threshold_px) else "REJECT",
    }
