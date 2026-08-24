# Camera calibration configuration

The live program expects an `.npz` file containing:

- `camera_matrix`: 3x3 intrinsic matrix
- `dist_coeffs`: distortion coefficients

For the first prototype, generate these values from chessboard images using `src/calibrate_intrinsics.py`, then save them with NumPy. Do not commit personal camera calibration values as project results unless they are explicitly part of the experiment.
