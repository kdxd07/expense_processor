from pydantic import BaseModel, field_validator
from datetime import date
from typing import Optional

class Expense(BaseModel):
    # This class sets up how my expense data should look
    transaction_date: date
    category: str
    amount: float
    description: Optional[str] = "No description"

    @field_validator('amount')
    @classmethod
    def amount_must_be_positive(cls, amount_value: float) -> float:
        # This part checks if the price is a positive number
        # I don't want any negative numbers in my list
        if amount_value <= 0:
            raise ValueError('Amount must be greater than zero')
        return amount_value