INSERT INTO staging.stg_coinranking_data
SELECT
  crypto_id,
  crypto_symbol,
  TRIM(crypto_name),
  ROUND(price_usd, 2),
  ROUND(volume_24h, 2),
  ROUND(market_cap, 2),
  time_last_update::TIMESTAMP,
  time_next_update::TIMESTAMP
FROM raw.coinranking_data;
