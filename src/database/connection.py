import os
import psycopg2
import logging
from typing import List, Optional
from dotenv import load_dotenv
from models.expense import Expense

# Load environment variables from .env file
load_dotenv()
logger = logging.getLogger(__name__)

def get_db_connection():
    """
    Establishes a connection to the PostgreSQL database using 
    credentials stored in environment variables.
    """
    try:
        connection = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        return connection
    except Exception as error:
        logger.error(f"❌ Database connection failed: {error}")
        return None
    
def insert_expenses(expenses: List[Expense]) -> None:
    """
    Cleans existing records and performs a bulk insertion of 
    validated Expense objects into PostgreSQL.
    """
    connection = get_db_connection()
    if not connection:
        return
    
    try:
        with connection.cursor() as cursor:
            # IMPORTANT: Clear existing data to prevent duplication on re-runs
            cursor.execute("TRUNCATE TABLE expenses;")
            logger.info("🧹 Database cleared for fresh synchronization.")

            insert_query = """
                INSERT INTO expenses (transaction_date, category, amount, description)
                VALUES (%s, %s, %s, %s)
            """
            
            # Prepare data: Convert Pydantic objects into a list of tuples
            data_to_insert = [
                (exp.transaction_date, exp.category, exp.amount, exp.description)
                for exp in expenses
            ]
            
            # Efficiently insert all records in one batch
            cursor.executemany(insert_query, data_to_insert)
            
            # Commit the transaction to make changes permanent
            connection.commit()
            logger.info(f"💾 Successfully inserted {len(data_to_insert)} records into PostgreSQL.")
            
    except Exception as error:
        logger.error(f"❌ Failed to insert data into database: {error}")
    finally:
        # Always close the connection to free up database resources
        connection.close()