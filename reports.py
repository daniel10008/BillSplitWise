# --- file: reports.py ---
import csv
import re
from typing import List
import webbrowser
import os
from fpdf import FPDF
from datetime import datetime
from settlement import simplify_debts


class PdfReport:
    """
    Creates a professional multi-page PDF report of flatmate bills.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmates: List, bill) -> None:
        pass
