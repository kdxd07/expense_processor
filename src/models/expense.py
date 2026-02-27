from pydantic import BaseModel, field_validator
from datetime import date
from typing import Optional

class Expense(BaseModel):
    transaction_date: date
    category: str
    amount: float
    description: Optional[str] = "No description"

    @field_validator('amount')
    @classmethod
    def amount_must_be_positive(cls, v: float) -> float:
        if v <= 0:
            raise ValueError('Amount must be greater than zero')
        return v