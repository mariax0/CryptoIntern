## Scenario

CryptoIntern is a startup focused on **cryptocurrency** analytics and trading, created for retail and institutional investors.

## Business Requirements

CryptoIntern offers a platform for cryptocurrency transactions, real-time price tracking, and market trend analysis.

### Core business goals

- **Cryptocurrency Analysis**: Aggregate price evolution for major cryptocurrencies.
- **Market Insights**: Track trends in crypto demand.
- **Price Trends**: Provide benchmarks for crypto prices.
- **Crypto Popularity**: Identify the most in-demand cryptocurrencies.
- **Portfolio Insights**: Analyze user trading patterns and portfolio performance.

### Reports

Buy transactions by cryptocurrency. \
Sell transactions by cryptocurrency. \
Price evolution of the top 10 cryptocurrencies by market cap or trading volume. \
Volatility reports for major cryptocurrencies (daily/weekly price swings).

### Dashboards

Current price of BTC vs other cryptocurrencies and USD. \
Maximum and minimum price of BTC on the current day. \
Historical price evolution of BTC and other top cryptocurrencies. \
Trading volume trends for the top 10 cryptocurrencies.

### KPIs

Total cryptocurrency transactions (buy/sell). \
Average transaction amount (in USD or BTC equivalent). \
Top 10 buy transactions by amount. \
Top 10 sell transactions by amount. \
Market share of top cryptocurrencies by trading volume.

## Data Warehouse Design

It has a server `CryptoIntern` and a database named `cryptointern_db`.

### Sources

- **CryptoIntern Platform**: Internal data on user transactions (buy/sell), wallet balances, and user portfolios.
- **[Coinranking API](https://developers.coinranking.com/api)**: External data for crypto prices, volumes, and metadata.

#### CryptoIntern Source

`cryptointern_data`

| Column Name      | Data Type      | Description                                    |
| ---------------- | -------------- | ---------------------------------------------- |
| transaction_id   | VARCHAR(50)    | Unique identifier of a transaction             |
| user_id          | VARCHAR(20)    | Platform user identifier                       |
| first_name       | VARCHAR(255)   | Customer first name (optional for privacy)     |
| last_name        | VARCHAR(255)   | Customer last name (optional for privacy)      |
| wallet_address   | VARCHAR(100)   | Crypto wallet address                          |
| crypto_symbol    | VARCHAR(10)    | Cryptocurrency identifier (e.g. BTC, ETH)      |
| crypto_to        | VARCHAR(10)    | Target cryptocurrency or fiat (e.g. USDT, USD) |
| transaction_type | VARCHAR(4)     | Type of the transaction (buy, sell, swap)      |
| transaction_time | TIMESTAMP      | Timestamp of the transaction                   |
| amount           | DECIMAL(18, 8) | Amount of money of the transaction             |
| price_usd        | DECIMAL(18, 2) | Transaction price in USD at the time           |
| total_usd        | DECIMAL(18, 2) | Total transaction value in USD (amount\*price) |

#### Coinranking Source

`coinranking_data`

| Column Name           | Data Type      | Description                                  |
| --------------------- | -------------- | -------------------------------------------- |
| crypto_id             | VARCHAR(50)    | Unique Coinranking ID for the cryptocurrency |
| crypto_symbol         | VARCHAR(10)    | Cryptocurrency symbol (e.g. BTC, ETH)        |
| crypto_name           | VARCHAR(50)    | Cryptocurrency name (e.g. Bitcoin)           |
| price_usd             | DECIMAL(18, 2) | Current price in USD                         |
| volume_24h            | DECIMAL(18, 2) | 24-hour trading volume in USD                |
| market_cap            | DECIMAL(18, 2) | Market capitalization in USD                 |
| time_last_update_unix | TIMESTAMP      | Timestamp of the last data update            |
| time_next_update_unix | TIMESTAMP      | Timestamp for the next expected update       |

## Architecture of Data Warehousing

The `cryptointern_db` database has 3 layers:

- raw --> initial source data
- staging --> transformed data
- trusted --> consumption data
