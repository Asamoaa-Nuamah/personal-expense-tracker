import calendar
from datetime import datetime , timedelta
from database import get_all_categories, get_expenses_by_category, get_expenses , get_expenses_by_date_range


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


def view_all_expenses():
    show_expenses(get_expenses(), "All expenses")


def view_by_year():
    while True:
        text = input("Enter year as YYYY (Enter for this year, 0 to go back): ").strip()

        if text == "0":
            return
        if text == "":
            chosen = datetime.today()
        else:
            try:
                chosen = datetime.strptime(text, "%Y")  # needs exactly 4 digits, e.g. 2026
            except ValueError:
                print("Invalid year. Use YYYY, for example 2026.")
                continue
        break

    # A year always runs from 1st January to 31st December
    start = f"{chosen.year}-01-01"
    end = f"{chosen.year}-12-31"

    show_expenses(get_expenses_by_date_range(start, end), f"Year {chosen.year}")


def view_by_month():
    while True:
        text = input("Enter month as YYYY-MM (Enter for this month, 0 to go back): ").strip()

        if text == "0":
            return
        if text == "":
            chosen = datetime.today()
        else:
            try:
                chosen = datetime.strptime(text, "%Y-%m")  # rejects bad input like 2026-13
            except ValueError:
                print("Invalid format. Use YYYY-MM, for example 2026-10.")
                continue
        break

    # monthrange gives the number of days in that month (28, 29, 30 or 31)
    last_day = calendar.monthrange(chosen.year, chosen.month)[1]
    start = f"{chosen.year}-{chosen.month:02d}-01"
    end = f"{chosen.year}-{chosen.month:02d}-{last_day:02d}"

    show_expenses(get_expenses_by_date_range(start, end), chosen.strftime("%B %Y"))


def view_by_week():
    while True:
        text = input("Enter any date in that week as YYYY-MM-DD (Enter for this week, 0 to go back): ").strip()

        if text == "0":
            return
        if text == "":
            chosen = datetime.today()
        else:
            try:
                chosen = datetime.strptime(text, "%Y-%m-%d")
            except ValueError:
                print("Invalid date. Use YYYY-MM-DD, for example 2026-10-12.")
                continue
        break

    # weekday() is 0 for Monday ... 6 for Sunday, so subtracting it lands on Monday
    monday = chosen - timedelta(days=chosen.weekday())
    sunday = monday + timedelta(days=6)

    start = monday.strftime("%Y-%m-%d")
    end = sunday.strftime("%Y-%m-%d")

    show_expenses(get_expenses_by_date_range(start, end), f"Week {start} to {end}")


def view_by_date():
    while True:
        text = input("Enter date as YYYY-MM-DD (Enter for today, 0 to go back): ").strip()

        if text == "0":
            return
        if text == "":
            chosen = datetime.today()
        else:
            try:
                chosen = datetime.strptime(text, "%Y-%m-%d")
            except ValueError:
                print("Invalid date. Use YYYY-MM-DD, for example 2026-10-12.")
                continue
        break

    day = chosen.strftime("%Y-%m-%d")  # same format the expenses are saved in
    show_expenses(get_expenses_by_date_range(day, day), day)


def view_expenses():
    """Submenu: lets the user choose how to view their expenses."""
    while True:
        print("\nView expenses")
        print("1. View by category")
        print("2. View all expenses")
        print("3. View by week")
        print("4. View by month")
        print("5. View by year")
        print("6. View by date")
        print("0. Back to main menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_by_category()
            return
        elif choice == "2":
            view_all_expenses()
            return
        elif choice == "3":
            view_by_week()
            return
        elif choice == "4":
            view_by_month()
            return
        elif choice == "5":
            view_by_year()
            return
        elif choice == "6":
            view_by_date()
            return
        elif choice == "0":
            return
        else:
            print("Please choose a number from 0 to 6.")