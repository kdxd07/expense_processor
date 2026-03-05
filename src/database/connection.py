import os
import psycopg2
import logging
from typing import List, Optional
from dotenv import load_dotenv
from models.expense import Expense

# Get the variables from my .env file
load_dotenv()
logger = logging.getLogger(__name__)

def get_db_connection():
    # This function helps me connect to the database
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
        # If the connection doesn't work, show the error
        logger.error(f"❌ Database connection failed: {error}")
        return None
    
def insert_expenses(expenses: List[Expense]) -> None:
    # This function puts my list of expenses into the table
    connection = get_db_connection()
    if not connection:
        return
    
    try:
        with connection.cursor() as cursor:
            # First, delete old stuff so I don't have the same data twice
            cursor.execute("TRUNCATE TABLE expenses;")
            logger.info("🧹 Database cleared for fresh synchronization.")

            # My SQL command to save the data
            insert_query = """
                INSERT INTO expenses (transaction_date, category, amount, description)
                VALUES (%s, %s, %s, %s)
            """
            
            # Change my expense objects into a list that SQL can understand
            data_to_insert = [
                (exp.transaction_date, exp.category, exp.amount, exp.description)
                for exp in expenses
            ]
            
            # Save all the rows at the same time
            cursor.executemany(insert_query, data_to_insert)
            
            # Make sure the changes are actually saved
            connection.commit()
            logger.info(f"💾 Successfully inserted {len(data_to_insert)} records into PostgreSQL.")
            
    except Exception as error:
        # Show an error if something goes wrong with the saving process
        logger.error(f"❌ Failed to insert data into database: {error}")
    finally:
        # Close the connection when I am finished
        connection.close()