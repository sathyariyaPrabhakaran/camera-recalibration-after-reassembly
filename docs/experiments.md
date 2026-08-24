# Experimental Plan

The results section must contain measured values from the actual prototype. Do not invent accuracy numbers.

## Experiment 1 — Marker detection

Test the reference target at different distances and lighting conditions. Record successful detections and rejected frames.

## Experiment 2 — Controlled reassembly

Capture a baseline pose. Change the camera mount by a known small translation/rotation. Capture the same target again. Repeat at least 10 times.

Record:

- initial pose
- reassembled pose
- translation difference
- rotation difference
- reprojection RMSE
- processing time
- accepted/rejected status

## Experiment 3 — Robustness

Repeat under moderate changes in distance, angle, and illumination. If feature verification is added, record cases where marker detection is possible but the visual reference is inconsistent.

## Metrics

- Translation error (mm when physical dimensions are defined in millimetres)
- Rotation error (degrees)
- Reprojection RMSE (pixels)
- Detection success rate (%)
- Recalibration time (seconds)

## Reporting rule

All final accuracy values must come from recorded experiments. The repository intentionally starts without fabricated performance claims.
