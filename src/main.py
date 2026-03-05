import os
import logging
from dotenv import load_dotenv

# Import my own functions from the other files
from utils.csv_helper import get_expenses_from_folder
from database.connection import insert_expenses
from utils.analytics import run_basic_analytics

# Basic setup for logging so I can see what the program is doing
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load my settings from the .env file
load_dotenv()

def main() -> None:
    # This is the main part of my program that runs everything in order
    logger.info("🚀 Starting Expense Processor...")
    
    # 1. Look for my folder where the CSV files are stored
    data_folder = os.getenv("DATA_FOLDER", "./data")
    
    # 2. Go get the expenses from that folder
    expenses = get_expenses_from_folder(data_folder)
    
    # 3. If I actually found some data, save it and show the results
    if expenses:
        # Save the list of expenses into my Postgres database
        insert_expenses(expenses)
        
        # Now run the math to show my total spending
        logger.info("📈 Running final analytics...")
        run_basic_analytics()
    else:
        # Show a warning if the folder was empty or files were bad
        logger.warning("⚠️ No valid expenses found to process. Check your data folder.")

if __name__ == "__main__":
    # This makes sure the program only starts if I run this specific file
    main()