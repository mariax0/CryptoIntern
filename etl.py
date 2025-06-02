# etl.py
import os
from dotenv import load_dotenv
from etl.extract.from_csv import load_csv_to_db
from etl.extract.from_api import fetch_and_insert
from etl.load.sql_runner import get_connection, run_sql_file

def get_all_sql_files(paths):
    sql_files = []
    for path in paths:
        for root, _, files in os.walk(path):
            for file in sorted(files):
                if file.endswith('.sql'):
                    sql_files.append(os.path.join(root, file))
    return sql_files

def etl():
    load_dotenv()

    print("Extracting data...")
    load_csv_to_db("data/cryptointern_data.csv")
    fetch_and_insert()

    print("Running transformations...")
    try:
        conn = get_connection()
        cursor = conn.cursor()

        base_dir = os.path.dirname(__file__)
        sql_dirs = [
            os.path.join(base_dir, 'db_files', 'schemas'),
            os.path.join(base_dir, 'db_files', 'tables', 'raw'),
            os.path.join(base_dir, 'db_files', 'tables', 'staging'),
            os.path.join(base_dir, 'db_files', 'tables', 'trusted')
        ]

        for file in get_all_sql_files(sql_dirs):
            run_sql_file(cursor, file)

        conn.commit()
        print("All SQL transformations applied.")

    except Exception as e:
        print(f"Pipeline failed: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()
        print("Database connection closed.")

if __name__ == "__main__":
    etl()
