import csv
import pathlib
import logging
from typing import List
from models.expense import Expense

# Setup my logger so I can see what is happening
logger = logging.getLogger(__name__)

def get_expenses_from_folder(folder_path: str) -> List[Expense]:
    # This function goes through my folder to read all the CSV files
    validated_expenses = []
    source_directory = pathlib.Path(folder_path)
    
    # Look for every file that ends with .csv
    for csv_file in source_directory.glob("*.csv"):
        logger.info(f"📁 Processing file: {csv_file.name}")
        
        try:
            # Open the file so I can read the rows
            with open(csv_file, mode='r', encoding='utf-8') as file_handle:
                csv_reader = csv.DictReader(file_handle)
                
                for row in csv_reader:
                    try:
                        # Use my Expense class to check if the data is correct
                        expense_entry = Expense(**row)
                        validated_expenses.append(expense_entry)
                    except Exception as error:
                        # If a row has bad data, show an error but keep going
                        logger.error(f"❌ Validation failed in {csv_file.name} for row {row}: {error}")
        except IOError as io_error:
            # Show an error if the file itself can't be opened
            logger.error(f"📂 Could not read file {csv_file.name}: {io_error}")
                    
    return validated_expenses