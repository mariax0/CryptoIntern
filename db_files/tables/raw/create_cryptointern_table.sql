CREATE TABLE IF NOT EXISTS raw.cryptointern_data (
    transaction_id	VARCHAR(50),
    user_id	VARCHAR(20),
    first_name VARCHAR(200),
    last_name VARCHAR(200),
    wallet_address VARCHAR(100),
    crypto_symbol VARCHAR(10),
    crypto_to VARCHAR(10),
    transaction_type VARCHAR(4),
    transaction_time TIMESTAMP,
    amount DECIMAL(18, 8),
    price_usd DECIMAL(18, 2),
    total_usd DECIMAL(18, 2)
)