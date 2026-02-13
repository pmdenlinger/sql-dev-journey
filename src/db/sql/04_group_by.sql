-- sql/quickstart/04_group_by.sql
-- Aggregations with GROUP BY
SELECT c.city, COUNT(*) AS num_orders, ROUND(SUM(o.amount), 2) AS total_amount
FROM orders o
JOIN customers c ON c.customer_id = o.customer_id
GROUP BY c.city
ORDER BY total_amount DESC;
