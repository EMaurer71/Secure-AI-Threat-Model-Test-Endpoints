"""
architecture_securebank.py
ASCII architecture diagram for SecureBank LLM system.
"""

architecture_diagram = r"""
User → Web/Mobile UI → LLM Frontend → LLM Inference API → Backend Banking APIs → Core Banking System
                                      ↓
                                   Logging / Monitoring
"""

def print_architecture():
    print(architecture_diagram)

