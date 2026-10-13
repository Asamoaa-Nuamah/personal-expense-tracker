# Controls the program logic: shows the menu and calls the right feature.

from add_expense import add_expense
from view_expense import view_expenses
from total_expense import calc_total_expenses
from delete_expense import delete_expense
from edit_expense import edit_expenses
from summary_expense import show_summary
from database import backup_database


def show_menu():
    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Calculate total expenses")
    print("4. Spending summary")
    print("5. Delete expense")
    print("6. Edit expense")
    print("7. Backup database")
    print("8. Exit")


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
            show_summary()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            edit_expenses()
        elif choice == "7":
            path = backup_database()
            print(f"Backup saved: {path}")
        elif choice == "8":
            backup_database()  # automatic backup on exit
            print("Backup saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose an option from 1 to 8.")

# Runs the program only when this file is executed directly (python main.py),
# not when another file imports it.
if __name__ == "__main__":
    main()