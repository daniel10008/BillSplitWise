# --- file: ledger.py ---
import csv
import os
from typing import List
from datetime import datetime


LEDGER_FILE = "ledger.csv"

def record_settlement(payer: str, receiver: str, amount: float, note: str = "", period: str = "") -> None:
    """
    Record a settlement transaction in the ledger.
    """
    pass



def view_ledger() -> List[dict]:
    """
    Display all transactions from the ledger.
    """
    if not os.path.exists(LEDGER_FILE):
        return []

    
