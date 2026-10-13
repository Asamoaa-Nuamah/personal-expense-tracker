from datetime import datetime, timedelta
from database import get_summary_by_category
from view_expense import (
    run_menu,
    ask_date,
    week_range,
    month_range,
    year_range,
    DATE_FORMAT,
)


# ---------- Display ----------

def print_summary(start, end, label):
    """Show each category's total, share of spending and expense count for a period.
    With start and end as None, it covers all time."""
    rows = get_summary_by_category(start, end)

    if not rows:
        print(f"\n{label}: no expenses found.")
        return

    grand_total = sum(total for _, total, _ in rows)

    print(f"\n--- Spending summary: {label} ---")
    for name, total, count in rows:
        # Guard against dividing by zero if every amount is 0
        percent = (total / grand_total * 100) if grand_total else 0
        plural = "expense" if count == 1 else "expenses"
        print(f"{name:<15} GHC {total:>10,.2f}  {percent:5.1f}%  ({count} {plural})")

    print(f"\nTotal: GHC {grand_total:,.2f}")


# ---------- Quick summaries: no typing needed ----------

def summary_all_time():
    print_summary(None, None, "All time")


def summary_this_week():
    start, end = week_range(datetime.today())
    print_summary(start, end, f"This week ({start} to {end})")


def summary_this_month():
    today = datetime.today()
    start, end = month_range(today)
    print_summary(start, end, today.strftime("This month (%B %Y)"))


def summary_this_year():
    year = datetime.today().year
    start, end = year_range(year)
    print_summary(start, end, f"This year ({year})")


def summary_last_week():
    start, end = week_range(datetime.today() - timedelta(days=7))
    print_summary(start, end, f"Last week ({start} to {end})")


def summary_last_month():
    # Day 1 of this month minus one day lands on the last day of the previous month
    last_month = datetime.today().replace(day=1) - timedelta(days=1)
    start, end = month_range(last_month)
    print_summary(start, end, last_month.strftime("Last month (%B %Y)"))


def summary_last_year():
    year = datetime.today().year - 1
    start, end = year_range(year)
    print_summary(start, end, f"Last year ({year})")


# ---------- Specific summaries: the user types a date ----------

def summary_specific_week():
    chosen = ask_date("Enter any date in that week as YYYY-MM-DD", DATE_FORMAT, "2026-10-07")
    if chosen is None:
        return
    start, end = week_range(chosen)
    print_summary(start, end, f"Week {start} to {end}")


def summary_specific_month():
    chosen = ask_date("Enter month as YYYY-MM", "%Y-%m", "2026-09")
    if chosen is None:
        return
    start, end = month_range(chosen)
    print_summary(start, end, chosen.strftime("%B %Y"))


def summary_specific_year():
    chosen = ask_date("Enter year as YYYY", "%Y", "2025")
    if chosen is None:
        return
    start, end = year_range(chosen.year)
    print_summary(start, end, f"Year {chosen.year}")


# ---------- Menus ----------

def summary_other_periods():
    """Second-level menu for previous periods and specific dates."""
    run_menu("Other periods", [
        ("Last week", summary_last_week),
        ("Last month", summary_last_month),
        ("Last year", summary_last_year),
        ("A specific week", summary_specific_week),
        ("A specific month", summary_specific_month),
        ("A specific year", summary_specific_year),
    ])


def show_summary():
    """Main summary menu. It stays open after each summary until the user chooses Back."""
    run_menu("Spending summary", [
        ("All time", summary_all_time),
        ("This week", summary_this_week),
        ("This month", summary_this_month),
        ("This year", summary_this_year),
        ("Other periods (last week/month/year, specific dates)...", summary_other_periods),
    ])