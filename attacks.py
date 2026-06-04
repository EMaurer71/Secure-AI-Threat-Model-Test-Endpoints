"""
attacks.py
Adversarial attack stubs for demonstration.
"""

import numpy as np


def fgsm_attack(image: np.ndarray, epsilon: float) -> np.ndarray:
    """
    Simple FGSM-style noise generator for demonstration.
    Not a real adversarial attack — placeholder only.
    """
    noise = epsilon * np.sign(np.random.randn(*image.shape))
    adv = np.clip(image + noise, 0, 255)
    return adv


def pgd_attack(image: np.ndarray, epsilon: float, steps: int = 5) -> np.ndarray:
    """
    Simple PGD-style iterative noise generator.
    Placeholder for demonstration.
    """
    adv = image.copy()
    for _ in range(steps):
        noise = epsilon * np.sign(np.random.randn(*image.shape))
        adv = np.clip(adv + noise, 0, 255)
    return adv

