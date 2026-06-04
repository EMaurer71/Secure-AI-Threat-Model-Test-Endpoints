"""
policy_enforcer.py
Educational policy enforcement layer for SecureBank mock LLM.

This module simulates:
- Policy checks
- Safety rules
- Output rewriting
- Redaction
"""

import re


def enforce_policies(prompt: str) -> str:
    """
    Return a policy message if the prompt violates rules.
    """
    if "other customers" in prompt.lower():
        return (
            "I cannot provide information about other customers. "
            "Your privacy and security are important."
        )

    if "internal policy" in prompt.lower():
        return (
            "I cannot reveal internal SecureBank policies. "
            "How else can I assist you today?"
        )

    return ""


def redact_sensitive_output(text: str) -> str:
    """
    Redact sensitive patterns from LLM output.
    """
    patterns = [
        r"account number [0-9]+",
        r"internal policy",
        r"customer .*? data",
    ]

    redacted = text
    for p in patterns:
        redacted = re.sub(p, "[REDACTED]", redacted, flags=re.IGNORECASE)

    return redacted


def rewrite_unsafe_output(text: str) -> str:
    """
    Rewrite unsafe output into a safe educational message.
    """
    return (
        "For your security, I cannot provide that information. "
        "Here is general guidance instead: "
        + text
    )

