from database import get_expenses, delete_expense as delete_expense_from_database
from view_expense import view_expences
def delete_expense():
    expenses = get_expenses() 
    if not expenses: #checks to see if there's an item to delete
        print("No expense to delete")
    else:
        for expense in expenses:
            print(f"{expense[0]}. {expense[1]} - GHC {expense[2]:,.2f}") #displays the expense items with their ids

        while True:
            try:
                user_choice = int(input("Enter the expense ID you want to delete: "))

                found = False

                for expense in expenses:
                    if expense[0] == user_choice:
                        found = True
                        break

                if found:
                    break
                else:
                    print("Please enter a valid expense ID.")

            except ValueError:
                print("Please enter a valid number.")
        delete_expense_from_database(user_choice)
        print('Expense deleted')