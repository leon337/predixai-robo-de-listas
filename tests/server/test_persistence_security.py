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



def test_restore_preserves_preexisting_temporary_file(tmp_path: Path) -> None:
    store = SQLitePersistence(tmp_path / "state.db")
    store.initialize()
    receipt = store.backup_to(tmp_path / "backup.db")
    destination = tmp_path / "restored.db"
    temporary = destination.with_suffix(destination.suffix + ".tmp")
    temporary.write_text("protected-temporary-content", encoding="utf-8")

    with pytest.raises(PersistenceError, match="RESTORE_TEMPORARY_PATH_OCCUPIED"):
        SQLitePersistence.restore_to_new_database(
            Path(receipt.backup_path),
            destination,
            expected_sha256=receipt.sha256,
        )

    assert temporary.read_text(encoding="utf-8") == "protected-temporary-content"
    assert not destination.exists()


def test_backup_and_restore_reject_dangling_symlink_destinations(tmp_path: Path) -> None:
    store = SQLitePersistence(tmp_path / "state.db")
    store.initialize()
    target = tmp_path / "redirected.db"
    backup_link = tmp_path / "backup-link.db"
    backup_link.symlink_to(target)

    with pytest.raises(PersistenceError, match="BACKUP_SYMLINK_REJECTED"):
        store.backup_to(backup_link)

    assert backup_link.is_symlink()
    assert not target.exists()

    receipt = store.backup_to(tmp_path / "safe-backup.db")
    restore_link = tmp_path / "restore-link.db"
    restore_link.symlink_to(target)
    with pytest.raises(PersistenceError, match="RESTORE_DESTINATION_SYMLINK_REJECTED"):
        SQLitePersistence.restore_to_new_database(
            Path(receipt.backup_path),
            restore_link,
            expected_sha256=receipt.sha256,
        )

    assert restore_link.is_symlink()
    assert not target.exists()


def test_backup_rejects_symlinked_parent_directory(tmp_path: Path) -> None:
    store = SQLitePersistence(tmp_path / "state.db")
    store.initialize()
    redirected_directory = tmp_path / "redirected"
    redirected_directory.mkdir()
    linked_directory = tmp_path / "linked"
    linked_directory.symlink_to(redirected_directory, target_is_directory=True)

    with pytest.raises(PersistenceError, match="BACKUP_SYMLINK_REJECTED"):
        store.backup_to(linked_directory / "backup.db")

    assert not (redirected_directory / "backup.db").exists()


def test_local_validator_binds_report_to_exact_remote_head_and_sha256() -> None:
    script = (
        Path(__file__).resolve().parents[2] / "scripts" / "local_validate_dat_001.sh"
    ).read_text(encoding="utf-8")

    assert '[[ "$REMOTE_BRANCH_HEAD" == "$EXPECTED_COMMIT" ]]' in script
    assert "merge-base --is-ancestor" not in script
    assert "DAT_001_LOCAL_VALIDATION_${EXPECTED_COMMIT}_${TIMESTAMP}.txt" in script
    assert 'VALIDATED_COMMIT="$(git rev-parse HEAD)"' in script
    assert 'REPORT_SHA256="$(sha256sum "$REPORT_FILE"' in script
    assert 'REPORT_SHA256_FILE="${REPORT_FILE}.sha256"' in script
