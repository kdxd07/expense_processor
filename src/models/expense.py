from pydantic import BaseModel, field_validator
from datetime import date
from typing import Optional

class Expense(BaseModel):
    """
    Data model for a single expense record.
    Handles automatic type conversion and validation for incoming data.
    """
    transaction_date: date
    category: str
    amount: float
    description: Optional[str] = "No description"

    @field_validator('amount')
    @classmethod
    def amount_must_be_positive(cls, amount_value: float) -> float:
        """
        Custom validator to ensure the expense is a positive number.
        This prevents accidental entry of negative expenses or refunds 
        into the main expense table.
        """
        if amount_value <= 0:
            raise ValueError('Amount must be greater than zero')
        return amount_value