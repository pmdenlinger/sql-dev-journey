-- Audit Log Schema
-- Purpose: Store Microsoft 365 audit activity in a normalized form

CREATE TABLE audit_events (
    event_id BIGINT PRIMARY KEY,
    event_time_utc TIMESTAMP,
    workload VARCHAR(128),
    operation VARCHAR(255),
    actor_upn VARCHAR(255),
    target_object VARCHAR(255),
    payload JSON
);
