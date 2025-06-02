import os
from zoneinfo import ZoneInfo
import psycopg2
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )

def load_insert_sql(file_path):
    with open(file_path, "r") as f:
        return f.read()

def fetch_and_insert():
    url = "https://api.coinranking.com/v2/coins"
    headers = {
        "x-access-token": os.getenv("COINRANKING_API_KEY")
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    coins = data["data"]["coins"]
    ro_tz = ZoneInfo("Europe/Bucharest")
    now = datetime.now(tz=ro_tz)
    next_update = now + timedelta(hours=24)

    insert_sql = load_insert_sql("db_files/tables/raw/insert_coinranking_table.sql")

    conn = get_connection()
    cursor = conn.cursor()

    for coin in coins:
        cursor.execute(insert_sql, (
            coin["uuid"],
            coin["symbol"],
            coin["name"],
            float(coin["price"]),
            float(coin["24hVolume"]),
            float(coin["marketCap"]),
            now,
            next_update
        ))

    conn.commit()
    cursor.close()
    conn.close()
    print("API data loaded successfully")

if __name__ == "__main__":
    fetch_and_insert()
