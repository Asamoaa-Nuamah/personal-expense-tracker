from database import get_expenses
def calc_spending_category():
    expenses = get_expenses()
    cat_expense = input("Enter expense category you want to calculate: ")
    found = False
    total = 0

    for expense in expenses:
        if expense[1].lower() == cat_expense.lower():      #calculating expenses based on category / expense category
            total += expense[2]
            found = True

    if found == False:
        print("No expense found in this category")
    else:
        print(f"Total spent on {cat_expense}: GHC {total:,.2f}")
