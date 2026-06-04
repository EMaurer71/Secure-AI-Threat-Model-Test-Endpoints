"""
stride_securebank.py
Machine-readable STRIDE threat dictionary for SecureBank.
"""

securebank_stride = {
    "chat_interface": {
        "Spoofing": "Attacker hijacks user session or uses stolen credentials.",
        "Tampering": "Malicious prompts injected into chat.",
        "Information Disclosure": "LLM reveals sensitive data via responses."
    },
    "llm_api": {
        "Spoofing": "Attacker calls LLM API directly, bypassing frontend.",
        "Tampering": "System prompts or policies modified.",
        "Information Disclosure": "Sensitive prompts/responses leaked via logs."
    },
    "backend_apis": {
        "Tampering": "LLM coerced into calling APIs with malicious parameters.",
        "Elevation of Privilege": "LLM attempts to trigger admin-level actions."
    },
    "logging_monitoring": {
        "Repudiation": "User denies LLM-initiated actions.",
        "Information Disclosure": "Logs contain sensitive data without redaction."
    }
}

