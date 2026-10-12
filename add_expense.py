import sqlite3
from datetime import date
from database import add_expense_to_database, insert_category, get_all_categories


def create_category():
    """Ask for a new category name. Returns its id, or None if it failed."""
    name = input("Enter the new category name: ").strip()
    if not name:
        print("Category name cannot be empty.")
        return None
    try:
        category_id = insert_category(name)
        print(f"Category '{name}' created.")           
        return category_id           #validates the category entered by user and ensures no creation of duplicate categories
    except sqlite3.IntegrityError:
        print(f"'{name}' already exists. Pick it from the list instead.")
        return None


def choose_category():
    """Let the user pick an existing category or create a new one. Returns the category id."""
    while True:
        categories = get_all_categories()

        print("\nCategories:")
        for category_id, name in categories:
            print(f"  {category_id}. {name}")
        print("  0. Create a new category")

        choice = input("Choose a category number: ").strip()
        if not choice.isdigit():
            print("Enter a valid number!")
            continue

        choice = int(choice)
        if choice == 0:
            new_id = create_category()
            if new_id is not None:
                return new_id
        elif choice in [category_id for category_id, _ in categories]:
            return choice
        else:
            print("No category with that number.")


def get_expense_name():
    """Keep asking until the user enters a non-empty expense name."""
    while True:
        name = input("Enter the name of the expense (e.g. Jollof): ").strip()
        if name:
            return name
        print("Expense name cannot be empty.")


def add_expense():
    while True:
        category_id = choose_category()
        name = get_expense_name()
        amount = get_amount()
        description = input("Description (optional, press Enter to skip): ").strip() or None

        add_expense_to_database(category_id, name, amount, description, str(date.today()))
        print("Expense created successfully")

        if not ask_yes_no("Do you want to add another expense? (Y/N): "):
            break


def get_amount():
    while True:
        try:
            amount = float(input("Enter the amount of expense: "))
            if amount < 0:
                print("Amount cannot be negative")
            else:
                return amount
        except ValueError:
            print("Enter a valid input!")


def ask_yes_no(question):
    while True:
        answer = input(question).strip().lower()
        if answer in ("y", "n"):
            return answer == "y"
        print("Invalid! Please enter Y or N.")


