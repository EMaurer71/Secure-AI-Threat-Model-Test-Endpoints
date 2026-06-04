"""
validation.py
Input validation utilities for the X-Ray Threat Model project.
"""

import numpy as np


def validate_xray(image: np.ndarray) -> bool:
    """
    Validate a 128x128 grayscale X-ray image.

    Checks:
    - Must be a NumPy array
    - Must be 2D
    - Must be 128x128
    - Pixel values must be in [0, 255]
    """
    if not isinstance(image, np.ndarray):
        raise ValueError("Input must be a NumPy array.")

    if image.ndim != 2:
        raise ValueError("X-ray must be a 2D grayscale image.")

    if image.shape != (128, 128):
        raise ValueError("Expected 128x128 image.")

    if image.min() < 0 or image.max() > 255:
        raise ValueError("Pixel values out of range [0, 255].")

    return True

