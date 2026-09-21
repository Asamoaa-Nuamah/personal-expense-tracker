from expense_data import expenses
def view_expences():
    if not expenses: #checking if expense list is empty
        print("No expenses found. Add an expense to view")
    else:
        for expense in expenses:
            print(f"{expense["type"]} - GHC{expense["amount"]:.2f}") #displaying expense items in the list
    print("Expense displayed successfully")
