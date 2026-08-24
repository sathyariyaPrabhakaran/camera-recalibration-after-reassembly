# Experimental Protocol

## Goal
Measure whether the saved reference target can recover the camera's changed extrinsic pose after controlled reassembly.

## Procedure

1. Fix the reference target to a stable surface.
2. Run intrinsic calibration once using several views of the target.
3. Capture and save a baseline pose.
4. Record the target's physical dimensions.
5. Move/reassemble the camera mount by a controlled amount.
6. Capture the same target again.
7. Estimate the new pose.
8. Compute the relative transformation.
9. Run the feature-verification gate.
10. Record translation error, rotation error, reprojection RMSE, processing time, and PASS/REJECT status.
11. Repeat for multiple reassembly trials.

## Important

Do not enter expected or fabricated measurements. The results directory should contain only measurements obtained from the actual camera setup.

## Suggested trials

Use several small changes in translation and rotation, then repeat each condition. Keep lighting and marker size controlled where possible.

## Acceptance criteria

The initial thresholds should be configuration values, not claims of accuracy. They must be tuned from real experiments and reported transparently.
