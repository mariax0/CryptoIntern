INSERT INTO staging.stg_cryptointern_data
SELECT
  transaction_id,
  user_id,
  INITCAP(TRIM(first_name)),
  INITCAP(TRIM(last_name)),
  wallet_address,
  crypto_symbol,
  crypto_to,
  UPPER(transaction_type),
  transaction_time::TIMESTAMP,
  amount,
  ROUND(price_usd, 2),
  ROUND(total_usd, 2)
FROM raw.cryptointern_data 
WHERE amount > 0 AND price_usd > 0 AND total_usd = amount * price_usd;


