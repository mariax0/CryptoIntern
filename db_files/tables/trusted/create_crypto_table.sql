CREATE TABLE IF NOT EXISTS trusted.crypto (
    crypto_id VARCHAR(50) PRIMARY KEY,
    crypto_symbol VARCHAR(10),
    crypto_name VARCHAR(50),
    price_usd DECIMAL(18, 2),
    volume_24h DECIMAL(18, 2),
    market_cap DECIMAL(18, 2),
    last_updated TIMESTAMP
);
