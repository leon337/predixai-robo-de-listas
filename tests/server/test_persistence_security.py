import json
import sqlite3
from pathlib import Path

import pytest

from server.config import ServerConfig
from server.contracts import ReasonCode, RuntimeState
from server.persistence import PersistenceError, SQLitePersistence
from server.service import SafeServerService


def test_migration_checksum_drift_fails_closed(tmp_path: Path) -> None:
    store = SQLitePersistence(tmp_path / "state.db")
    store.initialize()
    with sqlite3.connect(store.database_path) as connection:
        connection.execute("UPDATE schema_migrations SET checksum = 'tampered' WHERE version = 1")

    with pytest.raises(PersistenceError, match="MIGRATION_CHECKSUM_MISMATCH"):
        store.initialize()


def test_service_degrades_when_persistence_startup_fails(tmp_path: Path) -> None:
    invalid_database = tmp_path / "occupied.db"
    invalid_database.write_text("not a sqlite database", encoding="utf-8")
    service = SafeServerService(ServerConfig(database_path=invalid_database))

    with pytest.raises((PersistenceError, sqlite3.DatabaseError)):
        service.start()

    assert service.state_snapshot() == (
        RuntimeState.DEGRADED,
        ReasonCode.PERSISTENCE_FAIL_CLOSED,
    )


def test_mutation_requires_actor_command_version_and_trace(tmp_path: Path) -> None:
    store = SQLitePersistence(tmp_path / "state.db")
    store.initialize()

    with pytest.raises(PersistenceError, match="MUTATION_METADATA_REQUIRED"):
        store.write_state(
            command_id="",
            actor_id="",
            expected_version=0,
            aggregate_type="configuration",
            aggregate_id="local",
            payload={},
            trace_id="",
        )
    assert store.read_state("configuration", "local") is None


def test_sensitive_payload_is_rejected_before_transaction(tmp_path: Path) -> None:
    store = SQLitePersistence(tmp_path / "state.db")
    store.initialize()

    with pytest.raises(PersistenceError, match="PERSISTENCE_SENSITIVE_PAYLOAD_REJECTED"):
        store.write_state(
            command_id="command",
            actor_id="operator",
            expected_version=0,
            aggregate_type="configuration",
            aggregate_id="local",
            payload={"api_token": "must-not-persist"},
            trace_id="trace",
        )

    assert store.read_state("configuration", "local") is None


def test_null_only_contract_is_preserved_when_database_is_enabled(tmp_path: Path) -> None:
    service = SafeServerService(ServerConfig(database_path=tmp_path / "state.db"))
    service.start()

    capabilities = service.capabilities()

    assert capabilities.database is True
    assert capabilities.external_effects is False
    assert capabilities.broker_connection is False
    assert capabilities.real_click is False
    assert capabilities.live_mode is False
    assert service.adapter.execute({}).reason_code is ReasonCode.NULL_ADAPTER_ACTIVE


def test_unreconciled_legacy_import_blocks_next_startup(tmp_path: Path) -> None:
    database = tmp_path / "state.db"
    store = SQLitePersistence(database)
    store.initialize()
    legacy = tmp_path / "legacy.json"
    legacy.write_text(
        json.dumps(
            {
                "version": 4,
                "profiles": [{"id": "duplicate"}, {"id": "duplicate"}],
                "history": [],
            }
        ),
        encoding="utf-8",
    )
    result = store.import_legacy_to_staging(legacy, tmp_path / "evidence")
    assert result.status == "BLOCKED_RECONCILIATION"
    service = SafeServerService(ServerConfig(database_path=database))

    with pytest.raises(PersistenceError, match="LEGACY_RECONCILIATION_BLOCKS_STARTUP"):
        service.start()

    assert service.state_snapshot() == (
        RuntimeState.DEGRADED,
        ReasonCode.PERSISTENCE_FAIL_CLOSED,
    )
