from database import get_expenses, get_expense_by_id, update_expense
from add_expense import choose_category, get_expense_name, get_amount


def choose_expense_id(expenses):
    """Ask for an expense ID until it matches one in the list. Returns None if cancelled."""
    valid_ids = [expense[0] for expense in expenses]

    while True:
        choice = input("Enter the expense ID you want to edit (0 to cancel): ").strip()
        if not choice.isdigit():
            print("Please enter a valid number.")
            continue

        choice = int(choice)
        if choice == 0:
            return None
        if choice in valid_ids:
            return choice
        print("Please enter a valid expense ID.")


def edit_expenses():
    expenses = get_expenses()

    if not expenses:
        print("No expenses to edit")
        return

    # List every expense with its ID so the user knows what to pick
    for expense_id, name, category, amount, description, date in expenses:
        print(f"{expense_id}. {name} ({category}) - GHC {amount:,.2f}  [{date}]")

    expense_id = choose_expense_id(expenses)
    if expense_id is None:
        return

    # Load the current values. We change only what the user picks,
    # then save everything back in one update.
    _, category_id, name, amount, description, _ = get_expense_by_id(expense_id)

    while True:
        print("\nWhat would you like to edit?")
        print("1. Name")
        print("2. Category")
        print("3. Amount")
        print("4. Description")
        print("0. Cancel")

        edit_choice = input("Enter your choice: ").strip()

        if edit_choice == "0":
            return
        elif edit_choice == "1":
            name = get_expense_name()
            break
        elif edit_choice == "2":
            category_id = choose_category()
            break
        elif edit_choice == "3":
            amount = get_amount()
            break
        elif edit_choice == "4":
            # Pressing Enter clears the description, since it is optional
            description = input("Enter the new description (press Enter to clear): ").strip() or None
            break
        else:
            print("Please choose a number from 0 to 4.")

    update_expense(expense_id, category_id, name, amount, description)
    print("Expense updated successfully")