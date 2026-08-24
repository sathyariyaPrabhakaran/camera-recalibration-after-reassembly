"""Feature-based verification of a saved reference image.

This is a verification layer, not the primary metric pose estimator. It helps
reject a recalibration when the captured scene is not sufficiently similar to
the saved reference.
"""
from __future__ import annotations

import cv2
import numpy as np


def match_reference(reference_gray: np.ndarray, current_gray: np.ndarray, min_good_matches: int = 12):
    """Return good ORB matches and a simple confidence score."""
    orb = cv2.ORB_create(nfeatures=1200)
    kp1, des1 = orb.detectAndCompute(reference_gray, None)
    kp2, des2 = orb.detectAndCompute(current_gray, None)
    if des1 is None or des2 is None:
        return [], 0.0

    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)
    raw = matcher.knnMatch(des1, des2, k=2)
    good = []
    for pair in raw:
        if len(pair) == 2:
            a, b = pair
            if a.distance < 0.75 * b.distance:
                good.append(a)

    confidence = min(1.0, len(good) / float(max(1, min_good_matches)))
    return good, confidence
