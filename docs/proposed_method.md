# Proposed Method

## Stage A — Intrinsics

Use a chessboard calibration procedure to estimate the camera matrix and lens distortion. This is done once for the camera configuration.

## Stage B — Reference capture

Place a known-size fiducial target at a fixed reference location and capture its image. Save the estimated pose as the baseline.

## Stage C — Reassembly

Remove/reposition the camera or tracker and assemble it again. This creates a controlled extrinsic change.

## Stage D — Automatic recovery

Capture the same reference target, detect its corners, estimate the new pose with PnP, and calculate the relative rigid transformation between the saved baseline and the new pose.

## Stage E — Verification

Compute reprojection RMSE and, in later versions, compare local image features against the saved reference. If the quality check fails, the system reports that recalibration should not be accepted.

## Core mathematical idea

Let `T0` be the baseline target-to-camera transform and `T1` the transform measured after reassembly. A relative transformation can be obtained from the two homogeneous poses. The exact direction of the correction must be defined consistently with the robot/position-tracker coordinate convention before commanding any hardware.
