from pathlib import Path

from fastapi.testclient import TestClient

from server.app import create_app
from server.config import ServerConfig


def test_health_endpoint_reports_safe_idle() -> None:
    with TestClient(create_app(ServerConfig())) as client:
        response = client.get("/api/v1/health")

    assert response.status_code == 200
    payload = response.json()
    assert payload["api_version"] == "v1"
    assert payload["state"] == "SAFE_IDLE"
    assert payload["mode"] == "NULL"
    assert payload["reason_code"] == "STARTUP_COMPLETE"
    assert payload["trace_id"]


def test_health_trace_id_correlates_with_audit_event() -> None:
    app = create_app(ServerConfig())
    with TestClient(app) as client:
        response = client.get("/api/v1/health")
        payload = response.json()
        events = app.state.service.audit.snapshot()

    correlated = [
        event
        for event in events
        if event.event == "health_snapshot_returned"
        and event.trace_id == payload["trace_id"]
        and event.reason_code == payload["reason_code"]
    ]
    assert len(correlated) == 1


def test_capabilities_are_fail_closed() -> None:
    with TestClient(create_app(ServerConfig())) as client:
        response = client.get("/api/v1/capabilities")

    assert response.status_code == 200
    payload = response.json()
    assert payload["mode"] == "NULL"
    assert payload["external_effects"] is False
    assert payload["real_click"] is False
    assert payload["broker_connection"] is False
    assert payload["live_mode"] is False
    assert payload["database"] is False
    assert payload["signal_engine"] is False


def test_persistence_health_is_enabled_locally_without_external_capabilities(
    tmp_path: Path,
) -> None:
    app = create_app(ServerConfig(database_path=tmp_path / "state.db"))

    with TestClient(app) as client:
        health = client.get("/api/v1/persistence/health")
        capabilities = client.get("/api/v1/capabilities")

    assert health.status_code == 200
    assert health.json()["integrity_check"] == "ok"
    assert health.json()["schema_version"] == 1
    assert health.json()["mode"] == "NULL_ONLY"
    assert capabilities.json()["database"] is True
    assert capabilities.json()["external_effects"] is False
    assert capabilities.json()["broker_connection"] is False
    assert capabilities.json()["real_click"] is False
    assert capabilities.json()["live_mode"] is False


def test_persistence_health_fails_closed_when_not_configured() -> None:
    with TestClient(create_app(ServerConfig())) as client:
        response = client.get("/api/v1/persistence/health")

    assert response.status_code == 503
    assert response.json()["detail"] == "PERSISTENCE_DISABLED"
