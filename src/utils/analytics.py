import logging
from database.connection import get_db_connection

logger = logging.getLogger(__name__)

def run_basic_analytics():
    conn = get_db_connection()
    if not conn:
        return
    
    try:
        cur = conn.cursor()
        
        # 1. Total Spending
        cur.execute("SELECT SUM(amount) FROM expenses;")
        total = cur.fetchone()[0]
        print(f"\n📊 TOTAL SPENDING: ${total:.2f}")

        # 2. Spending by Category
        print("\n📂 SPENDING BY CATEGORY:")
        cur.execute("""
            SELECT category, SUM(amount) 
            FROM expenses 
            GROUP BY category 
            ORDER BY SUM(amount) DESC;
        """)
        for row in cur.fetchall():
            print(f" - {row[0]}: ${row[1]:.2f}")

        cur.close()
    except Exception as e:
        logger.error(f"❌ Analytics failed: {e}")
    finally:
        conn.close()