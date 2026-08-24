"""Calibrate camera intrinsics from chessboard photographs."""
from __future__ import annotations
import argparse
from pathlib import Path
import cv2
import numpy as np


def calibrate(image_dir: str, cols: int, rows: int, square_m: float):
    obj = np.zeros((rows * cols, 3), np.float32)
    obj[:, :2] = np.mgrid[0:cols, 0:rows].T.reshape(-1, 2) * square_m
    object_points, image_points = [], []
    size = None
    for path in sorted(Path(image_dir).glob("*")):
        img = cv2.imread(str(path))
        if img is None: continue
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        found, corners = cv2.findChessboardCorners(gray, (cols, rows), None)
        if found:
            corners = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1),
                (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001))
            object_points.append(obj.copy()); image_points.append(corners); size = gray.shape[::-1]
    if not image_points: raise RuntimeError("No chessboard corners found.")
    rms, K, D, _, _ = cv2.calibrateCamera(object_points, image_points, size, None, None)
    return rms, K, D

if __name__ == "__main__":
    p=argparse.ArgumentParser(); p.add_argument("image_dir"); p.add_argument("--cols",type=int,default=9); p.add_argument("--rows",type=int,default=6); p.add_argument("--square-m",type=float,default=0.025); a=p.parse_args()
    rms,K,D=calibrate(a.image_dir,a.cols,a.rows,a.square_m)
    print("RMS reprojection error:",rms); print("Camera matrix:\n",K); print("Distortion:\n",D)
