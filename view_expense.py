from database import get_all_categories, get_expenses_by_category, get_expenses


def view_by_category():
    categories = get_all_categories()

    if not categories:
        print("No categories found. Add an expense to view.")
        return

    valid_ids = [category_id for category_id, _ in categories]

    while True:
        print("\nCategories:")
        for category_id, name in categories:
            print(f"  {category_id}. {name}") 
        print("  0. Back")

        choice = input("Choose a category to view: ").strip()
        if not choice.isdigit():
            print("Enter a valid number!")
            continue

        choice = int(choice)
        if choice == 0:
            return
        if choice in valid_ids:
            break
        print("No category with that number.")

    category_name = dict(categories)[choice]
    expenses = get_expenses_by_category(choice)

    if not expenses:
        print(f"\nNo expenses found under {category_name}.")
        return

    print(f"\n--- {category_name} ---")
    total = 0
    for expense_id, name, amount, description, date in expenses:
        line = f"{expense_id}. {name} - GHC {amount:,.2f}  ({date})"
        if description:
            line += f"\n     Note: {description}"
        print(line)
        total += amount

    print(f"\nTotal spent on {category_name}: GHC {total:,.2f}")


def view_all_expenses():
    expenses = get_expenses()  # (id, name, category, amount, description, date)

    if not expenses:
        print("No expenses found. Add an expense to view.")
        return

    print("\n--- All expenses ---")
    total = 0
    for expense_id, name, category, amount, description, date in expenses:
        line = f"{expense_id}. {name} ({category}) - GHC {amount:,.2f}  ({date})"
        if description:
            line += f"\n     Note: {description}"
        print(line)
        total += amount

    print(f"\nTotal of all expenses: GHC {total:,.2f}")


def view_expenses():
    """Submenu: lets the user choose how to view their expenses."""
    while True:
        print("\nView expenses")
        print("1. View by category")
        print("2. View all expenses")
        print("0. Back to main menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_by_category()
            return
        elif choice == "2":
            view_all_expenses()
            return
        elif choice == "0":
            return
        else:
            print("Please choose 0, 1 or 2.")