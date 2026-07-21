from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import SecretStr

from server.app import create_app
from server.config import ServerConfig

ADMIN_HEADERS = {"X-PredixAI-Admin-Secret": "local-test-admin"}


def configured_app() -> FastAPI:
    return create_app(ServerConfig(admin_secret=SecretStr("local-test-admin")))


def pair(client: TestClient) -> dict[str, object]:
    challenge_response = client.post(
        "/api/v1/identity/pairing/challenges",
        headers=ADMIN_HEADERS,
        json={"device_id": "device-001", "operator_id": "operator-001"},
    )
    assert challenge_response.status_code == 200
    challenge = challenge_response.json()["challenge"]
    response = client.post(
        "/api/v1/identity/pair",
        json={
            "challenge": challenge,
        },
    )
    assert response.status_code == 200
    return response.json()


def test_identified_client_reads_null_capabilities_without_grant() -> None:
    app = configured_app()
    with TestClient(app) as client:
        session = pair(client)
        response = client.get(
            "/api/v1/identity/capabilities",
            headers={"Authorization": f"Bearer {session['access_token']}"},
        )

    assert response.status_code == 200
    payload = response.json()
    assert payload["device_id"] == "device-001"
    assert payload["mode"] == "NULL"
    assert payload["command_grant"] is False
    assert payload["real_click"] is False
    assert payload["broker_connection"] is False
    assert payload["live_mode"] is False


def test_admin_secret_is_required_and_never_returned() -> None:
    app = configured_app()
    with TestClient(app) as client:
        request = {"device_id": "device-001", "operator_id": "operator-001"}
        missing = client.post("/api/v1/identity/pairing/challenges", json=request)
        wrong = client.post(
            "/api/v1/identity/pairing/challenges",
            headers={"X-PredixAI-Admin-Secret": "wrong"},
            json=request,
        )
        accepted = client.post(
            "/api/v1/identity/pairing/challenges",
            headers=ADMIN_HEADERS,
            json=request,
        )

    assert missing.status_code == 401
    assert wrong.status_code == 401
    assert accepted.status_code == 200
    assert "local-test-admin" not in accepted.text
    assert "local-test-admin" not in repr(app.state.service.audit.snapshot())


def test_client_cannot_self_assign_an_elevated_role() -> None:
    app = configured_app()
    with TestClient(app) as client:
        challenge = client.post(
            "/api/v1/identity/pairing/challenges",
            headers=ADMIN_HEADERS,
            json={
                "device_id": "device-001",
                "operator_id": "operator-001",
                "role": "ADMIN",
            },
        )

    assert challenge.status_code == 422


def test_client_cannot_replace_admin_bound_identity_during_pairing() -> None:
    app = configured_app()
    with TestClient(app) as client:
        challenge = client.post(
            "/api/v1/identity/pairing/challenges",
            headers=ADMIN_HEADERS,
            json={"device_id": "device-001", "operator_id": "operator-001"},
        ).json()["challenge"]
        response = client.post(
            "/api/v1/identity/pair",
            json={
                "challenge": challenge,
                "device_id": "attacker-device",
                "operator_id": "attacker-operator",
            },
        )

    assert response.status_code == 422


def test_revocation_blocks_existing_session() -> None:
    app = configured_app()
    with TestClient(app) as client:
        session = pair(client)
        token = str(session["access_token"])
        revoked = client.post(
            "/api/v1/identity/devices/device-001/revoke",
            headers=ADMIN_HEADERS,
        )
        capabilities = client.get(
            "/api/v1/identity/capabilities",
            headers={"Authorization": f"Bearer {token}"},
        )

    assert revoked.status_code == 200
    assert revoked.json()["sessions_terminated"] == 1
    assert capabilities.status_code == 401


def test_presence_and_reconnection_do_not_create_grant() -> None:
    app = configured_app()
    with TestClient(app) as client:
        session = pair(client)
        headers = {"Authorization": f"Bearer {session['access_token']}"}
        first = client.post("/api/v1/identity/presence", headers=headers)
        second = client.post("/api/v1/identity/presence", headers=headers)

    assert first.status_code == 200
    assert second.status_code == 200
    assert first.json()["sequence"] == 1
    assert second.json()["sequence"] == 2
    assert second.json()["authorization_grant"] is False


def test_identity_can_be_disabled_fail_closed() -> None:
    app = create_app(
        ServerConfig(
            identity_enabled=False,
            admin_secret=SecretStr("local-test-admin"),
        )
    )
    with TestClient(app) as client:
        response = client.post(
            "/api/v1/identity/pairing/challenges",
            headers=ADMIN_HEADERS,
            json={"device_id": "device-001", "operator_id": "operator-001"},
        )

    assert response.status_code == 503
