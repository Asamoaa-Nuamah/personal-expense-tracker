from expense_data import expenses
def add_expense():
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
        "amount" : amount
    }
    expenses.append(expense_storage) #storing the dictionary in a list

    print("Expense created successfully")
