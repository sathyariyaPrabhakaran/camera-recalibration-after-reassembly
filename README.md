# Camera Recalibration After Position Tracker Reassembly

A low-cost computer-vision prototype for automatically estimating the change in camera pose after a position-tracking setup is reassembled, using the same reference target.

> **Project status:** Prototype / research implementation. The underlying calibration techniques are established; this project focuses on a practical, low-cost reassembly workflow and quantitative verification.

## Problem

When a camera or position-tracking assembly is removed and reinstalled, its extrinsic pose relative to the reference frame can change. Repeating a complete manual calibration procedure is inconvenient. This project investigates whether a known reference target can be used to recover the changed camera pose and compute the transformation needed to restore the tracking coordinate relationship.

## Proposed workflow

1. Capture a reference target with the laptop camera.
2. Calibrate camera intrinsics once.
3. Estimate the initial reference pose.
4. Reassemble/move the camera or tracker.
5. Capture the **same** reference target again.
6. Estimate the new pose.
7. Compute the relative rigid transformation between the two poses.
8. Verify the correction using reprojection and pose-error metrics.

## Planned improvement

The baseline uses a fiducial marker for metric pose estimation. The prototype is designed to add image-feature verification so the system can reject unreliable recalibration when the reference target is poorly detected or the scene does not match the saved reference.

## Technology

- Python 3.10+
- OpenCV
- NumPy
- ArUco/fiducial marker detection
- Perspective-n-Point (PnP) pose estimation
- Rotation/translation transformations
- Optional ORB feature verification

## Cost target

The software prototype is designed to run on a laptop using its built-in camera. A printed reference target costs only a few rupees. Optional ESP32/servo hardware can be added later for a physical robotics demonstration, but it is **not required for the core algorithm**.

## Repository structure

```text
camera-recalibration-after-reassembly/
├── README.md
├── requirements.txt
├── src/
│   ├── camera_calibration.py
│   ├── reference_detection.py
│   ├── pose_estimation.py
│   ├── transformation.py
│   ├── verification.py
│   └── main.py
├── experiments/
│   └── README.md
├── docs/
│   ├── problem_statement.md
│   ├── existing_methods.md
│   ├── proposed_method.md
│   └── experiments.md
└── tests/
    └── test_transformation.py
```

## Important terminology

The repeated operation is primarily **extrinsic recalibration**: recovering the camera's changed rotation and translation relative to a known reference. Camera intrinsics (focal length, principal point, distortion) normally do not need to be recalculated merely because the camera was physically reassembled, provided the lens/camera configuration has not changed.

## Disclaimer

This is a student prototype and is not intended for safety-critical robot calibration or clinical/industrial deployment without further validation.
