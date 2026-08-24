"""Intrinsic camera calibration from chessboard images."""

from __future__ import annotations

import cv2
import numpy as np


def calibrate_from_chessboards(
    image_paths: list[str],
    board_size: tuple[int, int] = (9, 6),
    square_size: float = 0.025,
):
    """Calibrate camera intrinsics from chessboard photographs.

    Returns camera matrix, distortion coefficients, and RMS calibration error.
    square_size can be any consistent physical unit; meters are recommended.
    """
    cols, rows = board_size
    pattern = np.zeros((rows * cols, 3), np.float32)
    pattern[:, :2] = np.mgrid[0:cols, 0:rows].T.reshape(-1, 2) * square_size

    object_points = []
    image_points = []
    image_size = None

    for path in image_paths:
        image = cv2.imread(path)
        if image is None:
            raise FileNotFoundError(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        found, corners = cv2.findChessboardCorners(gray, board_size, None)
        if not found:
            continue
        refined = cv2.cornerSubPix(
            gray,
            corners,
            (11, 11),
            (-1, -1),
            (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001),
        )
        object_points.append(pattern.copy())
        image_points.append(refined)
        image_size = gray.shape[::-1]

    if not object_points or image_size is None:
        raise RuntimeError("No valid chessboard images were found.")

    rms, camera_matrix, dist_coeffs, _, _ = cv2.calibrateCamera(
        object_points, image_points, image_size, None, None
    )
    return camera_matrix, dist_coeffs, float(rms)
