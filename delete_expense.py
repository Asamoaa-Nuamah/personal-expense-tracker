from database import get_expenses, delete_expense as delete_expense_from_database
from add_expense import ask_yes_no
from view_expense import run_menu


def delete_one_expense():
    expenses = get_expenses()

    if not expenses:
        print("No expense to delete")
        return

    # List every expense with its ID so the user knows what to pick
    for expense_id, name, category, amount, description, date in expenses:
        print(f"{expense_id}. {name} ({category}) - GHC {amount:,.2f}  [{date}]")

    # Build the list of valid IDs once, outside the loop
    ids = [expense[0] for expense in expenses]

    while True:
        user_choice = input("Enter the expense ID you want to delete (0 to cancel): ").strip()

        if not user_choice.isdigit():
            print("Please enter a valid number.")
            continue

        user_choice = int(user_choice)

        if user_choice == 0:
            print("Delete has been cancelled")
            return

        if user_choice not in ids:
            print("Please enter a valid expense ID.")
            continue

        # ask_yes_no keeps asking until the answer is y or n
        if ask_yes_no("Are you sure you want to delete this expense? (Y/N): "):
            delete_expense_from_database(user_choice)
            print("Expense deleted")
        else:
            print("Delete has been cancelled")
        return


def delete_expense():
    """Delete menu. It stays open after each deletion until the user chooses Back."""
    run_menu("Delete expense", [
        ("Delete an expense", delete_one_expense),
    ])