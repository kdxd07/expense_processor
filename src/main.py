import os
import logging
from dotenv import load_dotenv

# Import our refined modules with updated function names
from utils.csv_helper import get_expenses_from_folder
from database.connection import insert_expenses
from utils.analytics import run_basic_analytics

# Standard logging configuration for production-ready output
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load secret credentials and configurations
load_dotenv()

def main() -> None:
    """
    Main execution entry point. Coordinates the ETL pipeline:
    Extract (CSV) -> Transform (Pydantic) -> Load (Postgres) -> Analyze.
    """
    logger.info("🚀 Starting Expense Processor...")
    
    # Retrieve data location from environment variables or use default
    data_folder = os.getenv("DATA_FOLDER", "./data")
    
    # PHASE 1: Data Ingestion and Validation
    # We call the renamed function from csv_helper.py
    expenses = get_expenses_from_folder(data_folder)
    
    # PHASE 2: Persistence and Analysis
    if expenses:
        # Attempt to store the validated records in the database
        insert_expenses(expenses)
        
        # PHASE 3: Business Intelligence
        logger.info("📈 Running final analytics...")
        run_basic_analytics()
    else:
        logger.warning("⚠️ No valid expenses found to process. Check your data folder.")

if __name__ == "__main__":
    # This ensures main() only runs if the script is executed directly
    main()