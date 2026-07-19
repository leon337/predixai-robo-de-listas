import pytest

from server.config import load_config
from server.contracts import AdapterMode


def test_default_config_is_local_and_null_only() -> None:
    config = load_config({})
    assert config.host == "127.0.0.1"
    assert config.mode is AdapterMode.NULL


def test_non_null_mode_is_rejected() -> None:
    with pytest.raises(ValueError, match="somente NULL"):
        load_config({"PREDIXAI_SERVER_MODE": "SIMULATED"})


def test_non_loopback_host_is_rejected() -> None:
    with pytest.raises(ValueError, match="fail-closed"):
        load_config({"PREDIXAI_SERVER_HOST": "0.0.0.0"})


def test_privileged_port_is_rejected() -> None:
    with pytest.raises(ValueError, match="fail-closed"):
        load_config({"PREDIXAI_SERVER_PORT": "80"})
