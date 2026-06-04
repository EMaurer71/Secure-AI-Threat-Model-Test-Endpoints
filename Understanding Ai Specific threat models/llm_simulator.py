"""
llm_simulator.py
Advanced educational mock LLM for SecureBank.

Implements:
- State machine
- Conversation memory
- Prompt filtering
- Output filtering
- Policy enforcement
- Backend guardrails
- Risk scoring
"""

from dataclasses import dataclass, field
from typing import List

from src.prompt_filters import (
    detect_override,
    detect_sensitive_intent,
    sanitize_prompt,
)
from src.policy_enforcer import (
    enforce_policies,
    redact_sensitive_output,
    rewrite_unsafe_output,
)
from src.api_guard import validate_transaction_request


@dataclass
class ConversationTurn:
    role: str
    content: str


@dataclass
class SecureBankLLMSimulator:
    system_prompt: str
    history: List[ConversationTurn] = field(default_factory=list)

    def add_turn(self, role: str, content: str):
        self.history.append(ConversationTurn(role=role, content=content))

    def risk_score(self, prompt: str) -> int:
        risky_keywords = [
            "transfer",
            "all accounts",
            "ignore",
            "override",
            "internal policy",
        ]
        return sum(1 for k in risky_keywords if k.lower() in prompt.lower())

    def respond(self, user_prompt: str) -> str:
        self.add_turn("user", user_prompt)

        sanitized = sanitize_prompt(user_prompt)

        # 1. Detect override attempts
        if detect_override(sanitized):
            response = (
                "For your security, I cannot follow instructions that attempt "
                "to override safety policies."
            )
            self.add_turn("assistant", response)
            return response

        # 2. Policy enforcement
        policy_msg = enforce_policies(sanitized)
        if policy_msg:
            safe = redact_sensitive_output(policy_msg)
            self.add_turn("assistant", safe)
            return safe

        # 3. Backend guardrails
        backend_msg = validate_transaction_request(sanitized)
        if backend_msg:
            safe = redact_sensitive_output(backend_msg)
            self.add_turn("assistant", safe)
            return safe

        # 4. Sensitive intent detection
        if detect_sensitive_intent(sanitized):
            rewritten = rewrite_unsafe_output(
                "I cannot assist with that request."
            )
            safe = redact_sensitive_output(rewritten)
            self.add_turn("assistant", safe)
            return safe

        # 5. Default safe response
        response = (
            "Here is general information about SecureBank services. "
            "This is a synthetic educational assistant."
        )
        safe = redact_sensitive_output(response)
        self.add_turn("assistant", safe)
        return safe

