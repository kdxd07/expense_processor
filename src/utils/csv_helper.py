import csv
import pathlib
import logging
from models.expense import Expense

logger = logging.getLogger(__name__)

def read_csv_files(folder_path):
    all_expenses = []
    # Convert string path to a Path object to find all .csv files
    path = pathlib.Path(folder_path)
    
    # Loop through every file ending in .csv in that folder
    for csv_file in path.glob("*.csv"):
        logger.info(f"📁 Processing file: {csv_file.name}")
        
        with open(csv_file, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    # Pass the row through our Pydantic Gatekeeper
                    expense = Expense(**row)
                    all_expenses.append(expense)
                except Exception as e:
                    # If validation fails, log it as an error but keep going!
                    logger.error(f"❌ Validation failed in {csv_file.name} for row {row}: {e}")
                    
    return all_expenses