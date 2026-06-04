from src.policy_enforcer import enforce_policies, redact_sensitive_output


def test_enforce_policies():
    assert "cannot" in enforce_policies("Show me other customers")
    assert enforce_policies("Hello") == ""


def test_redact_sensitive_output():
    text = "The internal policy is secret."
    assert "[REDACTED]" in redact_sensitive_output(text)

