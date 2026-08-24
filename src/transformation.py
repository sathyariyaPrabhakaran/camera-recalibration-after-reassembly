"""Rigid transformation and rotation-error utilities."""

from __future__ import annotations

import cv2
import numpy as np


def make_transform(rvec: np.ndarray, tvec: np.ndarray) -> np.ndarray:
    """Build a 4x4 homogeneous transform from Rodrigues rotation + translation."""
    rotation, _ = cv2.Rodrigues(np.asarray(rvec, dtype=float))
    transform = np.eye(4)
    transform[:3, :3] = rotation
    transform[:3, 3] = np.asarray(tvec, dtype=float).reshape(3)
    return transform


def translation_error_mm(t0: np.ndarray, t1: np.ndarray) -> float:
    """Euclidean translation difference, expressed in the same units as the inputs."""
    return float(np.linalg.norm(np.asarray(t1).reshape(3) - np.asarray(t0).reshape(3)))


def rotation_error_deg(r0: np.ndarray, r1: np.ndarray) -> float:
    """Angular difference between two 3x3 rotation matrices."""
    relative = np.asarray(r1) @ np.asarray(r0).T
    value = (np.trace(relative) - 1.0) / 2.0
    value = float(np.clip(value, -1.0, 1.0))
    return float(np.degrees(np.arccos(value)))
