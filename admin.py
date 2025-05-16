# --- file: admin.py ---
import os
import csv

USER_FILE = "users.csv"

CATEGORY_FILE = "categories.txt"


def add_category(category_name: str, filepath: str = CATEGORY_FILE) -> None:
    """
    Adds a new category to the category list if it does not already exist.
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True) if os.path.dirname(filepath) else None
    try:
        pass
    except Exception as e:
        print(f"Error: {e}")


def list_categories(filepath: str = CATEGORY_FILE) -> list:
    """
    Reads and returns the list of available categories.
    """
    try:
       pass
    except FileNotFoundError:
        return []


def remove_category(category_name: str, filepath: str = CATEGORY_FILE) -> None:
    """
    Removes a category from the category list.
    """
    try:
        pass
    except FileNotFoundError:
        print("⚠️ No categories found to remove.")


# --- User Management ---


def add_user(username: str, email: str) -> None:
    """
    Adds a new user with unique username and email.
    """
    os.makedirs(os.path.dirname(USER_FILE), exist_ok=True) if os.path.dirname(USER_FILE) else None
    

def list_users() -> list:
    """
    Returns list of users from file.
    """
    pass

def remove_user(username: str) -> None:
    """
    Removes a user by username.
    """
    pass
