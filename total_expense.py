from database import get_total_expenses


def calc_total_expenses():
    total = get_total_expenses()  # returns 0 when there are no expenses

    if total == 0:
        print("No expenses found. Add an expense first.")
    else:
        print(f"Your total expense is: GHC {total:,.2f}")