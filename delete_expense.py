from expense_data import expenses
from view_expense import view_expences
def delete_expense():
    if not expenses: #checks to see if there's an item to delete
        print("No expense to delete")
    else:
        for number, expense in enumerate(expenses, start=1):
            print(f"{number}. {expense['type']} - GHC {expense['amount']:,.2f}") #displays the expense items in a numbering form

        while True:
            try:
                user_choice = int(input("Enter the expense number you want to delete: "))

                if user_choice < 1 or user_choice > len(expenses):              #validates the value entered by the user
                    print("Please enter a number within the valid range.")   
                else:
                    break                       
                                                        
            except ValueError:
                print("Please enter a valid number.")

        expense_number = user_choice - 1   #sets the value to the expense index in the list
        del expenses[expense_number]  #deletes the expense
        print('Expense deleted')

    view_expences()