"""Generate a printable ArUco reference target."""
from __future__ import annotations

import argparse
import cv2


def generate(marker_id: int, pixels: int, output: str) -> None:
    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
    marker = cv2.aruco.generateImageMarker(dictionary, marker_id, pixels)
    cv2.imwrite(output, marker)
    print(f"Saved marker {marker_id} to {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", type=int, default=23)
    parser.add_argument("--pixels", type=int, default=1000)
    parser.add_argument("--output", default="reference_marker.png")
    args = parser.parse_args()
    generate(args.id, args.pixels, args.output)
