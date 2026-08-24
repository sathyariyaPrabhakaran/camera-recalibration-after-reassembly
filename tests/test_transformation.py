import numpy as np

from src.transformation import rotation_error_deg, translation_error_mm


def test_zero_translation_error():
    assert translation_error_mm([1, 2, 3], [1, 2, 3]) == 0.0


def test_rotation_error_identity():
    identity = np.eye(3)
    assert rotation_error_deg(identity, identity) == 0.0
