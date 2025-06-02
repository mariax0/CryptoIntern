INSERT INTO trusted.crypto  
SELECT DISTINCT
    crypto_id,
    crypto_symbol,
    INITCAP(TRIM(crypto_name)),
    price_usd,
    volume_24h,
    market_cap,
    time_last_update
FROM staging.stg_coinranking_data;
