from database import get_all_categories, get_expenses_by_category


def view_expenses():
    categories = get_all_categories()

    # Nothing to choose from if no category has been created yet
    if not categories:
        print("No categories found. Add an expense to view.")
        return

    valid_ids = [category_id for category_id, _ in categories]

    # Keep asking until the user picks a valid category (or goes back)
    while True:
        print("\nCategories:")
        for category_id, name in categories:
            print(f"  {category_id}. {name}")
        print("  0. Back to main menu")

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

    category_name = dict(categories)[choice]  # turns the (id, name) rows into a lookup
    expenses = get_expenses_by_category(choice)

    if not expenses:
        print(f"\nNo expenses found under {category_name}.")
        return

    print(f"\n--- {category_name} ---")
    total = 0
    for expense_id, name, amount, description, date in expenses:
        line = f"{expense_id}. {name} - GHC {amount:,.2f}  ({date})"
        if description:  # only show the description when the user provided one
            line += f"\n     Note: {description}"
        print(line)
        total += amount

    print(f"\nTotal spent on {category_name}: GHC {total:,.2f}")