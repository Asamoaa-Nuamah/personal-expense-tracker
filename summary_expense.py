import calendar
from datetime import datetime, timedelta
from database import get_summary_by_category


def ask_date():
    """Ask for a reference date. Returns a datetime, or None if the user goes back."""
    while True:
        text = input("Enter any date in that period as YYYY-MM-DD (Enter for today, 0 to go back): ").strip()

        if text == "0":
            return None
        if text == "":
            return datetime.today()
        try:
            return datetime.strptime(text, "%Y-%m-%d")
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD, for example 2026-10-12.")


def choose_period():
    """Let the user pick a period. Returns (start, end, label), or None to go back.
    For 'All time', start and end are None."""
    while True:
        print("\nSpending summary")
        print("1. All time")
        print("2. Week")
        print("3. Month")
        print("4. Year")
        print("0. Back to main menu")

        choice = input("Enter your choice: ").strip()

        if choice == "0":
            return None
        if choice == "1":
            return None, None, "All time"
        if choice not in ("2", "3", "4"):
            print("Please choose a number from 0 to 4.")
            continue

        chosen = ask_date()
        if chosen is None:
            continue  # user went back, so show the period menu again

        if choice == "2":
            # Week runs Monday to Sunday
            monday = chosen - timedelta(days=chosen.weekday())
            sunday = monday + timedelta(days=6)
            start, end = monday.strftime("%Y-%m-%d"), sunday.strftime("%Y-%m-%d")
            return start, end, f"Week {start} to {end}"

        if choice == "3":
            last_day = calendar.monthrange(chosen.year, chosen.month)[1]
            start = f"{chosen.year}-{chosen.month:02d}-01"
            end = f"{chosen.year}-{chosen.month:02d}-{last_day:02d}"
            return start, end, chosen.strftime("%B %Y")

        #choice == "4":
        return f"{chosen.year}-01-01", f"{chosen.year}-12-31", f"Year {chosen.year}"


def show_summary():
    period = choose_period()
    if period is None:
        return

    start, end, label = period
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