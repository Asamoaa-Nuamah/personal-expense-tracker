from expense_data import expenses
def calc_total_expenses():
    if not expenses:
        print("Cannot add non existing values")
    else:
        total = 0
        for expense in expenses:
            total += expense["amount"]
        print("Your total expense is: ", total)
