import os
from dotenv import load_dotenv
from models.expense import Expense

# 1. Load the .env file
load_dotenv()

def verify_setup():
    print("--- Day 1 Verification ---")
    
    # Check Environment Variables
    db_name = os.getenv("DB_NAME")
    print(f"[INFO] Database Name from .env: {db_name}")
    
    # Test Pydantic Model with sample data
    test_data = {
        "transaction_date": "2026-02-27",
        "category": "Food",
        "amount": 450.75,
        "description": "Day 1 Celebration"
    }
    
    try:
        expense = Expense(**test_data)
        print(f"[SUCCESS] Pydantic validated: {expense.category} - {expense.amount}")
    except Exception as e:
        print(f"[ERROR] Validation failed: {e}")

if __name__ == "__main__":
    verify_setup()