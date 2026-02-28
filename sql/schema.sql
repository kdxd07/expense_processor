CREATE TABLE IF NOT EXISTS expenses (
    id SERIAL PRIMARY KEY,
    transaction_date DATE NOT NULL,
    category VARCHAR(100) NOT NULL,
    amount DECIMAL(12, 2) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);