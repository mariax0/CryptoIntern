INSERT INTO raw.cryptointern_data (
    transaction_id,
    user_id,
    first_name,
    last_name,
    wallet_address,
    crypto_symbol,
    crypto_to,
    transaction_type,
    transaction_time,
    amount,
    price_usd,
    total_usd
) VALUES (
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s
);