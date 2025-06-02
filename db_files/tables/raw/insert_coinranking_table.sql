INSERT INTO raw.coinranking_data (
    crypto_id,
    crypto_symbol,
    crypto_name,
    price_usd,
    volume_24h,
    market_cap,
    time_last_update,
    time_next_update
) VALUES (
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s
);