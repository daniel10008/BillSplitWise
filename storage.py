import csv
from typing import Dict, List
import os

def save_bill_to_csv(period: str, flatmate_shares: List[Dict[str, str]], filepath: str = "bill_history.csv") -> None:
    """Appends the bill record to a CSV file for historical tracking without duplicates."""

    existing_keys = set()

    # Step 1: Load existing keys from file (Period + Name + Category)
    

    # Step 2: Prepare to write new entries
    
