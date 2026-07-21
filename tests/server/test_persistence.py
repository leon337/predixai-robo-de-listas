import json
import sqlite3
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import pytest

from server.persistence import PersistenceError, SQLitePersistence


def initialized_store(tmp_path: Path) -> SQLitePersistence:
    store = SQLitePersistence(tmp_path / "state.db")
    store.initialize()
    return store


def table_count(database: Path, table: str) -> int:
    with sqlite3.connect(database) as connection:
        return int(connection.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0])


def test_initialization_applies_schema_with_wal_and_foreign_keys(tmp_path: Path) -> None:
    store = initialized_store(tmp_path)

    health = store.health()

    assert health == {
        "integrity_check": "ok",
        "foreign_keys": 1,
        "journal_mode": "wal",
        "schema_version": 1,
        "mode": "NULL_ONLY",
    }


def test_state_and_versioned_event_are_committed_atomically(tmp_path: Path) -> None:
    store = initialized_store(tmp_path)

    state = store.write_state(
        command_id="cmd-1",
        actor_id="operator-1",
        expected_version=0,
        aggregate_type="configuration",
        aggregate_id="local",
        payload={"theme": "safe"},
        trace_id="trace-1",
        event_type="configuration.updated",
    )
    events = store.pending_events()

    assert state.version == 1
    assert store.read_state("configuration", "local") == state
    assert len(events) == 1
    assert events[0].event_version == "v1"
    assert events[0].aggregate_version == 1
    assert events[0].payload == {"theme": "safe"}


def test_command_id_is_idempotent_and_conflicts_fail_closed(tmp_path: Path) -> None:
    store = initialized_store(tmp_path)
    arguments = {
        "command_id": "cmd-stable",
        "actor_id": "operator-1",
        "expected_version": 0,
        "aggregate_type": "configuration",
        "aggregate_id": "local",
        "payload": {"value": 1},
        "trace_id": "trace-1",
    }

    first = store.write_state(**arguments)
    repeated = store.write_state(**arguments)

    assert repeated == first
    assert len(store.pending_events()) == 1
    with pytest.raises(PersistenceError, match="IDEMPOTENCY_KEY_CONFLICT"):
        store.write_state(**{**arguments, "payload": {"value": 2}})


def test_stale_write_rolls_back_state_event_and_receipt(tmp_path: Path) -> None:
    store = initialized_store(tmp_path)
    store.write_state(
        command_id="cmd-1",
        actor_id="operator-1",
        expected_version=0,
        aggregate_type="configuration",
        aggregate_id="local",
        payload={"value": 1},
        trace_id="trace-1",
    )

    with pytest.raises(PersistenceError, match="STALE_EXPECTED_VERSION"):
        store.write_state(
            command_id="cmd-2",
            actor_id="operator-2",
            expected_version=0,
            aggregate_type="configuration",
            aggregate_id="local",
            payload={"value": 2},
            trace_id="trace-2",
        )

    assert store.read_state("configuration", "local").payload == {"value": 1}  # type: ignore[union-attr]
    assert table_count(store.database_path, "command_results") == 1
    assert table_count(store.database_path, "outbox_events") == 1


def test_sqlite_serializes_competing_writers(tmp_path: Path) -> None:
    store_a = initialized_store(tmp_path)
    store_b = SQLitePersistence(store_a.database_path)
    barrier_arguments = [
        (store_a, "cmd-a", "trace-a"),
        (store_b, "cmd-b", "trace-b"),
    ]

    def write(arguments: tuple[SQLitePersistence, str, str]) -> str:
        store, command_id, trace_id = arguments
        try:
            store.write_state(
                command_id=command_id,
                actor_id="operator",
                expected_version=0,
                aggregate_type="configuration",
                aggregate_id="shared",
                payload={"winner": command_id},
                trace_id=trace_id,
            )
        except PersistenceError as exc:
            return exc.reason_code
        return "PASS"

    with ThreadPoolExecutor(max_workers=2) as executor:
        results = list(executor.map(write, barrier_arguments))

    assert sorted(results) == ["PASS", "STALE_EXPECTED_VERSION"]
    assert table_count(store_a.database_path, "aggregate_state") == 1
    assert table_count(store_a.database_path, "outbox_events") == 1


def test_outbox_acknowledgement_is_durable_and_unknown_event_is_rejected(tmp_path: Path) -> None:
    store = initialized_store(tmp_path)
    store.write_state(
        command_id="cmd-1",
        actor_id="operator",
        expected_version=0,
        aggregate_type="configuration",
        aggregate_id="local",
        payload={},
        trace_id="trace",
    )
    event = store.pending_events()[0]

    store.mark_event_published(event.event_id)

    assert store.pending_events() == []
    with pytest.raises(PersistenceError, match="OUTBOX_EVENT_UNKNOWN"):
        store.mark_event_published("unknown")


def test_backup_and_restore_prove_hash_integrity_and_state(tmp_path: Path) -> None:
    store = initialized_store(tmp_path)
    store.write_state(
        command_id="cmd-1",
        actor_id="operator",
        expected_version=0,
        aggregate_type="configuration",
        aggregate_id="local",
        payload={"durable": True},
        trace_id="trace",
    )
    receipt = store.backup_to(tmp_path / "evidence" / "backup.db")

    restored_receipt = SQLitePersistence.restore_to_new_database(
        Path(receipt.backup_path),
        tmp_path / "restored" / "state.db",
        expected_sha256=receipt.sha256,
    )
    restored = SQLitePersistence(Path(restored_receipt.backup_path))

    assert restored.health()["integrity_check"] == "ok"
    assert restored.read_state("configuration", "local").payload == {"durable": True}  # type: ignore[union-attr]


