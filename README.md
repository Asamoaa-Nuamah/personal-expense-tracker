# Personal Expense Tracker

A simple command-line Personal Expense Tracker built with Python. The project allows users to record, view, categorize, edit, delete, and analyze their expenses.

This project was built as a Python practice project to strengthen my understanding of programming fundamentals, including variables, data types, lists, dictionaries, loops, conditional statements, functions, input validation, modules, and basic project organization.

## Features

### 1. Add Expense

Users can add an expense by providing:

* The type/category of the expense (for example, Food or Utility Bills)
* The amount of the expense

The program validates the expense amount and does not allow negative values or invalid numeric input.

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
Food - GHC35.50
Transport - GHC20.00
Utility Bills - GHC50.00
```

### 4. Calculate Total Expenses

The program calculates the total amount spent by looping through the stored expenses and adding each expense amount to a running total.

Example:

```text
Food - GHC35.50
Transport - GHC20.00
Utility Bills - GHC50.00

Total expenses: GHC105.50
```

## Expense Tracker 2.0 Features

### 5. Categorize and Filter Expenses

Users can search for expenses by category.

The program performs a case-insensitive comparison, meaning categories such as `Food`, `food`, and `FOOD` can be treated as the same category.

If no expenses match the selected category, the program informs the user that no expenses were found.

Example:

```text
Enter expense category: food

Food - GHC200.00
Food - GHC800.00
```

### 6. Calculate Spending by Category

Users can calculate the total amount spent within a specific category.

The program loops through the expenses, identifies matching categories, and adds their amounts to a running total.

Example:

```text
Enter expense category: food

Total spent on food: GHC1,000.00
```

If no expenses are found in the selected category, the program displays an appropriate message.

### 7. Delete an Expense

Users can select an expense by its displayed number and delete it from the expense list.

The program:

* Displays expenses with user-friendly numbers.
* Validates the selected expense number.
* Handles non-numeric input.
* Prevents selections outside the valid range.
* Deletes the selected expense.
* Displays the updated expense list.

Example:

```text
1. Food - GHC 200.00
2. Transport - GHC 50.00
3. Food - GHC 800.00

Enter the expense number you want to delete: 2

Expense deleted
```

### 8. Edit an Expense

Users can edit an existing expense by selecting its number and choosing what they want to change.

The program allows users to:

1. Edit the category
2. Edit the amount
3. Edit both the category and amount

Input validation is applied to both fields.

* Categories cannot be empty.
* Amounts must be valid numeric values.
* Negative amounts are not allowed.

After the update, the program displays a confirmation message and the updated expense list.

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
├── category_total.py
├── delete_expense.py
├── edit_expense.py
└── expense_data.py
```

## File Descriptions

### `main.py`

Controls the overall flow of the application. It imports the functions from the other modules and coordinates the different expense-management operations.

### `add_expense.py`

Contains the function responsible for adding an individual expense. It collects the expense type and amount, validates the amount, creates an expense dictionary, and adds it to the shared expense list.

### `view_expense.py`

Contains the functionality for displaying all recorded expenses. It checks whether the expense list is empty and, if not, loops through the list and displays each expense.

### `total_expense.py`

Contains the functionality for calculating the total amount spent. It loops through the expenses and adds each amount to a running total.

### `category_total.py`

Contains the functionality for calculating the total amount spent within a selected expense category.

### `delete_expense.py`

Contains the functionality for selecting and deleting an expense. It validates the user's selection and removes the corresponding expense from the list.

### `edit_expense.py`

Contains the functionality for editing an existing expense. Users can update the category, amount, or both, with input validation applied to the new values.

### `expense_data.py`

Contains the shared `expenses` list used by the different modules in the application.

### `.gitignore`

Specifies files and folders that Git should ignore, such as Python's `__pycache__` directory.

### `README.md`

Contains information about the project, its features, structure, concepts practiced, limitations, and future improvements.

## Concepts Practiced

This project has helped me practice:

* Variables and data types
* Strings and floating-point numbers
* Lists
* Dictionaries
* `if` statements
* `for` loops
* `while` loops
* Functions
* Input validation
* `try`/`except` and `ValueError`
* Dictionary access and modification
* List operations
* `enumerate()`
* Modules and imports
* Sharing data between Python modules
* Case-insensitive string comparison
* Program flow and control
* Debugging
* Git and GitHub
* Project organization
* Writing pseudocode before implementation
* Breaking requirements into smaller programming tasks

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

The project currently uses an in-memory list rather than a database or file based storage system.

## Future Improvements

Possible future features include:

* Saving expenses to a JSON or CSV file
* Adding dates to expenses
* Using a database such as SQLite
* Generating spending summaries and reports
* Adding a graphical or web-based interface
* Adding more advanced filtering and reporting features

## Project Goal

The goal of this project is to progressively develop a practical expense management application while strengthening Python programming, problem solving, debugging, modular programming, input validation, and software development skills.

The project is being developed incrementally, with each new feature providing an opportunity to practice a different programming concept and improve the overall structure of the application.
