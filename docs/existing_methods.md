# Existing methods and project differentiation

## Important scope note

Automatic camera/robot extrinsic calibration is an established field. ArUco/fiducial-marker pose estimation, PnP, feature matching, and robot-camera calibration should therefore be treated as established building blocks rather than claimed as inventions of this project.

## Baseline concept

A conventional workflow can detect a known target, estimate camera pose, and derive the camera-to-reference transformation. A complete calibration procedure may involve multiple views or a specialized target/robot setup.

## Our prototype variation

The project keeps the lab requirement intact — use the same reference target after reassembly — but focuses on a low-cost workflow:

1. Intrinsic calibration is performed once for the fixed laptop camera.
2. A reference pose is saved before disassembly/reassembly.
3. The same reference target is detected after reassembly.
4. A new extrinsic pose is estimated.
5. The relative transformation is calculated automatically.
6. Reprojection error is used as a quantitative acceptance check.
7. A later feature-verification layer can reject a calibration when the visual reference is inconsistent.

## Why this is a useful student prototype

The contribution is an engineering implementation and evaluation, not a claim that camera recalibration itself is novel. The emphasis is low cost, repeatability, measurable error, and a clear reassembly workflow that can run on a normal laptop.
