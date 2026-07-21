"""SQLite, escritor único, outbox, backup, restore e staging do legado."""

from __future__ import annotations

import json
import os
import shutil
import sqlite3
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from threading import Lock
from typing import Any, Iterator, Mapping
from uuid import uuid4

SCHEMA_VERSION = 1
MIGRATIONS_DIR = Path(__file__).with_name("migrations")
SENSITIVE_KEYS = {"secret", "password", "token", "cookie", "credential", "api_key"}


class PersistenceError(RuntimeError):
    """Falha fechada com reason code estável."""

    def __init__(self, reason_code: str) -> None:
        self.reason_code = reason_code
        super().__init__(reason_code)


@dataclass(frozen=True, slots=True)
class DurableState:
    aggregate_type: str
    aggregate_id: str
    version: int
    payload: dict[str, Any]
    updated_at_utc: str


@dataclass(frozen=True, slots=True)
class DurableEvent:
    sequence: int
    event_id: str
    event_type: str
    event_version: str
    process_id: str
    trace_id: str
    aggregate_type: str
    aggregate_id: str
    aggregate_version: int
    payload: dict[str, Any]
    occurred_at_utc: str
    published_at_utc: str | None


@dataclass(frozen=True, slots=True)
class BackupReceipt:
    source_path: str
    backup_path: str
    sha256: str
    integrity_check: str
    schema_version: int


@dataclass(frozen=True, slots=True)
class LegacyImportResult:
    run_id: str
    idempotency_key: str
    source_hash: str
    status: str
    inventory_count: int
    accepted_count: int
    rejected_count: int
    source_backup_path: str
    database_backup_path: str


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _hash_bytes(value: bytes) -> str:
    return sha256(value).hexdigest()


