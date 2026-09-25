from expense_data import expenses
from view_expense import view_expences
def delete_expense():
    if not expenses:
        print("No expense to delete")
    else:
        for number, expense in enumerate(expenses, start=1):
            print(f"{number}. {expense['type']} - GHC {expense['amount']:,.2f}")

        while True:
            try:
                user_choice = int(input("Enter the expense number you want to delete: "))

                if user_choice < 1 or user_choice > len(expenses):
                    print("Please enter a number within the valid range.")
                else:
                    break

            except ValueError:
                print("Please enter a valid number.")

        expense_number = user_choice - 1
        del expenses[expense_number]
        print('Expense deleted')

    view_expences()