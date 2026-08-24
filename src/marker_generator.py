"""Generate a printable ArUco reference marker."""
from pathlib import Path
import cv2


def generate_marker(marker_id: int = 23, pixels: int = 1200, output: str = "reference/aruco_marker_23.png"):
    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
    marker = cv2.aruco.generateImageMarker(dictionary, marker_id, pixels)
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(path), marker)
    return path


if __name__ == "__main__":
    print(generate_marker())
