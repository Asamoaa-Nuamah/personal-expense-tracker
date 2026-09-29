from database import get_expenses  #importhing data from our database
def view_expences():
    expenses = get_expenses()
    if not expenses: #checking if expense list is empty
        print("No expenses found. Add an expense to view")
    else:
        for expense in expenses:
            print(f"{expense[1]} - GHC {expense[2]:,.2f}") #displaying expense from the database
    print("Expense displayed successfully")