def test_restore_rejects_tampered_hash_and_existing_destination(tmp_path: Path) -> None:
    store = initialized_store(tmp_path)
    receipt = store.backup_to(tmp_path / "backup.db")

    with pytest.raises(PersistenceError, match="RESTORE_BACKUP_HASH_MISMATCH"):
        SQLitePersistence.restore_to_new_database(
            Path(receipt.backup_path), tmp_path / "restored.db", expected_sha256="0" * 64
        )
    existing = tmp_path / "existing.db"
    existing.write_text("protected", encoding="utf-8")
    with pytest.raises(PersistenceError, match="RESTORE_DESTINATION_MUST_BE_NEW"):
        SQLitePersistence.restore_to_new_database(
            Path(receipt.backup_path), existing, expected_sha256=receipt.sha256
        )
    assert existing.read_text(encoding="utf-8") == "protected"


def test_down_migration_is_reversible_only_while_database_is_empty(tmp_path: Path) -> None:
    empty = initialized_store(tmp_path / "empty")
    empty.rollback_latest_if_empty()
    assert empty.schema_version() == 0

    populated = initialized_store(tmp_path / "populated")
    populated.write_state(
        command_id="cmd",
        actor_id="operator",
        expected_version=0,
        aggregate_type="configuration",
        aggregate_id="local",
        payload={},
        trace_id="trace",
    )
    with pytest.raises(PersistenceError, match="ROLLBACK_BLOCKED_NONEMPTY_DATABASE"):
        populated.rollback_latest_if_empty()
    assert populated.schema_version() == 1


def test_legacy_import_is_staged_idempotent_and_never_authoritative(tmp_path: Path) -> None:
    store = initialized_store(tmp_path)
    source = tmp_path / "legacy-v3.json"
    source_payload = {
        "version": 3,
        "profiles": [{"id": "profile-1", "name": "Local"}],
        "history": [{"id": "history-1", "result": "archived"}],
    }
    source.write_text(json.dumps(source_payload), encoding="utf-8")
    before = source.read_bytes()

    first = store.import_legacy_to_staging(source, tmp_path / "evidence")
    repeated = store.import_legacy_to_staging(source, tmp_path / "evidence")

    assert first == repeated
    assert first.status == "CUTOVER_READY"
    assert first.inventory_count == first.accepted_count == 2
    assert first.rejected_count == 0
    assert source.read_bytes() == before
    assert table_count(store.database_path, "migration_runs") == 1
    assert table_count(store.database_path, "legacy_staging") == 2
    assert table_count(store.database_path, "aggregate_state") == 0
    assert Path(first.source_backup_path).read_bytes() == before
    assert Path(first.database_backup_path).is_file()


def test_legacy_divergence_blocks_cutover_and_redacts_sensitive_payload(tmp_path: Path) -> None:
    store = initialized_store(tmp_path)
    source = tmp_path / "legacy-v4.json"
    source.write_text(
        json.dumps(
            {
                "version": 4,
                "profiles": [
                    {"id": "duplicate", "name": "A"},
                    {"id": "duplicate", "name": "B"},
                    {"id": "secret", "api_token": "must-not-persist"},
                ],
                "legacy_history": [],
            }
        ),
        encoding="utf-8",
    )

    result = store.import_legacy_to_staging(source, tmp_path / "evidence")

    assert result.status == "BLOCKED_RECONCILIATION"
    assert result.accepted_count == 1
    assert result.rejected_count == 2
    with sqlite3.connect(store.database_path) as connection:
        stored = " ".join(row[0] for row in connection.execute("SELECT payload_json FROM legacy_staging"))
    assert "must-not-persist" not in stored
    assert table_count(store.database_path, "aggregate_state") == 0


@pytest.mark.parametrize(
    ("payload", "reason"),
    [
        (b"not-json", "LEGACY_SOURCE_JSON_INVALID"),
        (b'{"version": 2, "profiles": [], "history": []}', "LEGACY_SCHEMA_VERSION_UNKNOWN"),
    ],
)
def test_invalid_legacy_source_fails_without_staging(
    tmp_path: Path, payload: bytes, reason: str
) -> None:
    store = initialized_store(tmp_path)
    source = tmp_path / "legacy.json"
    source.write_bytes(payload)

    with pytest.raises(PersistenceError, match=reason):
        store.import_legacy_to_staging(source, tmp_path / "evidence")

    assert table_count(store.database_path, "migration_runs") == 0
    assert table_count(store.database_path, "legacy_staging") == 0


def test_database_path_rejects_symlink_and_unsupported_extension(tmp_path: Path) -> None:
    real = tmp_path / "real.db"
    real.touch()
    symlink = tmp_path / "link.db"
    symlink.symlink_to(real)

    with pytest.raises(PersistenceError, match="DATABASE_SYMLINK_REJECTED"):
        SQLitePersistence(symlink)
    with pytest.raises(PersistenceError, match="DATABASE_EXTENSION_REJECTED"):
        SQLitePersistence(tmp_path / "state.txt")
