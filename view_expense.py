from datetime import datetime
from database import (
    get_all_categories,
    get_expenses_by_category,
    get_expenses_by_date_range,
)

DATE_FORMAT = "%Y-%m-%d"  # the format expenses are saved in


# ---------- Menu helper ----------

def run_menu(title, options):
    """Show a numbered menu and keep it open until the user picks 0.
    `options` is a list of (label, function) pairs; the chosen function is called,
    then the menu appears again."""
    while True:
        print(f"\n{title}")
        for number, (label, _) in enumerate(options, start=1):
            print(f"{number}. {label}")
        print("0. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "0":
            return
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            options[int(choice) - 1][1]()  # run the chosen view, then loop back to the menu
        else:
            print(f"Please choose a number from 0 to {len(options)}.")


# ---------- Date helper ----------

def ask_date(prompt, fmt, example):
    """Ask until the input matches `fmt`. Returns a datetime, or None if the user goes back."""
    while True:
        text = input(f"{prompt} (0 to go back): ").strip()

        if text == "0":
            return None
        try:
            return datetime.strptime(text, fmt)  # rejects impossible dates like 2026-02-31
        except ValueError:
            print(f"Invalid input. Use the format shown, for example {example}.")


# ---------- Display ----------

def show_expenses(expenses, title):
    """Print a list of expenses (id, name, category, amount, description, date) with a total."""
    if not expenses:
        print(f"\n{title}: no expenses found.")
        return

    print(f"\n--- {title} ---")
    total = 0
    for expense_id, name, category, amount, description, expense_date in expenses:
        line = f"{expense_id}. {name} ({category}) - GHC {amount:,.2f}  ({expense_date})"
        if description:
            line += f"\n     Note: {description}"
        print(line)
        total += amount

    print(f"\nTotal ({title}): GHC {total:,.2f}")


# ---------- The three views ----------

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


def view_today():
    day = datetime.today().strftime(DATE_FORMAT)
    show_expenses(get_expenses_by_date_range(day, day), f"Today ({day})")


def view_specific_date():
    chosen = ask_date("Enter date as YYYY-MM-DD", DATE_FORMAT, "2026-10-12")
    if chosen is None:
        return
    day = chosen.strftime(DATE_FORMAT)
    show_expenses(get_expenses_by_date_range(day, day), day)


# ---------- Menu ----------

def view_expenses():
    """View menu. It stays open after each view until the user chooses Back."""
    run_menu("View expenses", [
        ("By category", view_by_category),
        ("Today", view_today),
        ("A specific date", view_specific_date),
    ])