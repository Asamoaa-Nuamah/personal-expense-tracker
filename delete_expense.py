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
                ids = [] #store the ids of expense items 
                for expense in expenses:
                    ids.append(expense[0])
                if user_choice not in ids:
                    print("Please enter a valid expense ID.")  #prompt user to enter a valid expense id
                else:
                    final_decision = input("Are you sure you want to delete this expense? y/n: ") #confirms if user would like to delete an item 
                    if final_decision == "Y" or final_decision == "y":
                        delete_expense_from_database(user_choice)
                        print('Expense deleted')
                        break

                    elif final_decision == "N" or final_decision == "n":  #cancels deletion
                        print("Delete has been cancelled")
                        break
                
                    else:
                        print("Please enter a valid response!")  #ensures user enters a valid response
                    
                    

            except ValueError:
                print("Please enter a valid number.") #ensures user enters a valid expense id
        