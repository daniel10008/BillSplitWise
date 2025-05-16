from typing import Dict, List
from bill import Bill

class Flatmate:
    """
    Represents a flatmate with name and days stayed.
    """
    def __init__(self, name: str, days_in_house: int):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill: Bill, flatmates: List['Flatmate']) -> Dict[str, float]:
        """
        Calculates the share of the flatmate for each expense category.
        """
        total_days = sum(f.days_in_house for f in flatmates)
        weight = self.days_in_house / total_days
        return {category: amount * weight for category, amount in bill.expenses.items()}