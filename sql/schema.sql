CREATE TABLE IF NOT EXISTS financial_transactions (

    transaction_id SERIAL PRIMARY KEY,

    customer_name VARCHAR(100),

    account_number VARCHAR(30),

    transaction_type VARCHAR(20),

    amount DECIMAL(12,2),

    currency VARCHAR(10),

    country VARCHAR(50),

    transaction_time TIMESTAMP,

    status VARCHAR(20)

);