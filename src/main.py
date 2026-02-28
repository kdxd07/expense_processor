import os
import logging
from dotenv import load_dotenv
from utils.csv_helper import read_csv_files
from database.connection import insert_expenses # New import

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

load_dotenv()

def main():
    logger.info("🚀 Starting Expense Processor...")
    
    data_folder = os.getenv("DATA_FOLDER", "./data")
    
    # 1. Ingest and Validate (from Day 2)
    expenses = read_csv_files(data_folder)
    
    # 2. Insert into Database (Day 3 Goal)
    if expenses:
        insert_expenses(expenses)
    else:
        logger.warning("⚠️ No valid expenses found to insert.")

if __name__ == "__main__":
    main()