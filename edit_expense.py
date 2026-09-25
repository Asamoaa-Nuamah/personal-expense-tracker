from expense_data import expenses
from view_expense import view_expences
def edit_expenses():
    if not expenses:
        print("No expenses to edit")
    else:
        for number, expense in enumerate(expenses, start=1):
            print(f"{number}. {expense['type']} - GHC {expense['amount']:,.2f}")

        while True:
            try:
                choice = int(input("Enter the expense you want to edit: "))  #which expense in the list
                if choice < 1 or choice > len(expenses):
                    print("Please enter a value within the valid range")      #validation logic
                else:
                    break
            except ValueError:
                print('Please enter a valid number')


        while True:
            try:
                edit_choice = int(input(
                    "What would you like to edit?\n"            #the expense to edit
                    "1. Category\n"
                    "2. Amount\n"
                    "3. Both\n"
                    "Enter your choice: "
                ))

                if edit_choice < 1 or edit_choice > 3:
                    print("Please choose 1, 2, or 3.")
                else:
                    break

            except ValueError:
                print("Please enter a valid number.")

        expense_number = choice - 1
        if edit_choice == 1:
            while True:
                new_cat = input('Enter your new category: ')
                if new_cat.strip() == "":
                    print('Category cannot be empty')
                else:
                    break
            expenses[expense_number]['type'] = new_cat

        elif edit_choice == 3:
            while True:
                new_cat = input('Enter your new category: ')
                if new_cat.strip() == "":
                    print('Category cannot be empty')
                else:
                    break
            expenses[expense_number]['type'] = new_cat

        if edit_choice == 2 or edit_choice == 3:
            while True:
                try:
                    new_amount = float(input('Enter your new amount: '))
                    if new_amount < 0:
                        print('Amount cannot be negative')
                    else:
                        expenses[expense_number]['amount'] = new_amount
                        break
                except ValueError:
                    print("Please enter valid value")

    print('Expense updated')
    view_expences()