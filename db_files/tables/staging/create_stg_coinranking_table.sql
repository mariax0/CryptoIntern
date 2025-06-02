CREATE TABLE IF NOT EXISTS staging.stg_coinranking_data (
    crypto_id VARCHAR(50),
    crypto_symbol VARCHAR(10),
    crypto_name	VARCHAR(50),
    price_usd DECIMAL(18, 2),
    volume_24h DECIMAL(18, 2),
    market_cap DECIMAL(18, 2),
    time_last_update TIMESTAMP,
    time_next_update TIMESTAMP
)