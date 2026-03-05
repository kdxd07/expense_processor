import logging
from database.connection import get_db_connection

# Setup logging to see if any errors happen
logger = logging.getLogger(__name__)

def run_basic_analytics() -> None:
    # This function connects to the database to show a summary of my spending
    connection = get_db_connection()
    if not connection:
        logger.error("❌ Could not connect to database. Skipping analytics.")
        return
    
    try:
        cursor = connection.cursor()
        
        # 1. Add up all my spending
        # I use COALESCE so it shows 0 instead of 'None' if the table is empty
        cursor.execute("SELECT COALESCE(SUM(amount), 0) FROM expenses;")
        total_result = cursor.fetchone()[0]
        print(f"\n📊 TOTAL SPENDING: ${float(total_result):.2f}")

        # 2. Show spending for each category
        # I group them together and sort by the highest price first
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
        # Show an error if the math or the SQL doesn't work
        logger.error(f"❌ Analytics processing failed: {error}")
    finally:
        # Close the connection when I'm done with the database
        connection.close()