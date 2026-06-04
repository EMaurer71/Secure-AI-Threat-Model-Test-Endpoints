from src.api_guard import validate_transaction_request


def test_validate_transaction_request():
    assert "cannot execute" in validate_transaction_request("transfer $500")
    assert validate_transaction_request("hello") == ""

