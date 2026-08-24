"""ArUco marker detection for the reference target."""

from __future__ import annotations

import cv2
import numpy as np


def detect_aruco(frame: np.ndarray, dictionary_id: int = cv2.aruco.DICT_4X4_50):
    """Detect ArUco markers and return corners, ids and rejected candidates."""
    dictionary = cv2.aruco.getPredefinedDictionary(dictionary_id)
    parameters = cv2.aruco.DetectorParameters()
    detector = cv2.aruco.ArucoDetector(dictionary, parameters)
    corners, ids, rejected = detector.detectMarkers(frame)
    return corners, ids, rejected


def marker_center(corners: np.ndarray) -> tuple[float, float]:
    """Return the center pixel of one four-corner marker."""
    pts = np.asarray(corners, dtype=float).reshape(4, 2)
    center = pts.mean(axis=0)
    return float(center[0]), float(center[1])
