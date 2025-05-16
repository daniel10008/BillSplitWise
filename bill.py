from typing import Dict

class Bill:
    """
    Object to store individual category expenses for a billing period.
    """
    def __init__(self, period: str, expenses: Dict[str, float]):
        self.period = period
        self.expenses = expenses

    def total_amount(self) -> float:
        """Returns the total amount of the bill."""
        return sum(self.expenses.values())
