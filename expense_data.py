#store expense data
import json
import os

expenses = []
def save_expenses():
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file)
    print('Expenses saved successfully')

def load_expenses():
    if os.path.exists('expenses.json'):
        with open('expenses.json', 'r') as file:
            return json.load(file)
    else:
        return []

expenses = load_expenses()
