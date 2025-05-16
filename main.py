# --- file: main.py ---
from datetime import datetime
import re
from flatmate import Flatmate
from bill import Bill
from utils import validate_positive_float, validate_positive_int
from storage import save_bill_to_csv
from reports import PdfReport
from admin import (
    list_categories, add_category, remove_category,
    add_user, list_users, remove_user
)
from settlement import simplify_debts
from ledger import view_ledger, record_settlement
from tabulate import tabulate
import os
import csv
from collections import defaultdict
from openpyxl import Workbook

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def generate_bill():
    pass


def admin_menu():
    clear_screen()
    while True:
        print("""
Admin Menu:
1. Add category
2. Remove category
3. List categories
4. Add user
5. Remove user
6. List users
7. Back to main menu
        """)
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            name = input("Enter new category name: ").strip()
            if name:
                add_category(name)
        elif choice == '2':
            name = input("Enter category name to remove: ").strip()
            if name:
                remove_category(name)
        elif choice == '3':
            cats = list_categories()
            if cats:
                print("\nAvailable Categories:")
                for i, cat in enumerate(cats, 1):
                    print(f"  {i}. {cat}")
            else:
                print("No categories found.")
        elif choice == '4':
            uname = input("Enter username: ").strip()
            email = input("Enter email: ").strip()
            if uname and email:
                add_user(uname, email)
        elif choice == '5':
            uname = input("Enter username to remove: ").strip()
            if uname:
                remove_user(uname)
        elif choice == '6':
            users = list_users()
            if users:
                print("\nRegistered Users:")
                for i, user in enumerate(users, 1):
                    print(f"  {i}. {user['Username']} ({user['Email']})")
            else:
                print("No users found.")
        elif choice == '7':
            break
        else:
            print("Invalid choice. Try again.")


def export_report_to_excel(data: list, filename: str = "bill_history.xlsx"):
    pass
    


def display_report(filepath: str = "bill_history.csv"):
    if not os.path.exists(filepath):
        print("No historical report found.")
        return

    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    if not data:
        print("No records to display.")
        return

    print("""
Report Filter Options:
1. View all records (with summary insights)
2. Filter by billing period
3. Filter by flatmate name
4. Export report to Excel
5. Back to main menu
    """)
    choice = input("Choose an option: ").strip()

    if choice == '1':
        filtered = data
    elif choice == '2':
        period = input("Enter billing period to filter (e.g., March 2025): ").strip()
        filtered = [row for row in data if row["Period"].lower() == period.lower()]
    elif choice == '3':
        name = input("Enter flatmate name to filter: ").strip()
        filtered = [row for row in data if row["Name"].lower() == name.lower()]
    elif choice == '4':
        export_report_to_excel(data)
        return
    else:
        return

    if filtered:
        print("\n📊 Filtered Bill Report:")
        print(tabulate(filtered, headers="keys", tablefmt="grid"))

        if choice == '1':
            print("\n📈 Report Summary and Insights:")
            
    else:
        print("No matching records found.")

def generate_pdf_from_history():
    if not os.path.exists("bill_history.csv"):
        print("❌ No billing history found.")
        return

    

def main():
    clear_screen()
    while True:
        print("""
Welcome to Flatmate Bill Splitter
1. Generate Bill
2. Admin Menu
3. Display Report
4. View Settlement Ledger
5. Generate PDF Report from History
6. Exit               
        """)
        choice = input("Select an option: ").strip()

        if choice == '1':
            generate_bill()
        elif choice == '2':
            admin_menu()
        elif choice == '3':
            display_report()
        elif choice == '4':
            ledger_data = view_ledger()
            if ledger_data:
                print("\n📒 Transaction Ledger:")
                print(tabulate(ledger_data, headers="keys", tablefmt="grid"))
            else:
                print("No transactions recorded yet.")
        elif choice == '5':
            generate_pdf_from_history()
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
