from expense_data import expenses
def calc_spending_category():
    cat_expense = input("Enter expense category you want to calculate: ")
    found = False
    total = 0

    for expense in expenses:
        if expense['type'].lower() == cat_expense.lower():
            total += expense['amount']
            found = True

    if found == False:
        print("No expense found in this category")
    else:
        print(f"Total spent on {cat_expense}: GHC {total:,.2f}")
