"""Interactive first-stage prototype using the laptop camera.

Run from the repository root:
    python src/main.py

Press Q to quit. The program detects the reference marker and displays its
pixel center. Pose estimation is enabled once calibrated camera parameters and
known marker dimensions are supplied.
"""

from __future__ import annotations

import cv2

from reference_detection import detect_aruco, marker_center


def main() -> None:
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        raise RuntimeError("Could not open the laptop camera.")

    print("Camera started. Show the reference ArUco marker to the camera.")
    print("Press Q to quit.")

    while True:
        ok, frame = camera.read()
        if not ok:
            break

        corners, ids, _ = detect_aruco(frame)
        if ids is not None:
            cv2.aruco.drawDetectedMarkers(frame, corners, ids)
            for marker_corners, marker_id in zip(corners, ids.flatten()):
                cx, cy = marker_center(marker_corners)
                cv2.circle(frame, (round(cx), round(cy)), 5, (0, 255, 0), -1)
                cv2.putText(
                    frame,
                    f"ID {marker_id}: ({cx:.0f}, {cy:.0f})",
                    (round(cx) + 10, round(cy)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    2,
                )

        cv2.imshow("Reassembly-Aware Camera Recalibration", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