def _hash_file(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _sql_statements(script: str) -> Iterator[str]:
    statement = ""
    for line in script.splitlines():
        statement += f"{line}\n"
        if sqlite3.complete_statement(statement):
            cleaned = statement.strip()
            if cleaned:
                yield cleaned
            statement = ""
    if statement.strip():
        raise PersistenceError("MIGRATION_SQL_INCOMPLETE")


def _contains_sensitive_key(value: Any) -> bool:
    if isinstance(value, Mapping):
        for key, item in value.items():
            normalized = str(key).lower()
            if any(marker in normalized for marker in SENSITIVE_KEYS):
                return True
            if _contains_sensitive_key(item):
                return True
    elif isinstance(value, list):
        return any(_contains_sensitive_key(item) for item in value)
    return False


class SQLitePersistence:
    """Única fronteira lógica autorizada a escrever no SQLite V1."""

    def __init__(
        self,
        database_path: Path,
        *,
        busy_timeout_ms: int = 5000,
        wal_enabled: bool = True,
        process_id: str | None = None,
    ) -> None:
        if database_path.is_symlink():
            raise PersistenceError("DATABASE_SYMLINK_REJECTED")
        if database_path.suffix.lower() not in {".db", ".sqlite", ".sqlite3"}:
            raise PersistenceError("DATABASE_EXTENSION_REJECTED")
        if not 100 <= busy_timeout_ms <= 30000:
            raise PersistenceError("DATABASE_BUSY_TIMEOUT_INVALID")
        self.database_path = database_path.resolve()
        self.busy_timeout_ms = busy_timeout_ms
        self.wal_enabled = wal_enabled
        self.process_id = process_id or uuid4().hex
        self._writer_lock = Lock()

    def initialize(self) -> None:
        self.database_path.parent.mkdir(parents=True, exist_ok=True)
        with self._writer_lock, self._connect() as connection:
            connection.execute(
                "CREATE TABLE IF NOT EXISTS schema_migrations ("
                "version INTEGER PRIMARY KEY, checksum TEXT NOT NULL, "
                "applied_at_utc TEXT NOT NULL)"
            )
            self._apply_migrations(connection)
            if self.integrity_check(connection) != "ok":
                raise PersistenceError("DATABASE_INTEGRITY_CHECK_FAILED")

    def _connect(self, *, read_only: bool = False) -> sqlite3.Connection:
        if read_only:
            connection = sqlite3.connect(
                f"file:{self.database_path}?mode=ro",
                uri=True,
                timeout=self.busy_timeout_ms / 1000,
                isolation_level=None,
            )
        else:
            connection = sqlite3.connect(
                self.database_path,
                timeout=self.busy_timeout_ms / 1000,
                isolation_level=None,
            )
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute(f"PRAGMA busy_timeout = {self.busy_timeout_ms}")
        if self.wal_enabled and not read_only:
            journal_mode = str(connection.execute("PRAGMA journal_mode = WAL").fetchone()[0])
            if journal_mode.lower() != "wal":
                connection.close()
                raise PersistenceError("DATABASE_WAL_UNAVAILABLE")
        return connection

    def _apply_migrations(self, connection: sqlite3.Connection) -> None:
        for version in range(1, SCHEMA_VERSION + 1):
            migration = MIGRATIONS_DIR / f"{version:04d}_initial.up.sql"
            sql = migration.read_text(encoding="utf-8")
            checksum = _hash_bytes(sql.encode("utf-8"))
            row = connection.execute(
                "SELECT checksum FROM schema_migrations WHERE version = ?", (version,)
            ).fetchone()
            if row is not None:
                if row["checksum"] != checksum:
                    raise PersistenceError("MIGRATION_CHECKSUM_MISMATCH")
                continue
            try:
                connection.execute("BEGIN IMMEDIATE")
                for statement in _sql_statements(sql):
                    connection.execute(statement)
                connection.execute(
                    "INSERT INTO schema_migrations(version, checksum, applied_at_utc) "
                    "VALUES (?, ?, ?)",
                    (version, checksum, _utc_now()),
                )
                connection.execute("COMMIT")
            except Exception:
                connection.execute("ROLLBACK")
                raise

    def schema_version(self) -> int:
        with self._connect(read_only=True) as connection:
            row = connection.execute("SELECT MAX(version) FROM schema_migrations").fetchone()
            return int(row[0] or 0)

    @staticmethod
    def integrity_check(connection: sqlite3.Connection) -> str:
        return str(connection.execute("PRAGMA integrity_check").fetchone()[0])

    def health(self) -> dict[str, Any]:
        with self._connect(read_only=True) as connection:
            return {
                "integrity_check": self.integrity_check(connection),
                "foreign_keys": int(connection.execute("PRAGMA foreign_keys").fetchone()[0]),
                "journal_mode": str(connection.execute("PRAGMA journal_mode").fetchone()[0]),
                "schema_version": self.schema_version(),
                "mode": "NULL_ONLY",
            }

    def assert_startup_ready(self) -> None:
        """Bloqueia startup quando a reconciliação legada possui divergências."""
        with self._connect(read_only=True) as connection:
            blocked = connection.execute(
                "SELECT COUNT(*) FROM migration_runs WHERE status = 'BLOCKED_RECONCILIATION'"
            ).fetchone()
            if int(blocked[0]) > 0:
                raise PersistenceError("LEGACY_RECONCILIATION_BLOCKS_STARTUP")

    def write_state(
        self,
        *,
        command_id: str,
        actor_id: str,
        expected_version: int,
        aggregate_type: str,
        aggregate_id: str,
        payload: Mapping[str, Any],
        trace_id: str,
        event_type: str = "state.updated",
    ) -> DurableState:
        if not all((command_id, actor_id, aggregate_type, aggregate_id, trace_id)):
            raise PersistenceError("MUTATION_METADATA_REQUIRED")
        if expected_version < 0:
            raise PersistenceError("EXPECTED_VERSION_INVALID")
        payload_dict = dict(payload)
        if _contains_sensitive_key(payload_dict):
            raise PersistenceError("PERSISTENCE_SENSITIVE_PAYLOAD_REJECTED")
        request = {
            "actor_id": actor_id,
            "expected_version": expected_version,
            "aggregate_type": aggregate_type,
            "aggregate_id": aggregate_id,
            "payload": payload_dict,
            "trace_id": trace_id,
            "event_type": event_type,
        }
        request_hash = _hash_bytes(_canonical_json(request).encode("utf-8"))

        with self._writer_lock, self._connect() as connection:
            try:
                connection.execute("BEGIN IMMEDIATE")
                previous = connection.execute(
                    "SELECT request_hash, response_json FROM command_results "
                    "WHERE command_id = ?",
                    (command_id,),
                ).fetchone()
                if previous is not None:
                    if previous["request_hash"] != request_hash:
                        raise PersistenceError("IDEMPOTENCY_KEY_CONFLICT")
                    connection.execute("COMMIT")
                    return DurableState(**json.loads(previous["response_json"]))

                current = connection.execute(
                    "SELECT version FROM aggregate_state "
                    "WHERE aggregate_type = ? AND aggregate_id = ?",
                    (aggregate_type, aggregate_id),
                ).fetchone()
                current_version = int(current["version"]) if current else 0
                if current_version != expected_version:
                    raise PersistenceError("STALE_EXPECTED_VERSION")

                new_version = current_version + 1
                occurred_at = _utc_now()
                payload_json = _canonical_json(payload_dict)
                connection.execute(
                    "INSERT INTO aggregate_state(aggregate_type, aggregate_id, version, "
                    "payload_json, updated_at_utc) VALUES (?, ?, ?, ?, ?) "
                    "ON CONFLICT(aggregate_type, aggregate_id) DO UPDATE SET "
                    "version=excluded.version, payload_json=excluded.payload_json, "
                    "updated_at_utc=excluded.updated_at_utc",
                    (aggregate_type, aggregate_id, new_version, payload_json, occurred_at),
                )
                connection.execute(
                    "INSERT INTO outbox_events(event_id, event_type, event_version, "
                    "process_id, trace_id, aggregate_type, aggregate_id, aggregate_version, "
                    "payload_json, occurred_at_utc) VALUES (?, ?, 'v1', ?, ?, ?, ?, ?, ?, ?)",
                    (
                        uuid4().hex,
                        event_type,
                        self.process_id,
                        trace_id,
                        aggregate_type,
                        aggregate_id,
                        new_version,
                        payload_json,
                        occurred_at,
                    ),
                )
                result = DurableState(
                    aggregate_type=aggregate_type,
                    aggregate_id=aggregate_id,
                    version=new_version,
                    payload=payload_dict,
                    updated_at_utc=occurred_at,
                )
                connection.execute(
                    "INSERT INTO command_results(command_id, actor_id, request_hash, "
                    "response_json, created_at_utc) VALUES (?, ?, ?, ?, ?)",
                    (command_id, actor_id, request_hash, _canonical_json(asdict(result)), occurred_at),
                )
                connection.execute("COMMIT")
                return result
            except Exception:
                if connection.in_transaction:
                    connection.execute("ROLLBACK")
                raise

    def read_state(self, aggregate_type: str, aggregate_id: str) -> DurableState | None:
        with self._connect(read_only=True) as connection:
            row = connection.execute(
                "SELECT * FROM aggregate_state WHERE aggregate_type = ? AND aggregate_id = ?",
                (aggregate_type, aggregate_id),
            ).fetchone()
            if row is None:
                return None
            return DurableState(
                aggregate_type=row["aggregate_type"],
                aggregate_id=row["aggregate_id"],
                version=int(row["version"]),
                payload=json.loads(row["payload_json"]),
                updated_at_utc=row["updated_at_utc"],
            )

    def pending_events(self, *, limit: int = 100) -> list[DurableEvent]:
        if not 1 <= limit <= 1000:
            raise PersistenceError("OUTBOX_LIMIT_INVALID")
        with self._connect(read_only=True) as connection:
            rows = connection.execute(
                "SELECT * FROM outbox_events WHERE published_at_utc IS NULL "
                "ORDER BY sequence LIMIT ?",
                (limit,),
            ).fetchall()
            return [self._event_from_row(row) for row in rows]

    def mark_event_published(self, event_id: str) -> None:
        with self._writer_lock, self._connect() as connection:
            connection.execute("BEGIN IMMEDIATE")
            cursor = connection.execute(
                "UPDATE outbox_events SET published_at_utc = COALESCE(published_at_utc, ?) "
                "WHERE event_id = ?",
                (_utc_now(), event_id),
            )
            if cursor.rowcount != 1:
                connection.execute("ROLLBACK")
                raise PersistenceError("OUTBOX_EVENT_UNKNOWN")
            connection.execute("COMMIT")

    @staticmethod
    def _event_from_row(row: sqlite3.Row) -> DurableEvent:
        return DurableEvent(
            sequence=int(row["sequence"]),
            event_id=row["event_id"],
            event_type=row["event_type"],
            event_version=row["event_version"],
            process_id=row["process_id"],
            trace_id=row["trace_id"],
            aggregate_type=row["aggregate_type"],
            aggregate_id=row["aggregate_id"],
            aggregate_version=int(row["aggregate_version"]),
            payload=json.loads(row["payload_json"]),
            occurred_at_utc=row["occurred_at_utc"],
            published_at_utc=row["published_at_utc"],
        )

    def backup_to(self, destination: Path) -> BackupReceipt:
        destination = destination.resolve()
        if destination.exists() or destination.is_symlink():
            raise PersistenceError("BACKUP_DESTINATION_MUST_BE_NEW")
        destination.parent.mkdir(parents=True, exist_ok=True)
        temporary = destination.with_suffix(destination.suffix + ".tmp")
        if temporary.exists():
            raise PersistenceError("BACKUP_TEMPORARY_PATH_OCCUPIED")
        try:
            with self._writer_lock, self._connect(read_only=True) as source:
                target = sqlite3.connect(temporary)
                try:
                    source.backup(target)
                    target.commit()
                    if self.integrity_check(target) != "ok":
                        raise PersistenceError("BACKUP_INTEGRITY_CHECK_FAILED")
                finally:
                    target.close()
            temporary.replace(destination)
            os.chmod(destination, 0o600)
            return BackupReceipt(
                source_path=str(self.database_path),
                backup_path=str(destination),
                sha256=_hash_file(destination),
                integrity_check="ok",
                schema_version=self.schema_version(),
            )
        finally:
            temporary.unlink(missing_ok=True)

    @classmethod
    def restore_to_new_database(
        cls,
        backup_path: Path,
        destination: Path,
        *,
        expected_sha256: str,
    ) -> BackupReceipt:
        backup_path = backup_path.resolve()
        destination = destination.resolve()
        if not backup_path.is_file() or backup_path.is_symlink():
            raise PersistenceError("RESTORE_BACKUP_INVALID")
        if destination.exists() or destination.is_symlink():
            raise PersistenceError("RESTORE_DESTINATION_MUST_BE_NEW")
        if _hash_file(backup_path) != expected_sha256:
            raise PersistenceError("RESTORE_BACKUP_HASH_MISMATCH")
        source = sqlite3.connect(f"file:{backup_path}?mode=ro", uri=True)
        try:
            if cls.integrity_check(source) != "ok":
                raise PersistenceError("RESTORE_BACKUP_INTEGRITY_FAILED")
            row = source.execute("SELECT MAX(version) FROM schema_migrations").fetchone()
            schema_version = int(row[0] or 0)
            if schema_version != SCHEMA_VERSION:
                raise PersistenceError("RESTORE_SCHEMA_VERSION_UNKNOWN")
        finally:
            source.close()
        destination.parent.mkdir(parents=True, exist_ok=True)
        temporary = destination.with_suffix(destination.suffix + ".tmp")
        try:
            shutil.copy2(backup_path, temporary)
            temporary.replace(destination)
            os.chmod(destination, 0o600)
            restored = cls(destination)
            if restored.health()["integrity_check"] != "ok":
                raise PersistenceError("RESTORE_DESTINATION_INTEGRITY_FAILED")
            return BackupReceipt(
                source_path=str(backup_path),
                backup_path=str(destination),
                sha256=_hash_file(destination),
                integrity_check="ok",
                schema_version=schema_version,
            )
        except Exception:
            temporary.unlink(missing_ok=True)
            if destination.exists():
                destination.unlink()
            raise

    def rollback_latest_if_empty(self) -> None:
        with self._writer_lock, self._connect() as connection:
            protected_tables = (
                "aggregate_state",
                "command_results",
                "outbox_events",
                "migration_runs",
                "legacy_staging",
            )
            if any(
                int(connection.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0])
                for table in protected_tables
            ):
                raise PersistenceError("ROLLBACK_BLOCKED_NONEMPTY_DATABASE")
            down = MIGRATIONS_DIR / "0001_initial.down.sql"
            try:
                connection.execute("BEGIN IMMEDIATE")
                for statement in _sql_statements(down.read_text(encoding="utf-8")):
                    connection.execute(statement)
                connection.execute("DELETE FROM schema_migrations WHERE version = 1")
                connection.execute("COMMIT")
            except Exception:
                if connection.in_transaction:
                    connection.execute("ROLLBACK")
                raise

    def import_legacy_to_staging(
        self,
        source_path: Path,
        evidence_dir: Path,
        *,
        importer_version: str = "1.0.0",
    ) -> LegacyImportResult:
        source_path = source_path.resolve()
        evidence_dir = evidence_dir.resolve()
        if not source_path.is_file() or source_path.is_symlink():
            raise PersistenceError("LEGACY_SOURCE_INVALID")
        raw = source_path.read_bytes()
        source_hash = _hash_bytes(raw)
        idempotency_key = f"{source_hash}|{importer_version}|{SCHEMA_VERSION}"

        existing = self._existing_import(idempotency_key)
        if existing is not None:
            return existing

        evidence_dir.mkdir(parents=True, exist_ok=True)
        source_backup = evidence_dir / f"legacy_source_{source_hash}.json"
        if not source_backup.exists():
            temporary = source_backup.with_suffix(".tmp")
            temporary.write_bytes(raw)
            temporary.replace(source_backup)
            os.chmod(source_backup, 0o600)
        if _hash_file(source_backup) != source_hash:
            raise PersistenceError("LEGACY_SOURCE_BACKUP_HASH_MISMATCH")

        run_id = uuid4().hex
        database_backup = evidence_dir / f"database_before_import_{source_hash}_{run_id}.db"
        database_receipt = self.backup_to(database_backup)
        staged, divergences = self._transform_legacy(raw)
        accepted_count = sum(1 for item in staged if item[3] == "ACCEPTED")
        rejected_count = len(staged) - accepted_count
        status = "CUTOVER_READY" if rejected_count == 0 else "BLOCKED_RECONCILIATION"
        counts = {
            "inventory": len(staged),
            "accepted": accepted_count,
            "rejected": rejected_count,
            "staged": len(staged),
            "authoritative": 0,
        }
        now = _utc_now()

        with self._writer_lock, self._connect() as connection:
            try:
                connection.execute("BEGIN IMMEDIATE")
                connection.execute(
                    "INSERT INTO migration_runs(run_id, idempotency_key, source_hash, "
                    "importer_version, target_schema_version, source_backup_path, "
                    "database_backup_path, status, counts_json, divergences_json, "
                    "created_at_utc, completed_at_utc) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (
                        run_id,
                        idempotency_key,
                        source_hash,
                        importer_version,
                        SCHEMA_VERSION,
                        str(source_backup),
                        database_receipt.backup_path,
                        status,
                        _canonical_json(counts),
                        _canonical_json(divergences),
                        now,
                        now,
                    ),
                )
                connection.executemany(
                    "INSERT INTO legacy_staging(run_id, source_key, payload_hash, "
                    "payload_json, status, reason_code) VALUES (?, ?, ?, ?, ?, ?)",
                    [(run_id, *item) for item in staged],
                )
                connection.execute("COMMIT")
            except Exception:
                if connection.in_transaction:
                    connection.execute("ROLLBACK")
                raise

        return LegacyImportResult(
            run_id=run_id,
            idempotency_key=idempotency_key,
            source_hash=source_hash,
            status=status,
            inventory_count=len(staged),
            accepted_count=accepted_count,
            rejected_count=rejected_count,
            source_backup_path=str(source_backup),
            database_backup_path=database_receipt.backup_path,
        )

    def _existing_import(self, idempotency_key: str) -> LegacyImportResult | None:
        with self._connect(read_only=True) as connection:
            row = connection.execute(
                "SELECT * FROM migration_runs WHERE idempotency_key = ?", (idempotency_key,)
            ).fetchone()
            if row is None:
                return None
            counts = json.loads(row["counts_json"])
            return LegacyImportResult(
                run_id=row["run_id"],
                idempotency_key=row["idempotency_key"],
                source_hash=row["source_hash"],
                status=row["status"],
                inventory_count=int(counts["inventory"]),
                accepted_count=int(counts["accepted"]),
                rejected_count=int(counts["rejected"]),
                source_backup_path=row["source_backup_path"],
                database_backup_path=row["database_backup_path"],
            )

    @staticmethod
    def _transform_legacy(raw: bytes) -> tuple[list[tuple[str, str, str, str, str | None]], list[str]]:
        try:
            payload = json.loads(raw.decode("utf-8"))
        except (UnicodeError, json.JSONDecodeError) as exc:
            raise PersistenceError("LEGACY_SOURCE_JSON_INVALID") from exc
        if not isinstance(payload, dict) or payload.get("version") not in {3, 4}:
            raise PersistenceError("LEGACY_SCHEMA_VERSION_UNKNOWN")

        profiles = payload.get("profiles", [])
        history = payload.get("history", payload.get("legacy_history", []))
        if not isinstance(profiles, list) or not isinstance(history, list):
            raise PersistenceError("LEGACY_COLLECTION_INVALID")

        staged: list[tuple[str, str, str, str, str | None]] = []
        divergences: list[str] = []
        seen_keys: set[str] = set()
        items = [("profile", item) for item in profiles] + [
            ("history", item) for item in history
        ]
        for index, (kind, item) in enumerate(items):
            identifier = item.get("id") if isinstance(item, dict) else None
            source_key = f"{kind}:{identifier or index}"
            reason: str | None = None
            if source_key in seen_keys:
                reason = "DUPLICATE_SOURCE_KEY"
            elif not isinstance(item, dict):
                reason = "LEGACY_ITEM_OBJECT_REQUIRED"
            elif not identifier:
                reason = "LEGACY_ITEM_ID_REQUIRED"
            elif _contains_sensitive_key(item):
                reason = "SENSITIVE_FIELD_REJECTED"
            seen_keys.add(source_key)
            if reason:
                safe_payload: Any = {"rejected": reason}
                status = "REJECTED"
                divergences.append(f"{source_key}:{reason}")
            else:
                safe_payload = item
                status = "ACCEPTED"
            payload_json = _canonical_json(safe_payload)
            staged.append(
                (
                    source_key,
                    _hash_bytes(payload_json.encode("utf-8")),
                    payload_json,
                    status,
                    reason,
                )
            )
        return staged, divergences
