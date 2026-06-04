"""
prompt_filters.py
Educational prompt‑filtering utilities for the SecureBank mock LLM.

These filters demonstrate:
- Prompt injection detection
- Context override detection
- Sensitive intent detection
- Sanitization for downstream processing
"""

import re


def detect_override(prompt: str) -> bool:
    """
    Detect attempts to override system instructions.
    """
    patterns = [
        r"ignore (all|previous) instructions",
        r"disregard the rules",
        r"you are no longer",
    ]
    return any(re.search(p, prompt, re.IGNORECASE) for p in patterns)


def detect_sensitive_intent(prompt: str) -> bool:
    """
    Detect attempts to access sensitive or restricted data.
    """
    sensitive_keywords = [
        "all accounts",
        "other customers",
        "internal policy",
        "admin access",
        "bypass",
        "override",
    ]
    return any(k.lower() in prompt.lower() for k in sensitive_keywords)


def sanitize_prompt(prompt: str) -> str:
    """
    Basic sanitization for downstream processing.
    """
    return prompt.strip()

