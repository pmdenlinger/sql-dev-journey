-- eDiscovery Case Metrics
-- Business Question:
-- How many cases were created, reviewed, and exported in a given period?

WITH cases AS (
    SELECT DISTINCT payload->>'caseId' AS case_id,
           event_time_utc
    FROM audit_events
    WHERE operation = 'CaseCreated'
)
SELECT COUNT(*) AS total_cases
FROM cases;
