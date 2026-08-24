"""Metric camera pose estimation from a planar reference target."""

from __future__ import annotations

import cv2
import numpy as np


def estimate_pose(
    object_points: np.ndarray,
    image_points: np.ndarray,
    camera_matrix: np.ndarray,
    dist_coeffs: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, float]:
    """Estimate target pose with solvePnP and return rvec, tvec and reprojection RMSE."""
    object_points = np.asarray(object_points, dtype=np.float32)
    image_points = np.asarray(image_points, dtype=np.float32)

    if len(object_points) < 4 or len(image_points) != len(object_points):
        raise ValueError("At least four corresponding 3D/2D points are required.")

    ok, rvec, tvec = cv2.solvePnP(
        object_points,
        image_points,
        camera_matrix,
        dist_coeffs,
        flags=cv2.SOLVEPNP_ITERATIVE,
    )
    if not ok:
        raise RuntimeError("solvePnP could not estimate a pose.")

    projected, _ = cv2.projectPoints(
        object_points, rvec, tvec, camera_matrix, dist_coeffs
    )
    projected = projected.reshape(-1, 2)
    residual = projected - image_points
    rmse = float(np.sqrt(np.mean(np.sum(residual**2, axis=1))))
    return rvec, tvec, rmse


def relative_transform(
    rvec_initial: np.ndarray,
    tvec_initial: np.ndarray,
    rvec_reassembled: np.ndarray,
    tvec_reassembled: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """Return the rigid transform from the initial camera pose to the reassembled pose."""
    r0, _ = cv2.Rodrigues(np.asarray(rvec_initial, dtype=float))
    r1, _ = cv2.Rodrigues(np.asarray(rvec_reassembled, dtype=float))
    t0 = np.asarray(tvec_initial, dtype=float).reshape(3, 1)
    t1 = np.asarray(tvec_reassembled, dtype=float).reshape(3, 1)

    # Camera-pose matrices map target-frame coordinates into camera coordinates.
    h0 = np.eye(4)
    h1 = np.eye(4)
    h0[:3, :3], h0[:3, 3:] = r0, t0
    h1[:3, :3], h1[:3, 3:] = r1, t1
    relative = h1 @ np.linalg.inv(h0)
    return relative[:3, :3], relative[:3, 3]
