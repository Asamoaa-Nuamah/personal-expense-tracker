# Controls the program logic: shows the menu and calls the right feature.

from add_expense import add_expense
from view_expense import view_expenses
from total_expense import calc_total_expenses
from delete_expense import delete_expense
from edit_expense import edit_expenses


def show_menu():
    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Calculate total expenses")
    print("4. Delete expense")
    print("5. Edit expense")
    print("6. Exit")


def main():
    while True:
        show_menu()

        # strip() ignores accidental spaces around the choice
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calc_total_expenses()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            edit_expenses()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose an option from 1 to 6.")


# Runs the program only when this file is executed directly (python main.py),
# not when another file imports it.
if __name__ == "__main__":
    main()