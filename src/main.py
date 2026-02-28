import os
import logging
from dotenv import load_dotenv

# 1. Imports from your custom modules
from utils.csv_helper import read_csv_files
from database.connection import insert_expenses
from utils.analytics import run_basic_analytics

# 2. Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

load_dotenv()

def main():
    logger.info("🚀 Starting Expense Processor...")
    
    data_folder = os.getenv("DATA_FOLDER", "./data")
    
    # STEP 1: Ingest and Validate
    expenses = read_csv_files(data_folder)
    
    # STEP 2: Insert into Database
    if expenses:
        insert_expenses(expenses)
        
        # STEP 3: Run Analytics (The Stretch Goal)
        logger.info("📈 Running final analytics...")
        run_basic_analytics()
    else:
        logger.warning("⚠️ No valid expenses found to process.")

if __name__ == "__main__":
    main()