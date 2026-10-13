import calendar
from datetime import datetime, timedelta
from database import (
    get_all_categories,
    get_expenses_by_category,
    get_expenses,
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


# ---------- Date range helpers (each returns start and end as YYYY-MM-DD text) ----------

def week_range(day):
    """Monday to Sunday of the week containing `day`."""
    monday = day - timedelta(days=day.weekday())  # weekday() is 0 for Monday
    sunday = monday + timedelta(days=6)
    return monday.strftime(DATE_FORMAT), sunday.strftime(DATE_FORMAT)


def month_range(day):
    """First to last day of the month containing `day`."""
    last_day = calendar.monthrange(day.year, day.month)[1]  # 28, 29, 30 or 31
    return f"{day.year}-{day.month:02d}-01", f"{day.year}-{day.month:02d}-{last_day:02d}"


def year_range(year):
    """1 January to 31 December of `year`."""
    return f"{year}-01-01", f"{year}-12-31"


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


def show_range(start, end, title):
    show_expenses(get_expenses_by_date_range(start, end), title)


# ---------- View by category and all ----------

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
    show_expenses(get_expenses(), "All expenses")


# ---------- Quick views: no typing needed ----------

def view_today():
    day = datetime.today().strftime(DATE_FORMAT)
    show_range(day, day, f"Today ({day})")


def view_this_week():
    start, end = week_range(datetime.today())
    show_range(start, end, f"This week ({start} to {end})")


def view_this_month():
    today = datetime.today()
    start, end = month_range(today)
    show_range(start, end, today.strftime("This month (%B %Y)"))


def view_this_year():
    year = datetime.today().year
    start, end = year_range(year)
    show_range(start, end, f"This year ({year})")


def view_last_week():
    start, end = week_range(datetime.today() - timedelta(days=7))
    show_range(start, end, f"Last week ({start} to {end})")


def view_last_month():
    # Day 1 of this month minus one day lands on the last day of the previous month
    last_month = datetime.today().replace(day=1) - timedelta(days=1)
    start, end = month_range(last_month)
    show_range(start, end, last_month.strftime("Last month (%B %Y)"))


def view_last_year():
    year = datetime.today().year - 1
    start, end = year_range(year)
    show_range(start, end, f"Last year ({year})")


# ---------- Specific views: the user types a date ----------

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


def view_specific_date():
    chosen = ask_date("Enter date as YYYY-MM-DD", DATE_FORMAT, "2026-10-12")
    if chosen is None:
        return
    day = chosen.strftime(DATE_FORMAT)
    show_range(day, day, day)


def view_specific_week():
    chosen = ask_date("Enter any date in that week as YYYY-MM-DD", DATE_FORMAT, "2026-10-07")
    if chosen is None:
        return
    start, end = week_range(chosen)
    show_range(start, end, f"Week {start} to {end}")


def view_specific_month():
    chosen = ask_date("Enter month as YYYY-MM", "%Y-%m", "2026-09")
    if chosen is None:
        return
    start, end = month_range(chosen)
    show_range(start, end, chosen.strftime("%B %Y"))


def view_specific_year():
    chosen = ask_date("Enter year as YYYY", "%Y", "2025")
    if chosen is None:
        return
    start, end = year_range(chosen.year)
    show_range(start, end, f"Year {chosen.year}")


# ---------- Menus ----------

def view_other_periods():
    """Second-level menu for previous periods and specific dates."""
    run_menu("Other periods", [
        ("Last week", view_last_week),
        ("Last month", view_last_month),
        ("Last year", view_last_year),
        ("A specific date", view_specific_date),
        ("A specific week", view_specific_week),
        ("A specific month", view_specific_month),
        ("A specific year", view_specific_year),
    ])


def view_expenses():
    """Main view menu. It stays open after each view until the user chooses Back."""
    run_menu("View expenses", [
        ("By category", view_by_category),
        ("All expenses", view_all_expenses),
        ("Today", view_today),
        ("This week", view_this_week),
        ("This month", view_this_month),
        ("This year", view_this_year),
        ("Other periods (last week/month/year, specific dates)...", view_other_periods),
    ])