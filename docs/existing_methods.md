# Existing Methods and Project Positioning

Automatic camera/robot extrinsic calibration is an established field. ArUco/fiducial-marker pose estimation, PnP, feature matching, and robot-camera calibration are established building blocks and are **not claimed as inventions of this project**.

## Baseline concept

A conventional workflow can detect a known target, estimate camera pose, and derive the camera-to-reference transformation. Complete calibration procedures may use multiple views, specialized targets, or robot-specific hardware.

## Our prototype variation

The lab requirement remains unchanged: use the same reference target after the position tracker is reassembled. Our implementation focuses on a low-cost, repeatable workflow:

1. Intrinsic calibration is performed once for the fixed laptop camera.
2. A reference pose is saved before disassembly/reassembly.
3. The same reference target is detected after reassembly.
4. A new extrinsic pose is estimated.
5. The relative rigid transformation is calculated automatically.
6. Reprojection error is used as a quantitative acceptance check.
7. ORB feature consistency can act as a second verification layer.
8. The system reports PASS/REJECT rather than silently accepting an unreliable calibration.

## Why this is useful

The contribution is an engineering implementation and evaluation, not a claim that camera recalibration itself is novel. The emphasis is low cost, repeatability, measurable error, and a clear reassembly workflow that can run on a normal laptop.
