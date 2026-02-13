-- sql/quickstart/00_seed.sql
-- Initialize demo tables and data for the SQL QuickStart lessons.
PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS orders;

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name        TEXT NOT NULL,
    city        TEXT NOT NULL,
    tier        TEXT NOT NULL
);

CREATE TABLE orders (
    order_id     INTEGER PRIMARY KEY,
    customer_id  INTEGER NOT NULL,
    order_date   TEXT NOT NULL,
    amount       REAL NOT NULL,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);

INSERT INTO customers (customer_id, name, city, tier) VALUES
(1, 'Alice',   'Seattle',   'Gold'),
(2, 'Bob',     'Portland',  'Silver'),
(3, 'Charlie', 'San Jose',  'Gold'),
(4, 'Diana',   'Seattle',   'Bronze'),
(5, 'Evan',    'Sacramento','Silver');

INSERT INTO orders (order_id, customer_id, order_date, amount) VALUES
(1001, 1, '2025-12-01', 120.50),
(1002, 1, '2025-12-15', 75.00),
(1003, 2, '2025-12-20', 200.00),
(1004, 3, '2026-01-05', 310.25),
(1005, 4, '2026-01-11', 45.00),
(1006, 5, '2026-01-12', 500.00),
(1007, 3, '2026-01-20', 88.88);
