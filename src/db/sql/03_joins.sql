-- sql/quickstart/03_joins.sql
-- Basic INNER JOIN between customers and orders
SELECT o.order_id, c.name AS customer, c.city, o.order_date, o.amount
FROM orders o
JOIN customers c ON c.customer_id = o.customer_id
ORDER BY o.order_date DESC, o.order_id DESC
LIMIT 20;
