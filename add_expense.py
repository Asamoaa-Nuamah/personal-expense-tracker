from expense_data import expenses
from datetime import date  #adds date description to expense added

def add_expense():
    while True:
        #asking user to add an expense
        expense_type = input("Enter the type of expense: ")
    

        #The expense amount cannot be negative and can't accept non-numeric values
        while True:
            try:
                amount = float(input("Enter the amount of expense: "))
                if amount < 0:
                    print("Amount cannot be negative")
                else:
                    break
            except ValueError:
                print('Enter a valid input!')

        #storing the expense added
        expense_storage = {
            "type" : expense_type,
            "amount" : amount,
            "date" : str(date.today())
        }
        expenses.append(expense_storage) #storing the dictionary in a list

        print("Expense created successfully")

        #asking the user to add another expense
        answer = input("Do you want to add another expense? (Y/N): ")
        while answer != "Y" and answer != "y" and answer != "N" and answer != "n":
            print("Invalid!\nMake a choice please")
            answer = input("Do you want to add another expense? (Y/N): ")

        if answer == "N" or answer == "n":
            break

