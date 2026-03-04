import logging
from database.connection import get_db_connection

# Initialize logger to track analytics performance and errors
logger = logging.getLogger(__name__)

def run_basic_analytics() -> None:
    """
    Connects to PostgreSQL and executes aggregation queries to 
    provide a summary of spending habits.
    """
    connection = get_db_connection()
    if not connection:
        logger.error("❌ Could not connect to database. Skipping analytics.")
        return
    
    try:
        cursor = connection.cursor()
        
        # 1. Calculate Total Spending
        # We use COALESCE to return 0.00 if the table is empty, preventing None errors
        cursor.execute("SELECT COALESCE(SUM(amount), 0) FROM expenses;")
        total_result = cursor.fetchone()[0]
        print(f"\n📊 TOTAL SPENDING: ${float(total_result):.2f}")

        # 2. Group Spending by Category
        # We order by sum descending to show the highest expenses at the top
        print("\n📂 SPENDING BY CATEGORY:")
        category_query = """
            SELECT category, SUM(amount) 
            FROM expenses 
            GROUP BY category 
            ORDER BY SUM(amount) DESC;
        """
        cursor.execute(category_query)
        
        category_rows = cursor.fetchall()
        if not category_rows:
            print(" - No data available.")
        else:
            for category, amount in category_rows:
                print(f" - {category}: ${float(amount):.2f}")

        cursor.close()
        
    except Exception as error:
        logger.error(f"❌ Analytics processing failed: {error}")
    finally:
        # Always close the connection to prevent memory leaks or hanging connections
        connection.close()