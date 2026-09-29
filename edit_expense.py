from database import update_expense, get_expenses
from view_expense import view_expences

def edit_expenses():
    expenses = get_expenses()

    if not expenses: #checks to see if the table is empty
        print("No expenses to edit")
    else:
        for expense in expenses:
            print(f"{expense[0]}. {expense[1]} - GHC {expense[2]:,.2f}")  #list items with their ids
        while True:
            try:
                choice = int(input("Enter the expense ID you want to edit: "))

                found = False

                for expense in expenses:
                    if expense[0] == choice:
                        found = True
                        break

                if found:
                    break
                else:
                    print("Please enter a valid expense ID.")

            except ValueError:
                print("Please enter a valid number.")


        while True:
            try:
                edit_choice = int(input(
                    "What would you like to edit?\n"            #allows user to make choice on what to edit
                    "1. Category\n"
                    "2. Amount\n"
                    "3. Both\n"
                    "Enter your choice: "
                ))

                if edit_choice < 1 or edit_choice > 3:   #ensures the value is within range expected
                    print("Please choose 1, 2, or 3.") 
                else:
                    break

            except ValueError:
                print("Please enter a valid number.")

        # Find the selected expense using its database ID
        for expense in expenses:
            if expense[0] == choice:
                old_type = expense[1]
                old_amount = expense[2]

                if edit_choice == 1:
                    while True:
                        new_cat = input("Enter your new category: ")

                        if new_cat.strip() == "":
                            print("Category cannot be empty")
                        else:
                            break

                    update_expense(new_cat, old_amount, choice)

                elif edit_choice == 2:
                    while True:
                        try:
                            new_amount = float(input("Enter your new amount: "))

                            if new_amount < 0:
                                print("Amount cannot be negative")
                            else:
                                break

                        except ValueError:
                            print("Please enter a valid value")

                    update_expense(old_type, new_amount, choice)

                elif edit_choice == 3:
                    while True:
                        new_cat = input("Enter your new category: ")

                        if new_cat.strip() == "":
                            print("Category cannot be empty")
                        else:
                            break

                    while True:
                        try:
                            new_amount = float(input("Enter your new amount: "))

                            if new_amount < 0:
                                print("Amount cannot be negative")
                            else:
                                break

                        except ValueError:
                            print("Please enter a valid value")

                    update_expense(new_cat, new_amount, choice)

                break

