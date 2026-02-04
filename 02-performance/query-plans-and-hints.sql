-- Query Plans and Performance
-- Purpose: Illustrate query plan considerations

SELECT /* review execution plan */
    matter_id,
    COUNT(*) AS event_count
FROM audit_events
GROUP BY matter_id;
