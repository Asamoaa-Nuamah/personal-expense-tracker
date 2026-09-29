#controlling the program logic

from add_expense import add_expense
from view_expense import view_expences
from total_expense import calc_total_expenses
from categorizing_expense import cat_expenses
from category_total import calc_spending_category
from delete_expense import delete_expense
from edit_expense import edit_expenses

while True:
    print("===== PERSONAL EXPENSE TRACKER =====")           #displays the main menu
    print("1. Add expense")
    print("2. View expenses")
    print("3. Calculate total expenses")
    print("4. Categorize expenses")
    print("5. Calculate spending by category")
    print("6. Delete expense")
    print("7. Edit expense")
    print("8. Exit")

    choice = input("Enter your choice: ")                    #allows the user to make choice from the options provided above

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expences()
    elif choice == '3':
        calc_total_expenses()
    elif choice == '4':
        cat_expenses()
    elif choice == '5':
        calc_spending_category()
    elif choice == '6':
        delete_expense()
    elif choice == '7':
        edit_expenses()
    elif choice == '8':
        break
    else:
        print("Invalid choice. Please choose an option from 1 to 8.")
