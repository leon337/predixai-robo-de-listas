from fastapi.testclient import TestClient

from server.app import create_app
from server.config import ServerConfig


def test_runtime_snapshot_is_null_only_and_read_only() -> None:
    with TestClient(create_app(ServerConfig())) as client:
        response = client.get("/api/v1/runtime")

    assert response.status_code == 200
    payload = response.json()
    assert payload["state"] == "SAFE_IDLE"
    assert payload["mode"] == "NULL"
    assert payload["external_effects"] is False
    assert "command" not in payload


def test_audit_events_are_paginated_and_redacted() -> None:
    app = create_app(ServerConfig())
    with TestClient(app) as client:
        client.get("/api/v1/health")
        response = client.get("/api/v1/audit/events", params={"offset": 0, "limit": 1})

    assert response.status_code == 200
    payload = response.json()
    assert payload["limit"] == 1
    assert payload["total"] >= 2
    assert len(payload["items"]) == 1
    assert set(payload["items"][0]) == {
        "event",
        "reason_code",
        "trace_id",
        "timestamp_utc",
    }


def test_audit_endpoint_rejects_unsafe_limits() -> None:
    with TestClient(create_app(ServerConfig())) as client:
        too_large = client.get("/api/v1/audit/events", params={"limit": 101})
        negative_offset = client.get("/api/v1/audit/events", params={"offset": -1})

    assert too_large.status_code == 422
    assert negative_offset.status_code == 422


def test_audit_filter_is_exact_and_bounded() -> None:
    with TestClient(create_app(ServerConfig())) as client:
        client.get("/api/v1/health")
        response = client.get(
            "/api/v1/audit/events",
            params={"event": "health_snapshot_returned", "limit": 100},
        )

    assert response.status_code == 200
    payload = response.json()
    assert payload["items"]
    assert all(item["event"] == "health_snapshot_returned" for item in payload["items"])


def test_diagnostics_remain_fail_closed() -> None:
    with TestClient(create_app(ServerConfig())) as client:
        response = client.get("/api/v1/diagnostics")

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "SAFE"
    assert payload["mode"] == "NULL"
    assert payload["external_effects"] is False
    assert payload["database"] is False
    assert payload["live_mode"] is False


def test_read_endpoints_do_not_accept_mutation_methods() -> None:
    with TestClient(create_app(ServerConfig())) as client:
        assert client.post("/api/v1/runtime").status_code == 405
        assert client.put("/api/v1/audit/events").status_code == 405
        assert client.delete("/api/v1/diagnostics").status_code == 405
