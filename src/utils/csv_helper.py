import csv
import pathlib
import logging
from typing import List
from models.expense import Expense

# Initialize logger for this module
logger = logging.getLogger(__name__)

def get_expenses_from_folder(folder_path: str) -> List[Expense]:
    """
    Reads all CSV files in a directory, validates data using Pydantic,
    and returns a list of Expense objects.
    """
    validated_expenses = []
    source_directory = pathlib.Path(folder_path)
    
    # Iterate through all CSV files in the target directory
    for csv_file in source_directory.glob("*.csv"):
        logger.info(f"📁 Processing file: {csv_file.name}")
        
        try:
            with open(csv_file, mode='r', encoding='utf-8') as file_handle:
                csv_reader = csv.DictReader(file_handle)
                
                for row in csv_reader:
                    try:
                        # Instantiate the Expense model to trigger Pydantic validation
                        expense_entry = Expense(**row)
                        validated_expenses.append(expense_entry)
                    except Exception as error:
                        # Log validation errors but continue processing the rest of the file
                        logger.error(f"❌ Validation failed in {csv_file.name} for row {row}: {error}")
        except IOError as io_error:
            logger.error(f"📂 Could not read file {csv_file.name}: {io_error}")
                    
    return validated_expenses