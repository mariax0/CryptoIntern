CREATE TABLE IF NOT EXISTS trusted.transactions (
    transaction_id VARCHAR(50) PRIMARY KEY,
    user_id VARCHAR(20),
    full_name VARCHAR(400),
    wallet_address VARCHAR(100),
    crypto_symbol VARCHAR(10),
    crypto_to VARCHAR(10),
    transaction_type VARCHAR(4),
    timestamp TIMESTAMP,
    amount DECIMAL(18, 8),
    unit_price_usd DECIMAL(18, 2),
    total_usd DECIMAL(18, 2),
    market_cap_usd DECIMAL(18, 2)
);