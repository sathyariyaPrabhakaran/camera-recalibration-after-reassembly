# Problem Statement

A position-tracking assembly can lose its original camera-to-reference relationship when the camera or tracker is removed and reassembled. Repeating a full calibration process is time-consuming and may require specialist equipment.

This project develops a low-cost prototype that uses the same known visual reference after reassembly to estimate the changed camera extrinsic pose and recover the relative transformation automatically.

## Objectives

- Use a laptop's built-in camera where possible.
- Calibrate camera intrinsics once rather than repeatedly.
- Detect the same physical reference target before and after reassembly.
- Estimate and compare camera poses.
- Compute the relative rigid transformation.
- Quantify calibration quality using reprojection error.
- Reject unreliable estimates rather than silently accepting them.
