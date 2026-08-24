# Reassembly experiment

Store measured experiment tables here after testing the physical prototype.

## Procedure

1. Fix the reference marker in a stable location.
2. Calibrate camera intrinsics once and save the camera matrix/distortion coefficients.
3. Capture and save the baseline reference image and pose.
4. Remove/reposition the camera or tracking assembly.
5. Reassemble it with a deliberate small translation/rotation change.
6. Capture the same reference target again.
7. Estimate the new pose and compute the relative transformation.
8. Run feature verification against the saved reference image.
9. Accept the recalibration only when the verification/error gates pass.
10. Repeat across several reassembly offsets and lighting conditions.

## Metrics

- Translation change (same units as marker size, normally mm)
- Rotation change (degrees)
- Reprojection RMSE (pixels)
- Feature-match confidence
- Processing/recalibration time (seconds)
- Acceptance/rejection outcome

## Results

Recommended CSV columns:

```text
trial,initial_tx_mm,initial_ty_mm,initial_tz_mm,reassembled_tx_mm,reassembled_ty_mm,reassembled_tz_mm,rotation_error_deg,reprojection_rmse_px,feature_confidence,processing_time_s,status
```

**Do not add fabricated measurements.** Capture values from the actual camera setup.
