DROP INDEX IF EXISTS idx_legacy_staging_status;
DROP INDEX IF EXISTS idx_outbox_unpublished;
DROP TABLE IF EXISTS legacy_staging;
DROP TABLE IF EXISTS migration_runs;
DROP TABLE IF EXISTS outbox_events;
DROP TABLE IF EXISTS command_results;
DROP TABLE IF EXISTS aggregate_state;
