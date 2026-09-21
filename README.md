# Personal Expense Tracker

A simple command line Personal Expense Tracker built with Python. The project allows users to record their expenses, view recorded expenses, and calculate their total spending.

This project was built as a Python practice project to strengthen my understanding of programming fundamentals, including variables, data types, lists, dictionaries, loops, conditional statements, functions, input validation, modules, and basic project organization.

## Features

### 1. Add Expense

Users can add an expense by providing:

* The type/category of the expense (for example, Food or Utility Bills)
* The amount of the expense

The program validates the expense amount and does not allow negative values.

Each expense is stored as a dictionary containing the expense type and amount. Multiple expenses are stored in a list of dictionaries.

Example:

```python
{
    "type": "Food",
    "amount": 35.50
}
```

### 2. Add Multiple Expenses

After adding an expense, the program asks the user:

```text
Do you want to add another expense? (Y/N):
```

The user can continue adding expenses or stop when they are finished.

The program also validates the user's response and asks again if an invalid option is entered.

### 3. View Expenses

Users can view all the expenses they have entered during the current program session.

The program checks whether the expense list is empty. If there are no expenses, it displays a message asking the user to add an expense first.

If expenses exist, each expense is displayed with its type and amount.

Example:

```text
Food - GH₵35.50
Transport - GH₵20.00
Utility Bills - GH₵50.00
```

### 4. Calculate Total Expenses

The program calculates the total amount spent by looping through the stored expenses and adding each expense amount to a running total.

For example:

```text
Food - GH₵35.50
Transport - GH₵20.00
Utility Bills - GH₵50.00

Total expenses: GH₵105.50
```

## Project Structure

```text
personal-expense-tracker/
│
├── .gitignore
├── README.md
├── main.py
├── add_expense.py
├── view_expense.py
├── total_expense.py
└── expense_data.py
```

### File Descriptions

**`main.py`**

Controls the overall flow of the application. It imports the functions from the other modules, controls the process of adding multiple expenses, validates the user's Y/N response, and determines when the program should stop adding expenses.

**`add_expense.py`**

Contains the function responsible for adding an individual expense. It collects the expense type and amount, validates the amount, creates an expense dictionary, and adds it to the shared expense list.

**`view_expense.py`**

Contains the functionality for displaying all recorded expenses. It checks whether the expense list is empty and, if not, loops through the list and displays each expense.

**`total_expense.py`**

Contains the functionality for calculating the total amount spent. It loops through the expenses and adds each amount to a running total.

**`expense_data.py`**

Contains the shared `expenses` list used by the different modules in the application.

**`.gitignore`**

Specifies files and folders that Git should ignore, such as Python's `__pycache__` directory.

**`README.md`**

Contains information about the project, its features, structure, and how to run it.

## Concepts Practiced

This project helped me practice:

* Variables and data types
* Strings and floating-point numbers
* Lists
* Dictionaries
* `if` statements
* `for` loops
* `while` loops
* Functions
* Input validation
* Dictionary access
* List operations
* Modules and imports
* Sharing data between Python modules
* Program flow and control
* Debugging
* Git and GitHub
* Project organization

## Data Structure

The application currently stores expenses in memory using a list of dictionaries:

```python
expenses = [
    {
        "type": "Food",
        "amount": 35.50
    },
    {
        "type": "Transport",
        "amount": 20.00
    }
]
```

The list allows multiple expenses to be stored, while each dictionary represents one individual expense.

## How to Run

Make sure Python is installed on your computer.

Clone the repository and navigate into the project directory.

Then run:

```bash
python main.py
```

Follow the prompts displayed in the terminal.

## Current Limitations

The current version stores expenses only while the program is running. Once the program is closed, the stored expenses are lost because the data is not yet saved to a permanent storage system.

Future versions can introduce persistent storage and additional expense-management features.

## Future Improvements

Possible future features include:

* Categorizing and filtering expenses
* Calculating spending by category
* Deleting expenses
* Editing expenses
* Saving expenses to a JSON or CSV file
* Using a database such as SQLite
* Adding dates to expenses
* Adding a graphical or web-based interface
* Generating spending summaries and reports

## Project Goal

The goal of this project is to progressively develop a practical expense management application while strengthening Python programming, problem solving, debugging, modular programming, and software development skills.
