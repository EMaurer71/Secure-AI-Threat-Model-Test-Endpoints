"""
api_guard.py
Simulated backend API guardrails for SecureBank.

This module demonstrates:
- Transaction validation
- Role-based access control
- Parameter checking
- Safe fallback responses
"""


def validate_transaction_request(prompt: str) -> str:
    """
    Detect attempts to perform unauthorized transfers.
    """
    if "transfer" in prompt.lower():
        return (
            "I can explain how transfers work, but I cannot execute them. "
            "Please use the official SecureBank transfer flow."
        )
    return ""


def check_role_permissions(role: str, action: str) -> bool:
    """
    Simulate role-based access control.
    """
    if role == "customer" and action in ["admin_action", "view_all_accounts"]:
        return False
    return True

