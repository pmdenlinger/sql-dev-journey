-- Data Modeling Basics
-- Purpose: Demonstrate normalized table design for compliance data

CREATE TABLE matters (
    matter_id INT PRIMARY KEY,
    matter_name VARCHAR(255),
    opened_date DATE
);

CREATE TABLE custodians (
    custodian_id INT PRIMARY KEY,
    custodian_name VARCHAR(255),
    email VARCHAR(255)
);
