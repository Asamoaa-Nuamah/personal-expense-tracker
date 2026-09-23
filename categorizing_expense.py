from expense_data import expenses
def cat_expenses():
    #ask user for expense category
    cat_expense = input("Enter category to view: ")

    #keeps track of whether an expense exist or not
    found = False

    for expense in expenses:
        if expense["type"].lower() == cat_expense.lower():  #eliminates the issue of case sensitivity
            print(f"{expense['type']} - GHC{expense['amount']:.2f}")
            found = True

    if found == False:
        print("No expenses found in this category")