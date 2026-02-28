import pytest
from src.models.expense import Expense

def test_valid_expense():
    # Tests if valid data passes
    data = {"transaction_date": "2026-01-01", "category": "Food", "amount": "50.00", "description": "Lunch"}
    expense = Expense(**data)
    assert expense.category == "Food"
    assert float(expense.amount) == 50.00

def test_invalid_amount():
    # Tests if negative amount raises an error
    data = {"transaction_date": "2026-01-01", "category": "Food", "amount": "-10.00", "description": "Error"}
    with pytest.raises(Exception):
        Expense(**data)
        