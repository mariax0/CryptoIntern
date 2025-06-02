import os
import psycopg2
import pandas as pd
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

def load_csv_to_db(csv_path):
    df = pd.read_csv(csv_path)

    insert_sql = load_insert_sql("db_files/tables/raw/insert_cryptointern_table.sql")

    conn = get_connection()
    cursor = conn.cursor()

    for row in df.itertuples(index=False):
        cursor.execute(insert_sql, tuple(row))

    conn.commit()
    cursor.close()
    conn.close()
    print("CSV data loaded successfully.")

if __name__ == "__main__":
    load_csv_to_db("data/cryptointern_data.csv")  
