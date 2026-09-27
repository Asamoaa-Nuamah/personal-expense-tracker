# Personal Expense Tracker

A command line personal expense tracker built with Python. The project allows users to record, view, categorize, calculate, edit, and delete expenses while maintaining data between program sessions using JSON storage.

The project was developed incrementally, with each version introducing new functionality and concepts.

---

## Features

### Version 1.0

* Add expenses
* Add multiple expenses in one session
* Validate expense amounts
* Prevent negative expense amounts
* Reject invalid non-numeric amounts
* View recorded expenses
* Calculate total expenses
* Interactive Git/GitHub project setup

### Version 2.0

* Filter expenses by category
* Calculate spending for a specific category
* Delete expenses
* Edit expense categories
* Edit expense amounts
* Edit both category and amount
* Improved input validation
* Case-insensitive category matching
* Formatted currency output

### Version 3.0

* Interactive main menu
* Improved program flow
* Persistent JSON storage
* Automatically load previously saved expenses
* Automatically save expenses when exiting
* Multiple expense entry integrated into the main menu
* Data remains available after restarting the program

---

# Version 1.0

The first version focused on building the core functionality of the expense tracker.

### Adding Expenses

Users can enter:

* Expense category/type
* Expense amount

The program validates the amount and prevents negative values or non-numeric input.

### Viewing Expenses

Users can view all recorded expenses, including the expense category and amount.

### Calculating Total Expenses

The program calculates the total amount spent across all recorded expenses.

### Multiple Expense Entry

Users can add multiple expenses during a single run of the program.

---

# Version 2.0

Version 2.0 expanded the application from a basic expense tracker into a more functional expense management system.

### Categorizing Expenses

Users can enter a category and view only expenses belonging to that category.

Category matching is case-insensitive, meaning inputs such as `Food`, `food`, and `FOOD` can refer to the same category.

### Category Spending

Users can calculate the total amount spent within a particular category.

For example:

```text
Enter expense category you want to calculate: Food

Total spent on Food: GHC1,250.00
```

### Delete Expenses

Expenses are displayed with numbers, allowing users to select and delete a specific expense.

The program validates the selected number before deleting the expense.

### Edit Expenses

Users can select an existing expense and choose to:

1. Edit the category
2. Edit the amount
3. Edit both

Input validation is applied when entering new categories and amounts.

---

# Version 3.0

Version 3.0 focused on improving the overall application flow and introducing persistent data storage.

## Interactive Main Menu

Instead of automatically executing every function sequentially, the program now presents an interactive menu:

```text
===== PERSONAL EXPENSE TRACKER =====
1. Add expense
2. View expenses
3. Calculate total expenses
4. Categorize expenses
5. Calculate spending by category
6. Delete expense
7. Edit expense
8. Exit
```

The user selects an option, the corresponding function is executed, and the program returns to the main menu when the function is finished.

The program continues running until the user selects **Exit**.

## Multiple Expense Entry

The `add_expense()` function now handles multiple expense entries internally.

After adding an expense, the user is asked whether they want to add another expense.

```text
Do you want to add another expense? (Y/N):
```

Choosing `Y` allows another expense to be entered, while choosing `N` returns the user to the main menu.

## Persistent JSON Storage

Version 3.0 introduced JSON based persistent storage.

Expenses are stored in:

```text
expenses.json
```

The program automatically loads previously saved expenses when it starts.

When the user exits the program, the current expenses are automatically saved to the JSON file.

This means expenses are preserved between program sessions.

### Data Flow

```text
Program starts
      ↓
Load expenses from JSON
      ↓
User adds / edits / deletes expenses
      ↓
Updated expenses remain in memory
      ↓
User chooses Exit
      ↓
Save expenses to JSON
      ↓
Program ends
```

When the program is opened again, the saved expenses are loaded automatically.

---

# Project Structure

```text
personal-expense-tracker/
│
├── .gitignore
├── README.md
├── main.py
├── add_expense.py
├── view_expense.py
├── total_expense.py
├── categorizing_expense.py
├── category_total.py
├── delete_expense.py
├── edit_expense.py
├── expense_data.py
└── expenses.json
```

## File Descriptions

| File                      | Purpose                                          |
| ------------------------- | ------------------------------------------------ |
| `main.py`                 | Controls the main program flow and menu          |
| `add_expense.py`          | Handles adding one or multiple expenses          |
| `view_expense.py`         | Displays recorded expenses                       |
| `total_expense.py`        | Calculates total expenses                        |
| `categorizing_expense.py` | Filters expenses by category                     |
| `category_total.py`       | Calculates spending for a selected category      |
| `delete_expense.py`       | Deletes a selected expense                       |
| `edit_expense.py`         | Edits an existing expense                        |
| `expense_data.py`         | Manages the shared expense list and JSON storage |
| `expenses.json`           | Stores expense data persistently                 |
| `README.md`               | Project documentation                            |

---

# Data Structure

Expenses are stored as a list of dictionaries.

Example:

```python
expenses = [
    {
        "type": "Food",
        "amount": 50.00
    },
    {
        "type": "Transport",
        "amount": 20.00
    }
]
```

This structure makes it possible to store multiple expenses while keeping the category and amount associated with each expense.

---

# Concepts Practiced

Throughout the development of this project, the following Python concepts were practiced:

* Variables
* Lists
* Dictionaries
* Functions
* Function imports
* Modules
* `if` / `elif` / `else`
* `while` loops
* Nested loops
* `for` loops
* `break`
* User input
* Input validation
* `try` / `except`
* `ValueError`
* String methods
* Formatted strings (f-strings)
* Dictionary access and modification
* List operations
* JSON serialization and deserialization
* File handling
* Persistent data storage
* Modular program design
* Git and GitHub

---

# How to Run

Clone the repository and navigate into the project directory.

Then run:

```bash
python main.py
```

The application will display the main menu and allow the user to select the desired operation.

---

# Current Limitations

The current version is a command line application and stores data locally in a JSON file.

It does not currently include:

* A graphical user interface
* A web interface
* User accounts or authentication
* A database
* Advanced reporting or data visualization
* Budget management
* Date-based expense tracking

---

# Future Improvements

Possible future improvements include:

* Add expense dates
* Add monthly and weekly spending summaries
* Add budget tracking
* Add income tracking
* Add spending reports
* Add data visualization
* Move from JSON storage to a database
* Build a graphical or web interface
* Add search functionality
* Improve error handling and user experience

---

# Project Goal

The goal of this project is to build a practical Python application while progressively developing software engineering skills.

The project began as a simple command line expense tracker and has evolved into a modular application with input validation, expense management features, an interactive menu, and persistent data storage.

Future versions will continue to expand the application's functionality while applying more advanced software development concepts.
