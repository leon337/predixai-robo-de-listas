from server.adapters import NullAdapter
from server.contracts import AdapterMode, ReasonCode


def test_null_adapter_never_creates_external_effect() -> None:
    result = NullAdapter().execute({"action": "ignored"})

    assert result.accepted is True
    assert result.mode is AdapterMode.NULL
    assert result.reason_code is ReasonCode.NULL_ADAPTER_ACTIVE
    assert result.external_effect is False
