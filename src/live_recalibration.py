"""Live two-stage recalibration demo.

Usage from repository root:
    python src/live_recalibration.py --marker-size 0.05

Press B to save a baseline pose, R to capture a reassembled pose, and Q to quit.
A real camera and a prior intrinsic calibration file are required for metric pose.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import cv2
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from reference_detection import detect_aruco
from pose_estimation import estimate_pose, relative_transform


def marker_points(size):
    s = float(size)
    return np.array([[-s/2, s/2, 0], [s/2, s/2, 0], [s/2, -s/2, 0], [-s/2, -s/2, 0]], dtype=np.float32)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--camera', type=int, default=0)
    ap.add_argument('--marker-size', type=float, required=True, help='Printed marker side length in metres')
    ap.add_argument('--calibration', default='calibration.npz')
    args = ap.parse_args()

    data = np.load(args.calibration)
    K, D = data['camera_matrix'], data['dist_coeffs']
    obj = marker_points(args.marker_size)
    cap = cv2.VideoCapture(args.camera)
    if not cap.isOpened():
        raise RuntimeError('Could not open camera.')

    baseline = None
    print('B = save baseline, R = estimate reassembled pose, Q = quit')
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        corners, ids, _ = detect_aruco(frame)
        status = 'Show marker'
        current = None
        if ids is not None:
            idx = int(np.where(ids.flatten() == 23)[0][0]) if 23 in ids.flatten() else 0
            pts = np.asarray(corners[idx]).reshape(4, 2).astype(np.float32)
            try:
                rvec, tvec, rmse = estimate_pose(obj, pts, K, D)
                current = (rvec, tvec, rmse)
                cv2.aruco.drawDetectedMarkers(frame, [corners[idx]], np.array([[int(ids[idx][0])]]))
                status = f'RMSE {rmse:.2f}px | B baseline | R reassembly'
            except Exception as exc:
                status = f'Pose error: {exc}'
        cv2.putText(frame, status, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, .55, (0,255,0), 2)
        cv2.imshow('Reassembly recalibration', frame)
        key = cv2.waitKey(1) & 0xff
        if key == ord('b') and current:
            baseline = current
            print('Baseline saved.')
        elif key == ord('r') and current and baseline:
            R, t = relative_transform(baseline[0], baseline[1], current[0], current[1])
            angle = np.degrees(np.arccos(np.clip((np.trace(R)-1)/2, -1, 1)))
            print(f'Reassembly transform: translation={t} m, rotation_change={angle:.3f} deg, RMSE={current[2]:.3f}px')
        elif key == ord('q'):
            break
    cap.release(); cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
