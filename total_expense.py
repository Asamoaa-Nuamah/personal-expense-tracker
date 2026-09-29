from database import get_expenses
def calc_total_expenses():
    expenses = get_expenses()
    if not expenses:
        print("No expenses found")
    else:
        total = 0
        for expense in expenses:
            total += expense[2]      #calculates total expenses stored
        print("Your total expense is: GHC ", total)
