from expense_data import expenses
def add_expense():
    #asking user to add an expense
    expense_type = input("Enter the type of expense: ")
    amount = float(input("Enter the amount of expense: "))

    #The expense amount cannot be negative
    while amount < 0:
        print("Amount cannot be negative")
        amount = float(input("Enter the amount again: "))

    #storing the expense added
    expense_storage = {
        "type" : expense_type,
        "amount" : amount
    }
    expenses.append(expense_storage) #storing the dictionary in a list

    print("Expense created successfully")
