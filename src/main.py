import os
import logging
from dotenv import load_dotenv
from utils.csv_helper import read_csv_files

# 1. Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# 2. Load the .env file
load_dotenv()

def main():
    logger.info("🚀 Starting Expense Processor...")
    
    # Fetch the folder path from .env
    data_folder = os.getenv("DATA_FOLDER", "./data")
    
    # 3. Call the Ingestor (We will create this next)
    expenses = read_csv_files(data_folder)
    
    logger.info(f"✅ Successfully validated {len(expenses)} total expenses.")

if __name__ == "__main__":
    main()