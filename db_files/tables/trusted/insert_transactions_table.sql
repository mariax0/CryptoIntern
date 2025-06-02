INSERT INTO trusted.transactions
SELECT DISTINCT
  s.transaction_id,
  s.user_id,
  INITCAP(s.first_name) || ' ' || INITCAP(s.last_name) AS full_name,
  s.wallet_address,
  s.crypto_symbol,
  s.crypto_to,
  s.transaction_type,
  s.transaction_time AS timestamp,
  s.amount,
  s.price_usd AS unit_price_usd,
  s.total_usd,
  c.market_cap
FROM staging.stg_cryptointern_data s
LEFT JOIN staging.stg_coinranking_data c
  ON s.crypto_symbol = c.crypto_symbol;
