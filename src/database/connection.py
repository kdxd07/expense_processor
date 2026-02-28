import os
import psycopg2
import logging
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        return conn
    except Exception as e:
        logger.error(f"❌ Database connection failed: {e}")
        return None
    
def insert_expenses(expenses):
    conn = get_db_connection()
    if not conn:
        return
    
    try:
        cur = conn.cursor()
        query = """
            INSERT INTO expenses (transaction_date, category, amount, description)
            VALUES (%s, %s, %s, %s)
        """
        # Convert Pydantic objects to tuples for SQL
        data_to_insert = [
            (e.transaction_date, e.category, e.amount, e.description)
            for e in expenses
        ]
        
        cur.executemany(query, data_to_insert)
        conn.commit()
        logger.info(f"💾 Successfully inserted {len(data_to_insert)} records into PostgreSQL.")
        cur.close()
    except Exception as e:
        logger.error(f"❌ Failed to insert data: {e}")
    finally:
        conn.close()