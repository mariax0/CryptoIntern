import os
import psycopg2
from dotenv import load_dotenv

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )

def get_all_sql_files(paths):
    sql_files = []
    for path in paths:
        for root, _, files in os.walk(path):
            for file in sorted(files):
                if file.endswith('.sql'):
                    sql_files.append(os.path.join(root, file))
    return sql_files

def run_sql_file(cursor, file_path):
    with open(file_path, 'r') as file:
        sql = file.read()
        
    if '%s' in sql:
        print(f"Skipping parameterized query: {os.path.relpath(file_path)}")
        return
    
    try:
        cursor.execute(sql)
        print(f"Ran: {os.path.relpath(file_path)}")
    except Exception as e:
        print(f"Error in {os.path.relpath(file_path)}: {e}")

def main():
    load_dotenv()
    try:
        conn = get_connection()
        cursor = conn.cursor()
        print("Connected to the database")

        base_dir = os.path.dirname(__file__)
        schemas_path = os.path.join(base_dir, 'db_files', 'schemas')
        tables_path = os.path.join(base_dir, 'db_files', 'tables')

        sql_paths = [
            schemas_path,
            os.path.join(tables_path, 'raw'),
            os.path.join(tables_path, 'staging'),
            os.path.join(tables_path, 'trusted')
        ]

        sql_files = get_all_sql_files(sql_paths)

        for sql_file in sql_files:
            run_sql_file(cursor, sql_file)

        conn.commit()
        print("All changes committed")

    except Exception as e:
        print(f"Operation failed: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()
        print("Connection closed")

if __name__ == "__main__":
    main()
