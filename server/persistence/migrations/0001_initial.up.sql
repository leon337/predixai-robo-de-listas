CREATE TABLE aggregate_state (
    aggregate_type TEXT NOT NULL,
    aggregate_id TEXT NOT NULL,
    version INTEGER NOT NULL CHECK (version > 0),
    payload_json TEXT NOT NULL,
    updated_at_utc TEXT NOT NULL,
    PRIMARY KEY (aggregate_type, aggregate_id)
);

CREATE TABLE command_results (
    command_id TEXT PRIMARY KEY,
    actor_id TEXT NOT NULL,
    request_hash TEXT NOT NULL,
    response_json TEXT NOT NULL,
    created_at_utc TEXT NOT NULL
);

CREATE TABLE outbox_events (
    sequence INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id TEXT NOT NULL UNIQUE,
    event_type TEXT NOT NULL,
    event_version TEXT NOT NULL,
    process_id TEXT NOT NULL,
    trace_id TEXT NOT NULL,
    aggregate_type TEXT NOT NULL,
    aggregate_id TEXT NOT NULL,
    aggregate_version INTEGER NOT NULL,
    payload_json TEXT NOT NULL,
    occurred_at_utc TEXT NOT NULL,
    published_at_utc TEXT,
    FOREIGN KEY (aggregate_type, aggregate_id)
        REFERENCES aggregate_state (aggregate_type, aggregate_id)
);

CREATE TABLE migration_runs (
    run_id TEXT PRIMARY KEY,
    idempotency_key TEXT NOT NULL UNIQUE,
    source_hash TEXT NOT NULL,
    importer_version TEXT NOT NULL,
    target_schema_version INTEGER NOT NULL,
    source_backup_path TEXT NOT NULL,
    database_backup_path TEXT NOT NULL,
    status TEXT NOT NULL,
    counts_json TEXT NOT NULL,
    divergences_json TEXT NOT NULL,
    created_at_utc TEXT NOT NULL,
    completed_at_utc TEXT NOT NULL
);

CREATE TABLE legacy_staging (
    run_id TEXT NOT NULL,
    source_key TEXT NOT NULL,
    payload_hash TEXT NOT NULL,
    payload_json TEXT NOT NULL,
    status TEXT NOT NULL,
    reason_code TEXT,
    PRIMARY KEY (run_id, source_key),
    FOREIGN KEY (run_id) REFERENCES migration_runs (run_id) ON DELETE RESTRICT
);

CREATE INDEX idx_outbox_unpublished
    ON outbox_events (published_at_utc, sequence);

CREATE INDEX idx_legacy_staging_status
    ON legacy_staging (run_id, status);
